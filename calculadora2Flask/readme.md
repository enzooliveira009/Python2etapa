Aula 7 — Calculadora Web com Flask

Contexto
Nesta aula você vai construir uma calculadora web usando Flask. O usuário preenche um formulário no navegador; ao clicar em Calcular, o navegador envia os dados ao servidor com POST; o Python faz a conta e devolve a página com o resultado.

O foco não é fazer a conta no JavaScript do navegador, e sim no servidor (Python).

Objetivos de aprendizagem
Organizar um projeto Flask com pastas templates e static
Entender a diferença entre GET (abrir a página) e POST (enviar o formulário)
Ler dados do formulário com request.form
Separar responsabilidades: app.py (rotas), calculadora.py (lógica), HTML (interface)
Exibir resultados no template com Jinja2 ({% if %}, {{ variavel }})
Tratar erros simples (divisão por zero, raiz de número negativo, operação inválida)

Estrutura:
Aula7/
├── app.py
├── calculadora.py
├── templates/
│   └── calculadora.html
└── static/
    └── css/
        └── style.css


Desenvolva uma calculadora web em Flask que:

Página inicial (/)

Em GET, exibe o formulário vazio.
Em POST, processa o cálculo e mostra o resultado na mesma página.
Formulário HTML

Campo num1 (primeiro número, obrigatório)
Campo operacao (select): somar, subtrair, multiplicar, dividir, potência e raiz quadrada
Campo num2 (segundo número) — obrigatório para todas as operações exceto raiz quadrada
Botão Calcular com method="POST" e action apontando para a rota /
Link ou botão para limpar e voltar ao formulário vazio
Lógica em calculadora.py

Função calcular() que lê request.form
Implementar: +, -, *, /, ** (potência) e sqrt (raiz de num1 apenas)
Divisão por zero: mensagem de erro amigável
Raiz de número negativo: mensagem de erro amigável
Retornar o template com etapas (conta montada) e resultados (valor final)
Estilos

CSS em static/css/style.css (não usar <style> grande dentro do HTML)
Link no template: {{ url_for('static', filename='css/style.css') }}
Comportamento da raiz (opcional com JavaScript)

Ao escolher Raiz quadrada, o campo num2 pode ser ocultado no formulário
No Python, não exigir num2 quando a operação for sqrt


REQUISITOS

ADIÇÃO,
SUBTRAÇÃO,
DIVISÃO,
MULTIPLICAÇÃO,
POTÊNCIA, 
UTILIZAR A BIBLIOTECA MATH
RAIZ QUADRADA,
LOGARITMO





Arquivos BASE

	calculadora.py


import math


from flask import render_template, request




def calcular():
    num1 = float(request.form["num1"])
    operacao = request.form["operacao"]


    if operacao == "sqrt":
        if num1 < 0:
            resultado = "Erro: número negativo"
            etapas = f"Não existe raiz real de {num1}."
        else:
            resultado = math.sqrt(num1)
            etapas = f"√{num1} = {resultado}"
    else:
        num2_valor = request.form.get("num2", "").strip()
        if not num2_valor:
            return render_template(
                "calculadora.html",
                etapas="Informe o segundo número para esta operação.",
                resultados="",
            )
        num2 = float(num2_valor)


        if operacao == "+":
            resultado = num1 + num2
            etapas = f"{num1} + {num2} = {resultado}"

CONTINUE


TEMPLATES
DOCUMENTO HTML
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Calculadora</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>


    <h1>Calculadora</h1>


    <div id="calculator">
        <!-- POST envia os dados para o Flask; a função calcular() no Python faz a conta -->
        <form method="POST" action="{{ url_for('index') }}">
            <div class="form-grupo">
                <label for="num1">Primeiro número</label>
                <input type="number" id="num1" name="num1" step="any" required
                       value="{{ request.form.get('num1', '') }}">
            </div>


            <div class="form-grupo">
                <label for="operacao">Operação</label>
                {% set op = request.form.get('operacao', '+') %}
                <select id="operacao" name="operacao" required onchange="atualizarNum2()">
                    <option value="+" {% if op == '+' %}selected{% endif %}>+ Somar</option>
                    <option value="-" {% if op == '-' %}selected{% endif %}>− Subtrair</option>
                    <option value="*" {% if op == '*' %}selected{% endif %}>× Multiplicar</option>
                    <option value="/" {% if op == '/' %}selected{% endif %}>÷ Dividir</option>
                    <option value="**" {% if op == '**' %}selected{% endif %}>^ Potência</option>
                    <option value="sqrt" {% if op == 'sqrt' %}selected{% endif %}>√ Raiz quadrada</option>
                </select>
            </div>


            <div class="form-grupo" id="grupo-num2">
                <label for="num2">Segundo número</label>
                <input type="number" id="num2" name="num2" step="any"
                       value="{{ request.form.get('num2', '') }}">
            </div>


            <button type="submit">Calcular</button>
        </form>


        {% if etapas %}
        <div class="resultado">
            <strong>Resposta do servidor (Python):</strong>
            <div>{{ etapas }}</div>
            <div>Resultado: {{ resultados }}</div>
        </div>
        {% endif %}


        <a href="{{ url_for('index') }}">Limpar / nova conta</a>
    </div>


    <script>
        function atualizarNum2() {
            const raiz = document.getElementById("operacao").value === "sqrt";
            const grupo = document.getElementById("grupo-num2");
            const num2 = document.getElementById("num2");
            grupo.style.display = raiz ? "none" : "block";
            num2.required = !raiz;
            if (raiz) num2.value = "";
        }
        atualizarNum2();
    </script>


</body>
</html>




CSS
body {
    text-align: center;
    font-family: Arial, sans-serif;
}


h1 {
    margin-top: 20px;
}


#calculator {
    display: inline-block;
    text-align: left;
    border: 1px solid #ccc;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    width: 320px;
    margin: 0 auto;
}


.form-grupo {
    margin-bottom: 12px;
}


label {
    display: block;
    margin-bottom: 4px;
    font-weight: bold;
}


input[type="number"],
select {
    width: 100%;
    padding: 8px;
    font-size: 18px;
    box-sizing: border-box;
}


button {
    width: 100%;
    padding: 10px;
    font-size: 18px;
    cursor: pointer;
    margin-top: 8px;
}


.resultado {
    margin-top: 16px;
    padding: 12px;
    background: #f0f4f8;
    border-radius: 4px;
    text-align: right;
    font-size: 18px;
}


.resultado strong {
    display: block;
    text-align: left;
    margin-bottom: 6px;
    font-size: 14px;
}


a {
    display: inline-block;
    margin-top: 12px;
    color: #2563eb;
}



