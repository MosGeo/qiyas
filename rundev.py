'''Script used for quick testing'''
import qiyas
from qiyas.construction.reader import get_unit_types, read_unit_tables, generate_graphs
from qiyas.construction.graph import UnitGraph
from qiyas.conversion.reader import load_from_qs_files

unit_types = get_unit_types(qiyas.UNIT_TABLES_DIRECTORY)

unit_graph = UnitGraph('Distance')
unit_graph.add_unit('m','meter')
unit_graph.add_unit('cm','centimeter')
is_unit = unit_graph.is_unit('cm')
# print(unit_graph.graph.nodes)


d = qiyas.UNIT_TABLES_DIRECTORY / "distance_names.csv"

generate_graphs(qiyas.UNIT_TABLES_DIRECTORY, qiyas.UNIT_GRAPHS_DIRECTORY)
g2 = load_from_qs_files(qiyas.UNIT_GRAPHS_DIRECTORY)
multplier = g2.get_multiplier('m','cm', 'distance')
print(multplier)
