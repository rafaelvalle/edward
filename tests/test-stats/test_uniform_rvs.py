
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf

from edward.stats import uniform
from scipy import stats

sess = tf.Session()


def _test(loc, scale, size):
  val_est = uniform.rvs(loc, scale, size=size).shape
  val_true = (size, ) + np.asarray(loc).shape
  assert val_est == val_true


def test_0d():
  _test(0.5, 0.5, 1)
  _test(np.array(0.5), np.array(0.5), 1)


def test_1d():
  _test(np.array([0.5]), np.array([0.5]), 1)
  _test(np.array([0.5]), np.array([0.5]), 5)
  _test(np.array([0.2, 0.8]), np.array([0.2, 0.8]), 1)
  _test(np.array([0.2, 0.8]), np.array([0.2, 0.8]), 10)
