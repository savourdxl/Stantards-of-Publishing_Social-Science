<img src="https://github.com/crahal/PopStudies_Review/blob/master/assets/cover_picture.png" width="900"/>


# Changing Stantards of Quantitative Social Science Publishing

[![Generic badge](https://img.shields.io/badge/Python-3.7-<red>.svg)](https://shields.io/) [![Generic badge](https://img.shields.io/badge/License-MIT-orange.svg)](https://shields.io/) [![Generic badge](https://img.shields.io/badge/Maintained-Yes-purple.svg)](https://shields.io/) [![Generic badge](https://img.shields.io/badge/BuildPassing-Yes-red.svg)](https://shields.io/) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4553236.svg)](https://doi.org/10.5281/zenodo.4553236)
---

## Introduction

This is a repository to accompany a scientometric review of the journal European Societies, written by Melinda C. Mills and Charles Rahal, entitled 'Disrupting Demography: A study of Population Studies'. It analyzes the ~2000 papers published by the journal in honour of the journal. Links to open-access (OSF) versions of the Paper will follow in due course. The basic analysis is divided into two parts.

## Pre-reqs

The library tries to minimize the number of pre-requisite installations outside of the standard library, and we recommend an Anaconda installation and a virtual environment to provide a managed package of comprehensive tools. However, a couple are necessary, including a range of modules found in the requirements.txt file (generated by pipreqs). Important libraries which the work couldnt be done without include [pandas](https://github.com/pandas-dev/pandas), [matplotlib](https://github.com/matplotlib/matplotlib), [NetworK-X](https://github.com/networkx), and [NLTK](https://github.com/nltk/nltk). The un-supervised LDA analysis is made possible with the help of [MALLET](http://mallet.cs.umass.edu/topics.php) (the 'MAchine Learning for LanguagE Toolkit'). Gender inference is done with a combination of [Gender-Guesser](https://github.com/lead-ratings/gender-guesser) and [Gender-Detector](https://github.com/malev/gender-detector).

## Data

The data originates from the [Scopus APIs](https://dev.elsevier.com/), using the appropriate ISSN (00324728) of the journal and the Search API. To recreate the dataset, first clone the repo:

```git clone https://github.com/crahal/PopStudies_Review.git```

```cd PopStudies_Review/src```

```python popstudies_scraper.py```

The functions in ```popstudies_preprocessor.py``` clean the data and prepare it for analysis. The formatted notebook which calls the analysis from ```popstudies_analysis.py``` is ```popstudies_notebook.ipynb```.

### License
This work is free. You can redistribute it and/or modify it under the terms of the MIT license. It comes without any warranty, to the extent permitted by applicable law.

### Acknowledgments
Research assistance for the manual data curation was provided by Sofia Gieystor and Jiani Yan. Funding generously provided by the Leverhulme Trust, Leverhulme Centre for Demographic Science, and Nuffield College. We're also grateful to Anne Shepherd at the Population Investigation Committee for invaluable knowledge surrounding the journal. As always, all errors remain our own.


#### TODO:

* Docstrings, docstrings, docstrings

Last updated: 2021-05-17
