import os
import tarfile
import datetime
import pysftp

# Define the source directory and its path
source_directory = '/home/backups'

# Create a timestamp for the tar file name
current_datetime = datetime.datetime.now()
timestamp = current_datetime.strftime('%Y%m%d_%H%M%S')

# Define the tar file name with the timestamp
tar_filename = f'backup_{timestamp}.tar'

# Create the tar file
with tarfile.open(tar_filename, 'w') as tar:
    tar.add(source_directory)

# Define SFTP connection parameters
sftp_host = '10.1.1.100'
sftp_username = 'your_sftp_username'
sftp_password = 'your_sftp_password'
sftp_destination = '/backups/server1'

# Upload the tar file to the SFTP server
with pysftp.Connection(sftp_host, username=sftp_username, password=sftp_password) as sftp:
    sftp.put(tar_filename, f'{sftp_destination}/{tar_filename}')

# Remove the local tar file
os.remove(tar_filename)

print("Directory compressed and uploaded successfully.")
