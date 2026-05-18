from flask import Flask

app = Flask(__name__)

@app.route("/decorator")

def decorator():
    return "Hello word!"

#Decorator em Python são funções que modificam ou estendem o comportamento de outras funções, métodos ou classes sem alterar seu código original

if __name__ == "__main__":
    app.run(debug=True)