#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Katherinne Lucia Paguatian Morena
# DATE CREATED: 11/07/2024                                  
# REVISED DATE: 
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse

# TODO 1: Define get_input_args function below please be certain to replace None
#       in the return statement with parser.parse_args() parsed argument 
#       collection that you created with this function
# 
def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to created and defined these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object  
    """
    # Create Parse using ArgumentParser
    parser = argparse.ArgumentParser(description = 'Arguments for pet image classifier')
    # Create 3 command line arguments as mentioned above using add_argument() from ArguementParser method
    parser.add_argument('--dir', type=str, default='pet_images/', help ='path to folder')
    parser.add_argument('--arch', type=str, default='vgg', help = 'CNN model Architecture')
    parser.add_argument('--dogfile', type=str, default='dognames.txt', help = 'Text file of dog names')
    # Replace None with parser.parse_args() parsed argument collection that 
    # you created with this function 

    arge = parser.parse_args()
    return arge
'''
argumento = get_input_args()
print("Argument 1:", argumento.dir)
if __name__ == "__main__":
  argument = get_input_args()
  print("Path to folder {}".format(argument.dir))
  print("CNN model architecture {}".format(argument.arch))
  print("File of dog's name {}".format(argument.dogfile))'''