const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    entry: './src/index.js', // Entry point of your application
    output: {
        path: path.resolve(__dirname, 'dist'), // Output directory
        filename: 'bundle.js', // Output bundle filename
        publicPath: '/', // Public URL of the output directory
    },
    module: {
        rules: [
            {
                test: /\.js$/, // Apply to JavaScript files
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader', // Transpile ES6+ to ES5
                },
            },
            {
                test: /\.css$/, // Apply to CSS files
                use: [
                    MiniCssExtractPlugin.loader, // Extract CSS into separate files
                    'css-loader', // Resolve @import and url() like import/require() and will resolve them
                ],
            },
            {
                test: /\.(png|svg|jpg|gif)$/, // Apply to image files
                use: ['file-loader'], // Copy images to output directory
            },
        ],
    },
    plugins: [
        new HtmlWebpackPlugin({
            template: './src/index.html', // HTML template file
            filename: 'index.html', // Output HTML filename
        }),
        new MiniCssExtractPlugin({
            filename: 'styles.css', // Output CSS filename
        }),
    ],
    devServer: {
        contentBase: './dist', // Serve content from this directory
        port: 8080, // Dev server port
        historyApiFallback: true, // Enable HTML5 History API routing
    },
};
