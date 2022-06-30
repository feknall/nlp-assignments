# Spell Correction Using Ngram Language Model
This project uses Ngram language model to do spell correction over APPLING1DAT.643 dataset which is part of Birkbec corpus.

## Project Structure
The misspelled dataset, `APPLING1DAT.643` is stored in `data/APPLING1DAT.643`.

`misspelled.py` reads `APPLING1DAT.643` from the file and returns a python object.

`ngram.py` uses `nltk` library to train an N-gram model and suggesting next words based on a history.

`evaluate_success_at.py` passes news genre of Brown dataset to `ngram.py` to train a model. Then, finds s@k by using `pytrec_eval` library for the misspelled words, `misspelled.py`, according to the suggestions of the trained model.

## Installation
This project is based on `python 3.8.12` and `conda`.
Install dependencies by using `conda`:

```
conda env create -f environment.yml
```
## How to Run
Run:

```
python evaluate_success_at.py
```

Output:
```
Start training 1-gram
Finish training 1-gram
N is: 1
success_1 average: 0.0, total: 0.0 success_5 average: 0.0, total: 0.0 success_10 average: 0.0, total: 0.0
Start training 2-gram
Finish training 2-gram
sentence: ['to'], make
sentence: ['I'], thought
sentence: ['they'], were
sentence: ['the', 'most'], famous
N is: 2
success_1 average: 0.0, total: 0.0 success_5 average: 0.015306122448979591, total: 3.0 success_10 average: 0.02040816326530612, total: 4.0
Start training 3-gram
Finish training 3-gram
sentence: ['on', 'and'], off
sentence: ['to'], make
sentence: ['I'], thought
sentence: ['they'], were
sentence: ['the', 'man', 'had'], tried
sentence: ['what', 'had'], happened
sentence: ['what', 'had'], happened
N is: 3
success_1 average: 0.01020408163265306, total: 2.0 success_5 average: 0.025510204081632654, total: 5.0 success_10 average: 0.030612244897959183, total: 6.0
Start training 5-gram
Finish training 5-gram
sentence: ['on', 'and'], off
sentence: ['to'], make
sentence: ['I'], thought
sentence: ['they'], were
sentence: ['the', 'man', 'had'], tried
sentence: ['what', 'had'], happened
sentence: ['what', 'had'], happened
N is: 5
success_1 average: 0.01020408163265306, total: 2.0 success_5 average: 0.025510204081632654, total: 5.0 success_10 average: 0.030612244897959183, total: 6.0
Start training 10-gram
Finish training 10-gram
sentence: ['on', 'and'], off
sentence: ['to'], make
sentence: ['I'], thought
sentence: ['they'], were
sentence: ['the', 'man', 'had'], tried
sentence: ['what', 'had'], happened
sentence: ['what', 'had'], happened
N is: 10
success_1 average: 0.01020408163265306, total: 2.0 success_5 average: 0.025510204081632654, total: 5.0 success_10 average: 0.030612244897959183, total: 6.0
```