from tornado.testing import AsyncHTTPTestCase
from tornado.escape import json_encode, json_decode

from src.boggle.application import WEB_SERVER


class BoggleBoardSolveTestCase(AsyncHTTPTestCase):

    def get_app(self):
        return WEB_SERVER

    def test_it_expects_correct_content_type(self):
        response = self.fetch("/", method='POST', body="123")
        assert response.code == 406

    def test_it_expects_valid_board(self):
        response = self.fetch("/", method='POST',
                              body=json_encode({"board": ["A"]}),
                              headers={"Content-Type": "application/json"})
        assert response.code == 409, response.body

    def test_it_expects_solves_a_board(self):
        board = [["G", "E", "L"], ["A", "F", "B"], ["X", "I", "S"]]
        response = self.fetch("/", method='POST',
                              body=json_encode({"board": board}),
                              headers={"Content-Type": "application/json"})
        assert response.code == 200
        solution = json_decode(response.body)
        assert "solution" in solution
        assert solution["solution"]





