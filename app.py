import bottle

import ttt


app = bottle.Bottle()

@app.route(path="/", method="get")
def index():
    bottle.response.content_type = "text/plain;charset=utf-8"

    try:
        return ttt.play(list(bottle.request.query.board), "o")
    except ValueError:
        bottle.abort(400, "Invalid board.")


if __name__ == "__main__":
    bottle.run(app, host="localhost", port=8080, debug=False, reloader=False)
