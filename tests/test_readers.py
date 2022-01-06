"""Tests reading"""
from qiyas import qs
from qiyas import UNIT_TABLES_DIRECTORY
from qiyas.conversion.reader import load_from_tables

   
def test_qiyas():
    """testing main qiyas functionality"""
    assert qs.convert(10, "m", "cm", "length") == 1000

def test_reader_tables():
    """Testing reader using tables"""
    qs_object = load_from_tables(UNIT_TABLES_DIRECTORY)
    assert qs_object.convert(10, "m", "cm", "length") == 1000
