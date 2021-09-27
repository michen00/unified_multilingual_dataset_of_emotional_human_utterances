## File naming conventions

The files in data/preprocessed are named as follows:
	
> {record ID}+{dataset code}+{speaker ID}+{speaker gender}+{emotion label}+{valence}+{ISO 639-3 code}+{ISO 639-1 - ISO 3166-1 codes}.wav

---

### Contents
* [Example](#Example)
* [Dataset codes](#Dataset-codes)
* [Speaker gender codes](#Speaker-gender-codes)
* [Emotion label codes](#Emotion-label-codes)
* [ISO codes](#ISO-codes)

---

### Example

**27417+esd+esd.0005+m+hap+1+cmn+zh-cn.wav**

	- Record no.: 27417
	- Data source: Emotional Speech Dataset
	- Speaker ID: esd.0005
	- Speaker gender: male
	- Emotion label: happy
	- Valence label: positive
	- ISO 639-3: Mandarin Chinese
	- ISO 639-1 - ISO 3166-1: Chinese - People's Republic of China

### Dataset codes

| data source abbrev. | name |
|-:|:-|
| aesdd | Acted Emotional Speech Dynamic Database |
| BAUM1 | Bahcesehir University Multimodal Face Database of Affective and Mental States |
| BAUM2 | Bahcesehir University Multilingual Affective Face Database |
| cafe | Canadian French Emotional Speech Database |
| CREMA-D | Crowd-sourced Emotional Multimodal Actors Dataset |
| dzafic | six samples used in schizophrenia research |
| ekorpus | Estonian Emotional Speech Corpus |
| EmoDB | Berlin Database of Emotional Speech |
| EmoReact_V_1.0 | EmoReact dataset |
| Emotional_EMA | Electromagnetic Articulography Database |
| EmoV-DB_sorted | Emotional Voices Database |
| enterface_db | eNTERFACE '05 Audio-Visual Emotion Database |
| esd | Emotional Speech Dataset |
| EYASE | Egyptian Arabic speech emotion database |
| jl-corpus | JL Corpus |
| LimaCastroScott | the corpus provided by Lima, Castro, and Scott |
| LEGOv2 | Carnegie Mellon University Let’s Go Spoken Dialogue Corpus |
| MAV | Montreal Affective Voices |
| MELD | Multimodal EmotionLines Dataset |
| MESS | Morgan Emotional Speech Set |
| oreau2 | French Emotional Speech Database - Oréau |
| ravdess | Ryerson Audio-Visual Database of Emotional Speech and Song |
| savee | Surrey Audio-Visual Expressed Emotion Database |
| ShEMO | Sharif Emotional Speech Database |
| tess | Toronto Emotional Speech Set |
| urdu | Urdu Language Speech Dataset |
| vivae | Variably Intense Vocalizations of Affect and Emotion Corpus |

(See [Multilingual Speech Valence Classification Datasets](https://github.com/michen00/multilingual_speech_valence_classification_datasets) for more information.)

### Speaker gender codes

| character | speaker gender |
|-:|:-|
| f | female |
| m | male |
| u | unknown |

### Emotion label codes

| three-letter code | emotion |
|-:|:-|
| ach | achievement |
| amu | amused |
| ang | angry |
| anx | anxious |
| apo | apologetic |
| bor | bored |
| bot | bothered |
| cal | calm |
| con | contemptuous |
| cur | curious |
| dis | disgusted |
| exc | excited |
| fea | fearful |
| fri | friendly |
| fru | frustrated |
| hap | happy |
| neu | neutral |
| pai | painful |
| ple | pleasure |
| rel | relieved |
| sad | sad |
| unc | uncertain |
| unk | unknown |

### ISO codes

I used the [SIL International code tables](https://iso639-3.sil.org/code_tables/639/data/all) to look up ISO 639 codes.

Country codes may be referenced from the Wikipedia article: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).

Note that the non-speech data sources still retain the language and country codes of the speakers.

[^top](#File-naming-conventions)
