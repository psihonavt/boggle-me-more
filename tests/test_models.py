
import pytest

from src.boggle.models import BoggleWordsFinder
from src.boggle.domain import BoggleBoard


@pytest.mark.parametrize('board, expected_results, word_length', [
    pytest.param([["X", "Q", "A", "E"],
                  ["Z", "O", "T", "S"],
                  ["I", "N", "D", "L"],
                  ["Y", "R", "U", "K"]],
                 {'ASTONY',
                  'KUNDRY',
                  'SETON',
                  'DOTES',
                  'DOATS',
                  'NOTES',
                  'RIOTS',
                  'LUNTS',
                  'ATONY',
                  'INDULTO',
                  'IOTAS',
                  'RINDS',
                  'DURION',
                  'STOND',
                  'DUNTS',
                  'STOAE',
                  'UNDRY',
                  'NIOTA',
                  'RUNTS',
                  'RYNDS',
                  'INDULT',
                  'AOTES',
                  'INDULTS',
                  'YIRDS',
                  'DURIO',
                  'ASTOND',
                  'STONY',
                  'IZOTE',
                  'ZONTA',
                  'DULSE',
                  'DRUNT'}, 5
                 ),
    # add more cases ... (use as a solver https://www.dcode.fr/boggle-solver-4x4)
])
def test(words_trie, board, expected_results, word_length):
    bboard = BoggleBoard(board)
    solver = BoggleWordsFinder(board=bboard, trie=words_trie, word_length=word_length)
    found_words = set(solver.find_words())
    assert found_words == expected_results, found_words | expected_results
