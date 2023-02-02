echo "Passw0rD@#2" | openssl enc -aes-256-cbc -md sha512 -a -pbkdf2 -iter 100000 \ 
-salt -pass pass:Secret@123#
