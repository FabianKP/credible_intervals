"""
Short demonstration of usage.
"""

from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

from credible_intervals import credible_intervals


n = 1000        # Number of samples.
d = 2          # Dimension.
alpha = 0.05    # Credibility parameter (corresponding to credibility level 1-alpha).
# Create random samples.
samples = np.random.randn(n, d)
# Compute credible intervals.
lb, ub = credible_intervals(samples, alpha)

# VISUALIZE
plt.figure()
ax = plt.axes()
# Plot samples.
ax.scatter(samples[:, 0], samples[:, 1], s=2, label="Samples")
# Plot rectangle [lb, ub].
ci = Rectangle(xy=(lb[0], lb[1]), width=ub[0] - lb[0], height=ub[1] - lb[1], fill=False, color="red",
               label="Simultaneous credible interval")
ax.add_patch(ci)
plt.legend()

plt.show()

