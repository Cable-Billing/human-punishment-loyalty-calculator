const fs = require('fs');
const readline = require('readline');
const http = require('http');

let r = readline.createInterface({ input: fs.createReadStream('./urls.txt') });
let i = '1';

r.on('line', function(text) {
    const file = fs.createWriteStream('./downloaded/' + i + '.png');
    i++;

    const request = http.get(text, function(response) {
        response.pipe(file);
        file.on("finish", () => {
            file.close();
            console.log("Download Completed");
        });
    });
});