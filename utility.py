import datetime
import numpy
import sys
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
global utility_debug_status


class Utility:
    def __init__(self,
                 custom_file_name='debug.txt',
                 custom_ident_number=0,
                 custom_title='No Title Set',
                 custom_turn_on_debug=True,
                 custom_debug_variable_dictionary={}):

        self.file_name = custom_file_name       # Get the file name
        self.indent_number = custom_ident_number        # Get the indentation number
        self.tab = self.get_number_of_tabs_as_string()      # Initialize and get the number of tabs
        self.title = custom_title       # Format the title in get_title() method
        self.turn_on_debug = custom_turn_on_debug
        self.debug_variable_dictionary = custom_debug_variable_dictionary

    #   Set option to print full numpy matrix
    def set_option_print_all_matrix(self):
        numpy.set_printoptions(threshold=sys.maxsize)

    #   Set option to print summarized matrix option
    def set_option_print_summarized_matrix(self):
        numpy.set_printoptions(threshold=1000)

    #   Gets the number of tabs as a string to print in debug. Set new tab attribute and run this to print
    #   nested loops with
    def get_number_of_tabs_as_string(self):
        tab = ""    # Initialize tab variable as empy string
        for index in range(self.indent_number):     # Loop the number of indents and create tab string
            tab += str('\t')        # Add the number of tabs base on the indent
        return tab  # Return the tab string to print

    def print_value_dictionary(self, debug_dictionary):
        new_line = '\n'     # Start a new line to separate each function
        with open(self.file_name, 'a') as text_file:  # 'a' to append to end of file with text_file object
            text_file.write(f"{new_line}{self.tab}{datetime.datetime.now()} {self.title}{new_line}")    # Print Title
            for key in self.debug_variable_dictionary:        # Loop through each key iin debug_dictionary
                # print(datetime.datetime.now(), key, +' = ', debug_dictionary[key])
                text_file.write(f"{self.tab}{datetime.datetime.now()} {key} = {self.debug_variable_dictionary[key]}{new_line}")       # Print key name and value

    def check_global_utility_debug_status_before_printing_value_dictionary(selfs, debug_dictionary):
        if utility_debug_status == True:
            return True
