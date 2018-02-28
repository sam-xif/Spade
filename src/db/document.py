"""
document.py
Contains a simple class that represents a Twitter-esque comment, with hashtags.
"""


class Document:
    """
    This class essentially takes in a list of tokenized words and stores two lists, one containing the words
    in the order that they appear and a set containing any hashtags in the comment.
    """

    def __init__(self, words, tags, raw):
        """
        words is expected to be a parameter of tokenized words in the comment
        They can be processed further.
        """

        self.words = words
        self.tags = tags
        self.raw = raw

    @classmethod
    def create_from_raw_list(cls, words, raw):
        d = Document([], set(), raw)
        for w in words:
            if w.startswith('#'):
                d.tags.add(w)
            else:
                d.words.append(w)
        return d

    def export(self):
        """
        Convert this object into a database model
        """
        pass
