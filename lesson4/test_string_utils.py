import pytest
from StringUtils import StringUtils

Utils = StringUtils()

@pytest.mark.skip
@pytest.mark.parametrize( 'string, result', 
[('skypro', 'Skypro'), ('hope', 'Hope'), (123, 123), ('', '')] )
def test_capitilize(string, result):
    res = Utils.capitilize(string)
    assert res == result

@pytest.mark.skip
@pytest.mark.parametrize( 'string, result', 
[('skypro', 'skypro'), (' hope', 'hope'), ('  hope', 'hope'), ('                     hope', 'hope'), (123, 123), ('', '')] )
def test_trim(string, result):
    res = Utils.trim(string)
    assert res == result

@pytest.mark.skip
@pytest.mark.parametrize( 'string, delimeter, result', 
[('a,b,c,d', ',', ["a", "b", "c", "d"]), ('a:b:c', ':', ["a", "b", "c"]), ('a-b-c', '-', ["a", "b", "c"]), ('', '', [])] )
def test_to_list(string, delimeter, result):
    res = Utils.to_list(string, delimeter)
    assert res == result

@pytest.mark.skip
@pytest.mark.parametrize( 'string, symbol, result', 
[("SkyPro", "S", True), ("SkyPro", "U", False), ("123", "2", True), ('', 'a', False), ('', 'a', True)] )
def test_contains(string, symbol, result):
    res = Utils.contains(string, symbol)
    assert res == result

@pytest.mark.skip
@pytest.mark.parametrize( 'string, symbol, result', 
[("SkyPro", "k", "SyPro"), ("SkyPro", "Pro", "Sky"), ("123", "2", "13"), ('', '', '')] )
def test_delete_symbol(string, symbol, result):
    res = Utils.delete_symbol(string, symbol)
    assert res == result

@pytest.mark.skip
@pytest.mark.parametrize( 'string, symbol, result', 
[("SkyPro", "S", True), ("SkyPro", "P", False), ("123", "1", True), ('', '', True)] )
def test_starts_with(string, symbol, result):
    res = Utils.starts_with(string, symbol)
    assert res == result

@pytest.mark.skip
@pytest.mark.parametrize( 'string, symbol, result', 
[("SkyPro", "o", True), ("SkyPro", "y", False), ("123", "3", True), ('', '', True)] )
def test_end_with(string, symbol, result):
    res = Utils.end_with(string, symbol)
    assert res == result

@pytest.mark.skip
@pytest.mark.parametrize( 'string, result', 
[("", True), (" ", True), ("SkyPro", False), ("SkyPro", True)] )
def test_is_empty(string, result):
    res = Utils.is_empty(string)
    assert res == result

#@pytest.mark.skip
@pytest.mark.parametrize( 'lst, joiner, result', 
[([1,2,3,4], ",", "1,2,3,4"), (["Sky", "Pro"], ":", "Sky:Pro"), (["Sky", "Pro"], "-", "Sky-Pro"), ([], '-', '')] )
def test_list_to_string(lst, joiner, result):
    res = Utils.list_to_string(lst, joiner)
    assert res == result