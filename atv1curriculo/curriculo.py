from flask import Flask

app = Flask(__name__)

@app.route("/curriculo")

def decorator():
    return '''
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Currículo</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 20px auto;
                padding: 20px;
                background-color: #f5f5f5;
            }
            .container {
                background-color: white;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            h1 {
                text-align: center;
                color: #333;
                border-bottom: 3px solid rgb(255, 0, 0);
                padding-bottom: 10px;
            }
            h2 {
                color: rgb(255, 0, 0);
                margin-top: 30px;
                border-bottom: 2px solid rgb(255, 0, 0);
                padding-bottom: 5px;
            }
            .info-pessoal p {
                margin: 10px 0;
                line-height: 1.6;
            }
            .experiencia-item {
                margin-bottom: 20px;
                padding-left: 20px;
                border-left: 4px solid rgb(255, 0, 0);
            }
            .experiencia-item h3 {
                margin: 0 0 5px 0;
                color: #333;
            }
            .cargo {
                color: #666;
                font-weight: bold;
            }
            .periodo {
                color: #999;
                font-size: 0.9em;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Currículo</h1>
            
            <h2>Informações Pessoais</h2>
            <div class="info-pessoal">
                <p><strong>Nome:</strong> Enzo Santos de Oliveira</p>
                <p><strong>Email:</strong> enzoliveira2052@gmail.com</p>
                <p><strong>Telefone:</strong> (31) 98613-5600</p>
            </div>
            
            <h2>Experiência Profissional</h2>
            <div class="experiencia-item">
                <h3>Empresa ERW Ltda</h3>
                <p class="cargo">Cargo: Desenvolvedor Python</p>
                <p class="periodo">Período: 01/2022 - Presente</p>
            </div>
            <div class="experiencia-item">
                <h3>Empresa UTO Corp</h3>
                <p class="cargo">Cargo: Técnico de Suporte</p>
                <p class="periodo">Período: 06/2020 - 12/2021</p>
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)