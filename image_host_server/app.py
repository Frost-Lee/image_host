import flask
import random

import config
import datamanager
import imageprocess

app = flask.Flask(__name__)

@app.route('/bloghost', methods=['GET', 'POST'])
def response_bloghost():
    return _save_image(config.BLOG_CONTAINER_PATH, 'bloghost')

@app.route('/bloghost/<path:filename>', methods=['GET', 'POST'])
def response_bloghost_fetch(filename):
    return flask.send_from_directory(config.BLOG_CONTAINER_PATH, filename)


def _save_image(container_path, path_extension):
    files, args = flask.request.files, flask.request.form
    if 'token' not in args or 'compress_quality' not in args or 'image' not in files:
        return random.choice(config.CURSES)
    if args['token'] not in config.ACCEPTED_TOKENS:
        return random.choice(config.CURSES)
    if len(files['image'].filename.split('.')) != 2 or files['image'].filename.split('.')[1].lower() not in config.ACCEPTED_FORMATS:
        return 'Wrong image format.'
    data_manager = datamanager.DataManager(files['image'], container_path)
    data_manager.save()
    if files['image'].filename.split('.')[1] in config.COMPRESSIBLE_FORMATS:
        imageprocess.compress_image(data_manager.path(), int(args['compress_quality']))
    return 'http://{}:{}/{}/{}'.format(config.EXTERNAL_IP, config.DEPLOY_PORT, path_extension, data_manager.file_name())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=config.DEPLOY_PORT)
