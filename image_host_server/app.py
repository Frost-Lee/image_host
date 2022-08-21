import flask

import config
import config_secure
import datamanager
import imageprocess


app = flask.Flask(__name__)

# nginx handled path based routing
@app.route('/', methods=['GET', 'POST'])
def post_image():
    try:
        files, args = flask.request.files, flask.request.form
        assert 'token' in args and 'compress_quality' in args and 'image' in files
        assert args['token'] in config_secure.ACCEPTED_TOKENS
        assert files['image'].filename.split('.')[-1].lower() in config.ACCEPTED_FORMATS
        data_manager = datamanager.DataManager(files['image'], config_secure.CONTAINER_PATH)
        data_manager.save()
        if files['image'].filename.split('.')[1] in config.COMPRESSIBLE_FORMATS:
            imageprocess.compress_image(data_manager.path(), int(args['compress_quality']))
        return {'message': 'ok', 'file_key': data_manager.file_name()}, 200
    except Exception as e:
        return {'message': 'Server internal error.', 'file_key': ''}, 500

# nginx handled path based routing
@app.route('/<path:file_key>', methods=['GET', 'POST'])
def get_image(file_key):
    return flask.send_from_directory(config_secure.CONTAINER_PATH, file_key)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        # should stay consistent with Dockerfile
        port=config_secure.DEPLOY_PORT
    )
