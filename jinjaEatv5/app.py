from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/base")
def index():
    nome = "Enzo"
    dados = {"nome": "Enzo", "idade": 16}
    usuario = {"nome": "Enzo", "email": "12400025@aluno.cotemig.com.br"}
    alunos = ["Enzo", "Theo", "Daniel", "Davi", "João"]
    nota = 9

    return render_template(
        "base.html", nome=nome, dados=dados, usuario=usuario, alunos=alunos, nota=nota
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")

        USUARIO_VALIDO = "Enzo"
        SENHA_VALIDA = "12400025"

        if usuario == USUARIO_VALIDO and senha == SENHA_VALIDA:
            return f"<h1>Bem-vindo, {usuario}!</h1>"
        else:
            return "<h1>Login inválido</h1>"
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)