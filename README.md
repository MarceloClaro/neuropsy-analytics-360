# NeuroPsy Analytics 360

**Protótipo exploratório para adultos (18+). Não é instrumento validado nem ferramenta diagnóstica.**

## Como executar

```bash
python -m venv .venv
source .venv/bin/activate # No Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
python -m pytest -q
streamlit run app.py
```

## Frontend autônomo

Abra `frontend/index.html` diretamente no navegador. Há navegação, questionário demonstrativo, resultados descritivos e exportação CSV/JSON/impressão. As respostas ficam apenas em memória da aba; não há backend nem persistência do frontend.

## Escopo

30 domínios em seis grupos, incluindo depressão, desatenção/TDAH e altas habilidades/superdotação. Há um item exploratório por domínio, sem validade psicométrica estabelecida. Não existem pontos de corte ou diagnóstico. **Não utilizar para laudos, seleção, triagem de crise, decisões clínicas ou identificação formal de altas habilidades.**

## SDD / TDD

Contratos: exatamente 30 domínios, respostas inteiras de 0 a 4, tratamento de ausências, ausência de itens protegidos e de classificação clínica. Testes unitários em `tests/`, executados por GitHub Actions.

## Segurança, privacidade e implantação

**Não insira nem publique dados clínicos reais, segredos ou identificadores no GitHub.** O código demo pode ser público, mas o uso com dados sensíveis exige conformidade LGPD, revisão ética, gestão de acesso, armazenamento protegido e governança clínica.

Para GitHub Pages: Settings → Pages → Build and deployment → GitHub Actions. O workflow `.github/workflows/pages.yml` publica a pasta `frontend`. Para o Streamlit, implante separadamente com `app.py` como entrada.

A publicação de código ou interface não confere validação científica aos itens exploratórios.
