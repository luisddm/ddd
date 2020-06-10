from tornado.web import RequestHandler

class MainHandler(RequestHandler):
    def get(self):
        system_1_url = self.reverse_url("health_check", "1")
        self.write(f'<a href="{system_1_url}">Check health of system 1</a>')
