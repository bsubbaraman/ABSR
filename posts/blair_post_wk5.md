## Building off the Sketches
Based on our sketches, here's an outline of how two interactions of interest might play out:

### Texting With Biosignals
Here are a few possible scenarios, with varying levels of control between model & human:

- Similar to some of Fannie Liu's work: biodata, such as heartrate, is monitored as someone texts. This heartrate is mapped to an emoji (through a to-be-determined model ;). The texter can write whatever they'd like, but they emoji will be appended to the message, which can complicate the meaning of the message. In an analogy to different 'keyboards' available on phones, the user could choose different sets of emoji as the 'keyboard' from which they're drawn. 

- I can also imagine heart rate being mapped to a word. Something like [word2vec](https://en.wikipedia.org/wiki/Word2vec) supplies word embeddings, and these embeddings then have geometric relationships with one another (a classic example is that word2vec will finish the analogy 'king is to queen as man is to woman'). The texter can supply any word they'd like at their resting heart rate, and when a significantly different heart rate is registered, the difference in heart rates is mapped to a 'difference' in words- this word could be sent on it's own, or it could be the prompt for a conversation. (There's maybe some analogy in here to autocorrect that could serve as some creative fodder :)

- In a more extreme example, EMG data could be collected from a texter's moving thumbs. While the texter types an actual sentence, the model takes in the EMG data, looking at things like speed & rythm, and outputs it's own text interpreted from this data. If it's possible to generate text or sound by directly using ASR techniques on the incoming biosignal, then this could be the output (it would be gibberish, but might still convey some emotion). Altneratively, text generation like GPT-3 could be used by some model of the EMG data, which would produce coherent text. 

Some of these ideas get away from the idea of ASR and more into NLP. I think they all, however, provide some affordances in using the body to communicate via text; you could try to manipulate your biosignals e.g. by going for a run, or thinking about an intense event.

### Autoportrait
I can imagine the autoportrait as a tool to prompt critical 'reflection'- the model can intake biodata apply some filter to visualize the signal. This visualization is applied literally to the body, e.g a colored aura. In thinking about this scaled to 2+ people, it could be interesting to apply it during a Zoom call so that it visualizes the data for the other person, similar to Howell's LED shirt. This can prompt emotional connection, especially during COVID-19. The use of a webcam here immediately invokes surveillance for me (shout out Michel ;'). Some biosensing has made national news lately, such as software which tracks student's line of sight during exams to ensure they do not cheat. This autoportrait could in part appropriate these surveillance tools towards social & emotional goals.

## Why is the body an interesting site to explore in relation to computation?*
- Surveillance technologies are prominent examples, with work like [Simone Browne's *Dark Matters: On the Surveillance of Blackness*](https://www.dukeupress.edu/dark-matters) or [Ruha Benjamin's *Race After Technology: Abolitionist Tools for the New Jim Code*](https://politybooks.com/bookdetail/?isbn=9781509526390) being relevant in how algorithms materially impact Black bodies.
- In a more philosophical argument, Alexander Galloway lays out an interesting take on [Being as a Computational Mode](http://cultureandcommunication.org/galloway/being-is-a-computational-mode#more-771) from his book Laruelle: Against the Digital. I'm not totally sure where to go with this, but it feels as thought it might offer a theoretical foothole in weaving computation and the body together.
- Resources from the School for Poetic Computation's class on the [Politics and Poetics of Computation](https://github.com/tchoi8/poetic-computation-16) might be interesting to review, too (this is how I initially found the Galloway essay above).


## A (very) brief ""exploration"" of biosignal to text
- It looks like software like OpenBCI can ouput an [OSC data stream](https://openbci.com/forum/index.php?p=/discussion/1534/convert-eeg-data-to-audio-signal) which can then be piped into e.g. [PureData for sonification](https://github.com/jajcayn/EEG-pd-sonification). 
- You can also [convert EEG data as a .wav file](https://github.com/chipaudette/OpenBCI/tree/master/Processing_GUI/ConvertToWAV), which is the format that most off-the-shelf ASR software wants to transcribe speech to text. I found a wav file of EEG data online and tried feeding it directly into [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech), but unsurprisingly, it didn't find any text in the file. So, direct biosignal-to-text will require some manipulation of the original data. I'm not sure if this would be something as simple as scaling it up/down to be in the same range as speech, or if it might be something more sophisticated- I'm not familiar enough with what the biodata actually 'looks like' right now.

<img src="/images/blair_sketch_wk5_1.JPG" width="40%"> <img src="/images/blair_sketch_wk5_2.jpg" width="40%">  
Blair's sketches. We decided to explore the "biosignal text messaging" idea further in a short write up (above), as well as incorporating the "biosignal synthesizer"'s exposing of the model parameters.
