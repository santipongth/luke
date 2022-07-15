[![license](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://github.com/santipongth/luke/blob/master/LICENSE)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/kex.svg)](https://github.com/santipongth/luke/)
[![PyPI status](https://img.shields.io/pypi/status/kex.svg)](https://github.com/santipongth/luke/)

# LUKE (Lightweight Unsupervised Keyword Extraction)
LUKE is a lightweight keyword extraction algorithm based on a term weighting scheme with multiple word features, including term frequency, inverse sentence frequency, term different sentence, term position, and term length. The goal is to automatically extract important words and phrases from unstructured text without training data or domain-specific knowledge.

## Motivation

The motivation for this algorithm is to develop a lightweight and robust keyword extraction tool based on the statistical information of words in the original text. This tool could be applied on mobile devices.

## Benchmark Datasets
The four common benchmark datasets are described to below:
- `SemEval-2010`: This dataset consists of 243 scientific articles with long-length documents from conferences and workshops of the ACM Digital Libraries with author and reader-assigned keyphrase annotations. 
- `NUS`: This contains 211 scientific conference papers with long documents ranging from 4 to 12 pages.
- `Inspec`: This consists of 2,000 short documents from scientific journal abstracts in the areas of computer science and information technology.
- `DUC-2001`: This is a collection of 308 news articles with medium-length newspapers from TREC-9.

### Supported language
Currently algorithms are available only in English, However, this algorithm provides the keyword extraction pipeline, which is easy to customize in other languages.

## Citation
To cite KeyBERT in your work, please use the following bibtex reference:

```bibtex
@misc{grootendorst2020keybert,
  author       = {Maarten Grootendorst},
  title        = {KeyBERT: Minimal keyword extraction with BERT.},
  year         = 2020,
  publisher    = {Zenodo},
  version      = {v0.3.0},
  doi          = {10.5281/zenodo.4461265},
  url          = {https://doi.org/10.5281/zenodo.4461265}
}
```

## References
Please cite the following works when using YAKE

<b>In-depth journal paper at Information Sciences Journal</b>

Campos, R., Mangaravite, V., Pasquali, A., Jatowt, A., Jorge, A., Nunes, C. and Jatowt, A. (2020). YAKE! Keyword Extraction from Single Documents using Multiple Local Features. In Information Sciences Journal. Elsevier, Vol 509, pp 257-289. [pdf](https://doi.org/10.1016/j.ins.2019.09.013)

## References
Below, you can find several resources that were used for the creation of KeyBERT
but most importantly, these are amazing resources for creating impressive keyword extraction models:

**Papers**:
* Sharma, P., & Li, Y. (2019). [Self-Supervised Contextual Keyword and Keyphrase Retrieval with Self-Labelling.](https://www.preprints.org/manuscript/201908.0073/download/final_file)

**Github Repos**:
* https://github.com/thunlp/BERT-KPE
* https://github.com/ibatra/BERT-Keyword-Extractor
* https://github.com/pranav-ust/BERT-keyphrase-extraction
* https://github.com/swisscom/ai-research-keyphrase-extraction

**MMR**:
The selection of keywords/keyphrases was modeled after:
* https://github.com/swisscom/ai-research-keyphrase-extraction

**NOTE**: If you find a paper or github repo that has an easy-to-use implementation
of BERT-embeddings for keyword/keyphrase extraction, let me know! I'll make sure to
add a reference to this repo.


## CONTACT

For any question, feel free to create an issue, and we will try our best to solve. \
**If the problem is more urgent**, you can send an email to me at the same time (I check email almost everyday 😉).

```
NAME: Si Sun
EMAIL: s-sun17@mails.tsinghua.edu.cn
```
