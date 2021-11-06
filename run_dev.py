"""Script used for quick testing"""
import qiyas
from qiyas.construction.reader import get_unit_types, generate_graphs
from qiyas.construction.graph import UnitGraph
from qiyas.conversion.reader import load_from_qs_files

unit_types = get_unit_types(qiyas.UNIT_TABLES_DIRECTORY)

unit_graph = UnitGraph("Distance")
unit_graph.add_unit("m", "meter")
unit_graph.add_unit("cm", "centimeter")
is_unit = unit_graph.has_unit("cm")
# print(unit_graph.graph.nodes)


d = qiyas.UNIT_TABLES_DIRECTORY / "distance_names.csv"

generate_graphs(qiyas.UNIT_TABLES_DIRECTORY, qiyas.UNIT_GRAPHS_DIRECTORY)
uc = load_from_qs_files(qiyas.UNIT_GRAPHS_DIRECTORY)
multplier = uc.get_multiplier("km", "cm", "length")
print(multplier)
x_m = 10
x_cm = uc.to(x_m, "cm")
print(x_cm)
