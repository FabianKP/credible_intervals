SIMULTANEOUS CREDIBLE INTERVALS
===============================

This is a Python program to compute empirical **simultaneous credible intervals** from samples. 
In contrast to marginal credible intervals, a simultaneous credible interval is a box $[l, u] \subset \mathbb{R}^d$
that contains a given percentage of samples as points in $\mathbb{R}^d$.

Let $x^{(1)}, \ldots, x^{(n)} \in \mathbb{R}^d$ be a sequence of random samples.
Then, given a credibility parameter $\alpha$, this program computes vectors $l, u \in \mathbb{R}^d$
such that

$ l_i <= x_i^{(k)} <= u_i $

for at least $(1 - \alpha) \cdot n$ indices $k$.

This program is an implementation of the algorithm described on page 30 of 
"Bayesian Computation and Stochastic Systems" by Besag, Green, Higdon and Mengersen (Statistical Science, 1995).

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