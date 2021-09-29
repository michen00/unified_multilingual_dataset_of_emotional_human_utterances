# Unified Multilingual Dataset of Emotional Human Utterances

---

## Contents

* [Summary](#Summary)
  * [Full Dataset](#Full-dataset)
  * [Core Dataset](#Core-dataset)
* [Data Sources](#Data-sources)
* [Preprocessing](#Preprocessing)
* [Emotion Categorization](#Emotion-Categorization)
  * [Valence of Calm](#Valence-of-Calm)
  * [Valence of Curiosity](#Valence-of-Curiosity)
  * [Valence of Surprise](#Valence-of-Surprise)
* [Datasets](#Datasets)
  * [English](#English)
  * [Non-English](#Non-English)
  * [Non-Speech](#Non-Speech)
* [References](#References)

---

Inquiries may be directed to Michael.Chen.0@gmail.com.

## Summary

The Unified Multilingual Dataset of Emotional Human Utterances provides 87,364 audio files of emotional human utterances with leading silences trimmed and encoded as PCM signed 16-bit little-endian .wav files sampled at 16 kHz with a sample width of 16 bits and bit rate of 128 kbps. For each audio file, labels are available for speaker gender, emotion category, and valence as well as unique speaker IDs and duration.

This dataset builds on prior research by unifying a broad set of multilingual data sources curated by [[1]](#1): 13 English data sources, 9 datasets in non-English languages, 2 datasets providing both English and non-English speech samples, and 3 datasets of affective human non-speech vocalizations for a total of 27 data sources in 9 languages. Altogether, the full unified dataset contains 258,332.5 seconds (71.76 hours) of audio comprised of 87,146 samples (about 7.8 GB) ranging from 0.213 seconds to 55.96 seconds in duration with a mean duration of 2.96 seconds (*SD* = 1.67).

Note that the end-user license agreements of the two Bahcesehir University datasets [[2]](#2)–[[3]](#3), the EmoReact dataset [[4]](#4), the Egyptian Arabic speech emotion database [[5]](#5) and the Surrey Audio-Visual Expressed Emotion Database [[6]](#6) do not allow for distribution of their data; these are not included in the core dataset.

### Full Dataset

*N* = 87,146

| Valence |  |
|:-|-:|
| Number of negative samples | 46,382 |
| Number of neutral samples | 22,770 |
| Number of positive samples | 17,994 |

| Samples by speaker gender |  |
|:-|-:|
| Number of samples from female speakers | 44,885 |
| Number of samples from male speakers | 41,950 |
| Number of samples from speakers of unknown gender | 311 |

| Speakers |  |
|:-|-:|
| Number of unique female speakers | 579 |
| Number of unique male speakers | 672 |
| Number of unique speakers of unknown gender | 56 |
| Number of unique speakers | 1,307 |

| Language |  |
|:-|-:|
| Number of English samples | 59,620 |
| Number of non-English samples | 26,234 |
| Number of non-speech samples | 1,292 |

### Core Dataset

*N* = 83,545

| Valence |  |
|:-|-:|
| Number of negative samples | 44,291 |
| Number of neutral samples | 22,257 |
| Number of positive samples | 16,997 |

| Samples by speaker gender |  |
|:-|-:|
| Number of samples from female speakers | 43,294 |
| Number of samples from male speakers | 39,940 |
| Number of samples from speakers of unknown gender | 311 |

| Speakers |  |
|:-|-:|
| Number of unique female speakers | 455 |
| Number of unique male speakers | 535 |
| Number of unique speakers of unknown gender | 56 |
| Number of unique speakers | 1,046 |

| Language |  |
|:-|-:|
| Number of English samples | 57,977 |
| Number of non-English samples | 24,276 |
| Number of non-speech samples | 1,292 |

## Data Sources

English audio samples with emotion labels were sourced from the [Carnegie Mellon University Let's Go Spoken Dialogue Corpus](https://www.ultes.eu/ressources/lego-spoken-dialogue-corpus/) [[7]](#7)–[[8]](#8), [Crowd-sourced Emotional Multimodal Actors Dataset](https://github.com/CheyneyComputerScience/CREMA-D) [[9]](#9)–[[10]](#10), the [Electromagnetic Articulography Database](https://span.usc.edu/owncloud/index.php/s/RTttck1EJ6Vcoyu) [[11]](#11), the [EmoReact dataset](https://www.behnaznojavan.com/data) [[4]](#4), the [eNTERFACE '05 Audio-Visual Emotion Database](http://www.enterface.net/enterface05/docs/results/databases/project2_database.zip) [[12]](#12), the [JL Corpus](https://www.kaggle.com/tli725/jl-corpus) [[13]](#13), the [Morgan Emotional Speech Set](https://zenodo.org/record/3813437) [[14]](#14)–[[15]](#15), the [Multimodal EmotionLines Dataset](https://affective-meld.github.io/) [[16]](#16)–[[17]](#17), the [Ryerson Audio-Visual Database of Emotional Speech and Song](https://zenodo.org/record/1188976) [[18]](#18), the [Surrey Audio-Visual Expressed Emotion Database](http://personal.ee.surrey.ac.uk/Personal/P.Jackson/SAVEE/Download.html) [[6]](#6), and the [Toronto Emotional Speech Set](https://dataverse.scholarsportal.info/dataset.xhtml?persistentId=doi%3A10.5683%2FSP2%2FE8H2MF) [[19]](#19). [[20]](#20) provides six samples (two each of positive, negative, and neutral valence) in Australian English (prepared for investigation of emotion perception in patients with schizophrenia). Although reported to contain Belgian French samples as well, only the English files of the [Emotional Voices Database](https://mega.nz/folder/KBp32apT#gLIgyWf9iQ-yqnWFUFuUHg) [[21]](#21) were available to me.

Most of the English-language datasets are of North American English with some dialectic variations. For instance, the Crowd-sourced Emotional Multimodal Actors Dataset [[9]](#9)–[[10]](#10) (amongst others) consists mostly of Mainstream American English recordings but also some samples of non-standard American English while the Toronto Emotional Speech Set [[19]](#19) was elicited from two actresses recruited from the eponymous metropolitan area in Canada. On the other hand, the JL Corpus [[13]](#13) is of New Zealand English and the Surrey Audio-Visual Expressed Emotion Database [[6]](#6) is of British English. In addition, the eNTERFACE '05 Audio-Visual Emotion Database [[12]](#12) consists of English spoken by participants of fourteen nationalities and the videos provided by [[20]](#20) are in Australian English.

Similar spoken corpora with emotion labels were obtained for Arabic ([Egyptian Arabic speech emotion database](https://www.researchgate.net/publication/341001383_EYASE_Database)) [[5]](#5), Estonian ([Estonian Emotional Speech Corpus](https://metashare.ut.ee/repository/download/4d42d7a8463411e2a6e4005056b40024a19021a316b54b7fb707757d43d1a889/)) [[22]](#22), French ([French Emotional Speech Database - Oréau](https://zenodo.org/record/4405783)) [[23]](#23) and Canadian (Québec) French ([Canadian French Emotional Speech Database](https://web.archive.org/web/20201129223923/https://www.gel.usherbrooke.ca/audio/cafe.htm)) [[24]](#24), German ([Berlin Database of Emotional Speech](https://www.kaggle.com/piyushagni5/berlin-database-of-emotional-speech-emodb)) [[25]](#25), Greek ([Acted Emotional Speech Dynamic Database](https://mega.nz/folder/0ShVXY7C#-73kVoK05OjTPEA95UUvMw)) [[26]](#26)–[[27]](#27), Persian ([Sharif Emotional Speech Database](https://github.com/mansourehk/ShEMO)) [[28]](#28), Turkish ([Bahcesehir University Multimodal Face Database of Affective and Mental States](https://archive.ics.uci.edu/ml/datasets/BAUM-1)) [[2]](#2), and Urdu ([Urdu Language Speech Dataset](https://www.kaggle.com/bitlord/urdu-language-speech-dataset)) [[29]](#29).

Two datasets contained non-English samples in addition to English samples: the [Bahcesehir University Multilingual Affective Face Database](https://archive.ics.uci.edu/ml/datasets/BAUM-2) (Turkish) [[3]](#3) and the [Emotional Speech Dataset](https://github.com/HLTSingapore/Emotional-Speech-Data) (Mandarin Chinese) [[30]](#30).

The [the corpus provided by Lima, Castro, and Scott](https://link.springer.com/article/10.3758/s13428-013-0324-3) [[31]](#31), the [Montreal Affective Voices](https://amubox.univ-amu.fr/index.php/s/JdF6fWC2M0lSr14) [[32]](#32), and the [Variably Intense Vocalizations of Affect and Emotion Corpus](https://zenodo.org/record/4066235) [[33]](#33) contained emotional non-speech vocalizations of humans. Respectively, vocalizations were elicited from native speakers of European Portuguese [[31]](#31), Canadian French [[32]](#32), and American English [[33]](#33).

See [[1]](#1) for the repository collecting these data sources.

## Preprocessing

Files were selected from the datasets curated in [[1]](#1). The `pydub` library was used for preprocessing, which consisted of the following steps:

1. *Load files.* The selected files were loaded as `AudioSegment`.
1. *Set sample width to 2 bytes.* Sample widths were set to 2 bytes (16 bits) if not already set as such.
1. *Normalize volume.* Volume was normalized to facilitate better comparison between datasets.
1. *Trim silence.* All leading silences were trimmed; most recordings already began at the first onset. Silence provides both linguistic information [[34]](#34) and paralinguistic information [[35]](#35) that inform prosody and emotion perception [[36]](#36), so within-utterance silence is unaltered. Silence can directly affect perceived valence whether it occurs between speaker turns [[37]](#37)–[[38]](#38) or between two utterances in the same turn [[36]](#36), so trailing silences in discourse contexts were preserved. If the file was not recorded in a discourse setting (e.g., following a laboratory elicitation prompt), trailing silence was trimmed too. -60 dFBS was used as the silence threshold.
1. *Filter by duration.* Audio files less than 200 ms in duration were discarded since they are barely perceptible. Those that exceeded 60,000 ms in duration were also discarded since they exceed the ostensible length of a single human utterance. As a result, recordings where the subject does not speak (e.g., a silent affective face video) and those where the speaker is inaudibly soft were omitted as well as some files that appeared to contain entire dialogues (or television scenes). About 218 files were omitted according to the duration criterion.
1. *Collapse multichannel sound.* Multichannel (including stereo) recordings were converted to monaural (mono) sound.
1. *Set sampling rate to 16 kHz.* Roughly 55% of the sound files were already sampled at 16 kHz and were not resampled. About 5% of the files were upsampled from 8 kHz such as those from [[7]](#7)–[[8]](#8) and the rest were downsampled from sampling rates ranging from 22.05 kHz (e.g., [[20]](#20)) to 192 kHz (e.g., [[24]](#24)).
1. *Export as .wav at 128 kbps with a signed 16-bit little-endian PCM codec.* Finally, the processed `AudioSegment` instances were exported as .wav files using the Pulse-Code Modulation (PCM) signed 16-bit little-endian encoder provided by `ffmpeg` (a dependency of `pydub`) with the bitrate set to 128 kbps.

## Emotion Categorization

In general, the valence of each utterance was easy to infer from the emotion label. Emotion labels like *joy* or *happy* would be positive, *neutral* would be neutral, and *anger*, *disgust*, *fear*, *sadness* would be negative. Some data sources like [[11]](#11) or [[31]](#31) provided continuous measures of perceived valence as well. Most of the data sources were already validated by perception checks and interrater consensus as per their original methods and were unambiguous in terms of emotion category and valence.

Other emotion labels were not canonical categories but were still easy to map to a discrete valence. Categories such as *achievement* or *pleasure* are uncontroversially positive just as *bothered* or *frustration* are negative. Some were trickier, but a valence mapping could be justified by the methods described by the original authors or by other supporting literature. For example, [[13]](#13) designed *apologetic* utterances to be negatively valenced and *boredom* is conventionally treated as a negative emotion [[39]](#39)–[[41]](#41). If I could not find support in the methods or literature to map an emotion category one way or another, I discarded those samples; discarded emotion labels include *assertive*, *concentrating*, *concerned*, *encouraging*, *thinking*, and *sleepy*.

In some cases (e.g., [[3]](#3), [[4]](#4), [[9]](#9)–[[10]](#10), [[11]](#11), [[22]](#22), or [[31]](#31)), perception scores for different emotion categories were provided in addition to or instead of a single label. In these cases, the emotion label was inferred from mean scores (for continuous or numeric discrete variables) or from binomial majority vote (for binary vote variables). If provided, valence scores/labels were checked and filtered for misalignment with the emotion label (e.g., positive *anger*, negative *joy*, non-neutral *neutral*, neutral *disgust*, etc.) or with the intended valence of the utterance (e.g., raters perceived positive valence when the speaker attempted to express *fear*).

Three emotion categories bear additional discussion as they are variably mapped to valence categories depending on the original methods: *calm*, *curious*, and *surprised*.

### Valence of Calm

In the Ryerson Audio-Visual Database of Emotional Speech and Song [[18]](#18), *calm* was treated as a second baseline emotion to complement *neutral* due to concern that *neutral* utterances may be unduly perceived as negatively valenced as in [[42]](#42). Thus, *calm* was mapped to neutral valence for data originating from [[18]](#18). On the other hand, the Morgan Emotional Speech Set employed *calm* specifically as a low-activation, high-pleasantness emotion [[14]](#14)–[[15]](#15), so it defaults to positive valence for this data source.

### Valence of Curiosity

According to [[43]](#43)–[[45]](#45), the valence evaluation of someone experiencing a curious state is largely dependent on context and attribution. The Bahcesehir University Multimodal Face Database of Affective and Mental States [[2]](#2) includes *interest* labels that were recoded to *curiosity*; these were mapped to positive valence since *interest*, which has been characterized as a positive emotion by [[39]](#39) and [[45]](#45), was used as a synonym for *curiosity* in the paper. The EmoReact dataset [[4]](#4) is the only other data source providing this emotion label and provides a valence score that was used to determine the valence classification. The *curious* label is thus only present in the core dataset and is associated with both positive and negative valence. (Theoretically, *curious* could be neutral too, but the data does not contain neutral *curious* samples.)

### Valence of Surprise

*Surprise* is another emotion where valence is dependent on context and attribution [[46]](#46)–[[49]](#49). However, there is evidence to suggest that the default interpretation of *surprise* is negative [[47]](#47)–[[48]](#48). Some authors like [[19]](#19) explicitly describe the intended emotion as *pleasant surprise*, in which case the valence is positive. Otherwise, valence ratings were used to code the valence of *surprise* samples where provided by the original data source or mapped to negative valence by default.

## Datasets

### English

* [CREMA-D](https://github.com/michen00/multilingual_speech_valence_classification_datasets/tree/main/datasets/CREMA-D) | Crowd-sourced Emotional Multimodal Actors Dataset [[9]](#9)–[[10]](#10)
* [dzafic](https://github.com/michen00/multilingual_speech_valence_classification_datasets/tree/main/datasets/dzafic) | Six samples from [[20]](#20)
* [EmoReact_V_1.0](https://github.com/michen00/multilingual_speech_valence_classification_datasets/tree/main/datasets/EmoReact_V_1.0) | EmoReact dataset [[4]](#4)
* [Emotional_EMA](https://github.com/michen00/multilingual_speech_valence_classification_datasets/tree/main/datasets/Emotional_EMA) | Electromagnetic Articulography Database [[11]](#11)
* [EmoV-DB_sorted](https://github.com/michen00/multilingual_speech_valence_classification_datasets/tree/main/datasets/EmoV-DB_sorted) | Emotional Voices Database [[21]](#21)
* [enterface_db](https://github.com/michen00/multilingual_speech_valence_classification_datasets/tree/main/datasets/enterface_db) | eNTERFACE '05 Audio-Visual Emotion Database [[12]](#12)
* [jl-corpus](https://github.com/michen00/multilingual_speech_valence_classification_datasets/tree/main/datasets/jl-corpus) | JL Corpus [[13]](#13)
* [LEGOv2](https://github.com/michen00/multilingual_speech_valence_classification_datasets/tree/main/datasets/LEGOv2) | Carnegie Mellon University Let’s Go Spoken Dialogue Corpus [[7]](#7)–[[8]](#8)
* [MELD](https://github.com/michen00/multilingual_speech_valence_classification_datasets/tree/main/datasets/MELD) | Multimodal EmotionLines Dataset [[16]](#16)–[[17]](#17)
* [MESS](https://github.com/michen00/multilingual_speech_valence_classification_datasets/tree/main/datasets/MESS) | Morgan Emotional Speech Set [[14]](#14)–[[15]](#15)
* [ravdess](https://github.com/michen00/multilingual_speech_valence_classification_datasets/tree/main/datasets/ravdess) | Ryerson Audio-Visual Database of Emotional Speech and Song [[18]](#18)
* [savee](https://github.com/michen00/multilingual_speech_valence_classification_datasets/tree/main/datasets/savee) | Surrey Audio-Visual Expressed Emotion Database [[6]](#6)
* [tess](https://github.com/michen00/multilingual_speech_valence_classification_datasets/tree/main/datasets/tess) | Toronto Emotional Speech Set [[19]](#19)

### Non-English

* [aesdd](https://github.com/michen00/multilingual_speech_valence_classification_datasets/tree/main/datasets/aesdd) | Acted Emotional Speech Dynamic Database (Greek) [[26]](#26)–[[27]](#27)
* [BAUM1](https://github.com/michen00/multilingual_speech_valence_classification_datasets/tree/main/datasets/BAUM1) | Bahcesehir University Multimodal Face Database of Affective and Mental States [[2]](#2)
* [BAUM2](https://github.com/michen00/multilingual_speech_valence_classification_datasets/tree/main/datasets/BAUM2) | Bahcesehir University Multilingual Affective Face Database [[3]](#3)
* [cafe](https://github.com/michen00/multilingual_speech_valence_classification_datasets/tree/main/datasets/cafe) | Canadian French Emotional Speech Database [[24]](#24)
* [ekorpus](https://github.com/michen00/multilingual_speech_valence_classification_datasets/tree/main/datasets/ekorpus) | Estonian Emotional Speech Corpus [[22]](#22)
* [EmoDB](https://github.com/michen00/multilingual_speech_valence_classification_datasets/tree/main/datasets/EmoDB) | Berlin Database of Emotional Speech (German) [[25]](#25)
* [esd](https://github.com/michen00/multilingual_speech_valence_classification_datasets/tree/main/datasets/esd) | Emotional Speech Dataset (Mandarin Chinese and English) [[30]](#30)
* [EYASE](https://github.com/michen00/multilingual_speech_valence_classification_datasets/tree/main/datasets/EYASE) | Egyptian Arabic speech emotion database [[5]](#5)
* [oreau2](https://github.com/michen00/multilingual_speech_valence_classification_datasets/tree/main/datasets/oreau2) | French Emotional Speech Database - Oréau [[23]](#23)
* [ShEMO](https://github.com/michen00/multilingual_speech_valence_classification_datasets/tree/main/datasets/ShEMO) | Sharif Emotional Speech Database (Persian) [[28]](#28)
* [urdu](https://github.com/michen00/multilingual_speech_valence_classification_datasets/tree/main/datasets/urdu) | Urdu Language Speech Dataset [[29]](#29)

### Non-Speech

* [LimaCastroScott](https://github.com/michen00/multilingual_speech_valence_classification_datasets/tree/main/datasets/LimaCastroScott) | the corpus provided by Lima, Castro, and Scott [[31]](#31)
* [MAV](https://github.com/michen00/multilingual_speech_valence_classification_datasets/tree/main/datasets/MAV) | Montreal Affective Voices [[32]](#32)
* [vivae](https://github.com/michen00/multilingual_speech_valence_classification_datasets/tree/main/datasets/vivae) | Variably Intense Vocalizations of Affect and Emotion Corpus [[33]](#33)

## References

<span aria-hidden="true"><h6><sub><sup><sub><sup>1</sup></sub></sup></sub></h6></span>

1. M. I. Chen. "Datasets for multilingual speech valence classification. V0.1.0." Github. Accessed: Sep. 29, 2021. [Online]. Available: https://github.com/michen00/multilingual_speech_valence_classification_datasets

<span aria-hidden="true"><h6><sub><sup><sub><sup>2</sup></sub></sup></sub></h6></span>

2. S. Zhalehpour, O. Onder, Z. Akhtar, and C. E. Erdem, "BAUM-1: A spontaneous audio-visual face database of affective and mental states," *IEEE Trans. Affect. Comput.,* vol. 8, no. 3, pp. 300–313, Jul./Sep. 2017, doi: https://doi.org/10.1109/TAFFC.2016.2553038.

<span aria-hidden="true"><h6><sub><sup><sub><sup>3</sup></sub></sup></sub></h6></span>

3. C. E. Erdem, C. Turan, and Z. Aydin, "BAUM-2: A multilingual audio-visual affective face database," *Multimedia Tools and Applications,* vol. 74, no. 18, pp. 7429–7459, May 9, 2015, doi: https://doi.org/10.1007/s11042-014-1986-2.

<span aria-hidden="true"><h6><sub><sup><sub><sup>4</sup></sub></sup></sub></h6></span>

4. B. Nojavanasghari, T. Baltrušaitis, C. E. Hughes, and L.-P. Morency, "EmoReact: A multimodal approach and dataset for recognizing emotional responses in children," in *Proc. 18th ACM Int. Conf. Multimodal Interaction,* Tokyo, Japan, Nov. 12–16 2016, pp. 137–144. doi: https://doi.org/10.1145/2993148.2993168.

<span aria-hidden="true"><h6><sub><sup><sub><sup>5</sup></sub></sup></sub></h6></span>

5. L. Abdel-Hamid, "Egyptian Arabic speech emotion recognition using prosodic, spectral, and wavelet features," *Speech Communication,* vol. 122, pp. 19–30, Sep. 2020, doi: https://doi.org/10.1016/j.specom.2020.04.005.

<span aria-hidden="true"><h6><sub><sup><sub><sup>6</sup></sub></sup></sub></h6></span>

6. S. Haq and P. J. B. Jackson, "Multimodal emotion recognition," in *Machine Audition: Principles, Algorithms and Systems,* W. Wang, Ed., Hershey, PA, USA: IGI Global Press, 2011, pp. 398–423. doi: https://doi.org/10.4018/978-1-61520-919-4.ch017.

<span aria-hidden="true"><h6><sub><sup><sub><sup>7</sup></sub></sup></sub></h6></span>

7. A. Schmitt, S. Ultes, and W. Minker, "A parameterized and annotated spoken dialog corpus of the CMU Let’s Go bus information system," in *Int. Conf. Lang. Resour. and Eval.,* Istanbul, Turkey, May 2012, pp. 3369–3373. Accessed: Feb. 8, 2021. Available: https://www.academia.edu/21586940/A_Parameterized_and_Annotated_Spoken_Dialog_Corpus_of_the_CMU_Lets_Go_Bus_Information_System

<span aria-hidden="true"><h6><sub><sup><sub><sup>8</sup></sub></sup></sub></h6></span>

8. S. Ultes, A. Schmitt, M. J. P. Sánchez, and W. Minker, "Analysis of an extended interaction quality corpus," in *Natural Lang. Dialog Syst. and Intell. Assistants,* G. G. Lee, H. K. Kim, M. Jeong, and J.-H. Kim, Eds., Cham, Switzerland: Springer Int. Publishing, 2015, pp. 41–52. doi: https://doi.org/10.1007/978-3-319-19291-8_4.

<span aria-hidden="true"><h6><sub><sup><sub><sup>9</sup></sub></sup></sub></h6></span>

9. H. Cao, D. G. Cooper, M. K. Keutmann, R. C. Gur, A. Nenkova, and R. Verma, "CREMA-D: Crowd-sourced Emotional Multimodal Actors Dataset," *IEEE Trans. Affect. Comput.,* vol. 5, no. 4, pp. 377–390, Oct./Dec. 2014, doi: https://doi.org/10.1109/TAFFC.2014.2336244.

<span aria-hidden="true"><h6><sub><sup><sub><sup>10</sup></sub></sup></sub></h6></span>

10. M. K. Keutmann, S. L. Moore, A. Savitt, and R. C. Gur, "Generating an item pool for translational social cognition research: Methodology and initial validation," *Behav. Res. Methods,* vol. 47, no. 1, pp. 228–234, Mar. 2015, doi: https://doi.org/10.3758/s13428-014-0464-0.

<span aria-hidden="true"><h6><sub><sup><sub><sup>11</sup></sub></sup></sub></h6></span>

11. S. Lee, S. Yildirim, A. Kazemzadeh, and S. S. Narayanan, "An articulatory study of emotional speech production," in *Proc. INTERSPEECH 2005,* Lisbon, Portugal, Sep. 4–8, 2005, pp. 497–500. Accessed: Feb. 8, 2021. [Online.] Available: https://sail.usc.edu/ema_web/LeeInterSpeech2005.pdf

<span aria-hidden="true"><h6><sub><sup><sub><sup>12</sup></sub></sup></sub></h6></span>

12. O. Martin, I. Kotsia, B. Macq, and I. Pitas, "The eNTERFACE '05 Audio-Visual Emotion Database," in *Proc. 22nd Int. Conf. on Data Eng. Workshops,* Atlanta, GA, USA, Apr. 3–7, 2006, p. 8. doi: https://doi.org/10.1109/ICDEW.2006.145.

<span aria-hidden="true"><h6><sub><sup><sub><sup>13</sup></sub></sup></sub></h6></span>

13. J. James, L. Tian, and C. Watson, "An open source emotional speech corpus for human robot interaction applications," in *Proc. INTERSPEECH 2018,* Hyderabad, India, Sep. 2–6, 2018, pp. 2768–2772. doi: https://doi.org/10.21437/Interspeech.2018-1349.

<span aria-hidden="true"><h6><sub><sup><sub><sup>14</sup></sub></sup></sub></h6></span>

14. S. D. Morgan, "Categorical and dimensional ratings of emotional speech: Behavioral findings from the Morgan Emotional Speech Set," *J. Speech, Lang., and Hearing Res.*, vol. 62, no. 11, pp. 4015–4029, Nov. 2019, doi: https://doi.org/10.1044/2019_JSLHR-S-19-0144.

<span aria-hidden="true"><h6><sub><sup><sub><sup>15</sup></sub></sup></sub></h6></span>

15. S. D. Morgan, *Morgan Emotional Speech Set. V4.* May 3, 2019. Distributed by Zenodo. Accessed: Sep. 20, 2021. [Dataset]. doi: https://doi.org/10.5281/zenodo.3813437.

<span aria-hidden="true"><h6><sub><sup><sub><sup>16</sup></sub></sup></sub></h6></span>

16. S.-Y. Chen, C.-C. Hsu, C.-C. Kuo, T.-H. Huang, and L.-W. Ku, "EmotionLines: An emotion corpus of multi-party conversations," 2018, *arXiv:1802.08379v2*. Accessed: Mar. 4, 2021. [Online]. Available: https://arxiv.org/pdf/1802.08379.pdf

<span aria-hidden="true"><h6><sub><sup><sub><sup>17</sup></sub></sup></sub></h6></span>

17. S. Poria, D. Hazarika, N. Majumder, G. Naik, E. Cambria, and R. Mihalcea, "MELD: A multimodal multi-party dataset for emotion recognition in conversations," 2018, *arXiv:1810.02508v6*. Accessed: Mar. 4, 2021. [Online]. Available: https://arxiv.org/pdf/1810.02508.pdf

<span aria-hidden="true"><h6><sub><sup><sub><sup>18</sup></sub></sup></sub></h6></span>

18. S. R. Livingstone and F. A. Russo, "The Ryerson Audio-Visual Database of Emotional Speech and Song (RAVDESS): A dynamic, multimodal set of facial and vocal expressions in North American English," *PLoS ONE,* vol. 13, no. 5, p. e0196391, May 16, 2018, doi: https://doi.org/10.1371/journal.pone.0196391.

<span aria-hidden="true"><h6><sub><sup><sub><sup>19</sup></sub></sup></sub></h6></span>

19. M. K. Pichora-Fuller and K. Dupuis, *Toronto Emotional Speech Set (TESS). V1.* 2020. Distributed by Scholars Portal Dataverse. Accessed: Feb. 8, 2021. doi: https://doi.org/10.5683/SP2/E8H2MF.

<span aria-hidden="true"><h6><sub><sup><sub><sup>20</sup></sub></sup></sub></h6></span>

20. I. Dzafic, *Example emotion videos used in investigation of emotion perception in schizophrenia.* 2017. Distributed by the University of Queensland. Accessed: Mar. 3, 2021. [Online]. doi: https://doi.org/10.14264/uql.2017.120.

<span aria-hidden="true"><h6><sub><sup><sub><sup>21</sup></sub></sup></sub></h6></span>

21. A. Adigwe, N. Tits, K. El Haddad, S. Ostadabbas, and T. Dutoit, "The Emotional Voices Database: Towards controlling the emotion dimension in voice generation systems," 2018, *arXiv:1806.09514*. Accessed: Feb. 8, 2021. [Online]. Available: https://arxiv.org/pdf/1806.09514.pdf

<span aria-hidden="true"><h6><sub><sup><sub><sup>22</sup></sub></sup></sub></h6></span>

22. H. Pajupuu, *Eesti Emotsionaalse Kõne Korpus. V5.* Jun. 12, 2012. Distributed by Center of Estonian Language Resources. Accessed: Feb. 9, 2021. [Online]. doi: https://doi.org/10.15155/EKI.000A.

<span aria-hidden="true"><h6><sub><sup><sub><sup>23</sup></sub></sup></sub></h6></span>

23. L. Kerkeni, C. Cleder, Y. Serrestou, and K. Raoff, *French Emotional Speech Database - Oréau. V2.* Dec. 31, 2020. Distributed by Zenodo. Accessed: Feb. 9, 2021. [Dataset]. doi: https://doi.org/10.5281/zenodo.4405783.

<span aria-hidden="true"><h6><sub><sup><sub><sup>24</sup></sub></sup></sub></h6></span>

24. O. Lahaie and P. Gournay, *Canadian French Emotional Speech Database. V1.1.* 2017. Distributed by Groupe de Recherche sur la Parole et l'Audio. Accessed: Feb. 8, 2021. [Online]. Available: [https://www.gel.usherbrooke.ca/audio/cafe.htm](https://web.archive.org/web/20201129223923/https://www.gel.usherbrooke.ca/audio/cafe.htm)

<span aria-hidden="true"><h6><sub><sup><sub><sup>25</sup></sub></sup></sub></h6></span>

25. F. Burkhardt, A. Paeschke, M. Rolfes, W. Sendlmeier, and B. Weiss, "A database of German emotional speech," in *Proc. INTERSPEECH 2005,* Lisbon, Portugal, Sep. 4–8, 2005. Accessed: Feb. 9, 2021. [Online]. Available: https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.130.8506&rep=rep1&type=pdf

<span aria-hidden="true"><h6><sub><sup><sub><sup>26</sup></sub></sup></sub></h6></span>

26. N. Vryzas, R. Kotsakis, A. Liatsou, C. A. Dimoulas, and G. Kalliris, "Speech emotion recognition for performance interaction," *J. Audio Eng. Soc.,* vol. 66, no. 6, pp. 457–467, Jun. 2018, doi: https://doi.org/10.17743/jaes.2018.0036.

<span aria-hidden="true"><h6><sub><sup><sub><sup>27</sup></sub></sup></sub></h6></span>

27. N. Vryzas, M. Matsiola, R. Kotsakis, C. A. Dimoulas, and G. Kalliris, "Subjective evaluation of a speech emotion recognition interaction framework," in *Proc. Audio Mostly 2018 Sound Immersion and Emotion,* North Wales, United Kingdom, Sep. 12–14, 2018, p. 34. doi: https://doi.org/10.1145/3243274.3243294.

<span aria-hidden="true"><h6><sub><sup><sub><sup>28</sup></sub></sup></sub></h6></span>

28. O. M. Nezami, P. J. Lou, and M. Karami, "ShEMO: A large-scale validated database for Persian speech emotion detection," *Lang. Resour. and Eval.,* vol. 53, no. 1, pp. 1–16, Oct. 8, 2018, doi: https://doi.org/10.1007/s10579-018-9427-x.

<span aria-hidden="true"><h6><sub><sup><sub><sup>29</sup></sub></sup></sub></h6></span>

29. S. Latif, A. Qayyum, M. Usman, and J. Qadir, "Cross lingual speech emotion recognition: Urdu vs. Western languages," 2020, *arXiv:1812.10411*. Accessed Feb. 10, 2021. [Online]. Available: https://arxiv.org/pdf/1812.10411.pdf

<span aria-hidden="true"><h6><sub><sup><sub><sup>30</sup></sub></sup></sub></h6></span>

30. K. Zhou, B. Sisman, R. Liu, and H. Li, "Seen and unseen emotional style transfer for voice conversion with a new emotional speech dataset," 2020, *arXiv:2010.14794v2*. Accessed Mar. 3, 2021. [Online]. Available: https://arxiv.org/pdf/2010.14794.pdf

<span aria-hidden="true"><h6><sub><sup><sub><sup>31</sup></sub></sup></sub></h6></span>

31. C. F. Lima, S. L. Castro, and S. K. Scott, "When voices get emotional: A corpus of nonverbal vocalizations for research on emotion processing," *Behav. Res. Methods,* vol. 45, no. 4, pp. 1234–1245, Feb. 27, 2013, doi: https://doi.org/10.3758/s13428-013-0324-3.

<span aria-hidden="true"><h6><sub><sup><sub><sup>32</sup></sub></sup></sub></h6></span>

32. P. Belin, S. Fillion-Bilodeau, and F. Gosselin, "The Montreal Affective Voices: A validated set of nonverbal affect bursts for research on auditory affective processing," *Behav. Res. Methods,* vol. 40, no. 2, pp. 531–539, May 2008, doi: https://doi.org/10.3758/BRM.40.2.531.

<span aria-hidden="true"><h6><sub><sup><sub><sup>33</sup></sub></sup></sub></h6></span>

33. N. Holz, P. Larrouy-Maestri, and D. Poeppel, *The Variably Intense Vocalizations of Affect and Emotion Corpus (VIVAE). V1.* Oct. 5, 2020. Distributed by Zenodo. Accessed: Feb. 8, 2021. [Dataset]. doi: https://doi.org/10.5281/zenodo.4066235.

<span aria-hidden="true"><h6><sub><sup><sub><sup>34</sup></sub></sup></sub></h6></span>

34. M. Ephratt, "Verbal silence as figure: Its contribution to linguistic theory," *Poznan Stud. Contemporary Linguistics,* vol. 52, no. 1, pp. 43–76, Mar. 17, 2016, doi: https://doi.org/10.1515/psicl-2016-0006.

<span aria-hidden="true"><h6><sub><sup><sub><sup>35</sup></sub></sup></sub></h6></span>

35. D. Kurzon, *Discourse of Silence*. John Benjamins Publishing, Mar. 15, 1998. [Online]. doi: https://doi.org/10.1075/pbns.49

<span aria-hidden="true"><h6><sub><sup><sub><sup>36</sup></sub></sup></sub></h6></span>

36. B. T. Atmaja and M. Akagi, "The effect of silence feature in dimensional speech emotion recognition," Apr. 21, 2020, *arXiv:2003.01277*. Accessed: Sep. 25, 2021. [Online]. Available: https://arxiv.org/pdf/2003.01277.pdf

<span aria-hidden="true"><h6><sub><sup><sub><sup>37</sup></sub></sup></sub></h6></span>

37. F. Roberts, A. L. Francis, and M. Morgan, "The interaction of inter-turn silence with prosodic cues in listener perceptions of ‘trouble’ in conversation," *Speech Communication*, vol. 48, no. 9, pp. 1079–1093, Sep. 2006, doi: https://doi.org/10.1016/j.specom.2006.02.001.

<span aria-hidden="true"><h6><sub><sup><sub><sup>38</sup></sub></sup></sub></h6></span>

38. F. Roberts, P. Margutti, and S. Takano, "Judgments concerning the valence of inter-turn silence across speakers of American English, Italian, and Japanese," *Discourse Processes*, vol. 48, no. 5, pp. 331–354, Jun. 2011, doi: https://doi.org/10.1080/0163853X.2011.558002.

<span aria-hidden="true"><h6><sub><sup><sub><sup>39</sup></sub></sup></sub></h6></span>

39. B. Kort, R. Reilly, and R. W. Picard, "An affective model of interplay between emotions and learning: Reengineering educational pedagogy-building a learning companion," in *Proc. IEEE Int. Conf. Adv. Learn. Technologies*, Madison, WI, USA, Aug. 6–8, 2001, pp. 43–46. doi: https://doi.org/10.1109/ICALT.2001.943850.

<span aria-hidden="true"><h6><sub><sup><sub><sup>40</sup></sub></sup></sub></h6></span>

40. R. L. Mandryk and M. S. Atkins, "A fuzzy physiological approach for continuously modeling emotion during interaction with play technologies," *Int. J. Human-Comput. Stud.*, vol. 65, no. 4, pp. 329–347, Apr. 2007, doi: https://doi.org/10.1016/j.ijhcs.2006.11.011.

<span aria-hidden="true"><h6><sub><sup><sub><sup>41</sup></sub></sup></sub></h6></span>

41. W. A. P. van Tilburg and E. R. Igou, "Boredom begs to differ: Differentiation from other negative emotions," *Emotion*, vol. 17, no. 2, pp. 309–322, 2017, doi: https://doi.org/10.1037/emo0000233.

<span aria-hidden="true"><h6><sub><sup><sub><sup>42</sup></sub></sup></sub></h6></span>

42. K. R. Scherer, R. Banse, H. G. Wallbott, and T. Goldbeck, "Vocal cues in emotion encoding and decoding," *Motivation and Emotion*, vol. 15, no. 2, pp. 123–148, 1991, doi: https://doi.org/10.1007/BF00995674.

<span aria-hidden="true"><h6><sub><sup><sub><sup>43</sup></sub></sup></sub></h6></span>

43. M. K. Noordewier and E. van Dijk, "Curiosity and time: From not knowing to almost knowing," *Cognition and Emotion,* vol. 31, no. 3, pp. 411–421, Apr. 2017, doi: https://doi.org/10.1080/02699931.2015.1122577.

<span aria-hidden="true"><h6><sub><sup><sub><sup>44</sup></sub></sup></sub></h6></span>

44. L. L. F. van Lieshout, I. J. Traast, F. P. de Lange, and R. Cools, "Curiosity or savouring? Information seeking is modulated by both uncertainty and valence," *PLoS One*, vol. 16, no. 9, p. e0257011, Jan. 2021, doi: https://doi.org/10.1371/journal.pone.0257011.

<span aria-hidden="true"><h6><sub><sup><sub><sup>45</sup></sub></sup></sub></h6></span>

45. D. D. Shin and S. Kim, "Homo curious: Curious or interested?," *Educational Psychol. Rev.*, vol. 31, no. 4, pp. 853–874, Dec. 2019, doi: https://doi.org/10.1007/s10648-019-09497-x.

<span aria-hidden="true"><h6><sub><sup><sub><sup>46</sup></sub></sup></sub></h6></span>

46. A. Koch, H. Alves, T. Krüger, and C. Unkelbach, "A general valence asymmetry in similarity: Good is more alike than bad," *J. Exp. Psychol.: Learn., Memory, and Cognition*, vol. 42, no. 8, pp. 1171–1192, 2016, doi: https://doi.org/10.1037/xlm0000243.

<span aria-hidden="true"><h6><sub><sup><sub><sup>47</sup></sub></sup></sub></h6></span>

47. M. Neta, F. C. Davis, and P. J. Whalen, "Valence resolution of facial expressions using an emotional oddball task," *Emotion*, vol. 11, no. 6, pp. 1425–1433, Dec. 2011, doi: https://doi.org/10.1037/a0022993.

<span aria-hidden="true"><h6><sub><sup><sub><sup>48</sup></sub></sup></sub></h6></span>

48. M. K. Noordewier and S. Breugelmans, "On the valence of surprise," *Cognition and Emotion,* vol. 27, no. 7, pp. 1326–1334, Apr. 2013, doi: https://doi.org/10.1080/02699931.2013.777660.

<span aria-hidden="true"><h6><sub><sup><sub><sup>49</sup></sub></sup></sub></h6></span>

49. M. K. Noordewier, S. Topolinski, and E. V. Dijk, "The temporal dynamics of surprise," *Social and Personality Psychol. Compass*, vol. 10, no. 3, pp. 136–149, 2016, doi: https://doi.org/10.1111/spc3.12242.

[^top](#Unified-Multilingual-Dataset-of-Emotional-Human-Utterances)
