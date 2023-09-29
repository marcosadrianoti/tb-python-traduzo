# Projeto Python Traduzo! :speech_balloon:
Projeto desenvolvido por mim durante o curso de Desenvolvimento Web na Trybe. Divulgado aqui como portfólio de aprendizado.

<details>
<summary><strong>Objetivos do projeto:</strong></summary>
 
  * Desenvolver uma aplicação de tradução de textos entre vários idiomas, utilizando Python com o Framework Flask, para criar uma aplicação Server Side.
  * Verificar se sou capaz de:
    * Implementar uma API utilizando arquitetura em camadas MVC.
    * Utilizar o Docker para projetos Python.
    * Aplicar conhecimentos de Orientação a Objetos no desenvolvimento WEB.
    * Escrever testes para APIs para garantir a implementação dos endpoints.
    * Interagir com um banco de dados não relacional MongoDB.
    * Desenvolver páginas web Server Side.
</details>
<details>
<summary><strong> Requisitos do projeto:</strong></summary>

  *  Criar a função `fetch`.
  *  Criar a função `scrape_updates`.
  *  Criar a função `scrape_next_page_link`.
  *  Criar a função `scrape_news`.
  *  Criar a função `get_tech_news` para obter as notícias.
  *  Testar a classe `ReadingPlanService`.
  *  Criar a função `search_by_title`.
  *  Criar a função `search_by_date`.
  *  Criar a função `search_by_category`.
</details>
  
## Rodando o projeto localmente

Para rodar o projeto em sua máquina, abra seu terminal, crie um diretório no local de sua preferência com o comando `mkdir` e acesse o diretório criado com o comando `cd`:

```bash
mkdir meu-diretorio &&
cd meu-diretorio
```

Clone o projeto com o comando `git clone`:

```bash
git clone git@github.com:marcosadrianoti/tb-python-tech-news.git
```

Acesse o diretório do projeto com o comando `cd`:

```bash
cd tb-python-tech-news
```

crie o ambiente virtual:
```bash
python3 -m venv .venv
```

Ative o ambiente virtual:
```bash
source .venv/bin/activate
```

Instale as dependências no ambiente virtual:
```bash
python3 -m pip install -r dev-requirements.txt
```

Rode o docker-compose para o banco de dados:
```bash
docker-compose up -d mongodb
```

Teste Manual:
* Abra um terminal Python importando a função através do comando:
```bash
python3 -i tech_news/scraper.py
```

* Agora invoque as funções. Exemplo:
```bash
html = fetch(https://blog.betrybe.com)
scrape_news(html)
```
