from flask import Flask, redirect
import os


def get_ips():
    ip_str = os.environ.get('IP_LIST')
    ip_str = ip_str.split('|')

    ip_str = list(map(lambda s: f"localhost:{s}", ip_str))

    return ip_str


IP_LIST = get_ips()
IP_POS = 0

app = Flask(__name__)


@app.route("/", defaults={"path": ""}, methods=['GET', 'POST'])
@app.route("/<path:path>", methods=['GET', 'POST'])
def catch_all(path):
    global IP_POS

    new_url = f"http://{IP_LIST[IP_POS]}/{path}"
    IP_POS = (IP_POS + 1) % len(IP_LIST)

    return redirect(new_url, code=302)


if __name__ == "__main__":
    app.run(port=8080)
