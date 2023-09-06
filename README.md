
# NLP using SpaCY

## Introduction
[spaCy](https://spacy.io/) is an open source softare library for advanced natural language processing system, written in the programming languages Python and Cython. It mainly focuses on providing software for production usage. SpaCy provides pre-trained models for a wide range of languages, making it a popular choice for tasks such as tokenization, part-of-speech tagging, named entity recognition, dependency parsing, and more.

### Key features and components of SpaCy:

- Tokenization: SpaCy can efficiently split text into individual words or tokens. It handles complex tokenization tasks, such as splitting contractions and handling punctuation.

- Part-of-Speech Tagging: SpaCy can assign parts of speech (e.g., nouns, verbs, adjectives) to each token in a text.

- Named Entity Recognition (NER): SpaCy can identify and classify entities in text, such as person names, locations, dates, and more.

- Dependency Parsing: SpaCy can analyze the grammatical structure of a sentence and determine the relationships between words, representing them as a dependency tree.

- Lemmatization: It can also perform lemmatization, which reduces words to their base or root forms. For example, "running" becomes "run."

- Word Vectors: SpaCy includes pre-trained word vectors, which can be used for various NLP tasks, including text similarity and word embeddings.

- Customization: Users can train their own models with SpaCy or modify existing models to suit their specific needs.

- Language Support: SpaCy supports a variety of languages and has pre-trained models for multiple languages.

- Integration: It can be easily integrated into Python applications and workflows, making it a popular choice for NLP projects.

- Performance: SpaCy is known for its speed and efficiency, making it suitable for processing large datasets and real-time applications.

## Installation of the spaCy
Activating virtual environments
```
py -m venv env
.\env\Scripts\activate
```
Installing spaCy
```
pip install -U pip setuptools wheel
pip install -U spacy
```
## Loading SpaCy's English Language Model for Natural Language Processing
SpaCy provides pre-trained language models for multiple languages and domains. In this case, we're loading the English language model, specifically the "en_core_web_sm" model.
```python
import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")
```
## Installation of the module
- Git clone
```
git clone git@github.com:rabinghimire2023/NLP-Using-SpaCY.git
```
- Installing requirements
```
pip install -r requirements.txt
```

## References
1. [spaCy](https://spacy.io/)
2. [spaCy: Everything you need to know](https://spacy.io/usage/spacy-101)
