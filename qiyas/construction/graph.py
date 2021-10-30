'''A Unit graph object'''
import importlib
from pathlib import Path
import pickle
import networkx as nx

# =================================================================================================
class UnitNotFound(Exception):
    '''An exception to raise when the unit is not found'''

    def __init__(self, unit):
        '''Initializes the exception'''
        super().__init__()
        self.message = f"Unit {unit} not found"
# =================================================================================================
class UnitGraph(nx.DiGraph):
    '''A unit graph for holding the unit table information'''

    def __init__(self, type_name:str):
        '''Initializes the unit graph'''
        super().__init__()
        self.type = type_name
    # ===========================================
    def add_unit(self, abbreviation:str, name:str=None, comment:str=None):
        '''Adds a unit to the graph'''
        self.add_node(abbreviation, name=name, comment=comment)
    # ===========================================
    def add_conversion(self, unit1:str, unit2:str, multiplier, is_force_add:bool=False):
        '''Adds a unit conversion'''

        # Check units
        for unit in [unit1, unit2]:
            if not self.is_unit(unit):
                self.add_node(unit)
                if is_force_add:
                    self.add_node(unit)
                else:
                    raise UnitNotFound(unit)

        self.add_weighted_edges_from([(unit1, unit2, multiplier),
                                            (unit2, unit1, 1/multiplier)])
    # ===========================================
    def is_unit(self, unit:str):
        '''Check if the unit is added to the graph'''
        return self.has_node(unit)
    # ===========================================
    def construct_full_graph(self):
        '''Constructs teh full unit graph'''
        print('dlfkjldf')
    # ===========================================
    def visualize(self):
        '''Visualizes the unit graph'''
        matplotlib_specs= importlib.util.find_spec('matplotlib')
        if matplotlib_specs is None:
            print('matplotlib is not installed. Please install this optional ' + \
                  'package to visualize unit graphs')
            return
    # ===========================================
    def save(self, filename:Path)->None:
        '''Saves the unit graph'''
        with open(filename, 'wb') as file_handler:
            pickle.dump(self, file_handler)
# =================================================================================================
def load_unit_graph(filename:Path)->UnitGraph:
    '''Loads teh unit graph'''
    with open(filename, 'rb') as file_handler:
        unit_graph = pickle.load(file_handler)
    return unit_graph
# =================================================================================================
