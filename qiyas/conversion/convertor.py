'''A unit convertor'''
from typing import Dict, List
from qiyas.construction.graph import UnitGraph


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
    def get_possible_types(self, type_names:List[str])->List[str]:
        '''Returns the possible types'''
        possible_types:List[str] = []
        for type_name in self.convertor_dictionary:
            current_unit_graph = self.convertor_dictionary[type_name]
            is_node = [x in current_unit_graph for x in type_names]
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
    def get_multiplier(self, unit1:str, unit2:str, type_name:str=None):
        '''retrieves the multiplier to convert unit1 to unit2'''

        used_type_name:str
        if type_name is not None:
            if type_name in self.convertor_dictionary:
                used_type_name = type_name
            else:
                raise TypeNotFound(type_name)
        else:
            units = [unit1, unit2]
            possible_types = self.get_possible_types(units)
            used_type_name = self.validate_possible_type(units, possible_types)

        unit_graph = self.convertor_dictionary[used_type_name]
        weight = unit_graph.get_edge_data(unit1, unit2)['weight']
        return weight
    # ===========================================

# =================================================================================================
