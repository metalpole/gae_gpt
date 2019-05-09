import logging
#import subprocess
from flask import Flask
import json
import os
import sample_model

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return "Hello world!"

@app.route('/generate')
def generate():
    return sample_model.sample_model()

# @app.route('/showmethemoney')
# def showmethemoney():
#     """Show me the money"""
#    subfile_output = subprocess.run('python3 src/generate_unconditional_samples.py --nsamples 1 --length 25 --temperature 0.7 --top_k 30', shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
#    return sample_model(nsamples=1, length=25, temperature=0.7, top_k=35)

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500
