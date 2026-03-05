def uses_only(word, letters):
    """Does word use only the allowed letters?"""
    for letter in word:
        if letter not in letters:
            return False
    return True

#print(uses_only('cake', 'kcboela'))
#print(uses_only('babson', 'kcboela'))

def must_use(word, letters):
    """Does word use all of the required letters at least once?"""
    for letter in letters:
        if letter not in word:
            return False
    return True

#print(must_use('cake', 'a'))

def is_valid_word(word, required_letters, allowed_letters):
    """Is word valid based on required and allowed letters?"""
    return must_use(word, required_letters) and uses_only(word, allowed_letters)

def is_english_word(word, word_set):
    """Check if word is in the English word set."""
    return word in word_set


def load_word_list(path):
    """Return a set containing all words from file at path."""
    try:
        with open(path, 'r') as f:
            return {line.strip().lower() for line in f if line.strip()}
    except FileNotFoundError:
        print(f"Word list file not found: {path}")
        return set()


def is_valid_word(word, required_letters, allowed_letters, word_set):
    """Is word valid based on required/allowed letters and english list."""
    word = word.lower()
    return (
        is_english_word(word, word_set)
        and must_use(word, required_letters)
        and uses_only(word, allowed_letters)
    )


if __name__ == '__main__':
    # example usage
    allowed = 'kcboela'
    required = 'a'
    word_set = load_word_list('data/words.txt')

    print(uses_only('cake', allowed))      # should be True
    print(uses_only('babson', allowed))    # False
    print(must_use('cake', required))      # True
    print(is_english_word('cake', word_set))
    print(is_english_word('xyzzy', word_set))
    print(is_valid_word('cake', required, allowed, word_set))