# Desafio Prático - Engenharia DevOps/Cloud (GCP)

Bem-vindo ao nosso desafio prático! 🚀

Neste repositório, você encontra uma API simples em Python/Flask já conteinerizada.

## 🎯 O Seu Objetivo
Fazer o deploy desta aplicação no **Google Cloud Platform (GCP)**, deixando-a acessível publicamente na internet.

Você tem total liberdade para escolher a arquitetura. Pode usar **Cloud Run, GKE (Kubernetes Engine) ou Compute Engine (GCE)**. Escolha a que você se sente mais confortável ou a que acha mais adequada para uma API Web moderna.

## ✅ Critérios de Sucesso
Para considerarmos o desafio concluído, os seguintes endpoints devem estar respondendo corretamente pela internet:

1. `GET /` -> Deve retornar status 200 e uma mensagem de boas-vindas.
2. `GET /health` -> Deve retornar status 200.
3. `GET /data` -> **Atenção aqui:** Este endpoint exige uma variável de ambiente chamada `API_KEY` injetada na aplicação. Se ela não estiver presente, a aplicação retornará erro 500. Você pode usar qualquer valor fictício (ex: `super-secret-key-123`) para essa variável, mas ela deve ser configurada de forma segura na infraestrutura.

## 🛠️ Regras do Jogo
- Você pode usar o Console web do GCP, a gcloud CLI ou Terraform.
- Pense em voz alta! Queremos entender o *porquê* das suas escolhas.
- Sinta-se à vontade para consultar a documentação oficial, Google, Stack Overflow, etc.

Boa sorte!
