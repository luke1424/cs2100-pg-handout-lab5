"""Character n-gram helpers (q4).

This module provides a function to generate the next character given a
prompt and n-gram counts.
"""

import random

def generate_next_char(prompt: str, counts: dict[str, int]) -> str:
    """Generate the next character given a (n-1)-length prompt and n-gram counts.

    If no n-gram starts with the prompt (or counts is empty / prompt length mismatches),
    return a random lowercase letter ('a'–'z').
    """
    # 1) 推断 n（n-gram 的长度）；counts 为空时退化为随机器
    if not counts:
        return chr(random.randint(ord("a"), ord("z")))
    n_size = len(next(iter(counts)))  # 从任意键的长度得到 n

    # 2) prompt 长度不等于 n-1，则无法匹配，直接随机回退
    if len(prompt) != n_size - 1:
        return chr(random.randint(ord("a"), ord("z")))

    # 3) 收集所有以 prompt 开头的 n-gram 的末字符频次
    options: dict[str, int] = {}
    for ngram, freq in counts.items():
        if ngram.startswith(prompt):
            next_char = ngram[-1]
            options[next_char] = options.get(next_char, 0) + freq

    # 4) 加权随机选择一个下一个字符；没有可选项则随机回退
    if not options:
        return chr(random.randint(ord("a"), ord("z")))
    letters = list(options.keys())
    weights = list(options.values())
    return random.choices(letters, weights=weights, k=1)[0]
