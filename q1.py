"""Utilities for simple word-counting used in the lab exercises.

This module provides a single function `count_words` that returns a
mapping from words (normalized to lowercase and stripped of punctuation)
to their frequencies in a given text.
"""

from collections import Counter
import string

def count_words(text: str) -> dict[str, int]:
    """Counts the number of times that each word appears in the text.

    This function ignores case and punctuation.

    Parameters
    ----------
    text : str
        The text in which we want to count words

    Returns
    -------
    dict[str, int]
        Maps from each word (lowercased, without punctuation)
        to the number of times it appears in the text.
    """
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    return dict(Counter(words))
