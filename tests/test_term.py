import pytest

from parser.term import Term


@pytest.mark.parametrize("content,_hash", [(["test"], 1516901269977571296)])
def test_hash(content, _hash):
    term = Term()
    for line in content:
        term.append(line)
    assert hash(term) == _hash
