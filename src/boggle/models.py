#code partially taken from
#https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1
from copy import deepcopy

from src.boggle.domain import SolvedBoggleBoard


class _TrieNode(object):
    """
    Our trie node implementation. Very basic. but does the job
    """

    def __init__(self, char: str):
        self.char = char
        self.children = []
        # Is it the last character of the word.`
        self.word_finished = False
        # How many times this character appeared in the addition process
        self.counter = 1


class WordsTrie:

    def __init__(self):
        self._root = _TrieNode("*")

    def add(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self._root
        for char in word:
            found_in_child = False
            # Search for the character in the children of the present `node`
            for child in node.children:
                if child.char == char:
                    # We found it, increase the counter by 1 to keep track that another
                    # word has it as well
                    child.counter += 1
                    # And point the node to the child that contains this char
                    node = child
                    found_in_child = True
                    break
            # We did not find it so add a new chlid
            if not found_in_child:
                new_node = _TrieNode(char)
                node.children.append(new_node)
                # And then point node to the new child
                node = new_node
        # Everything finished. Mark it as the end of a word.
        node.word_finished = True

    def find_prefix(self, prefix):
        """
        :type prefix: str
        :rtype: tuple[bool, bool]
        """
        node = self._root
        # If the root node has no children, then return False.
        # Because it means we are trying to search in an empty trie
        if not self._root.children:
            return False, 0
        for char in prefix:
            char_not_found = True
            # Search through all the children of the present `node`
            for child in node.children:
                if child.char == char:
                    # We found the char existing in the child.
                    char_not_found = False
                    # Assign node as the child containing the char and break
                    node = child
                    break
            # Return False anyway when we did not find a char.
            if char_not_found:
                return False, 0
        # Well, we are here means we have found the prefix. Return true to indicate that
        # And also the counter of the last node. This indicates how many words have this
        # prefix
        return True, node.word_finished


class BoggleWordsFinder:

    _WORD_LENGTH = 3

    def __init__(self, board, trie, word_length=_WORD_LENGTH):
        """
        :type board: src.boggle.domain.BoggleBoard
        :type trie: WordsTrie
        """
        self._board = board
        self._trie = trie
        self._collected_words = set()
        self._word_length = word_length

    def find_words(self):
        """
        :rtype: list[str]
        """
        for col in range(self._board.width):
            for row in range(self._board.height):
                vmap = [[False for _ in range(self._board.width)] for _ in range(self._board.height)]
                self._search_prefixes(vmap, row, col, "")
        return list(self._collected_words)

    def _search_prefixes(self, vmap, row, col, current_prefix):
        try:
            if col < 0 or row < 0:
                raise IndexError()
            maybe_char = self._board.get_char(row, col)
            if not vmap[row][col]:
                vmap[row][col] = True
                current_prefix += maybe_char
                if len(current_prefix) >= self._word_length:
                    prefix_valid, is_complete_word = self._trie.find_prefix(current_prefix)
                    if not prefix_valid:
                        return
                    if is_complete_word:
                        self._collected_words.add(current_prefix)
                for new_x_pos, new_y_pos in [
                    (col + 1, row),  # look right
                    (col - 1, row),  # look left
                    (col, row + 1),  # look above
                    (col, row - 1),  # look below
                    (col + 1, row + 1),  # look diagonal up and right
                    (col - 1, row - 1),  # look diagonal down and left
                    (col + 1, row - 1),  # look diagonal down and right
                    (col - 1, row + 1),  # look diagonal up and left
                ]:
                    self._search_prefixes(deepcopy(vmap), new_y_pos, new_x_pos, current_prefix)
        except IndexError:
            return


class BoggleSolver:

    def __init__(self, words_trie):
        """
        :type words_trie: WordsTrie
        """
        self._trie = words_trie

    def solve(self, board):
        """
        :type board: src.boggle.domain.BoggleBoard
        :rtype: src.boggle.domain.SolvedBoggleBoard
        """
        words = BoggleWordsFinder(board, self._trie).find_words()
        return SolvedBoggleBoard(words)
