const path = require('path');

module.exports = {
  computationPath: path.resolve(
    __dirname,
    'index.js'
  ),
  local: [{
    dirs: ['site1'],
  }, {
    dirs: ['site2'],
  },{
    dirs: ['site3'],
  },{
    dirs: ['site4'],
//  },{
//    dirs: ['site5'],
//  },{
//    dirs: ['site6'],
//  },{
//    dirs: ['site7'],
  },{
    dirs: ['site11'],
  },{
    dirs: ['site_test'],
  }],
  verbose: true,
};

