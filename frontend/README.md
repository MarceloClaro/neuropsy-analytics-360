# Frontend autônomo — NeuroPsy Analytics 360

Abra `index.html` no navegador. Não é necessário Python, Streamlit, servidor, login ou conexão à internet para as funcionalidades locais (a fonte remota tem fallback local).

- Navegação, questionário de 30 domínios, respostas 0–4 opcionais, progresso, painel descritivo, exportações CSV/JSON e impressão/PDF.
- Respostas ficam somente na memória da aba e são descartadas ao fechar/recarregar; sem API, cookies ou localStorage.
- **Não é instrumento psicométrico validado e não fornece diagnóstico, triagem de crise ou identificação de superdotação.** Itens genéricos e resultados brutos, sem ponto de corte.

Para publicar: Settings → Pages → Build and deployment → GitHub Actions. O workflow na raiz `.github/workflows/pages.yml` publica o diretório `frontend/`.
