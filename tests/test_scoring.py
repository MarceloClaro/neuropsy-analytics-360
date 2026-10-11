import pytest
from core.scoring import summarize
from core.domains import DOMAINS

def test_thirty_domains():
    assert len([d for ds in DOMAINS.values() for d in ds]) == 30

def test_score():
    assert summarize({'a': 0, 'b': 4}) == {'n': 2, 'mean': 2.0, 'total': 4}

@pytest.mark.parametrize('responses', [{}, {'a': 5}, {'a': -1}, {'a': 2.5}, {'a': True}])
def test_invalid(responses):
    with pytest.raises(ValueError):
        summarize(responses)
