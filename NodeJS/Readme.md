### Install prerequisites

npm install express --save

npm install ws
sudo npm i -g pm2 

### Use pm2 to autostart nodejs app after reboot
pm2 start /directory/server.js
pm2 startup
pm2 save
