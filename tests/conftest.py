from pytest import fixture


@fixture
def translator():
    from drago import Translator
    return Translator()