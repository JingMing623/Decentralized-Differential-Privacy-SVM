'use strict';

module.exports = {
  name: 'dpSVM',
  version: '0.0.1',
  cwd: __dirname,
  local: {
    type: 'cmd',
    cmd: 'python',
    args: ['./dpSVM_local.py'],
    verbose: true,
  },
  remote: {
    type: 'cmd',
    cmd: 'python',
    args: ['./dpSVM_remote.py'],
    verbose: true,
  },
  plugins:['group-step'],
};
