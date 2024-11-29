
# continuos variable representation code

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Normal distribution parameters
mu, sigma = 170, 10  # mean and standard deviation
x = np.linspace(140, 200, 100)
pdf = norm.pdf(x, mu, sigma)

plt.plot(x, pdf, label='Normal Distribution')
plt.title('Height Distribution')
plt.xlabel('Height (cm)')
plt.ylabel('Probability Density')
plt.legend()
plt.show()
