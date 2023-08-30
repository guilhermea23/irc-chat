const net = require('net');
const readline = require('readline');

const client = new net.Socket();
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

client.connect(5555, '127.0.0.1', () => {
    rl.on('line', (input) => {
        client.write(input);
    });

    client.on('data', (data) => {
        console.log(data.toString());
    });

    client.on('close', () => {
        console.log('Connection closed');
        process.exit(0);
    });
});
