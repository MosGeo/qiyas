'''A unit convertor'''

# =================================================================================================
from typing import Dict

from qiyas.construction.graph import UnitGraph


class UnitConvertor():
    '''A unit convertor object'''

    def __init__(self, convertor_dictionary:Dict[str,UnitGraph]):
        '''Initializes teh unit convertor'''
        self.convertor_dictionary = convertor_dictionary
    # ===========================================
    def get_multiplier(self, unit1:str, unit2:str, type_name:str=None):
        '''retrieves the multiplier to convert unit1 to unit2'''

        used_type_name:str
        if type_name is not None:
            used_type_name = type_name

        unit_graph = self.convertor_dictionary[used_type_name]
        return 'hello'
    # ===========================================
    def get_type_names(self):
        '''Returns all the type names'''
        return list(self.convertor_dictionary.keys())

# =================================================================================================
