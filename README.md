# Teste de Implantação Cloud Run

**Objetivo:**

Este teste avalia sua capacidade de implantar uma aplicação "Hello World" no Google Cloud Run.

**Passos:**

1.  **Crie um Dockerfile:**
    *   Crie um arquivo chamado `Dockerfile` na raiz deste repositório.
    *   Este `Dockerfile` deve:
        *   Usar uma imagem Python base apropriada (ex: `python:3.9-slim`).
        *   Copiar os arquivos da aplicação (que você precisará criar, `app.py` e `requirements.txt`, seguindo o exemplo que dei acima).
        *   Instalar as dependências (Flask, gunicorn, ou outras que você escolher).
        *   Definir o comando para executar a aplicação (usando `gunicorn` ou o servidor de desenvolvimento do Flask *apenas para este teste*).  Em produção, use `gunicorn`.
        *   Expor a porta 8080 (Cloud Run usa essa porta por padrão).

2.  **Crie a Aplicação "Hello World":**
    *   Crie um arquivo `app.py` com o código Python para uma aplicação Flask simples que retorne "Hello, World!" na rota `/`.
    *   Crie um arquivo `requirements.txt` listando as dependências (Flask, gunicorn).

3.  **Configure o Cloud Build:**
    *   Vá para a seção Cloud Build no console do Google Cloud.
    *   Crie um novo gatilho (trigger).
    *   Conecte o gatilho a este repositório GitHub.
    *   Configure o gatilho para executar em cada push para a branch `main` (ou a branch que você preferir).
    *   Escolha a opção de configuração "Cloud Build configuration file (yaml or json)".
    *   O Cloud Build irá procurar por um arquivo `cloudbuild.yaml` na raiz do repositório.  Você não precisa criar este arquivo, o Cloud Build o usará *se ele existir*, mas vamos criar o gatilho primeiro.

4.  **Crie o arquivo cloudbuild.yaml**
    * Crie um arquivo chamado `cloudbuild.yaml`
    * Use o exemplo provido acima.
    * Troque o nome do servico e a regiao.

5. **Push e Teste:**
    * Faça um commit e push das suas alterações (Dockerfile, app.py, requirements.txt, cloudbuild.yaml) para o repositório.
    * O Cloud Build deve ser acionado automaticamente.
    * Verifique os logs do Cloud Build para garantir que a build e o deploy foram bem-sucedidos.
    * Acesse a URL do serviço Cloud Run (disponível no console) para verificar se o "Hello, World!" está sendo exibido.

6. **Configurar Cloud Build Trigger**
    * Configurar um trigger para sempre que um push for feito na branch main, executar o cloudbuild.yaml

**Dicas:**

*   Certifique-se de que a conta de serviço do Cloud Run tenha as permissões corretas (listadas acima).
*   Use nomes descritivos para seus recursos (serviço Cloud Run, imagem Docker).
*   Teste localmente (construindo a imagem Docker e executando o contêiner) antes de implantar no Cloud Run.
*   Se tiver problemas, consulte a documentação do Google Cloud.

**O que Será Avaliado:**

*   **Funcionamento:** A aplicação deve estar funcionando corretamente no Cloud Run.
*   **Dockerfile:** A construção correta e eficiente da imagem Docker.
*   **Cloud Build:** A configuração correta do gatilho e do arquivo `cloudbuild.yaml`.
*   **Organização:** A estrutura do código e a clareza das suas ações.
*   **Resolução de Problemas:** Sua capacidade de identificar e corrigir erros.

**Boa sorte!**
