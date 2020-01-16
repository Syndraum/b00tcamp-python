import numpy as np


class NumPyCreator:
    def from_list(self, lst):
        if not isinstance(lst, list):
            return None
        return np.array(lst)

    def from_tuple(self, tpl):
        if not isinstance(tpl, tuple):
            return None
        return np.array(tpl)

    def from_iterable(self, itr):
        a = np.array([])
        for elmt in itr:
            a = np.append(a, elmt)
        return a

    def from_shape(self, shape, value=0):
        return np.full(shape, value)

    def random(self, shape):
        return np.random.rand(shape[0], shape[1])

    def identity(self, n):
        return np.identity(n)
