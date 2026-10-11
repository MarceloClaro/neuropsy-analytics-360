"""Estatísticas descritivas, sem pontos de corte clínicos."""
def summarize(responses: dict[str, int]) -> dict:
    if not responses or any(type(v) is not int or v not in (0, 1, 2, 3, 4) for v in responses.values()):
        raise ValueError('Respostas devem ser inteiros de 0 a 4.')
    return {'n': len(responses), 'mean': round(sum(responses.values()) / len(responses), 2), 'total': sum(responses.values())}
