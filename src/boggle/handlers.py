from uuid import uuid4

from tornado import web
from tornado.escape import json_decode, json_encode
from valideer import ValidationError

from src.boggle.application import BOGGLE_SOLVER
from src.boggle.domain import BoggleBoard


class BoggleBoardSolverHandler(web.RequestHandler):

    def post(self):
        if self.request.headers["Content-Type"] != "application/json":
            self.set_status(406)
            self.finish("Please submit request as a valid JSON")

        try:
            request = json_decode(self.request.body)
        except TypeError:
            self.set_status(406)
            self.finish("Please submit request as a valid JSON")

        try:
            bboard = BoggleBoard.parse(request)
        except ValidationError as ex:
            self.set_status(409)
            self.finish("Invalid request: {}".format(ex.message))

        try:
            solved_board = BOGGLE_SOLVER.solve(bboard)
            self.set_status(200)
            self.set_header("Content-Type", "application/json")
            self.write(json_encode(solved_board.json()))
        except Exception:
            self.set_status(500)
            error_code = str(uuid4())
            # write stacktrace associated with this code
            self.set_header("Content-Type", "application/json")
            self.write(json_encode({"error": error_code}))