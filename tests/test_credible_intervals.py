
import numpy as np

from credible_intervals import credible_intervals


def test_credible_interval():
    # Runs a hundred tests with pseudo-random input data.
    num_tests = 100
    np.random.seed(98623)
    for i in range(num_tests):
        n = np.random.randint(low=100, high=10000)
        d = np.random.randint(low=1, high=100)
        alpha = np.random.uniform(low=1e-8, high=1 - 1e-8)
        _test_credible_intervals_parametrized(n, d, alpha)


def _test_credible_intervals_parametrized(n, d, alpha):
    k = np.ceil(n * (1 - alpha)).astype(int)
    samples = np.random.uniform(low=-1., high=1, size=(n, d))
    lb, ub = credible_intervals(samples, alpha)
    samples_inside = [x for x in samples if np.all(x >= lb) and np.all(x <= ub)]
    num_inside = len(samples_inside)

    assert num_inside >= k