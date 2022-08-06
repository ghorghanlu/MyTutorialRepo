from collections import OrderedDict
from collections import namedtuple
from itertools import product


class RunBuilder():
    @staticmethod
    def get_runs(params):
        Run = namedtuple("Run", params.keys())
        runs = []
        for v in product(*params.values()):
            runs.append(Run(*v))
        return runs

params = OrderedDict(
    lr = [0.01, 0.001],
    batch_size = [1000, 10000],
    device = ["cpu", "gpu"]
)


print(RunBuilder.get_runs(params))


"""
X = [4, 7, 8]
Y = [0, 1, 2]

c = [(x, y) for x in X for y in Y]
print(c)
"""