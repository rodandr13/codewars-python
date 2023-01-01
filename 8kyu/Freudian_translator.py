"""
def to_freud(sentence):
    return ' '.join('sex' for _ in sentence.split())
"""
"""
def to_freud(s):
    return (len(s.split()) * "sex ").strip()
"""


def to_freud(sentence):
    sentence = sentence.split()
    result = len(sentence) * " sex"
    return result.strip()
