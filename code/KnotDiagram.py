import numpy as np
import random


class KnotDiagram:

    def __init__(self, n_dim):
        self.n_dim = n_dim
        self.o_permutation_rep = []
        self.x_permutation_rep = []

    def __gen_diagram(self):
        diag = np.array(['*' for _ in range(self.n_dim ** 2)]).reshape((self.n_dim, self.n_dim))
        diag[:] = "*"
        labels = [('x', 'o')] * self.n_dim
        for l, row in zip(labels, diag):
            x_idx, o_idx = sorted(random.sample(range(0, self.n_dim), 2))
            row[x_idx], row[o_idx] = l
            #self.x_permutation_rep.append(x_idx)
            #self.o_permutation_rep.append(o_idx)

        return diag

    def generate_sample_knot(self, number):

        for i in range(number):
            yield self.__gen_diagram()




    def permutation_rep(self):
        return np.array([self.x_permutation_rep, self.o_permutation_rep])
