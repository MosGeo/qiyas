'''A unit convertor'''
from typing import Dict, List
from networkx.algorithms.shortest_paths.generic import shortest_path
from qiyas.construction.graph import UnitGraph
# =================================================================================================
class UnitsTypeMismatch(Exception):
    '''Exception for when units are not found in the type defined'''

    def __init__(self, units:List[str], type_name:str):
        '''Initializes the exception'''
        super().__init__()
        self.message = f"Some or all of units {units} not found in type {type_name}"
# =================================================================================================
class TypeNotFound(Exception):
    '''Exception for when type is not found'''

    def __init__(self, type_name:str):
        '''Initializes the exception'''
        super().__init__()
        self.message = f"Type {type_name} is not defined."

# =================================================================================================
class TypeDetectionNotPossible(Exception):
    '''An exception to raise when multiple possible types are found'''

    def __init__(self, units:List[str], possible_types:List[str]=None):
        '''Initializes the exception'''
        super().__init__()
        if possible_types is not None:
            self.message = f"Multiple types {possible_types} for input units {units}. " + \
                            "Please define the type_name explictly."
        else:
            self.message = f"No type detected for input for input units {units}."
# =================================================================================================
class UnitConvertor():
    '''A unit convertor object'''

    def __init__(self, convertor_dictionary:Dict[str,UnitGraph]):
        '''Initializes teh unit convertor'''
        self.convertor_dictionary = convertor_dictionary
    # ===========================================
    def get_type_names(self):
        '''Returns all the type names'''
        return list(self.convertor_dictionary.keys())
    # ===========================================
    def get_possible_types(self, units:List[str])->List[str]:
        '''Returns the possible types'''
        possible_types:List[str] = []
        for type_name in self.convertor_dictionary:
            current_unit_graph = self.convertor_dictionary[type_name]
            is_node = [x in current_unit_graph for x in units]
            if all(is_node):
                possible_types.append(type_name)

        return possible_types
    # ===========================================
    def validate_possible_type(self, units:List[str], possible_types:List[str])->str:
        '''Validates the possible type and returns the one type if available'''
        if len(possible_types)==0:
            raise TypeDetectionNotPossible(units, None)
        elif len(possible_types)==1:
            used_type_name = possible_types[0]
        else:
            raise TypeDetectionNotPossible(units, possible_types)
        return used_type_name
    # ===========================================
    def validate_units(self, units:List[str], type_name:str)->None:
        unit_graph = self.convertor_dictionary[type_name]
        is_valid_unit_type = all([x in unit_graph for x in units])
        if not is_valid_unit_type:
            raise UnitsTypeMismatch(units, type_name)
    # ===========================================
    def get_multiplier(self, unit1:str, unit2:str, type_name:str=None):
        '''retrieves the multiplier to convert unit1 to unit2'''

        # Get used type name
        used_type_name:str
        if type_name is not None:
            if type_name in self.convertor_dictionary:
                used_type_name = type_name
                self.validate_units([unit1, unit2], type_name)
            else:
                raise TypeNotFound(type_name)
        else:
            units = [unit1, unit2]
            possible_types = self.get_possible_types(units)
            used_type_name = self.validate_possible_type(units, possible_types)

        # Get the unit graph
        unit_graph = self.convertor_dictionary[used_type_name]

        # If it is fully constructed, it is a simple lookup
        if unit_graph.is_constructed:
            weight = unit_graph.get_edge_data(unit1, unit2)['weight']
            return weight

        # If it is not fully constructed, we calculate it manually
        weight = 10
        path:List[str] = shortest_path(unit_graph, unit1, unit2, weight='weight')

        print(path)

        return weight

# =================================================================================================
