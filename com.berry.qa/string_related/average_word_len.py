"""
Average Word Length
# For a given sentence, return the average word length.
# Note: Remember to remove punctuation first.
"""

sentence = "Hi this is Bhaskar Berry! Welocme to basic Python"


def avg_word_count(sentence):
    punctuations = "!@#$%^&*()"

    for p in punctuations:
        sentence = sentence.replace(p, '')

    words = sentence.split()

    return round(sum(len(word) for word in words) / len(words), 2)


print("Average word length : ", avg_word_count(sentence))
