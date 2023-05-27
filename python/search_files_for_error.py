# The code searches through the files in /home/user/dir1 and if it finds the
# word "error" or "ERROR" in a file, it adds the name of that file to the
# error_log.txt file located in the same directory as the .py file.

import os
import datetime

now = datetime.datetime.now()

def search_files_for_error(directory):
    log_file = 'error_log.txt'
    error_files = []

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                contents = file.read()
                if 'ERROR' in contents or 'error' in contents:
                    error_files.append(filename)
                    with open(log_file, 'a') as log:
                        log.write(f'{now:%d-%m-%Y}---- ERROR found in {filename}\n')

    return error_files

if __name__ == '__main__':
    directory_path = '/home/user/dir1'
    error_files = search_files_for_error(directory_path)
    print(f'Files with errors: {error_files}')
