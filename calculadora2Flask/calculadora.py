from flask import Flask, render_template, request
import math

app = Flask(__name__)

def calcular():
    etapas = ""
    resultado = ""
    
    if request.method == "POST":
        num1_valor = request.form.get("num1", "").strip()
        operacao = request.form.get("operacao", "+")
        
        if not num1_valor:
            return render_template(
                "calculadora.html",
                etapas="Informe o primeiro número.",
                resultado="",
            )
        
        num1 = float(num1_valor)

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
                    resultado="",
                )
            
            num2 = float(num2_valor)

            if operacao == "+":
                resultado = num1 + num2
                etapas = f"{num1} + {num2} = {resultado}"
            elif operacao == "-":
                resultado = num1 - num2
                etapas = f"{num1} - {num2} = {resultado}"
            elif operacao == "*":
                resultado = num1 * num2
                etapas = f"{num1} * {num2} = {resultado}"
            elif operacao == "/":
                if num2 == 0:
                    etapas = "Erro: Divisão por zero!"
                    resultado = None
                else:
                    resultado = num1 / num2
                    etapas = f"{num1} / {num2} = {resultado}"
            elif operacao == "**":
                resultado = num1 ** num2
                etapas = f"{num1} ** {num2} = {resultado}"

    return render_template("calculadora.html", etapas=etapas, resultado=resultado)


