/* global require __dirname module */

const { merge } = require('webpack-merge');
const common = require("./webpack.common.js");
const pp = "http://localhost:8080/static/dist/";

module.exports = merge(common, {
    mode: "development",
    output: {
        publicPath: pp
    },
    module: {
        rules: [{
            test: /\.mjs$/,
            include: /node_modules/,
            type: "javascript/auto",
        }]
    },
    devtool: "inline-source-map",
    devServer: {
        headers: { "Access-Control-Allow-Origin": "*" },
        contentBase: "./assets",
        watchContentBase: true,
        compress: true,
        publicPath: pp,
        port: 8080
    }
});