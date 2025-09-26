def count_words(text: str) -> dict[str, int]:
    """Counts the number of times that each word appears in the text.
    
    Parameters
    ----------
    text : str
        The text in which we want to count words
    
    Returns
    -------
    dict[str, int]
        Maps from each word to the number of times it appears in the text.
    """
    words = text.split(" ")   
    counts: dict[str, int] = {}
    
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    
    return counts
