"""A script to generate qs files"""
from qiyas import UNIT_TABLES_DIRECTORY, UNIT_GRAPHS_DIRECTORY
from qiyas.generator import generate_graphs
generate_graphs(UNIT_TABLES_DIRECTORY, UNIT_GRAPHS_DIRECTORY)