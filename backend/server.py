from sanic import Sanic
from sanic.response import json
from views import *
from models import *
app = Sanic()

@app.route("/api/test", methods=['GET','POST'])
def a1(request):
    return test2(request)

@app.route("/api/sign_in", methods=['POST'])
def a2(request):
    return sign_in(request)

@app.route("/api/sign_up", methods=['POST'])
def a3(request):
    return sign_up(request)


@app.route("/api/sign_out", methods=['POST'])
def a4(request):
    return sign_out(request)

# @app.route("/")
# async def test(request):
#     test3()


if __name__ == "__main__":
    db.connect()
    db.create_tables([Person, Session])
    app.run(host="0.0.0.0", port=8000)