import re
import emoji
import spacy
import PyPDF2

nlp = spacy.load('pt_core_news_sm')

def clean_text(text):
    text = emoji.replace_emoji(text, replace="")
    text = re.sub(r'[^\w\sáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ]', '', text, flags=re.UNICODE)
    text = text.lower()
    text = re.sub(r'\d+', '', text) #remoção de números
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_text_from_pdf(file_steam):
    """
    Recebe o caminho de um arquivo PDF e retorna o texto extraído
    """
    texto_total = ""
    pdf_reader = PyPDF2.PdfReader(file_steam)
    for pagina in pdf_reader.pages:
            texto_pagina = pagina.extract_text()
            if texto_pagina:
                texto_total += texto_pagina + "\n"
    return texto_total

def preprocess_text(text):
   """
   Recebe um texto retorna texto limpo após pré-processamento:
   remoção de stop words, pontuação, números, lematização.
   """
   doc = nlp(text)
   tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop and not token.like_num]
   texto_processado = " ".join(tokens).lower()
   return texto_processado
