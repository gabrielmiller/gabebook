const path = require('path');

module.exports = {
    entry: './static/ts/main.ts',
    mode: 'development',
    output: {
        filename: path.resolve(__dirname, './static/js'),
    },
}
