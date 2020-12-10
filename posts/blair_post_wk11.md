## Logging Text Data

### Concept
What are (some of) the smallest changes to current biosensing technologies that might leverage the exiting political capacities of biosensing to speak to our research questions? Following up on the [provocation](https://bsubbaraman.github.io/ABSR/posts/blair_post_wk10.html) from last week, one such change might be to log text instead of numbers; to tell a (literal) story with your body.

### Prototyping
I stuck to software (mostly) this past week to get a sense of the interaction. The code is in the [`main` branch](https://github.com/bsubbaraman/ABSR/tree/main) of the working repo. It uses [Natural Language Toolkit](https://www.nltk.org/) to tokenize text documents into sentences and to evaluate sentiment (this in turn uses [VADER-sentiment-analysis](https://github.com/cjhutto/vaderSentiment)) which provides 'sentiment' from -1 (most negative) to 1 (most positive). As far as I know, these are standard ways to quickly set up basic nlp projects. Might be interesting to speak to people who do NLP Stuff, too- though since this is a design intevention not a technological one, it seems worthwhile to minimize complexity here. I've included a few texts - Maggie Nelson's _Bluets_ (poetry), Foucault's _Discipline & Punish_, and a physics textbook on optics -  as starting examples, but any text can be uploaded for use (more on that below).

In lieu of any biosensor, I have a temperature sensor connected to an Arduino, communicating with python over serial. Incoming temperature data is mapped from to the range [-1,1], and the sentence of the source material chosen with the closest sentiment is printed out. The text data is also kept in a log to see everything together at once, as well as the raw data from the Arduino so the text log can be re-generated with different texts/mappings/etc. For control over mappings, I added a few 'curves' that might work something like ['easing functions'](https://easings.net/) for text: after translating the data into a range from -1 to 1, you can specify the mapping to be of order 1,2, or 3; one is linear (low values are mapped to negative sentiments & high values to positive), 2 is parabolic (no negative results, low & high values are both mapped to very positive with the middle being more neutral), and 3 is cubic (low values are negative and high values are positive, but the transition is quicker making it more polarized). Definitely more thought to be put into these mappings.

### Examples
Here's some output, all using *the same raw data* from me blowing on the temperature sensor and letting it cool off:

#### Bluets (linear)
You might as well act as if objects had the colors, the Encyclopedia says.—Well, it is as you please.

To be fair, this book will not tell you about any, either.

We cannot read the darkness.

When I looked up you were escaping on a skiff, suddenly wanted.

Daily I think about moving the most vulnerable objects to a “cool, dark place,” but the truth is that I have little to no instinct for protection.

Such demands are murderous to beauty.

Are you sure—one would like to ask—that it cannot love you back?

The disaster did not come then, but it did come later.

It will not say, Isn’t X beautiful?

What depression ever felt like a fire?

But why bother with diagnoses at all, if a diagnosis is but a restatement of the problem?

“This indicates extreme weakness of the organ, its inability to recover itself,” he observes.

Imagine, for example, someone who fucks like a whore.

When the pain is bad it drains her color.

This is how a prince of blue becomes a pain devil.

#### Foucault (linear)
But the delicate mechanism of the passions must not be constrained in the same way or with the same insistence when they begin to improve; the punishment should diminish as it produces its effects.

And, in this respect, the peasants, farmers and artisans were often its principal victims.

And he is not alone in judging.

If one confined oneself to the evolution of legislation or of penal procedures, one would run the risk of allowing a change in the collective sensibility, an increase in humanization or the development of the human sciences to emerge as a massive, external, inert and primary fact.

But apart from these cases, when the process of agitation had been triggered off previously and for reasons that did not concern some measure of penal justice, one finds many examples when the agitation was provoked directly by a verdict and an execution: small, but innumerable ‘disturbances around the scaffold’.

It was a time when, in Europe and in the United States, the entire economy of punishment was redistributed.

‘After these tearings with the pincers, Damiens, who cried out profusely, though without swearing, raised his head and looked at himself; the same executioner dipped an iron spoon in the pot containing the boiling potion, which he poured liberally over each wound.

Of two perjurers, how much more criminal is he on whom one has striven from his childhood to impress feelings of honour than he who, abandoned to nature, never received the benefit of education’ (Marat, 34).

We should admit rather that power produces knowledge (and not simply by encouraging it because it serves power or by applying it because it is useful); that power and knowledge directly imply one another; that there is no power relation without the correlative constitution of a field of knowledge, nor any knowledge that does not presuppose and constitute at the same time power relations.

It occupied a strict place in a complex penal mechanism, in which the procedure of an inquisitorial type was reinforced with elements of the accusatory system; in which the written demonstration required an oral correlative; in which the techniques of proof administered by the magistrates were mingled with the methods of the ordeal to which the accused was challenged; in which he was called upon – if necessary by the most violent persuasion – to play the role of voluntary partner in the procedure; in which it was a question, in short, of producing truth by a mechanism consisting of two elements – that of the investigation carried out in secret by the judicial authority and that of the act ritually performed by the accused.

His presence, assured for ever in the paradise of the aesthetes of crime, is surprising enough: despite all his good will, his neophyte’s zeal, he was only able to commit, and even then with a singular lack of skill, no more than a few minor crimes; he was so strongly suspected of being a police spy that the administration had to protect him against his fellow prisoners, who tried to kill him (the charge was formally taken up by Canler, 15), and it was the fashionable society of Louis-Philippe’s Paris that gave him, before his execution, a feast beside which many a later literary resurrection has been little more than academic homage.

The whole indefinite domain of the non-conforming is punishable: the soldier commits an ‘offence’ whenever he does not reach the level required; a pupil’s ‘offence’ is not only a minor infraction, but also an inability to carry out his tasks.

This individualization was to weigh very heavily throughout the history of modern penal law; it is rooted precisely here: in terms of the theory of law and according to the requirements of everyday practice, it is no doubt in radical opposition to the principle of codification; but from the standpoint of the economy of the power to punish, and of the techniques by which one wishes to circulate throughout the social body precisely calibrated signs of punishment, with neither excesses nor loopholes, with neither a useless ‘expenditure’ of power nor with timidity, it becomes evident that the codification of the offences-punishments system and the modulation of the criminal-punishment dyad go side by side, each requiring the other.

They even go beyond it … God, who has imprinted in our hearts an aversion to pain for ourselves and for our fellow men, are they then those same beings, whom thou hast created so weak and so sensible, who have invented such barbarous, such refined tortures?’ (Lacretelle, 129).

In this way all arbitrariness ceases; the penalty does not depend on the caprice of the legislator, but on the nature of the thing; it is not man who does violence to man, but the man’s own action’ (article 67).

#### Physics Textbook (linear)
You might think that it would be extremely difficult to analyze this, but in fact it is quite easy.

Einstein predicted that light beams would be very slightly deflected by strong gravitational fields, and he was proven correct by observations of rays of starlight that came close to the sun, but obviously that’s not what makes mirrors and lenses work!

This is an example of a general idea enunciated by the physicist Niels Bohr, called the correspondence principle: when flaws in a physical theory lead to the creation of a new and more general theory, the new theory must still agree with the old theory within its more restricted area of applicability.

(If your house has electric heat, then there is absolutely no point in fastidiously turning off lights in the winter; the lights will help to heat the house at the same dollar rate as the electric heater.)

Let’s start with the motion of light that is not interacting with matter at all.

Christian fundamentalists who perceive a conflict between evolution and their religion have claimed that the eye is such a perfect device that it could never have arisen through a process as helter-skelter as evolution, or that it could not have evolved because half of an eye would be useless.

No, the reason it has to be so big is a matter of wave optics.

That would just be too bizarre to believe!

Newton wrote a book on optics, and his prestige and political prominence tended to discourage questioning of his model.

The equation he came up with was

sin 0 |

——= constant .

In general, what combinations of distances will lead to completely destructive and completely constructive interference?

There are two ways in which restriction (2) might commonly be violated.

The trouble with this approach is that one is then forced to memorize tables of sign conventions, e.g.

Section 3.1 A Real Image Formed by an In-Bending Mirror


3.2 Other Cases With Curved Mirrors

The equation = (1 If - l/ify) can easily produce a negative result,

but we have been thinking of d. as a distance, and distances can’t be negative.

One interesting result is that the average light-skinned person in the U.S. would rather lose an arm than suffer the racist treatment routinely endured by African-Americans.



#### Bluets (parabolic)
“You cannot step into the same river twice”—a heartening anthem, without a doubt.

My Thought has thought itself through and reached a Pure Idea.

A friend had been in an accident.

When I looked up you were escaping on a skiff, suddenly wanted.

Duras did not think of alcohol as a false god, but rather as a kind of placeholder, a squatter in the space made by God’s absence.

Goethe describes blue as a lively color, but one devoid of gladness.

To be fair, this book will not tell you about any, either.

But really this is like hoisting a harness onto an invisible horse.

It was around this time that I first had the thought: we fuck well because he is a passive top and I am an active bottom.

An appreciation, an affinity.

“A spectacle and nothing strange a single hurt color and an arrangement in a system to pointing,” I read aloud, scanning the room for a face that also shows signs of being worried about hurt colors.

Others, like Epicurus, proposed the inverse—that objects themselves project a kind of ray that reaches out toward the eye, as if they were looking at us (and surely some of them are).


#### Foucault (cubic)
It was a coded action, of course, since custom and, often quite explicitly, the sentence prescribed its principal episodes.

The reforming jurists, on the other hand, saw punishment as a procedure for requalifying individuals as subjects, as juridical subjects; it uses not marks, but signs, coded sets of representations, which would be given the most rapid circulation and the most general acceptance possible by citizens witnessing the scene of punishment.

The great terrifying ritual of the public execution gives way, day after day, street after street, to this serious theatre, with its multifarious and persuasive scenes.

‘Finally, he was quartered,’ recounts the Gazette d’Amsterdam of 1 April 1757.

‘Finally, he was quartered,’ recounts the Gazette d’Amsterdam of 1 April 1757.

Natural history no doubt offered the most adequate schema: the taxonomy of species according to an uninterrupted gradation.

But apart from these cases, when the process of agitation had been triggered off previously and for reasons that did not concern some measure of penal justice, one finds many examples when the agitation was provoked directly by a verdict and an execution: small, but innumerable ‘disturbances around the scaffold’.

And, in any case, how important is such a change, when compared with the great institutional transformations, the formulation of explicit, general codes and unified rules of procedure; with the almost universal adoption of the jury system, the definition of the essentially corrective character of the penalty and the tendency, which has become increasingly marked since the nineteenth century, to adapt punishment to the individual offender?

After two thirds of his sentence had been served, he could pass to the ‘gêne’ (a cell with light, chain around the waist, solitary work for five hours a day, but with other prisoners on the other two days; this work would be paid and would enable him to improve his daily fare).

The combination of the fait divers and the detective novel has produced for the last hundred years or more an enormous mass of ‘crime stories’ in which delinquency appears both as very close and quite alien, a perpetual threat to everyday life, but extremely distant in its origin and motives, both everyday and exotic in the milieu in which it takes place.

Let us hear once more what Servan has to say: the ideas of crime and punishment must be strongly linked and ‘follow one another without interruption … When you have thus formed the chain of ideas in the heads of your citizens, you will then be able to pride yourselves on guiding them and being their masters.

Monsieur le Breton went up to him again and asked him if he had anything to say; he said no.

Today we are rather inclined to ignore it; perhaps, in its time, it gave rise to too much inflated rhetoric; perhaps it has been attributed too readily and too emphatically to a process of ‘humanization’, thus dispensing with the need for further analysis.

And, according to particular circumstances or tactics, the reformers laid more stress on one or the other.

The other, on the contrary, has had much more rapid and decisive effects in so far as it was linked more directly to the reorganization of the power to punish: codification, definition of offences, the fixing of a scale of penalties, rules of procedure, definition of the role of magistrates.


### Using the Code
(I'll add a readme to the repo, but for now:) 

- clone the repo
- `pip3 install -r requirements.txt` (i'm using python3.8)
- you can either print a log in realtime (will also save to `/logs/raw` and `/logs/text`), add a new source material, or generate a text log from raw data
`absr.py [-h] [--newfile NEWFILE] [--realtime] [--process PROCESS] [--source {bluets,foucault}] [--curve CURVE]`
