"""Character n-gram helpers (q2).

This module provides a utility to count character n-grams in a string.
"""


def count_char_n_grams(text: str, n_size: int = 3) -> dict[str, int]:
    """Count the frequency of character n-grams in the given text.

    An n-gram is a sequence of n consecutive characters in the string.
    For example, with text = "Rasika" and n = 4, the n-grams are:
    "Rasi", "asik", and "sika".

    Parameters
    ----------
    text : str
        The text in which we want to count character n-grams.
    n_size : int, optional
        The length of each n-gram (default is 3).

    Returns
    -------
    dict[str, int]
        A dictionary mapping each character n-gram to the number of
        times it appears in the text.
    """
    counts: dict[str, int] = {}
    for i in range(len(text) - n_size + 1):
        ngram = text[i : i + n_size]
        counts[ngram] = counts.get(ngram, 0) + 1
    return counts
