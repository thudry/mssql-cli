import pytest
from mssqlcli.mssqlbuffer import _is_complete


class TestMssqlCliMultiline:
    testdata = [
        (None, False),
        ('', False),
        ('select 1 /* open comment!\ngo', False),
        ('select 1\ngo -- another comment', True),
        ('select 1; select 2, "open quote: go', False),
        ('select 1\n"go"', False),
        ('select 1; GO', False),
        ('SELECT 4;\nGO', True),
        ('select 1\n select 2;\ngo', True),
        ('select 1;', False),
        ('select 1 go', False),
        ('select 1\ngo go go', False),
        ('GO select 1', False),
        ('GO', True)
        # tests below to be enabled when sqlparse supports retaining newlines
        # when stripping comments (tracking here:
        # https://github.com/andialbrecht/sqlparse/issues/484):
        # ('select 3 /* another open comment\n*/   GO', True),
        # ('select 1\n*/go', False),
        # ('select 1 /*\nmultiple lines!\n*/go', True)
    ]

    @staticmethod
    @pytest.mark.parametrize("query_str, is_complete", testdata)
    def test_multiline_completeness(query_str, is_complete):
        """
        Tests the _is_complete helper method, which parses a T-SQL multiline
        statement on each newline and determines whether the script should
        execute.
        """
        assert _is_complete(query_str) == is_complete
