
<p align="center">
<img src="./images/preview.png"/> <br />
<span>Nox'Spellenzolder Boardgames Scoring dataset.</span>
</p>

<p align="center">
  <a href="#installation">Installation</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#usage">Usage</a>
</p>

## About

<a href="https://www.youtube.com/channel/UCtzMObnv92ni0T_8CHGtDag" target="_BLANK">Nox' Spellenzolder</a> is a Dutch Youtuber giving reviews of boardgames and scoring them. With the help of <a href="https://github.com/JPAntonisse/nox-spellenzolder-rating">JPAntonisse/nox-spellenzolder-rating</a> a list of boardgames with Nox' score is now available under ```results/dataset.csv```.



## Top 10
| title                                                | link                                        |  stars  |score ↓¹ | date ↓²             |
|:-----------------------------------------------------|:--------------------------------------------|--------:|--------:|:--------------------|
| Star Wars Armada: Super Star Destroyer (NL)          | <a href="https://www.youtube.com/watch?v=fDiCnbDd6Tg">YouTube</a> |     nan |      10 | 2019-02-09 00:00:00 |
| Fury of Dracula - 3rd Edition (NL)                   | <a href="https://www.youtube.com/watch?v=Bk6-AvuEdIg">YouTube</a> |       5 |      10 | 2016-12-19 00:00:00 |
| Magic the Gathering (NL)                             | <a href="https://www.youtube.com/watch?v=AYu5ool4YTo">YouTube</a> |       5 |      10 | 2016-10-16 00:00:00 |
| Codenames (NL) - Vanuit spellenwinkel "Spellenpoort" | <a href="https://www.youtube.com/watch?v=isuTVvwDt_I">YouTube</a> |       5 |      10 | 2015-10-12 00:00:00 |
| Legendary Encounters (NL)                            | <a href="https://www.youtube.com/watch?v=NmsICtnjEcg">YouTube</a> |       5 |      10 | 2015-09-02 00:00:00 |
| Sherlock Holmes - Consulting Detective (NL)          | <a href="https://www.youtube.com/watch?v=WIZGG7wepQQ">YouTube</a> |       5 |      10 | 2015-06-25 00:00:00 |
| 5-Minute Mystery (NL)                                | <a href="https://www.youtube.com/watch?v=XyDy0reI9LI">YouTube</a> |     nan |       9 | 2020-09-23 00:00:00 |
| It's a Wonderful World (NL)                          | <a href="https://www.youtube.com/watch?v=eHmLxN1dxpk">YouTube</a> |     nan |       9 | 2020-08-28 00:00:00 |
| Detective: L.A. Crimes & Dig Deeper (NL)             | <a href="https://www.youtube.com/watch?v=Dw6IVfFFhJs">YouTube</a> |     nan |       9 | 2020-08-27 00:00:00 |
| De Crew (NL)                                         | <a href="https://www.youtube.com/watch?v=woJbhpMOOEo">YouTube</a> |     nan |       9 | 2020-06-30 00:00:00 |



## Dataset
The complete ranking of Nox' boardgames is available in the dataset ```results/dataset.csv```.  The available columns in the datasets are listed below. The only thing to note is that the columns 'stars' is a rating out of 5, that is normalized to score (out of 10). This is due to legacy videos graded with stars instead of score.

```code
title;link;id;stars;score;date
```

### Statistics

| variable: score  | dtype: float64 |
| ------------- | ------------- |
|count | 1110.000000|
|mean | 6.289189|
|std |  1.807252|
|min |  2.0|
|25% |  6.00|
|50% |  7.0|
|75% |  8.0|
|max | 10.0|

### limits
The extraction process of the scores is limited to the caption translation of Youtube, therefore, it is prone to mistakes during scoring. The correctness of this dataset is estimated, by sampling, to be ~80%. Because of importance to the top-10, the scores with ```10.0``` are manually checked and corrected where necessary.  

## Installation

```console
# clone the repo
$ git clone https://github.com/JPAntonisse/nox-spellenzolder-rating.git

# install the requirements
$ python3 -m pip install -r requirements.txt
```


## Usage

```console
$ python3 noxdataset
```

