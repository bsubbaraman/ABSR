import serial
import pandas as pd
import argparse
import nltk
import pickle as pkl 
import numpy as np
import time
import os
from pathlib import Path
import glob
import csv
nltk.download('vader_lexicon') #grab it if you need it
nltk.download('punkt')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize

sources = [Path(t).stem for t in glob.glob('./data/*.txt')] #["bluets", "foucault"] are default; plus any added by user

def setup_serial():
    """using pyserial for communication. (automated way to get the serial port?)"""
    try:
        ser = serial.Serial("/dev/cu.usbmodem142101", 9600)
        ser.flushInput()
    except:
        print("check your port!")
    return ser

def realtime(source, curve):
    ser = setup_serial()
    outfile = time.strftime('%Y%m%d-%H%M%S', time.localtime()) + f"_{source}.txt"
    raw_outfile = "./logs/raw/" + outfile
    text_outfile = "./logs/text/" + outfile
    f1 = open(raw_outfile, 'a')
    f2 = open(text_outfile, 'a')
    df = pd.read_csv(f'./data/{source}.sentiment.csv', delimiter=',')
    sentence_data = [list(row) for row in df.values]
    sentiments = [float(x[1]) for x in sentence_data]
    while True:
        try:
            ser_bytes = ser.readline()
            decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            data = remap(decoded_bytes, 75, 85, -1, 1, curve) #input range will vary on biodata(/person/etc). output should be [-1,1] for compound sentiment 
            sentence = biodata_to_text(data, sentence_data, sentiments)
            f1.write(str(decoded_bytes)+'\n')
            f2.write(sentence+'\n\n')
        except KeyboardInterrupt:
            f1.close()
            f2.close()
            print(f'data saved to {raw_outfile} and {text_outfile}')
            exit(0)

def get_sentiments(file_path):
    filename, file_extension = os.path.splitext(file_path)
    outfile = filename + ".sentiment.csv"
    if not os.path.exists(outfile):
        f = open(file_path, 'r').read()
        sentences = sent_tokenize(f)
        sentences = [s.strip() for s in sentences]
        sentences = [s for s in sentences if s != "" and s != '"']

        sentiment = SentimentIntensityAnalyzer()
        sentiments = [] 
        for sentence in sentences:
            compound = sentiment.polarity_scores(sentence)['compound']
            sentiments.append(compound)

        data = sorted((zip(sentences, sentiments)), key = lambda x: x[1])
        fields = ['Line', 'Score']  
        with open(outfile, 'w') as csvout:
            csvwriter = csv.writer(csvout)  
            csvwriter.writerow(fields)
            csvwriter.writerows(data)

    return outfile

def get_log(raw_file, source, curve):
    outfile = './logs/text/' + Path(raw_file).stem + f"_{source}.txt"
    df = pd.read_csv(f'./data/{source}.sentiment.csv', delimiter=',')
    sentence_data = [list(row) for row in df.values]
    sentiments = [float(x[1]) for x in sentence_data]
    lines = open(raw_file, 'r').readlines()
    with open(outfile, 'w') as f:
        for data in lines:
            sentence_match = biodata_to_text(remap(float(data), 75, 85, -1, 1, curve), sentence_data, sentiments)
            f.write(sentence_match + '\n\n')

    return outfile


def biodata_to_text(data, sentence_data, sentiments):  
    sentiment_match = min(sentiments, key = lambda x: abs(x-data))
    sentence_match = sentence_data[sentiments.index(sentiment_match)]
    print(sentence_match)
    return sentence_match[0]

def remap(value, min_i, max_i, min_f, max_f, curve):
    """
    remap a value from on range to another. 
    """
    range_i = max_i - min_i
    range_f = max_f - min_f
    tmp_val = float(value - min_i) / float(range_i)
    new_val = min_f + (tmp_val * range_f)

    if curve == 1:
        return new_val
    elif curve == 2:
        print(new_val**2)
        return new_val**2
    elif curve == 3:
        return new_val**3
    else:
        return new_val

def main():
    parser = argparse.ArgumentParser(description="ABSR provides an interpretive biodata log")
    parser.add_argument(
        "--newfile",
        "-n",
        dest="newfile",
        help="get sentiments from new .txt file"
    )
    parser.add_argument(
        "--realtime",
        "-r", 
        dest="realtime",
        action='store_true',
        help="get realtime data over serial"
    )
    parser.add_argument(
        "--process",
        "-p",
        dest="process",
        help="get a new log from raw data",
    )
    parser.add_argument(
        "--source",
        "-s",
        dest="source",
        help="the source material to use",
        choices=sources
    )
    parser.add_argument(
        "--curve",
        "-c",
        type=int,
        default=1,
        dest="curve",
        help="mapping function. currently, polynomial of order [1,2,3]"
    )

    args = parser.parse_args()
    if sum([1 for i in [args.newfile, args.realtime, args.process] if i]) != 1:
        print('please specify one of: newfile, realtime, or process options')
    
    if args.newfile:
        print("getting sentiments...")
        outfile = get_sentiments(args.newfile)
        print(f"saved sentiments to {outfile}")
    elif args.realtime:
        if not args.source:
            print('please specify a source material!')
            return
        print("setting up realtime logging...")
        realtime(args.source, args.curve)

    elif args.process:
        if not args.source:
            print('please specify a source material!')
            return
        outfile = get_log(args.process, args.source, args.curve)
        print(f'log saved to {outfile}')
        

if __name__ == "__main__":
    main()