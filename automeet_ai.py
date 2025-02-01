import streamlit as st
import uuid
from mp4_to_mp3 import mp4_to_mp3
from mp3_to_text import mp3_to_text
from gpt_caller import gpt_request
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

st.title('AutoMeet AI')

uploaded_file = st.file_uploader("Choose a file", accept_multiple_files=False, type=['mp4'])


if uploaded_file is not None:
    mp4_filename = uploaded_file.name
    mp3_filename = uuid.uuid4().hex + ".mp3"

    st.text(mp3_filename)

    st.text("Converting mp4 to mp3...")
    print("-------------> Converting mp4 to mp3...")
    mp4_to_mp3(mp4_filename=mp4_filename, mp3_filename=mp3_filename)

    st.text("Converting mp3 to text...")
    print("-------------> Converting mp3 to text...")
    transcricao = mp3_to_text(mp3_filename=mp3_filename)

    st.text("Generating minutes...")
    print("-------------> Generating minutes...")
    openai_api_token = os.getenv("OPENAI_API_TOKEN")
    openai_client = OpenAI(api_key=openai_api_token)

    system_prompt = "Você é um ótimo gerente de projetos com õtimas capacidades de gerar atas de reunião."
    user_prompt = f"""em redação de nível especializado, resuma as notas da reunião em um único parágrafo.
    Em seguida, esceva ua lista de cada um de seus pontos-chaves tratados na reunião.
    Por fim, liste as próxias etapas ou itens de ação sugeridos pelos palestrante, se houver.
    O texto transcrito da reunião segue abaixo:
    {transcricao}"""

    st.text("Result: ")
    print("-------------> Result: ")
    st.text(gpt_request(openai_client, system_prompt, user_prompt))
    print(gpt_request(openai_client, system_prompt, user_prompt))
