# Atividade Aula 12 — Model, Controller e View (StreamFlix)

**Disciplina:** Python / Flask  
**Profª:** Janaína Duarte  
**Projeto:** `flask/Aula12/`  
**Objetivo:** Explorar o código, localizar arquivos e explicar o que cada camada faz.

---

## Como responder

1. Abra a pasta `flask/Aula12/` no editor ou GitHub.
2. Navegue pelas pastas `models/`, `controllers/` e `views/`.
3. Rode o site (`python app.py`) quando a pergunta pedir para testar no navegador.
4. Responda com **caminho do arquivo** + **explicação em suas palavras**.

**Identificação**

- Nome: _______________________________
- Turma: _______________________________

---

## Bloco A — Model (perguntas 1 a 10)

**1.** Em qual pasta ficam as classes que representam tabelas do banco SQLite? Cite o caminho.

na pasta H:\PYTHON\PYTHON 2°ETAPA\Aula12 - Alunos\models\base.py

**2.** Qual é o nome do arquivo de banco criado quando o app roda? Em qual arquivo Python essa configuração está?

streamflix.db configurado em app.py

**3.** Quais classes Model existem no projeto (nome das classes)? Em quais arquivos `.py` cada uma está?

ModeloBase dentro de models\base.py, FilmeFavorito dentro de models\filme_favorito.py e HistoricoBusca dentro de models\historico_busca.py

**4.** De qual superclasse `FilmeFavorito` e `HistoricoBusca` herdam? O que elas ganham automaticamente por herança (cite 3 campos)?

ModeloBase ganham  id, data_criacao e data_atualizacao

**5.** Qual é o `__tablename__` da tabela de favoritos? Por que usamos `__tablename__` em vez de só o nome da classe?

filmes_favoritos ele é usado para definir o nome da tabela

**6.** No model `FilmeFavorito`, qual coluna guarda o id do filme vindo da API TMDB? Ela tem alguma restrição especial (`unique`, `nullable`)?

tmdb_id restrição em unique e nullable false

**7.** Abra `models/filme_favorito.py`. O que o método `@classmethod adicionar` faz passo a passo? O que acontece se o filme já existir nos favoritos?

O método adicionar verifica se o filme já existe nos favoritos usando buscar_por_tmdb() se existir volta um None caso não existir ele cria um novo FilmeFavorito e salva no banco.

**8.** Onde está o método que lista as últimas 8 buscas? Qual é o nome da classe e do método?

HistoricoBusca método ultimas

**9.** O model grava dados da API TMDB inteira ou só alguns campos espelhados? Cite 4 campos salvos em `FilmeFavorito`.

Só em alguns campos são eles: tmdb_id, titulo, poster_path e nota

**10.** Em `models/__init__.py`, o que é exportado além de `db`? Por que o controller importa `from models import FilmeFavorito` em vez de importar o arquivo inteiro da pasta?

ModeloBase, HistoricoBusca e FilmeFavorito são exportados no __init__.py

---

## Bloco B — Controller (perguntas 11 a 20)

**11.** Quantos Blueprints existem no projeto? Cite o **nome** de cada um e o **url_prefix** (se tiver).

3 blueprints são eles: filmes no /filmes, favoritos no /favoritos e dashbord sem prefixo

**12.** Em qual arquivo está a rota `/filmes/populares`? Qual é o nome da função Python que responde essa URL?

controllers/filme_controller.py função populares

**13.** O que a função `populares()` faz antes de chamar `render_template`? Cite duas chamadas (Model, Service ou API).

busca os filmes favoritos e populares

**14.** Quando o usuário busca um filme em `/filmes/buscar`, qual controller registra o termo no banco? Qual model é usado e em qual linha aproximada?

filmes_controller.py usando historicoBusca

**15.** Abra `controllers/favoritos_controller.py`. Qual método HTTP é exigido para adicionar favorito (`GET` ou `POST`)? Qual a URL completa de exemplo para adicionar o filme id 550?

POST /adiconar/550

**16.** No `filmes_controller.py`, rota `detalhe(filme_id)`: o que acontece se `api.detalhe(filme_id)` retornar `None`?

manda para os filmes populares

**17.** Onde os Blueprints são **registrados** no Flask? Cite o arquivo e o comando usado (3 registros).

no app.py ele usa app.register_blueprint

**18.** Qual controller cuida da página inicial `/`? Quais variáveis ele envia para o template `index.html`?

dashboard_controller.py populares, melhores, total_favoritos, historico e modo_demo

**19.** A pasta `services/tmdb_api.py` é Model, Controller ou View? Justifique: quem chama essa classe e para quê?

Service os controllers usam para acessar a API do IMDB

**20.** No controller de busca, de onde vem o termo digitado quando o usuário usa o formulário da home (`index.html`)? É `request.form` ou `request.args`? Explique a diferença nesse projeto.

request.args o formulário usa o get

---

## Bloco C — View (perguntas 21 a 30)

**21.** Onde ficam os templates HTML? Qual caminho completo da pasta?

views/templates

**22.** Qual template é a “base” de todas as páginas (layout com menu)? Como os outros templates usam esse layout (qual comando Jinja)?

layout.html e extends

**23.** Abra `views/templates/layout.html`. Liste os 5 links do menu e o `url_for` de cada um.

incio, populares, melhores, busca e favoritos

**24.** Qual arquivo HTML exibe a seção **“Onde assistir (Brasil)”**? De onde vem a variável `streaming` usada nessa tela?

filmes/detalhe.html ele vem do controller

**25.** O arquivo `filmes/_card.html` é uma página inteira ou um pedaço reutilizado? Quem inclui esse arquivo e com qual tag Jinja?

Um pedaço reutilizado include

**26.** Em `filmes/detalhe.html`, como a View sabe se o filme já está nos favoritos? Qual variável booleana/objeto controla o botão “Salvar” vs “Remover”?

pela variável favorito

**27.** Onde está o CSS do site? Como o `layout.html` carrega esse arquivo (função Flask/Jinja)?

views/static/css/style.css ele usa o url_for

**28.** Na listagem de favoritos (`favoritos/lista.html`), qual loop Jinja percorre os registros? Cite 3 campos exibidos na tabela.

for fav in favoritos os campos são: nota, ano e titulo

**29.** O que significa `{% if modo_demo %}` no layout? Quem disponibiliza essa variável para **todos** os templates?

mostra o modo demonstração quem disponibiliza é o app.context_processor

**30.** Desenhe ou descreva o fluxo completo quando o aluno clica em **“Salvar favorito”** no detalhe do filme, indicando **View → Controller → Model** (e redirect de volta). Cite arquivos envolvidos.

os arquivos são filmes/detalhe.html, filme_favorito.py, favoritos_controller.py e o redirect volta para a página do filme

---

## Entrega

- Arquivo `.txt` ou `.md` com as 30 respostas 

**Critério:** respostas que mostrem que você **abriu o código**, não chute.

Boa exploração!
