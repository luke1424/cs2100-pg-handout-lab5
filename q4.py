import random

def generate_next_char(prompt: str, counts: dict[str, int]) -> str:
    """Generates the next character given a prompt and n-gram counts.
    
    This function uses the character n-gram counts to probabilistically
    choose the next character following a given (n-1)-character prompt.
    
    Parameters
    ----------
    prompt : str
        A string of length n-1 representing the preceding characters.
    counts : dict[str, int]
        A dictionary mapping n-grams (length n strings) to their counts,
        as produced by count_char_n_grams().
    
    Returns
    -------
    str
        The next character, chosen randomly based on the frequency of 
        observed n-grams. If no n-grams start with the prompt, a random
        lowercase letter ('a'–'z') is returned.
    """
    options = next_letter_frequency(prompt, counts)

    if not options:
        # 没有匹配 n-gram，就随机返回 a–z 的字母
        return chr(random.randint(ord('a'), ord('z')))
    
    # 按照频率加权随机选择
    letters = list(options.keys())
    weights = list(options.values())
    return random.choices(letters, weights=weights, k=1)[0]
