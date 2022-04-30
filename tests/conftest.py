from importlib import resources

import pytest

from src.boggle.models import WordsTrie


@pytest.fixture(scope="session")
def words_trie():
    trie = WordsTrie()
    with resources.open_text("src.boggle", "words.csv") as dictionary:
        for word in dictionary.readlines():
            trie.add(word.strip("\n ").upper())
    return trie
