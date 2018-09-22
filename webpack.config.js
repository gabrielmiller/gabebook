const path = require('path');
const copyPlugin = require('copy-webpack-plugin');

module.exports = {
    entry: './static/ts/main.ts',
    mode: 'production',
    module: {
        rules: [
            {
                test: /\.ts?$/,
                use: 'ts-loader',
            }
        ]
    },
    output: {
        filename: 'app.js',
        path: path.resolve(__dirname, 'static/js'),
    },
    plugins: [
        new copyPlugin([
            { from: './node_modules/zone.js/dist/zone.min.js', to: 'zone.min.js'}
        ])
    ],
    resolve: {
        extensions: ['.ts', '.js'],
    },
}
