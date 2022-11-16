def break_words(stuff):
    """This function will break up words for us"""
    words = stuff.split(" ")
    return words


def sort_words(words):
    """Sorts the words."""
    words = break_words(words)
    return sorted(words)


def print_first_word(words):
    """Print the first word after popping it off"""
    words = break_words(words)
    words = words.pop(0)
    print(words)


def print_last_word(words):
    """Print the last word after popping it off"""
    words = break_words(words)
    words = words.pop(-1)
    print(words)
