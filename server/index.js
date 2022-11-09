const Game = require('./src/models/game');

const express = require('express');
const app = express();
const http = require('http');
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);

const game = new Game(io);

io.on('connection', (socket) => {
    console.log('\x1b[33m%s\x1b[0m','['+ socket.username +'] join server',"\x1b[0m");
    // create player
    game.addPlayer(socket);

    socket.on('click', () => {
        console.log("click")
    });

    socket.on('disconnect', () => {
        console.log('\x1b[33m%s\x1b[0m','['+ socket.username +'] left server',"\x1b[0m");
        // delete player
        game.deletePlayer(socket);
    });
});

server.listen(80, () => {
    console.log('listening on *:80');
});