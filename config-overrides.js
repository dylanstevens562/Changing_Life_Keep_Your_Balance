const { alias, configPaths } = require('react-app-rewire-alias');
const path = require('path');

const customConfig = alias(configPaths('./tsconfig.paths.json'));

module.exports = function override(config) {
  return customConfig(config);
};
