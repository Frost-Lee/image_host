import flask
import os

import config
import datamanager
import imageprocess


app = flask.Flask(__name__)

# nginx handled path based routing
@app.route('/upload', methods=['GET', 'POST'])
def post_image():
    try:
        files, args = flask.request.files, flask.request.form
        assert 'token' in args and 'compress_quality' in args and 'image' in files
        assert args['token'] in config.ACCEPTED_TOKENS
        assert files['image'].filename.split('.')[-1].lower() in config.ACCEPTED_FORMATS
        data_manager = datamanager.DataManager(files['image'], config.CONTAINER_PATH)
        data_manager.save()
        if files['image'].filename.split('.')[1] in config.COMPRESSIBLE_FORMATS:
            imageprocess.compress_image(data_manager.path(), int(args['compress_quality']))
        return {'message': 'ok', 'file_key': data_manager.file_name()}, 200
    except AssertionError:
        return {'message': 'Invalid request parameters'}, 400
    except Exception as e:
        return {'message': 'Server internal error.', 'file_key': ''}, 500

# nginx handled path based routing
@app.route('/<path:file_key>', methods=['GET', 'POST'])
def get_image(file_key):
    try:
        file_ext = file_key.split('.')[-1].lower()
        if file_ext not in config.ACCEPTED_FORMATS:
            return {'message': 'Invalid file format'}, 400

        file_path = os.path.join(config.CONTAINER_PATH, file_key)
        if not os.path.exists(file_path):
            return {'message': 'File not found'}, 404

        return flask.send_from_directory(config.CONTAINER_PATH, file_key)
    except Exception as e:
        app.logger.error(f"Error serving file: {str(e)}")
        return {'message': 'Server internal error'}, 500

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=config.DEPLOY_PORT
    )
