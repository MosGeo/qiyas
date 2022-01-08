"""Tests reading"""
from pathlib import Path
from qiyas.convertor import load_convertor_from_tables
from qiyas.generator import generate_graphs, get_unit_types

QIYAS_DIRECTORY = Path(__file__).parent
UNIT_TABLES_DIRECTORY = QIYAS_DIRECTORY / "data" / "unit_tables"
UNIT_GRAPHS_DIRECTORY = QIYAS_DIRECTORY / "data" / "unit_graphs"

print(UNIT_TABLES_DIRECTORY)


def test_reader_tables():
    """Testing reader using tables"""
    qs_object = load_convertor_from_tables(UNIT_TABLES_DIRECTORY)
    assert qs_object.convert(10, "m", "cm", "length") == 1000


def test_reader_qs():
    """Testing reader using qs"""
    generate_graphs(UNIT_TABLES_DIRECTORY, UNIT_GRAPHS_DIRECTORY, is_construct=True)
    unit_types = get_unit_types(UNIT_GRAPHS_DIRECTORY)
    assert unit_types == {"length", "mass", "volume"}
