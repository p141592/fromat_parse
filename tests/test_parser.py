import pytest

from parser import Parser, CodeExcept
from parser.term import ListExcept, BlockEndExcept, TitleExcept


def test_parser():
    assert Parser.check_document('about.txt') == 'about.txt'


def test_title_except():
    with pytest.raises(TitleExcept):
        Parser.read_line('====')


def test_code_except():
    with pytest.raises(CodeExcept):
        Parser.read_line('    test')
    with pytest.raises(CodeExcept):
        Parser.read_line('        test')
    with pytest.raises(CodeExcept):
        Parser.read_line('            test')


def test_list_exception():
    with pytest.raises(ListExcept):
        Parser.read_line('* test')
    with pytest.raises(ListExcept):
        Parser.read_line('  * test')
    with pytest.raises(ListExcept):
        Parser.read_line('    * test')


def test_block_end():
    with pytest.raises(BlockEndExcept):
        Parser.read_line('\n')