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