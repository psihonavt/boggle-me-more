import tornado.ioloop
from src.boggle.application import WEB_SERVER

if __name__ == "__main__":
    WEB_SERVER.listen(8888)
    tornado.ioloop.IOLoop.current().start()
