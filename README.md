
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

<a href="https://www.youtube.com/channel/UCtzMObnv92ni0T_8CHGtDag" target="_BLANK">Nox' Spellenzolder</a> is a Dutch Youtuber giving reviews of boardgames and scoring them. With the help of <a href="https://github.com/JPAntonisse/nox-spellenzolder-rating">JPAntonisse/nox-spellenzolder-rating</a> a complete list of scoring is achieved.



## Dataset
The complete ranking of Nox' boardgames is available in the dataset ```dataset.csv```. 

```code
title;link;id;stars;score
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
The extraction process of the scores is limited to the caption translation of Youtube, therefore, it is prone to mistakes during scoring. The correctness of this dataset is estimated, by sampling, to be ~80%. Because of importance to the top-10, the scores with ```10``` are manually checked and corrected where necessary.  



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

