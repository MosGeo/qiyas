"""Script used for quick testing"""
import qiyas
from qiyas.generator import get_unit_types, generate_graphs
from qiyas.graph import UnitGraph
from qiyas.convertor import load_convertor_from_qs_files

unit_types = get_unit_types(qiyas.UNIT_TABLES_DIRECTORY)

unit_graph = UnitGraph("Distance")
unit_graph.add_unit("m", "meter")
unit_graph.add_unit("cm", "centimeter")
is_unit = unit_graph.has_unit("cm")
# print(unit_graph.graph.nodes)


d = qiyas.UNIT_TABLES_DIRECTORY / "distance_names.csv"

generate_graphs(qiyas.UNIT_TABLES_DIRECTORY, qiyas.UNIT_GRAPHS_DIRECTORY)
uc = load_convertor_from_qs_files(qiyas.UNIT_GRAPHS_DIRECTORY)
multplier = uc.get_multiplier("km", "cm", "length")
print(multplier)
value_m = 10  # pylint: disable=invalid-name
value_cm = uc.to(value_m, "cm")
print(value_cm)
multplier = uc.get_multiplier("km", "cm")