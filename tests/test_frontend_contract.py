from pathlib import Path
import json
from core.domains import DOMAINS

ROOT = Path(__file__).resolve().parents[1]
FRONT = ROOT / 'frontend'
PAGES = ROOT / 'docs'


def test_registry_has_30_unique_domains():
    assert len(DOMAINS) == 6
    all_names = [name for domains in DOMAINS.values() for name in domains]
    assert len(all_names) == 30
    assert len(set(all_names)) == 30


def test_frontend_registry_matches_backend():
    with (FRONT / 'domains.json').open(encoding='utf-8') as f:
        ui_registry = json.load(f)
    assert ui_registry == DOMAINS


def test_frontend_stores_nothing_and_fetches_nothing():
    js = (FRONT / 'app.js').read_text(encoding='utf-8')
    css = (FRONT / 'styles.css').read_text(encoding='utf-8')
    html = (FRONT / 'index.html').read_text(encoding='utf-8')
    for forbidden in ('localStorage', 'sessionStorage', 'indexedDB', 'fetch(', 'XMLHttpRequest', 'sendBeacon', 'eval('):
        assert forbidden not in js
    assert '@import' not in css
    assert 'https://' not in css
    assert '<script src="https://' not in html


def test_pages_mirror_matches_frontend():
    for filename in ('index.html', 'app.js', 'styles.css', 'domains.json'):
        assert (PAGES / filename).read_bytes() == (FRONT / filename).read_bytes()


def test_adult_gate_is_present():
    html = (FRONT / 'index.html').read_text(encoding='utf-8')
    js = (FRONT / 'app.js').read_text(encoding='utf-8')
    assert 'id="confirm-adult"' in html
    assert 'id="confirm-demo"' in html
    assert "view==='survey'" in js
    assert "$('confirm-adult').checked" in js


def test_non_diagnostic_messages():
    html = (FRONT / 'index.html').read_text(encoding='utf-8')
    js = (FRONT / 'app.js').read_text(encoding='utf-8')
    assert 'Não há classificação clínica, diagnóstico' in html
    assert 'não diagnóstica' in js
