"""Initializes qiyas"""
from pathlib import Path

from qiyas.convertor import load_convertor_from_qs_files


QIYAS_DIRECTORY = Path(__file__).parent
UNIT_TABLES_DIRECTORY = QIYAS_DIRECTORY / "unit_tables"
UNIT_GRAPHS_DIRECTORY = QIYAS_DIRECTORY / "unit_graphs"

qs = load_convertor_from_qs_files(UNIT_GRAPHS_DIRECTORY)
