
"""Functions to output features from list of tokens and get predicted labels from classifiers"""

import pandas as pd
import numpy as np


def find_features(words):
    """Takes as input a list of tokenized words and outputs features"""
    features = {}
    for w in word_features:
        features[w] = (w in words) # the dict has the word as key and boolean as value
    return features


def classify_list(classifier, token_list):
    """Get predicted label from classifier"""
    values = []
    for nested_list in token_list:
        value = classifier.classify(find_features(nested_list))
        values.append(value)
    return values