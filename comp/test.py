from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys

import tensorflow as tf

from comp import model

FLAGS = None

def main(_):
  tf.logging.set_verbosity(tf.logging.INFO)

  sess = tf.InteractiveSession()

  if FLAGS.load_checkpoint:
    model.load_variables_from_checkpoint(sess, FLAGS.load_checkpoint)
  else:
    raise ValueError("checkpoint is not specified")

  # TODO(qijiazhou)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument(
    '--data_dir',
      type=str,
      default='data/test/audio/'
  )
  parser.add_argument(
    '--load_checkpoint',
    type=str,
    default=''
  )
  FLAGS, unparsed = parser.parse_known_args()
  tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)