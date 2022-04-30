from __future__ import unicode_literals, absolute_import, division, print_function

from importlib import resources

from src.boggle.models import WordsTrie, BoggleSolver

__all__ = ("BOGGLE_SOLVER", )


_WORDS_TRIE = WordsTrie()
with resources.open_text("src.boggle", "words.csv") as words:
    for word in words.readlines():
        _WORDS_TRIE.add(word.strip("\n ").upper())


BOGGLE_SOLVER = BoggleSolver(_WORDS_TRIE)

