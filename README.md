[![license](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://github.com/santipongth/luke/blob/master/LICENSE)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/kex.svg)](https://pypi.python.org/pypi/luke/)
[![PyPI status](https://img.shields.io/pypi/status/kex.svg)](https://pypi.python.org/pypi/luke/)

# LUKE (Lightweight Unsupervised Keyword Extraction)
LUKE is a lightweight keyword extraction algorithm based on a term weighting scheme with multiple word features, including term frequency, inverse sentence frequency, term different sentence, term position, and term length. The goal is to automatically extract important words and phrases from unstructured text without training data or domain-specific knowledge.

## Benchmark Datasets
The four common benchmark datasets are described to below:
- `SemEval-2010`: This dataset consists of 243 scientific articles with long-length documents from conferences and workshops of the ACM Digital Libraries with author and reader-assigned keyphrase annotations. 
- `NUS`: This contains 211 scientific conference papers with long documents ranging from 4 to 12 pages.
- `Inspec`: This consists of 2,000 short documents from scientific journal abstracts in the areas of computer science and information technology.
- `DUC-2001`: This is a collection of 308 news articles with medium-length newspapers from TREC-9.

### Supported language
Currently algorithms are available only in English, However, this algorithm provides the keyword extraction pipeline, which is easy to customize in other languages.
