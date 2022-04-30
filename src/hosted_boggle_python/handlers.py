from importlib import resources

from tornado import web


def load_dictionary() -> list[str]:
    with resources.open_text("hosted_boggle_python", "words.csv") as dictionary:
        return dictionary.readlines()


class BoggleBoardSolverHandler(web.RequestHandler):
    def post(self):
        # TODO: implement me.
        pass
