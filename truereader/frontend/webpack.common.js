/* global require __dirname module */

const path = require("path");
const webpack = require("webpack");
const TerserPlugin = require("terser-webpack-plugin");
const { WebpackManifestPlugin } = require("webpack-manifest-plugin");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const OptimizeCSSAssetsPlugin = require("optimize-css-assets-webpack-plugin");
const assetsFolder = "./assets/";
const outputFolder = "../static/dist";

module.exports = {
  entry: {
    sandstone: assetsFolder + "scss/sandstone.scss",
    cerulean: assetsFolder + "scss/cerulean.scss",
    darkly: assetsFolder + "scss/darkly.scss",
    slate: assetsFolder + "scss/slate.scss",
    styles: assetsFolder + "scss/style.scss",

    scripts: assetsFolder + "js/scripts.js",
  },
  output: {
    path: path.resolve(__dirname, outputFolder),
    filename: "[name]-[chunkhash].js",
    chunkFilename: "[name]-[chunkhash].js",
  },
  module: {
    rules: [
      {
        test: /\.(sa|sc|c)ss$/,
        use: [MiniCssExtractPlugin.loader, "css-loader", "sass-loader"],
      },
      {
        test: /\.(jpg|gif|webp|ico|tiff|bmp|png|woff|woff2|eot|ttf|svg)$/,
        loader: "file-loader",
        options: {
          name: "[name]-[chunkhash].[ext]",
        },
      },
    ],
  },
  resolve: {
    modules: ["node_modules", assetsFolder],
  },
  target: "web",
  plugins: [
    new CleanWebpackPlugin(),
    new MiniCssExtractPlugin({
      filename: "[name]-[chunkhash].css",
      chunkFilename: "[name]-[chunkhash].css",
    }),
    new webpack.ProvidePlugin({
      $: "jquery",
      jQuery: "jquery",
      jquery: "jquery",
      "window.jQuery": "jquery",
      Popper: ["popper.js", "default"],
    }),
    new WebpackManifestPlugin({
      fileName: path.resolve(__dirname, "../manifest.json"),
      writeToFileEmit: true,
    }),
  ],
  optimization: {
    minimizer: [
      // CSS optimizer
      new OptimizeCSSAssetsPlugin(),
      // JS optimizer by default
      new TerserPlugin(),
    ],
    runtimeChunk: "single",
    splitChunks: {
      chunks: "all",
      maxInitialRequests: Infinity,
      minSize: 0,
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name(module) {
            // get the name. E.g. node_modules/packageName/not/this/part.js
            // or node_modules/packageName
            const packageName = module.context.match(
              /[\\/]node_modules[\\/](.*?)([\\/]|$)/
            )[1];

            // npm package names are URL-safe, but some servers don't like @ symbols
            return `node-${packageName.replace("@", "")}`;
          },
        },
      },
    },
  },
};
