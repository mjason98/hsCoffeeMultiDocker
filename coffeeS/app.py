from flask import Flask, jsonify, request
from flask import Response
from flask import make_response
from services.auth import auth_checker
from services.coffee import get_best_coffee
from services.coffee import get_top3_coffee
from services.coffee import set_top3_coffee
from services.coffee import get_top3_leaderboard

app = Flask(__name__)


@app.route('/v1/coffee/favourite', methods=['GET'])
def get_favorite_coffe():
    userid = auth_checker(request.authorization)
    if userid == 0:
        return Response('Unauthorized', 401,
                        {'WWW-Authenticate': 'Basic realm="Login Required"'})

    best_coffee = get_best_coffee(userid)

    result = {'data': {
        "favouriteCofee": best_coffee
        }
              }
    return jsonify(result)


@app.route('/v1/admin/coffee/favourite/leadeboard', methods=['GET'])
def get_favorite_drinks():
    userid = auth_checker(request.authorization)
    if userid == 0:
        return Response('Unauthorized', 401,
                        {'WWW-Authenticate': 'Basic realm="Login Required"'})

    top3 = get_top3_leaderboard()

    result = {'data': {"top3": list(top3)}}

    return jsonify(result)


@app.route('/v1/coffee/favourite', methods=['POST'])
def post_favorite_coffes():
    userid = auth_checker(request.authorization)
    if userid == 0:
        return Response('Unauthorized', 401,
                        {'WWW-Authenticate': 'Basic realm="Login Required"'})

    body = request.get_json()['top3']

    set_top3_coffee(userid, body)

    top3 = get_top3_coffee(userid)

    result = {'data': {"top3": list(top3)}}

    return jsonify(result)


@app.route('/v1/healthcheck', methods=['GET'])
def healh_check():
    response = make_response("OK")
    response.status_code = 200
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
