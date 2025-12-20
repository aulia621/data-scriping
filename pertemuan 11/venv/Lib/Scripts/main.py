from flask import Flask,request

app= Flask(__name__)

# @app.route("/")
# def hello_world():
#     return"<p>Hello, World!</p>"

# @app.route("/nama/<nama>")
# def nama(nama):
#     return f"<p>Hallo World, namaku {nama}</p>"

# @app.route("/login", methods=["GET"])
# def login():
#     user = request.args.get("user")
#     password = request.args.get("pass")

#     return (user + ":" + password)

@app.route("/login", methods=["GET"])
def login():
    user = request.args.get("user")
    password = request.args.get("pass")

    # Menggunakan modulo sebagai index list: 0 untuk Genap, 1 untuk Ganjil
    status = ["GENAP", "GANJIL"][int(password) % 2]

    return (user + ":" + password + " adalah " + status)

app.run(debug=True)