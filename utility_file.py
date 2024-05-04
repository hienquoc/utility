import datetime
import sys
import os
import pickle
# numpy.set_printoptions(threshold=sys.maxsize) # Uncomment to print full matrix
'''
Example on how to print dictionary to debug.txt file
from utility.utility import Utility
debug = Utility(custom_ident_number=1)
debug_variable_dictionary = {'loop_number: loop_number,     # Print the loop number in while loops
                             'cap': cap,
                             'ret': ret,
                             'frame': frame}
debug.print_value_dictionary(debug_variable_dictionary)
'''
class utility_class:
    def __init__(self):
        pass
    #   Set option to print full numpy matrix
    @classmethod
    def utility_save_list_of_objects_to_file(cls, inputs):
        ri = {
            "full_path_file_name": None,
            "object_list": [],
        }
        ri.update(inputs)
        # Let's assume you have a list of objects you want to save
        my_objects = ri['object_list']  # Replace these with your actual objects

        # Specify your filename
        filename = ri['full_path_file_name']

        # Open a file in binary write mode and use pickle to dump the list of objects
        try:
            if filename is None:
                raise ValueError("Filename cannot be None.")
            with open(filename, 'wb') as file:
                pickle.dump(my_objects, file)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    @classmethod
    def utility_load_list_of_objects_from_file(cls, inputs):
        ri = {
            "full_path_file_name": None,
        }
        ri.update(inputs)

        # Specify your filename (must be the same as the one used for saving)
        filename = ri['full_path_file_name']

        try:
            with open(filename, 'rb') as file:
                loaded_objects = pickle.load(file)
                print('Successfully loaded objects:')
                print(loaded_objects)
        except EOFError:
            # File exists but is empty
            print('File is empty, returning an empty list.')
            loaded_objects = []  # Return an empty list if the file is empty
        except FileNotFoundError:
            # Handle case where file does not exist
            print('File not found, returning an empty list.')
            loaded_objects = []
        except Exception as e:
            # Handle other potential exceptions
            print(f'An error occurred: {e}')
            loaded_objects = []

        return loaded_objects