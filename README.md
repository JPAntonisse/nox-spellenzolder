
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
| title                                                 | link                                        |   stars |   score | date       |
|:------------------------------------------------------|:--------------------------------------------|--------:|--------:|:-----------|
| Star Wars Armada: Super Star Destroyer (NL)           | <a href="https://www.youtube.com/watch?v=fDiCnbDd6Tg">YouTube</a> |     nan |      10 | 02-09-2019 |
| Codenames (NL) - Vanuit spellenwinkel "Spellenpoort"  | <a href="https://www.youtube.com/watch?v=isuTVvwDt_I">YouTube</a> |       5 |      10 | 10-12-2015 |
| Fury of Dracula - 3rd Edition (NL)                    | <a href="https://www.youtube.com/watch?v=Bk6-AvuEdIg">YouTube</a> |       5 |      10 | 19-12-2016 |
| Magic the Gathering (NL)                              | <a href="https://www.youtube.com/watch?v=AYu5ool4YTo">YouTube</a> |       5 |      10 | 16-10-2016 |
| Sherlock Holmes - Consulting Detective (NL)           | <a href="https://www.youtube.com/watch?v=WIZGG7wepQQ">YouTube</a> |       5 |      10 | 25-06-2015 |
| Legendary Encounters (NL)                             | <a href="https://www.youtube.com/watch?v=NmsICtnjEcg">YouTube</a> |       5 |      10 | 09-02-2015 |
| Detective: A Modern Crime Board Game (NL)             | <a href="https://www.youtube.com/watch?v=WzMpmvzMxN0">YouTube</a> |     nan |       9 | 17-09-2018 |
| Wingspan (NL)                                         | <a href="https://www.youtube.com/watch?v=0Hyi3yOnPUw">YouTube</a> |     nan |       9 | 08-04-2019 |
| De Legenden van Andor "Deel 3" - De Laatste Hoop (NL) | <a href="https://www.youtube.com/watch?v=KYTX07UbAqY">YouTube</a> |     nan |       9 | 15-01-2018 |
| Lords of Hellas (NL)                                  | <a href="https://www.youtube.com/watch?v=fZxtV39jmHs">YouTube</a> |     nan |       9 | 05-05-2018 



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

