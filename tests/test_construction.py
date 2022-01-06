"""Tests construction"""
import pytest
from qiyas.graph import UnitGraph, UnitNotFound


def test_unit_type():
    """Tests the creation of UnitGraph"""
    unit_graph = UnitGraph("Distance")
    assert unit_graph.unit_type == "Distance"


def test_adding_unit():
    "Tests adding unit"
    unit_graph = UnitGraph("Distance")
    unit_graph.add_unit("m", "meter", "m")
    unit_graph.add_unit("cm", "centimeter", "cm")
    assert len(unit_graph.get_units()) == 2
    assert unit_graph.get_units() == ["m", "cm"]
    assert unit_graph.has_unit("m") is True
    assert unit_graph.has_unit("nm") is False


def test_adding_conversion():
    "Tests adding unit"
    unit_graph = UnitGraph("Distance")
    unit_graph.add_unit("m", "meter", "m")
    unit_graph.add_unit("cm", "centimeter", "cm")
    unit_graph.add_conversion("m", "cm", 100)
    assert unit_graph["m"]["cm"]["weight"] == 100
    assert unit_graph["cm"]["m"]["weight"] == 0.01

    with pytest.raises(UnitNotFound):
        unit_graph.add_conversion("m", "mm", 1000)

    unit_graph.add_conversion("m", "mm", 1000, is_force_add=True)
    assert unit_graph["m"]["mm"]["weight"] == 1000
    assert unit_graph["mm"]["m"]["weight"] == 0.001


def test_constructing_full_graph():
    """Tests constructing full graph"""
    unit_graph = UnitGraph("Distance")
    unit_graph.add_unit("m", "meter", "m")
    unit_graph.add_unit("cm", "centimeter", "cm")
    unit_graph.add_unit("mm", "millimeter", "mm")
    unit_graph.add_conversion("m", "cm", 100)
    unit_graph.add_conversion("m", "mm", 1000)
    assert unit_graph.has_edge("cm", "mm") is False
    unit_graph.construct_full_graph()
    assert unit_graph["cm"]["mm"]["weight"] == 10
