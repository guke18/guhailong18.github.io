var fs = require('fs');
var version = 'latest'
fs.readFile('./BUILD_NUMBER.txt', function (error, data) {
    if (error) {
      console.log('load BUILD_NUMBER.txt fails, ' + error)
    } else {
        version = data.toString().trim();
    }
});

const source = (path, cache, ext) => {
    if (cache) {
        const minFile = `${path}${ext === '.js' ? '.min' : ''}${ext}`;
        const jsdelivrCDN = hexo.config.jsdelivr;
        return jsdelivrCDN.enable ? `//${jsdelivrCDN.baseUrl}/gh/${jsdelivrCDN.gh_user}/${jsdelivrCDN.gh_repo}@${version}/${minFile}` : `${minFile}?v=${version}`
    } else {
        return path + ext
    }
}
hexo.extend.helper.register('theme_js', (path, cache) => source(path, cache, '.js'))
hexo.extend.helper.register('theme_css', (path, cache) => source(path, cache, '.css'))
