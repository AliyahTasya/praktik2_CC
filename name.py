from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        return f"""
        <html>
        <head>
            <style>
                body {{ font-family: 'Poppins', sans-serif; text-align: center; margin: 0; padding: 0; background: linear-gradient(to right, #ff9a9e, #fad0c4); display: flex; justify-content: center; align-items: center; height: 100vh; }}
                .container {{ max-width: 400px; padding: 20px; border-radius: 10px; box-shadow: 5px 5px 15px rgba(0,0,0,0.2); background: white; text-align: center; }}
                input[type=text], input[type=email] {{ width: calc(100% - 20px); padding: 10px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; }}
                input[type=submit] {{ background: #ff758c; color: white; padding: 10px 15px; border: none; border-radius: 5px; cursor: pointer; transition: 0.3s; }}
                input[type=submit]:hover {{ background: #ff3c6f; }}
                h1 {{ color: white; text-shadow: 2px 2px 5px rgba(0,0,0,0.2); }}
            </style>
        </head>
        <body>
            <div class="container">
                <h2>Halo {name}, email Anda {email} telah diterima.</h2>
                <a href="/">Kembali</a>
            </div>
        </body>
        </html>
        """
    return """
    <html>
    <head>
        <style>
            body {{ font-family: 'Poppins', sans-serif; text-align: center; margin: 0; padding: 0; background: linear-gradient(to right, #ff9a9e, #fad0c4); display: flex; justify-content: center; align-items: center; height: 100vh; }}
            .container {{ max-width: 400px; padding: 20px; border-radius: 10px; box-shadow: 5px 5px 15px rgba(0,0,0,0.2); background: white; text-align: center; }}
            input[type=text], input[type=email] {{ width: calc(100% - 20px); padding: 10px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; }}
            input[type=submit] {{ background: #ff758c; color: white; padding: 10px 15px; border: none; border-radius: 5px; cursor: pointer; transition: 0.3s; }}
            input[type=submit]:hover {{ background: #ff3c6f; }}
            h1 {{ color: white; text-shadow: 2px 2px 5px rgba(0,0,0,0.2); }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello, World!</h1>
            <h2>Formulir</h2>
            <form method="post">
                Nama: <input type="text" name="name" required><br>
                Email: <input type="email" name="email" required><br>
                <input type="submit" value="Kirim">
            </form>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
