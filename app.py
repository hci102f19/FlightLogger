from flask import Flask, url_for, redirect

from logger import Logger

app = Flask(__name__)

logger = None


@app.route('/')
def home():
    status = 'Running' if logger is not None else 'Stopped'

    html = "<span>Status: {}</span><br/>".format(status)
    html += "<a href=\"{}\">Start</a> | ".format(url_for('start'))
    html += "<a href=\"{}\">Stop</a>".format(url_for('stop'))

    return html


@app.route('/start')
def start():
    if logger is None:
        global logger
        logger = Logger()
        logger.start()

    return redirect(url_for('home'))


@app.route('/stop')
def stop():
    global logger
    if logger is not None:
        logger.stop()
        logger = None

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000
    )
