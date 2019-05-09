import logging
import subprocess
from flask import Flask
import json
import os
import numpy as np
import tensorflow as tf
import model, sample, encoder

def sample_model(
    model_name='117M',
    seed=None,
    nsamples=1,
    batch_size=1,
    length=40,
    temperature=0.9,
    top_k=35,
):
    enc = encoder.get_encoder(model_name)
    hparams = model.default_hparams()
    with open(os.path.join('models', model_name, 'hparams.json')) as f:
        hparams.override_from_dict(json.load(f))

    if length is None:
        length = hparams.n_ctx
    elif length > hparams.n_ctx:
        raise ValueError("Can't get samples longer than window size: %s" % hparams.n_ctx)

    with tf.Session(graph=tf.Graph()) as sess:
        np.random.seed(seed)
        tf.set_random_seed(seed)

        output = sample.sample_sequence(
            hparams=hparams, length=length,
            start_token=enc.encoder['<|endoftext|>'],
            batch_size=batch_size,
            temperature=temperature, top_k=top_k
        )[:, 1:]

        saver = tf.train.Saver()
        ckpt = tf.train.latest_checkpoint(os.path.join('models', model_name))
        saver.restore(sess, ckpt)

        generated = 0
        while nsamples == 0 or generated < nsamples:
            out = sess.run(output)
            for i in range(batch_size):
                generated += batch_size
                text = enc.decode(out[i])
                print("=" * 40 + " SAMPLE " + str(generated) + " " + "=" * 40)
                print(text)

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return sample_model()
#    return 'Hello World!'

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
