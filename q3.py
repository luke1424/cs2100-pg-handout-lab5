def next_letter_frequency(prompt: str, counts: dict[str, int]) -> dict[str, int]:
    """Computes the frequency of possible next characters given a prompt.
    
    Given a string `prompt` of length n-1 and a dictionary of n-gram counts,
    this function returns a dictionary mapping each possible next character
    to the number of times it follows the given prompt in the text.
    
    Parameters
    ----------
    prompt : str
        A string of length n-1 representing the preceding characters.
    counts : dict[str, int]
        A dictionary mapping character n-grams (length n) to their counts,
        as produced by count_char_n_grams().
    
    Returns
    -------
    dict[str, int]
        A dictionary where the keys are the possible next characters (the nth
        character in each n-gram starting with `prompt`), and the values are
        how many times that character follows the prompt in the text.
    """
    result: dict[str, int] = {}
    for ngram, freq in counts.items():
        if ngram.startswith(prompt):  
            next_char = ngram[-1]     
            result[next_char] = result.get(next_char, 0) + freq
    return result

