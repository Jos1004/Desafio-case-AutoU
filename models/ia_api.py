import os
from huggingface_hub import InferenceClient

#algoritmo
palavras_chave_produtivo = ['priorizar', 'urgência', 'urgencia', 'organizar', 'organização',
'encaminhar', 'notificar', 'notificação', 'emergência', 'emergencia', 'ajuda', 'prazo',
'prazos', 'pendente', 'pendencias', 'problema', 'resultados', 'suporte', 'técnico', 'tecnico',
'meta', 'metas', 'confirmar', 'informar', 'informações', 'impressora', 'computador', 'arquivo',
'arquiva', 'arquivado', 'arquivados', 'escritório', 'escritorio', 'machucou', 'feriu', 'ausentou',
'problemas', 'problema', 'manutenção', 'vagas', 'seleção', 'empresa', 'financeiro', 'sponsor',
'cotas', 'equipamentos', 'investimentos', 'investi', 'investiu', 'reunião', 'time', 'equipe',
'trabalho', 'evento', 'projeto', 'modelagem', 'analise', 'análise', 'analista', 'recursos',
'beneficios', 'benefício', 'dinheiro', 'bens', 'serviços', 'serviço', 'desenvolvimento', 'teste',
 'testado', 'fase', 'etapa', 'metodologia', 'metologias', 'team', 'publicidade', 'financiar',
 'capital', 'patrocínio', 'patrocinios', 'stakeholders', 'ágeis', 'ágil', 'objetivos', 'responavel',
 'responsive', 'responsável', 'rh', 'recusa', 'administrar', 'custos', 'gastos', 'gestão',
'assunção', 'orçamento', 'orçamentário', 'orçamentários', 'orçamentario', 'orçamentário', 'vendas', 'venda'
'financiador', 'despesas', 'poupar', 'monitorar', 'monitoração', 'desempenho', 'qualifica',
'qualificações', 'terceiros', 'dívidas', 'dúvidas', 'dividas', 'duvidas', 'analitica', 'renda',
 'padronizar', 'cargo', 'demissão', 'demissões', 'comercial', 'impostos', 'fluxos', 'entidade',
'apresentação', 'finanças', 'economia', 'gerencia', 'gerenciar', 'mensalidades', 'bimestre', 'trimestre',
'atraso', 'entrega', 'atrasar', 'solicitação', 'agenda', 'agendar', 'resolve', 'resolver', 'relatório',
'relatórios', 'solicito', 'importante', 'ação', 'ações', 'requerimento', 'critico','decisão', 'atingir',
'finalizar', 'concluir', 'importante', 'finalizado', 'plano', 'clientes', 'cliente', 'quebrado', 'concerto',
'configurar', 'cortês', 'configurações','sistema', 'atualizações', 'atualizar', 'enviar', 'envio',
 'marketing','funcionalidade', 'funcionalidade', 'contas', 'comunicado', 'comunicar', 'colaborador',
'colaborar', 'colaboradores', 'lider', 'líder', 'lideranças', 'liderança', 'produtivo', 'produto final',
'produto', 'produtividade', 'solicito', 'solução']

