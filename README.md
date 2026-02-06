# 🤖 First AI Project

Um repositório simples e direto ao ponto para você criar **sua primeira IA** usando duas abordagens:

* 🧠 **Machine Learning clássico com Spark (Olist)**
* 💬 **Chatbot com a API do Google Gemini**

A ideia é mostrar, de forma prática, como sair do zero e chegar em um **projeto real de portfólio**.

---

# 🚀 O que você vai encontrar aqui

## 1️⃣ Notebook de Machine Learning (Spark + Olist)

Projeto de **classificação binária** para prever:

> **Um pedido vai atrasar ou não?**

### Tecnologias usadas

* PySpark
* Spark MLlib
* Random Forest
* Dataset público da Olist

### Pipeline implementado

* Carregamento de dados
* Feature engineering com datas
* Criação da variável alvo (**atrasado ou não**)
* Treinamento do modelo
* Avaliação com **AUC**

Esse notebook demonstra:

✔ Pensamento de negócio
✔ Processamento de dados em escala
✔ ML clássico aplicado ao mundo real

---

## 2️⃣ First API – Chatbot com Gemini

Um exemplo mínimo de **IA generativa funcionando no terminal**.

### Código principal

```python
from google import genai

client = genai.Client(api_key="SUA_CHAVE_DE_API_AQUI")

print("-- Chatbot --")
print("Digite 'sair' para encerrar o chatbot.")

while True:
    pergunta = input("Você: ")
    if pergunta.lower() == "sair":
        print("Chatbot encerrado.")
        break

    resposta = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=pergunta
    )

    print("Chatbot:", resposta.text)
```

### O que isso demonstra

* Consumo de API de IA
* Loop de conversa em tempo real
* Estrutura base para criar:

  * assistentes
  * bots de atendimento
  * ferramentas com IA

---

# ⚙️ Como rodar o projeto

## 1️⃣ Clonar o repositório

```bash
git clone https://github.com/GabrielG71/first-ai-project.git
cd first-ai-project
```

## 2️⃣ Instalar dependências

```bash
pip install pyspark
pip install google-genai
```

---

## 🧠 Rodar o ML com Spark

Abra o notebook:

```bash
jupyter notebook
```

Execute o arquivo dentro de `notebooks/`.

---

## 💬 Rodar o chatbot Gemini

1. Gere uma chave de API no **Google AI Studio**
2. Substitua no código:

```python
api_key="SUA_CHAVE_DE_API_AQUI"
```

3. Execute:

```bash
python first-api/chatbot_gemini.py
```

---

# 🎯 Objetivo do repositório

Este projeto foi criado para ser:

* 🪜 **Seu primeiro passo em IA**
* 📂 **Um projeto simples de portfólio**
* ⚡ **Rápido de entender e rodar**

Se você consegue rodar isso, você já:

✔ Treinou um modelo de ML real
✔ Consumiu uma API de IA generativa
✔ Tem algo concreto para mostrar no GitHub

---

# 👨‍💻 Autor

**Gabriel Gonçalves**
Desenvolvedor focado em **Dados, IA e Backend**.

Se esse projeto te ajudou, deixa um like.
