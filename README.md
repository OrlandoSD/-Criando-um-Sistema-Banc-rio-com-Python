# Sistema Bancário

Um sistema bancário simples desenvolvido com Flask para o back-end e HTML/CSS/JavaScript para o front-end.

## Índice

- [Descrição](#descrição)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Descrição

Este projeto é um sistema bancário simples que permite aos usuários realizar operações bancárias básicas, como depósito, saque e visualização de extrato. O back-end é construído com Flask, enquanto o front-end utiliza HTML, CSS e JavaScript.

## Funcionalidades

- Depósito de valores na conta
- Saque de valores da conta, respeitando um limite diário e o saldo disponível
- Visualização do extrato das operações realizadas
- Sair do sistema

## Tecnologias Utilizadas

- [Flask](https://flask.palletsprojects.com/) - Micro framework para o back-end
- HTML - Estrutura do front-end
- CSS - Estilização do front-end
- JavaScript - Interatividade no front-end

## Estrutura do Projeto

bank_system/
├── app.py
├── static/
│ └── styles.css
└── templates/
└── index.html


## Instalação

1. Clone o repositório para sua máquina local:
   ```bash
   git clone https://github.com/seu-usuario/sistema-bancario.git

cd sistema-bancario

python -m venv venv
    #No Windows
    venv\Scripts\activate

    No macOS/Linux:
    source venv/bin/activate

Instale as Dependências:

pip install Flask


Execute o servidor Flask

python app.py


Abra o navegador e acesse http://127.0.0.1:5000.

Utilize a interface para realizar depósitos, saques e visualizar o extrato.


