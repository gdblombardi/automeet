from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def gpt_request(openai_client, system_prompt, user_prompt):
    resposta = openai_client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature = 0.7,
    )

    return resposta.choices[0].message.content

if __name__ == "__main__":
    
    openai_api_token = os.getenv("OPENAI_API_TOKEN")
    openai_client = OpenAI(api_key=openai_api_token)
    system_prompt = "O sistema está conversando com um usuário sobre o uso de algoritmos de inteligência artificial para a geração de textos."
    user_prompt = "Qual é a sua opinião sobre o uso de algoritmos de inteligência artificial para a geração de textos?"
    print(gpt_request(openai_client=openai_client, system_prompt=system_prompt, user_prompt=user_prompt))