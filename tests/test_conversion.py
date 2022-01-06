"""Tests conversion"""
import sys
import pytest
from qiyas.graph import UnitGraph
from qiyas.convertor import (
    UnitConvertor,
    TypeDetectionNotPossible,
    UnitsTypeMismatch,
    TypeNotFound,
)


def test_initializaiton_quick_convert():
    "Test initialization of unit conversion"
    unit_convertor = UnitConvertor({})
    if sys.version_info.minor >= 8:
        assert unit_convertor.is_quick_convert_possible is True
    else:
        assert unit_convertor.is_quick_convert_possible is False


def test_unit_types():
    """Testing convertor dictionary"""
    unit_graph1 = UnitGraph("length")
    unit_graph2 = UnitGraph("Weight")
    convertor_dictionary = dict()
    convertor_dictionary["length"] = unit_graph1
    convertor_dictionary["Weight"] = unit_graph2
    unit_convertor = UnitConvertor(convertor_dictionary)
    assert unit_convertor.get_unit_types() == ["length", "Weight"]


def test_possible_types():
    """Test possible types"""
    unit_graph1 = UnitGraph("U1")
    unit_graph2 = UnitGraph("U2")
    unit_graph3 = UnitGraph("U3")

    unit_graph1.add_unit("m", "meter", "m")
    unit_graph1.add_unit("cm", "centimeter", "cm")
    unit_graph2.add_unit("cm", "centimeter", "cm")
    unit_graph3.add_unit("m", "meter", "m")

    convertor_dictionary = {}
    convertor_dictionary["U1"] = unit_graph1
    convertor_dictionary["U2"] = unit_graph2
    convertor_dictionary["U3"] = unit_graph3

    unit_convertor = UnitConvertor(convertor_dictionary)
    possible_types = unit_convertor.get_possible_types(["m"])
    assert possible_types == ["U1", "U3"]
    with pytest.raises(TypeDetectionNotPossible):
        unit_convertor.validate_possible_type("m", possible_types)

    possible_types = unit_convertor.get_possible_types(["m", "cm"])
    assert possible_types == ["U1"]
    unit_type = unit_convertor.validate_possible_type(["m", "cm"], possible_types)
    assert unit_type == "U1"

    possible_types = unit_convertor.get_possible_types(["mm"])
    assert len(possible_types) == 0
    with pytest.raises(TypeDetectionNotPossible):
        unit_convertor.validate_possible_type(["mm"], possible_types)


def test_validate_units():
    """Test units validation"""
    unit_graph1 = UnitGraph("U1")
    unit_graph1.add_unit("m", "meter", "m")
    unit_graph1.add_unit("cm", "centimeter", "cm")
    unit_graph1.add_unit("mm", "millimeter", "mm")
    convertor_dictionary = {}
    convertor_dictionary["U1"] = unit_graph1
    unit_convertor = UnitConvertor(convertor_dictionary)
    unit_convertor.validate_units(["m", "cm"], "U1")
    with pytest.raises(UnitsTypeMismatch):
        unit_convertor.validate_units(["m", "um"], "U1")


def test_get_multiplier():
    """Test get multiplier"""
    unit_graph = UnitGraph("length")
    unit_graph.add_unit("m", "meter", "m")
    unit_graph.add_unit("cm", "centimeter", "cm")
    unit_graph.add_unit("mm", "millimeter", "mm")
    unit_graph.add_conversion("m", "mm", 1000)
    unit_graph.add_conversion("m", "cm", 100)

    convertor_dictionary = {}
    convertor_dictionary["length"] = unit_graph

    unit_convertor = UnitConvertor(convertor_dictionary)

    assert unit_convertor.get_multiplier("cm", "m")[2] == 0.01
    assert unit_convertor.get_multiplier("cm", "m", "length")[2] == 0.01

    with pytest.raises(TypeNotFound):
        unit_convertor.get_multiplier("cm", "m", "Weight")

    unit_graph.construct_full_graph()
    assert unit_convertor.get_multiplier("cm", "m", "length")[2] == 0.01


def test_convertion():
    """Testing conversion"""
    unit_graph = UnitGraph("length")
    unit_graph.add_unit("m", "meter", "m")
    unit_graph.add_unit("cm", "centimeter", "cm")
    unit_graph.add_unit("mm", "millimeter", "mm")
    unit_graph.add_conversion("m", "mm", 1000)
    unit_graph.add_conversion("m", "cm", 100)

    convertor_dictionary = {}
    convertor_dictionary["length"] = unit_graph

    unit_convertor = UnitConvertor(convertor_dictionary)
    value_m = 10
    value_cm = unit_convertor.convert(value_m, "m", "cm")
    assert value_cm == 1000

    if sys.version_info.minor >= 8:
        value_cm = unit_convertor.to(value_m, "cm")
        assert value_cm == 1000
