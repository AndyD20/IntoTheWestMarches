from flask import Flask


class MarkersTask:
    app = Flask(__name__)

    @app.route('/some_route')
    def some_route(self):
        return "This is the response from the new endpoint"