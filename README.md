# Pormalizer

There are different unicode for lots of persian characters and for computers do not understand this. So before any NLP
task first we need to normalize our text and come to singular form for any characters. We also remove any non-alphabet
characters and all change all white-space characters into a single space.

## Installation

Simply you can install it from PyPi by following command:

```bash
pip install -U pormalizer
```

or if you prefer the latest development version, you can install it from the source:

```bash
git clone https://github.com/xurvan/pormalizer.git
cd pormalizer
python setup.py install
```

## Quickstart

A very simple usage could be like:

```python
from pormalizer import Pormalizer

pormalizer = Pormalizer()

pormalizer.normalize("متن امتحانی")

```