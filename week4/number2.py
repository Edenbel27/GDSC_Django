import os
import shutil
import time

# Function to determine if file has been created or modified in the last 24 hours
def is_recently_modified(file):
    current_time = time.time()
    file_stats = os.stat(file)
    if (current_time - file_stats.st_mtime) < 86400 or (current_time - file_stats.st_ctime) < 86400:
        return True
    else:
        return False

# Function to update identified files
def update_files(files):
    for file in files:
        with open(file, 'a') as f:
            f.write("updated at: " + time.ctime())

# Check if "last_24hours" folder exists, if not create it
if not os.path.exists("last_24hours"):
    os.makedirs("last_24hours")

# List all files in current directory
current_files = os.listdir()

# Identify and collect files created or modified in the last 24 hours
recently_modified_files = [file for file in current_files if is_recently_modified(file)]

# Update identified files
update_files(recently_modified_files)

# Move identified and updated files to "last_24hours" folder
for file in recently_modified_files:
    shutil.move(file, os.path.join("last_24hours", file))

print("Files created or modified in the last 24 hours have been updated and moved to the 'last_24hours' folder.")