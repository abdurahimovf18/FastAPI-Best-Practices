from inspect import Signature, signature

from src.utils import misc


@misc.memorize
def add(a: int, b: int) -> int:
    return a + b


def test_memorize():
    memorized_resp = add(1, 2)
    assert memorized_resp == add(1, 2)


def test_inspect_function():
    result = misc.inspect_function(add)

    assert isinstance(result, Signature)
    assert result == signature(add)
