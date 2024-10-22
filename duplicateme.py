# DUPLICATEME
# (C) Copyright 2024 Gadgeter Software

import sys
import shutil
import os

# sys.argv[0] is script name
ignore_directory_names = [sys.argv[3:]]
copy_directory = sys.argv[2]
copy_file = sys.argv[1]

if copy_directory == None or copy_file == None:
    print("error: missing arguments (copy_file and copy_directory are required)")
    exit(1)

copy_file_size = os.path.getsize(copy_file)
copy_file_total_bytes = 0

written_directories = 0
bad_tracebacks = 0

# get directories functions

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def copy(directory):
    tracebacks = 0

    try:
        shutil.copyfile(copy_file, directory + "/" + copy_file)
    except Exception:
        # nothing lol
        tracebacks += 1
    
    return tracebacks

# do stuff

def copy_loop(directory):
    tracebacks = 0
    wbytes = 0
    dirs = 0

    copy_to_directories = get_immediate_subdirectories(directory)
    shutil.copyfile(copy_file, directory + "/" + copy_file)

    if len(copy_to_directories) > 0:
        for sub_directory in copy_to_directories:
            shutil.copyfile(copy_file, sub_directory + "/" + copy_file)
            wbytes += copy_file_size
            dirs += 1
            tracebacks = 0                   
    
    return tracebacks, dirs, wbytes

bad_tracebacks, written_directories, copy_file_total_bytes = copy_loop(copy_directory)

print("done (duplicated across " + str(written_directories) + " directories, copied " + str(copy_file_total_bytes) + " bytes, with " + str(bad_tracebacks) + " tracebacks)")
exit(0)