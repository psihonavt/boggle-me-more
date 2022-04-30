import tornado.web

from src.boggle.handlers import BoggleBoardSolverHandler

urlmap = [
    (r"/", BoggleBoardSolverHandler)
]

WEB_SERVER = tornado.web.Application(urlmap)