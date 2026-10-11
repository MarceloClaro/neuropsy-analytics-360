# SDD — NeuroPsy Analytics 360 v0.3.0

**Status:** protótipo exploratório, NÃO validado para avaliação psicométrica clínica. Público-alvo: adultos (18+). Altas habilidades/superdotação é um tema de autoexploração, não de identificação formal.

## Requisitos verificáveis

| ID | Contrato do sistema | Evidência |
|---|---|---|
| SDD-01 | 6 grupos, 30 domínios únicos | `test_registry_has_30_unique_domains` |
| SDD-02 | Escore descritivo aceita apenas inteiros de 0 a 4, recusando vazio e inválidos | `test_score`, `test_invalid` |
| SDD-03 | Registros frontend e backend idênticos | `test_frontend_registry_matches_backend` |
| SDD-04 | Frontend não envia respostas à rede, não persiste dados, não depende de fontes externas | `test_frontend_stores_nothing_and_fetches_nothing` |
| SDD-05 | Espelho de Pages em /docs corresponde a /frontend | `test_pages_mirror_matches_frontend` |
| SDD-06 | Exige confirmação de maioridade e ciência de limites | `test_adult_gate_is_present` |
| SDD-07 | Linguagem descritiva, não diagnóstica | `test_non_diagnostic_messages` |
| SDD-08 | JavaScript sintaticamente válido | `node --check frontend/app.js` e `node --check docs/app.js` |
| SDD-09 | CI configura Python, Node, Pytest e análise de sintaxe | `.github/workflows/tests.yml` |
| SDD-10 | Credenciais e respostas reais não entram no controle de versão | Revisão manual, `.gitignore` |

## Fluxo

1. O adulto lê o aviso e confirma idade mínima de 18 anos e os limites de uso.
2. Seleciona um grupo, responde opcionalmente os itens 0–4.
3. Visualiza exclusivamente respostas brutas descritivas e ausências.
4. Exporta CSV/JSON/imprime ou limpa a sessão.
5. Ao recarregar ou fechar a aba, as respostas são descartadas.

## Segurança e limites científicos

- Não usar itens protegidos, pontos de corte não validados ou escores inventados.
- Este protótipo não avalia risco suicida nem faz classificação automática.
- Não é adequado para laudos, seleção de pessoas, diagnóstico ou identificação formal de altas habilidades.
- Para uso com dados sensíveis, implementar arquitetura separada com conformidade LGPD, acesso controlado, auditoria, revisão ética e governança clínica.
- A acessibilidade requer ainda testes manuais com tecnologias assistivas.
- Testes de software não equivalem a evidências de validade ou precisão psicométrica.
