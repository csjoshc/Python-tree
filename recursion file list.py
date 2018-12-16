# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 19:54:59 2018
Works mostly ok, for folders and directories with full read/write access
can't get the text file to work right at the moment, but the summary confirms 
accuracy
@author: Joshua Chiu
"""
import os

dir_list = [] #keep track of folders already processed; hidden
output_str = '' #running list of all the files
file_count = 0
fold_count = 0
perm_denial_folders = []
perm_denied = 0

def recursive_tree(folder):
    global file_count, fold_count, output_str
    os.chdir(folder)
    #print("cwd is " + os.getcwd())
    cd = os.getcwd()
    #paths = []
    for directory in os.listdir(cd):
        path = os.path.join(cd, directory)
        if os.path.isdir(path) and path not in dir_list:
            if list_fold == 'y':
                fold_count+=1
                output_str += path + '\n'
                if to_print == 'y':
                    print("Folder: "+ path)    
            dir_list.append(path)
            recursive_tree(directory)
        elif not os.path.isdir(path):
            if list_fold == 'y':
                directory = '     ' + directory #add spacing to distinguish files
            if to_print == 'y':
                print(directory)
            output_str += directory + '\n'
            file_count+=1
    os.chdir("..") 

base_directory = input("What directory tree do you want to list? Copy the path"
                      " in C:\Directory format: ")
list_fold = input("Do you want to list folders in addition to files? (y/n), default is No: ")
to_print = input("Do you want to print the list to console as we go? " +
                 "This takes a lot of extra time for large directory trees! (y/n), default is No: ")

def running_function(target):        
    global file_count, fold_count, perm_denied
    try:
        recursive_tree(target)
    except FileNotFoundError:
        print("Sorry, not a valid directory!")
    except PermissionError:
        print("Permission error for: " + str(os.getcwd()))
        perm_denial_folders.append(os.getcwd())
        perm_denied += 1
        print("Files counted: " + str(file_count))
        print("Re-entering recursion, skipping over denied folders")
        running_function(target)

running_function(base_directory)
if to_print != 'y':
    print(output_str)  #run, then print all at once
print("Total file count is: " + str(file_count))
print("Total folder count is: " + str(fold_count))
print("Permissions denied " + str(perm_denied) + " times")



