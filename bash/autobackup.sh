#!/bin/bash

############################ For scheduled backup keep this file in crontab ###########################

#Compress www directory and move the file to /tmp
input=("/var/www")
output=/tmp/www_$(date +%Y-%m-%d_%H%M%S).tar.gz
tar -czf "$output" "$input"
echo "Backup of $input completed! Detailes are :"
ls -l $output

#Transfer all compressed files in FTP server
HOST='10.19.1.4'
USER='mahdiar'
PASSWD='cat secret.txt | openssl enc -aes-256-cbc -md sha512 -a -d -pbkdf2 \ 
-iter 100000 -salt -pass pass:Secret@123#'
FILE='*.tar.gz'

ftp -ni $HOST <<END_TRANSFER
quote USER $USER
quote PASS $PASSWD
binary \
prompt OFF
lcd /tmp
mput $FILE
quit
END_TRANSFER


#Remove the compressed files from the local storage
rm -rf /tmp/*.tar.gz
