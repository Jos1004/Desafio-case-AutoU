# Desafio-case-AutoU

Objetivo desse código é simplicaficar a leitura de textos de e-mails os classificando em produtivo e improdutivo, isso realizado através da API do Hugging Face e fazendo o uso também de um algoritmo que basease em um conjuto de palavras chaves para ajudar a determinar o resultado.

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

o link para o deploy (foi utilizado render): https://desafio-case-autou.onrender.com/

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Para executar o repositório em um localhost, primeiro faça o download do repositório e instale as dependências tudo de uma vez no arquivo requirements.txt 
Os principais pacotes usados neste projeto são:

emoji
Flask
huggingface-hub
spacy
regex
requests
PyPDF2
pt_core_news_sm
gunicorn

Após todo o projeto estar em ordem e os dependências instaladas, abra o seu terminal localize o diretório aonde está o app.py em seguida digite o seguinte comando:
python app.py

Abra seu navegador e acesse:
http://127.0.0.1:5000/
