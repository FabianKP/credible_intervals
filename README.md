SIMULTANEOUS CREDIBLE INTERVALS
===============================

This is a Python program to compute empirical **simultaneous credible intervals** from samples. 
In contrast to marginal credible intervals, a simultaneous credible interval is a box $[l, u] \subset \mathbb{R}^d$
that contains a given percentage of samples *simultaneously*, as points in $\mathbb{R}^d$.

More precisely: Let $x^{(1)}, \ldots, x^{(n)} \in \mathbb{R}^d$ be a sequence of random samples.
Then, given a credibility parameter $\alpha$, this program computes vectors $l, u \in \mathbb{R}^d$
such that

$$ l_i <= x_i^{(k)} <= u_i. $$

for at least $\lceil (1 - \alpha) \cdot n \rceil$ values of $k$.

This program is an implementation of the algorithm described on page 30 of 
"Bayesian Computation and Stochastic Systems" by Besag, Green, Higdon and Mengersen (Statistical Science, 1995).

Disclaimer
----------

The method works well on low-dimensional samples, but breaks down for high-dimensional samples with complicated distribution. Usually you will end up
with simultaneous credible intervals that are too large, sometimes containing *all* of the samples. Use with care.

Installation
------------

You can download the wheel file
[credible_intervals-1.0-py3-none-any.whl](https://github.com/FabianKP/credible_intervals/blob/main/dist/credible_intervals-1.0-py3-none-any.whl)
and then pip-install:

```console
pip install credible_intervals-1.0-py3-none-any.whl
```

Usage
-----

See also the file "demo.py" in the "demo"-folder.
```python

import numpy as np
from credible_intervals import credible_intervals

n = 1000        # Number of samples.
d = 10          # Dimension.
alpha = 0.05    # Credibility parameter corresponding to 95%-credibility.

x = np.random.randn(n, d)   # Array of random samples.

lb, ub = credible_intervals(x, alpha)

# Count how much samples are inside [lb, ub].
num_inside = len([xi for xi in x if np.all(xi >= lb) and np.all(xi <= ub)])
print(f"Samples inside interval: {num_inside}.")

```
