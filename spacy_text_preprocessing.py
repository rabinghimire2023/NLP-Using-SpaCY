"""
Moudle for text preprocessing using Spacy.
    
"""
import spacy

# load the english model 
nlp = spacy.load("en_core_web_sm")

# remove stopwords
def remove_stopwords(text):
    """
    Removes stopwords from the input text using Spacy.

    Args:
        text (str): The input textt from which stopwords will be removed.

    Returns:
        str: The input text with stopwords removed.
    """
    doc = nlp(text)
    filtered_tokens = [token.text for token in doc if not token.is_stop]
    cleaned_text = ' '.join(filtered_tokens)
    return cleaned_text


# tokenize word
def tokenize_text(text):
    """
    Tokenize the input text into words using Spacy.

    Args:
        text (str): The input text to be tokenized.

    Returns:
        list of str: A list of tokens (words) extracted from the input text.
    """
    doc = nlp(text)
    tokens = [token.text for token in doc]
    return tokens


# tokenize sentences
def sentence_tokenize(text):
    """
    Tokenize the input text into sentences using SpaCy.

    Args:
        text (str): The input text to be tokenize into sentences.

    Returns:
        list of str: A list of sentences extracted from the input text.
    """
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    return sentences


# lower casing
def lowercase_text(text):
    """
    Converts the text input text to lowercase.

    Args:
        text (str): The input text to be converted to lowercase.

    Returns:
        str: The input text converted to lowercase.
    """
    lowercase = text.lower()
    return lowercase


# remove punctuation
def remove_punctuation(text):
    """
    Removes punctuation marks from the input text usin SpaCy.

    Args:
        text (str): The input text from which punctuation will be removed.

    Returns:
        str: The input text with punctuation marks removed.
    """
    doc = nlp(text)
    cleaned_text = ' '.join(token.text for token in doc if not token.is_punct)
    return cleaned_text


# stemming
def stem_text(text):
    """
    Stems the words in the input text using Spacy's lemmatization.

    Args:
        text (str): The input text whose words will be removed.

    Returns:
        str: The input text with words stemmed.
    """
    doc = nlp(text)
    stemmed_words = [token.lemma_ for token in doc]
    stemmed_text = ' '.join(stemmed_words)
    return stemmed_text


# lemmatization 
def lemmatize_text(text):
    """
    Lemmatizes the input text using SpaCy.

    Args:
        text (str): The input text to be lemmatized.

    Returns:
        str: The lemmatized text.
    """
    doc = nlp(text)
    lemmatized_words = [token.lemma_ for token in doc]
    lemmatized_text = ' '.join(lemmatized_words)
    return lemmatized_text
     

# POS Tagging
def pos_tag_text(text):
    """
    Performs Part-of-Speech (POS) tagging on the input text using Spacy.

    Args:
        text (str): The input text in which POS tags will be recognized.

    Returns:
        list of tuple: A list of (word, POS tag) pairs for each word in the input text.
    """
    doc = nlp(text)
    pos_tags = [(token.text, token.pos_) for token in doc]
    return pos_tags


# named entity recognition
def named_entity_recognition(text):
    """
    Performs Named Entity Recognition (NER) on the input text using SpaCy.

    Args:
        text (str): The input text in which named entities will be recognized.

    Returns:
        list of tuple: A list of (entity text, entity label) pais for each recognized named entity.
    """
    doc = nlp(text)
    named_entities = [(entity.text, entity.label_) for entity in doc.ents]
    return named_entities


if __name__ == "__main__":
    # removing stopwords
    text = "This is an example sentence with some stopwords."
    cleaned_text = remove_stopwords(text)
    print("Original Text:", text)
    print("Text with Stopwords Removed:", cleaned_text)
    
    # tokenize words
    text = "This is an example sentence."
    tokens = tokenize_text(text)
    print("Original Text:",text)
    print("Tokens:",tokens)
    
    # tokenize sentences
    text = "This is the first sentence. And here is the second one!"
    sentences = sentence_tokenize(text)
    print("Original Text:",text)
    print("Sentences:",sentences)
    
    # lower casing
    text = "This Is An Example Sentence."
    lowercase = lowercase_text(text)
    print("Original Text:", text)
    print("Lowercased Text:", lowercase)
    
    # removing punctuation
    text = "Hello, world! This is an example."
    cleaned_text = remove_punctuation(text)
    print("Original Text:", text)
    print("Text with Punctuation Removed:", cleaned_text)
    
    # Stemming
    text = "running quickly in the park"
    stemmed_text = stem_text(text)
    print("Original Text:", text)
    print("Stemmed Text:", stemmed_text)
    
    # lemmatizing
    text = "I am running in the park"
    lemmatized_text = lemmatize_text(text)
    print("Original Text:", text)
    print("Lemmatized Text:", lemmatized_text)
    
    # POS tagging
    text = "I am running in the park"
    pos_tags = pos_tag_text(text)
    print("Original Text:", text)
    print("POS Tags:", pos_tags)
    
    # Named entity recognition
    text = "Apple Inc. is headquartered in Cupertino, California."
    named_entities = named_entity_recognition(text)
    print("Original Text:", text)
    print("Named Entities:", named_entities)
    
    
    
    
    