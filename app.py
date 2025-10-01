from flask import Flask, render_template, request
from utils.preprocessing import clean_text, extract_text_from_pdf, preprocess_text
from models.ia_api import chamar_api_ia

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'pdf', 'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processar', methods=['GET', 'POST'])
def processar():
   if request.method == 'POST':
      print("Recebendo a requisição POST no Flask")
      texto_email = request.form.get('text', '')
      arquivo = request.files.get('file')
      texto_final = ""

      if arquivo and allowed_file(arquivo.filename):
        ext = arquivo.filename.rsplit('.', 1)[1].lower()
        if ext == 'pdf':
            texto_pdf = extract_text_from_pdf(arquivo)
            texto_final = texto_pdf
        elif ext == 'txt':
            texto_txt = arquivo.read().decode('utf-8')
            texto_final = texto_txt
      elif texto_email:
          texto_final = texto_email

      if texto_final:
          texto_limpo = clean_text(texto_final)
          texto_processado = preprocess_text(texto_limpo)

          #print("Texto limpo:", texto_limpo)
          #print("Texto_preprocessado:", texto_processado)

          status, mensagem_classificacao = chamar_api_ia(texto_limpo)

          return render_template('index.html',
          mensagem=mensagem_classificacao, status=status, texto_processado=texto_processado)

print('teste ;)')

if __name__ == '__main__':
    app.run(debug=True)