# stdlib
import json
import os
# libs
from flask import (
    Flask,
    render_template,
    request,
    send_file,
    send_from_directory,
)


app = Flask(__name__, static_folder='techtalks')


# Set up routes for the techtalks static stuff
# One for defaulting to index
@app.route('/techtalks/<string:folder>/')
def techtalks(folder):
    return send_from_directory(f'techtalks/{folder}', 'index.html')


# And one for other files in the directory
@app.route('/techtalks/<string:folder>/<string:file>/')
def send_techtalks(folder, file):
    return send_from_directory(f'techtalks/{folder}', file)


# Need routes for sending the demo image and style
@app.route('/demo.png')
def send_demo_image():
    return send_file('static/demo.png')


@app.route('/style.css')
def send_style():
    return send_file('static/style.css')


@app.route('/')
def index():
    # Generate the index page and fill out the index template
    talks = []
    for name in sorted(os.listdir('techtalks')):
        path = f'techtalks/{name}'
        if os.path.isdir(path):
            # Assume that it is a techtalk
            # Open the meta.json
            with open('%s/meta.json' % path) as f:
                meta = json.load(f)
                meta['path'] = path
                for k, v in meta.items():
                    meta[k] = str(v).lower()
                talks.append(meta)
    return render_template(
        'index.html',
        cards=talks,
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0')
