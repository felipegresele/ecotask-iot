# Projeto IoT GS-FIAP - Consultor de Sustentabilidade com Gemini API

Este projeto é uma aplicação Flask simples que atua como um consultor de sustentabilidade, utilizando a API do Google Gemini (modelo `gemini-2.5-flash`). Ele recebe um contexto do usuário e um objetivo de sustentabilidade, e então gera um plano de ação detalhado para alcançar esse objetivo.

## Funcionalidades

- Recebe `userContext` e `sustainabilityGoal` via API REST.
- Utiliza a API do Gemini para gerar planos de ação de sustentabilidade.
- Retorna o plano gerado em formato JSON.

## Configuração e Execução

Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

### Pré-requisitos

Certifique-se de ter o Python 3 instalado em seu sistema.

### Instalação

1.  **Clone o repositório** (se ainda não o fez):

    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd iot
    ```

    *(Substitua `<URL_DO_SEU_REPOSITORIO>` pelo link real do seu repositório, se aplicável.)*

2.  **Crie e ative um ambiente virtual** (recomendado):

    ```bash
    python -m venv venv
    ```

    -   No Windows (PowerShell):
        ```bash
        .\venv\Scripts\activate
        ```
    -   No macOS/Linux (Bash/Zsh):
        ```bash
        source venv/bin/activate
        ```

3.  **Instale as dependências**:

    Com o ambiente virtual ativado, instale as bibliotecas necessárias usando `pip`:

    ```bash
    pip install -r requirements.txt
    ```

### Execução da Aplicação

1.  **Inicie o servidor Flask**:

    Com o ambiente virtual ainda ativado, execute o seguinte comando no diretório `iot`:

    ```bash
    python app.py
    ```
    python d:\gs-fiap\iot\app.py

    O servidor será iniciado e ficará disponível em `http://127.0.0.1:5000`.

### Testando a API no Postman

Para testar a API, você pode enviar uma requisição POST para o endpoint `/api/generate-plan`. Abra um **novo terminal** (sem fechar o terminal onde o servidor Flask está rodando) e use o `curl`:

```bash
curl -X POST -H "Content-Type: application/json" -d "{
    \"userContext\": \"uma família com duas crianças em um apartamento\",
    \"sustainabilityGoal\": \"reduzir o consumo de energia elétrica\"
}" http://127.0.0.1:5000/api/generate-plan
```

Você deverá receber uma resposta JSON contendo o plano de sustentabilidade gerado pela IA.

### Chave da API do Gemini

A chave da API do Gemini está atualmente incorporada diretamente no arquivo `app.py` para simplicidade de demonstração. Em um ambiente de produção, é fortemente recomendado o uso de variáveis de ambiente para a chave da API.
