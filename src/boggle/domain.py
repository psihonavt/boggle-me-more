from string import ascii_uppercase

from valideer import HomogeneousSequence, Enum, parse


class BoggleBoard:

    _parser = parse({
        "+board": HomogeneousSequence(
            HomogeneousSequence(Enum(ascii_uppercase), min_length=3, max_length=6),
            min_length=3, max_length=6)
    })

    @staticmethod
    def parse(request):
        """
        :rtype: BoggleBoard
        """
        return BoggleBoard(BoggleBoard._parser.validate(request)["board"])

    def __init__(self, chars):
        """
        :type chars: list[list[string]]
        """
        assert len(chars)
        assert len(chars[0])
        self.width = len(chars[0])
        self.height = len(chars)
        self._chars = chars

    def get_char(self, row, col):
        """
        :type row: int
        :type col: int
        :rtype: str | None
        """
        return self._chars[row][col]


class SolvedBoggleBoard:

    def __init__(self, words):
        """
        :type words: list[str]
        """
        self._words = words

    def json(self):
        return {"solution": self._words}