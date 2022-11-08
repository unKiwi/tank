const Map = require('./map');
const Player = require('./player');

module.exports = class Game {
    tps = 20;
    map = new Map();
    players = {};

    constructor(io) {
        this.io = io;
        setInterval(() => {
            io.emit("state", {
                map: this.map,
                tanks: this.players,
            });
        }, 1000 / this.tps);
    }

    addPlayer(socket) {
        socket.emit("id", socket.id)
        this.players[socket.id] = new Player();
    }

    deletePlayer(socket) {
        delete this.players[socket.id];
    }
}