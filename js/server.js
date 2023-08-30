const { log } = require('console');
const net = require('net');

const server = net.createServer();

const clients = [];

server.on('connection', (client) => {
    clients.push(client);

    client.on('data', (data) => {
        console.log(data.toString());
        for (const c of clients) {
            if (c !== client) {
                c.write(data);
            }
        }
    });

    client.on('end', () => {
        const index = clients.indexOf(client);
        if (index !== -1) {
            clients.splice(index, 1);
        }
    });
});

server.listen(5555, '127.0.0.1');
