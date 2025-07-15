def count_words(sentence):
    """
    Counts the number of words in a given sentence.

    Args:
        sentence: the input string (a sentence)

    Returns:
        the number of words in the sentence
    """
    n = len(sentence)
    if n == 0:
        return 0
    else:
        counter = 0
        i = 0
        while i < n:
            # Skip spaces
            while i < n and sentence[i] == ' ':
                i += 1
            # Count word if not end of sentence
            if i < n:
                counter += 1
                while i < n and sentence[i] != ' ':
                    i += 1
        return counter
        
#   return len(sentence.split(" "))


if __name__ == '__main__':
    sentence = "This is a sample sentence for counting words."
    word_count = count_words(sentence)
    print(word_count)  # 8 should be printed
