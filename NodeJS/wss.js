const WebSocket = require("ws").Server;
const HttpsServer = require('https').createServer;
const fs = require("fs");

server = HttpsServer({
    cert: fs.readFileSync("/etc/letsencrypt/live/sports.ir/cert.pem"),
    key: fs.readFileSync("/etc/letsencrypt/live/sports.ir/privkey.pem")
})
socket = new WebSocket({
    server: server
});


socket.on('connection', ws => {
  ws.on('message', message => {
    console.log(`Received message => ${message}`)
  })
  ws.send('Hello! Message From WSS!!')
})
server.listen(5000);
