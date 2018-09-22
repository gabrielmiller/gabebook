const path = require('path');
const copyPlugin = require('copy-webpack-plugin');
const AotPlugin = require('@ngtools/webpack').AoTPlugin;

const prodPlugins = [
    new AotPlugin({
      tsConfigPath: 'tsconfig-prod.json',
      entryModule: path.resolve(__dirname, 'src/app/app.module#AppModule')
    }),
   ];

const IS_DEV = process.env.NODE_ENV !== 'production';

module.exports = {
    entry: './static/ts/' + path.join(root.src, IS_DEV ? 'main.ts' : 'main-prod.ts'),
    mode: 'production',
    module: {
        rules: [
            {
                test: /\.tsx?$/,
                use: IS_DEV ? ['ts-loader', 'angular2-template-loader'] : '@ngtools/webpack',
                exclude: IS_DEV ? [/node_modules/] : []
            /*},
            {
                test: /(?:\.ngfactory\.js|\.ngstyle\.js|\.ts)$/,
                loader: '@ngtools/webpack'*/
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
        ]),
        new AotPlugin({
            tsConfigPath: './tsconfig.json',
            entryModule: path.resolve(__dirname, 'static/ts/app.module#AppModule'),
            sourceMap: true
        })
    ],
    resolve: {
        extensions: ['.ts', '.js'],
    },
    watch: true,
    watchOptions: {
        ignored: ['node_modules'],
    }
}
