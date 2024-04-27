const path = require('path');

module.exports = {
  mode: 'development',
  entry: './ts/joystick.ts',
  output: {
    filename: 'bokeh_joystick_widget.js',
    path: path.resolve(__dirname, '../../dist'),
  },
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/,
      },
      {
        test: /\.js$/,
        use: ['raw-loader'],
      }
    ],
  },
  resolve: {
    extensions: ['.tsx', '.ts', '.js'],
  },
};
