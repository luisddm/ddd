from tornado.ioloop import IOLoop

from application import app

PORT = 8888

if __name__ == "__main__":
    app.listen(PORT)
    print(f'Running web server at port {PORT}')
    IOLoop.current().start()

