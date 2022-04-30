#!/usr/bin/env python3
import tornado.ioloop
from tornado import web

from hosted_boggle_python import handlers


def make_app() -> web.Application:
    return web.Application([
        (r"/boggle_board/solve", handlers.BoggleBoardSolverHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
