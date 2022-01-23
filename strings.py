vocab_words = ['en', 'lighten', 'joy', 'close']

def add_prefix_un(word):
    """

    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """
    new_word = "un" + word
    return(new_word)

def make_word_groups(vocab_words):
    """

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """
    prefix = vocab_words[0]
    new_list = [prefix]
    for words in vocab_words[1:]:
        words = prefix + words
        new_list.append(words)
        
    new_list = ' :: '.join(new_list)
    return(new_list)

def adjective_to_verb(sentence, index):
    """

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """
    sentence = sentence.split()
    word = sentence[index]
    word = word + 'en'
    return(word)

print(make_word_groups(vocab_words))

def remove_suffix_ness(word):
    word = word[:-4]
    if word[-1] == 'i':
        word = word[:-1]
        word = word +'y'
        return(word)
    else:
        return(word)

print(make_word_groups(vocab_words))
print(adjective_to_verb('I need to make that bright.', -1 ))
print(remove_suffix_ness('Lockness'))