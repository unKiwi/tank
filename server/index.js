const Game = require('./src/models/game');

const express = require('express');
const app = express();
const http = require('http');
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);

const game = new Game(io);

io.on('connection', (socket) => {
    console.log('a user connected');
    // create player
    game.addPlayer(socket);

    socket.on('click', () => {
        console.log("click")
    });

    socket.on('disconnect', () => {
        console.log('user disconnected');
        // delete player
        game.deletePlayer(socket);
    });
});

server.listen(80, () => {
    console.log('listening on *:80');
});