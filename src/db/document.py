"""
document.py
Contains a simple class that represents a Twitter-esque comment, with hashtags.
"""


class Document:
    """
    This class essentially takes in a list of tokenized words and stores two lists, one containing the words
    in the order that they appear and a set containing any hashtags in the comment.
    """

    def __init__(self, words, raw):
        """
        words is expected to be a parameter of tokenized words in the comment
        They can be processed further.
        """

        self.words = []
        self.tags = set()
        self.raw = raw
        for w in words:
            if w.startswith('#'):
                self.tags.add(w)
            else:
                self.words.append(w)