palavras_chave_improdutivo = ['obrigado', 'obrigada', 'agradecimentos', 'agradeço', 'melhoras'
, 'possibilitou', 'agradecimento', 'amo', 'amor', 'carinho', 'apoio', 'felicidades', 'universo'
, 'amiga', 'amigo', 'fofoca', 'sorrir', 'felicidade', 'melhor', 'proteger', 'proteção', 'esperança'
'momentos', 'sorriso', 'coração', 'gratidão', 'sonhar', 'inveja', 'vida', 'gostaria', 'apoiar',
'odio', 'odeio', 'sonho', 'querido', 'querida', 'invejo', 'sentir', 'emociona', 'emocionada'
,'emocionado', 'valeu', 'ferrar', 'apoiado', 'apoiada', 'grato', 'grata', 'gratidão', 'acredito',
'gosto', 'gosta', 'saudades', 'aconchego', 'deus', 'desabafar', 'família', 'alegre', 'alegria',
'generosidade', 'acolhe', 'acolhimento', 'generoso', 'generosa', 'conforta', 'conforto',
'acolheu', 'lembranças', 'grandiosas', 'vitórias', 'vitória', 'vitoria', 'dançar', 'dança',
'samba', 'sambar', 'divertisse', 'inspirar', 'inspiração', 'celebre', 'celebramos', 'venceu', 'chaveco'
, 'inspira', 'belas', 'deusa', 'anjo', 'juro', 'jura', 'jurar','bondade', 'bom dia','boa tarde',
'boa noite', 'n/a','rir', 'chorar', 'gritar', 'newsletter' ,'lagrimas', 'lindo', 'sinto',
 'linda', 'bonita', 'bonito', 'namorar', 'sentimentos', 'namorada', 'namorado',
'superação', 'desejo', 'mundo', 'deuses', 'dores', 'xaveco', 'aniversario', ' aniversário', 'aniversariante',
'especial', 'conquistas', 'conquistou', 'celebra', 'parabéns', 'parabens', 'realizações', 'cativa', 'enoja'
'enjoa', 'abençoe', 'harmonia', 'paz', 'encanto', 'encantamento', 'valorosas', 'valorizar', 'emoções',
 'comemorar', 'comemorações', 'festejar', 'amizade', 'fugir', 'ódio', 'falso', 'falsa', 'risos',
 'puto', 'puta', 'arrombado', 'viver', 'frieza', 'covardia', 'covarde', 'dor', 'raivoso',
 'rancoroso', 'rancorosa', 'cicatriz', 'cicatrizes', 'terror', 'abalada', 'natal', 'pascoa', 'páscoa',
 'graças', 'cinzas', 'crianças', 'feriado', 'tiradentes', 'feriados', 'finados', 'corpus', 'christi',
 'divertido', 'divertidissimo', 'divertidíssimo', 'diversão', 'inimigo', 'inimigos', 'carnaval',
 'folia', 'sacanagem', 'doente', 'doença', 'tristeza', 'tristesa', 'riso', 'raiva','rancor',
 'cacete', 'caralho', 'arrombar', 'arrombada', 'esporro','ignorante',
 'insensível', 'apaixonada', 'apaixonado', 'paixão']

def classificar_por_palavras_chaves(texto):
    texto_tokens = texto.split()
    pontuacao_produtivo = sum(token in palavras_chave_produtivo for token in texto_tokens)
    pontuacao_improdutivo = sum(token in palavras_chave_improdutivo for token in texto_tokens)

    if pontuacao_produtivo > pontuacao_improdutivo:
        return "produtivo"
    if pontuacao_improdutivo > pontuacao_produtivo:
        return "improdutivo"
    else:
        return "indefinido"

#classficação pela API
hf_token = os.getenv("HUGGINGFACE_API_TOKEN")
if not hf_token:
    raise ValueError("A variável de ambiente HUGGINGFACE_API_TOKEN não está definida.")

client = InferenceClient(token=hf_token)

def chamar_api_ia(texto):
    resultado_local = classificar_por_palavras_chaves(texto)

    # Define mensagens baseadas no resultado local
    if resultado_local == "produtivo":
        mensagem_local = "necessita de atenção imediata."
    elif resultado_local == "improdutivo":
        mensagem_local = "não é importante e pode ser ignorado."
    else:
        mensagem_local = "A prioridade deste e-mail é indefinida."

    try:
        # Chama a API Hugging Face
        response = client.text_classification(
            texto,
            model="nlptown/bert-base-multilingual-uncased-sentiment"
        )
        label = response[0]['label'].lower()

        if label in ["1 stars", "5 stars"]:
            return "improdutivo", f"Este e-mail é: improdutivo {mensagem_local}"
        else:
            return "produtivo", f"Este e-mail é: produtivo {mensagem_local}"
    except Exception as e:
        print("Erro na chamada da API externa", e)
        return mensagem_local
