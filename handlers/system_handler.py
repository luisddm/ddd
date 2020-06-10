from tornado.web import RequestHandler

class SystemHandler(RequestHandler):
    def initialize(self, actions):
        self._actions = actions

    def get(self, system_id):
        system_status = self._actions['get'].execute(system_id)
        self.write(f"System {system_id} is {system_status}")
