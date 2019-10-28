import flask
import random

import config

app = flask.Flask(__name__)

@app.route('/bloghost', methods=['GET', 'POST'])
def response_bloghost():
    files, args = flask.request.files, flask.request.form
    if 'token' not in args or 'compress_quality' not in args or 'image' not in files:
        return random.choice(config.CURSES)
    if args['token'] not in config.ACCEPTED_TOKENS:
        return random.choice(config.CURSES)
    if len(files['image'].filename.split('.')) != 2 or files['image'].filename.split('.')[1] not in config.ACCEPTED_FORMATS:
        return 'Wrong image format.'
    
    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
