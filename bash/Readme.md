## save the encrypted password to a file 

echo "Passw0rD" | openssl enc -aes-256-cbc -md sha512 -a -pbkdf2 -iter 100000 \ 
-salt -pass pass:Secret@123# > secret.txt
