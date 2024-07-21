#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER:  Katherinne Lucia Paguatian Moreno
# DATE CREATED:   12/07/2024                               
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
# listdir method retrieves all file names in a folder
# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """

    # Create a pet labels dictionary based on image file names from the 
    # directory
    filename_list = listdir(image_dir)
    dict_pet = dict()
    # This returns a list of file names in the given directory
    # This is to check if the retrieved file list is correct
    # Here we are going to make a dictionary, where the key is the image name and the value is the pet name
    # With parameters that the value of the key is in lowercase, and without underscores, and without numbers
    for index in range (0, len(filename_list), 1):
        if filename_list[index][0] != ".": # Checks that the first character of the file it iterates over is not a dot, because it means it is not an image
            low_pet = filename_list[index].lower() 
            pet_slip = low_pet.split("_")
            pet_name = ""
            for x in pet_slip:
                if x.isalpha(): # Checks that they are only alphabetical
                    pet_name += x + ""
            pet_name = pet_name.strip()
            
            if filename_list[index] not in dict_pet:
                dict_pet[filename_list[index]] = [pet_name]
            else:
                print("**Warning: Key=", filename_list[index], "already exists in dict with value=", dict_pet[filename_list[index]])
            
    return dict_pet        
        
        
