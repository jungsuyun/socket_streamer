import os, glob
import os.path
from flask import Flask, Response

app = Flask(__name__)
app.config.from_object(__name__)
jpserver_path = '/home/jungsu/.local/share/jupyter/runtime/*.html'

def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))

def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        # Figure out how flask returns static files
        # Tried:
        # - render_template
        # - send_file
        # This should not be so non-obvious
        return open(src).read()
    except IOError as exc:
        return str(exc)

def html_file():
    files = glob.glob(jpserver_path)
    files.sort(key=os.path.getmtime, reverse=True)
    return files[0]

@app.route('/')
def index():
    print(html_file())
    content = get_file(html_file())
    return Response(content)

if __name__ == '__main__':  # pragma: no cover
    app.run(host='192.168.0.107', port=5000)