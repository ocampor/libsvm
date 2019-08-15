import os

import pytest

from libsvm.commonutil import svm_read_problem
from libsvm.svmutil import svm_train, svm_predict
from tests.resources import TEST_RESOURCES_PATH


@pytest.fixture
def heart_scale():
    return svm_read_problem(os.path.join(TEST_RESOURCES_PATH, 'heart_scale'))


def test_heart_scale_correctly_loaded(heart_scale):
    y, x = heart_scale
    expected_x: dict = {
        1: 0.708333,
        2: 1,
        3: 1,
        4: -0.320755,
        5: -0.105023,
        6: -1,
        7: 1,
        8: -0.419847,
        9: -1,
        10: -0.225806,
        12: 1,
        13: -1
    }
    assert y[:5] == [+1, -1, +1, -1, -1]
    assert x[0] == expected_x


def test_libsvm_trains_correctly(heart_scale):
    y, x = heart_scale
    m = svm_train(y[:200], x[:200], '-c 4')
    p_label, p_acc, p_val = svm_predict(y[200:], x[200:], m)
    assert p_acc == pytest.approx([84.28571428571429, 0.6285714285714286, 0.463744141163496])
    assert p_label[:6] == [-1.0, 1.0, 1.0, -1.0, 1.0, -1.0]
