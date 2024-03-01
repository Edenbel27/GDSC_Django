import os
import shutil
import time

#This function checks whether file has been created or modified in the last 24 hours
def is_recently_modified(file_path):
    current_time = time.time()
    file_stats = os.stat(file_path)
    if (current_time - file_stats.st_mtime) < 86400 or (current_time - file_stats.st_ctime) < 86400:
        return True
    else:
        return False

#This function is update identified files
def update_files(files):
    for file in files:
        with open(file, 'a') as f:
            f.write("updated at: " + time.ctime())

# It is the directory where the script is executed
current_directory = os.getcwd()

# This Checks if "last_24hours" folder exists. If it does not exist, create it.
destination_folder = os.path.join(current_directory, "last_24hours")

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# List all files in current directory-->line 21
current_files = os.listdir(current_directory)

# This identify and collect files created or modified in the last 24 hours.
recently_modified_files = [file for file in current_files if is_recently_modified(file) and os.path.isfile(file)]

# For Updating identified files
update_files(recently_modified_files)

# Move identified and updated files to "last_24hours" folder.
for file in recently_modified_files:
    shutil.move(file, os.path.join(destination_folder, file))

print("Files created or modified in the last 24 hours have been updated and moved to the last_24hours folder")