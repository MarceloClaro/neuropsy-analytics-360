"""NeuroPsy Analytics 360: demonstração, não dispositivo diagnóstico."""
import json
from datetime import datetime, timezone
from io import BytesIO
import pandas as pd
import streamlit as st
from core.domains import DOMAINS

st.set_page_config(page_title='NeuroPsy Analytics 360', layout='wide')
st.title('NeuroPsy Analytics 360')
st.warning('Protótipo de pesquisa não validado. Não diagnostica depressão, TDAH, superdotação ou outros transtornos. Não substitui avaliação profissional.')
st.caption('Somente adultos (18+). Dados desta demonstração ficam na sessão; não são gravados pelo código do aplicativo.')

with st.sidebar:
    st.header('Configuração')
    adult = st.checkbox('Confirmo ter 18 anos ou mais')
    consent = st.checkbox('Concordo com o processamento temporário das respostas nesta sessão')
    st.info('Não informe nome, CPF, e-mail ou informações que permitam identificação.')
    if st.button('Limpar sessão'):
        st.session_state.clear()
        st.rerun()

if not (adult and consent):
    st.info('Confirme maioridade e consentimento para habilitar a demonstração.')
    st.stop()

st.markdown('### Formulário exploratório')
st.write('Os itens abaixo são perguntas genéricas de auto-observação, não são itens oficiais de escalas psicométricas. Respostas de 0 (nunca) a 4 (muito frequentemente), referentes às últimas duas semanas. Para altas habilidades, esta janela é apenas uma convenção demonstrativa e não é apropriada para identificação formal.')
choices = ['0 — Nunca', '1 — Raramente', '2 — Às vezes', '3 — Frequentemente', '4 — Muito frequentemente']
with st.form('screening'):
    answers = {}
    for group, domains in DOMAINS.items():
        with st.expander(group, expanded=False):
            for name in domains:
                item_id = f'{group}::{name}'
                answer = st.selectbox(f'Com que frequência você percebe aspectos relacionados a **{name}** em sua experiência?', ['Selecione uma resposta'] + choices, key=item_id)
                answers[item_id] = None if answer == 'Selecione uma resposta' else int(answer[0])
    submitted = st.form_submit_button('Calcular estatísticas descritivas')

if submitted:
    if any(v is None for v in answers.values()):
        st.error('Responda aos 30 itens antes de continuar. Nenhuma resposta foi salva.')
    else:
        st.session_state['result'] = {'answers': answers, 'created_at': datetime.now(timezone.utc).isoformat()}

if 'result' in st.session_state:
    result = st.session_state['result']
    rows = []
    for group, domains in DOMAINS.items():
        for name in domains:
            rows.append({'Grupo': group, 'Domínio': name, 'Resposta (0–4)': result['answers'][f'{group}::{name}']})
    df = pd.DataFrame(rows)
    st.subheader('Perfil descritivo (sem interpretação clínica)')
    st.dataframe(df, hide_index=True, use_container_width=True)
    grouped = df.groupby('Grupo', sort=False)['Resposta (0–4)'].mean()
    st.bar_chart(grouped)
    st.caption('Médias entre domínios não representam gravidade, diagnóstico, risco clínico ou identificação de altas habilidades.')
    st.download_button('Exportar CSV', df.to_csv(index=False).encode('utf-8-sig'), 'respostas_exploratorias.csv', 'text/csv')
    st.download_button('Exportar JSON', json.dumps(result, ensure_ascii=False, indent=2).encode('utf-8'), 'respostas_exploratorias.json', 'application/json')
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
        from reportlab.lib.styles import getSampleStyleSheet
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4)
        styles = getSampleStyleSheet()
        story = [Paragraph('NeuroPsy Analytics 360 — Demonstração', styles['Title']), Paragraph('Resultados exploratórios, não diagnósticos.', styles['Normal']), Spacer(1, 12)]
        for row in rows:
            story.append(Paragraph(f"{row['Domínio']}: {row['Resposta (0–4)']}/4", styles['Normal']))
        doc.build(story)
        st.download_button('Exportar PDF', buffer.getvalue(), 'relatorio_exploratorio.pdf', 'application/pdf')
    except ImportError:
        st.info('Instale reportlab para habilitar o PDF.')
