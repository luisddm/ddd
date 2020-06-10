from tornado.web import Application, url

from handlers.main_handler import MainHandler
from handlers.system_handler import SystemHandler

from actions.health_check_action import HealthCheckAction

health_check_action = {}
health_check_action['get'] = HealthCheckAction()

app = Application([
    url(r"/", MainHandler),
    url(r"/system/([0-9]+)", SystemHandler, dict(actions=health_check_action), name="health_check"),
], debug=True)
