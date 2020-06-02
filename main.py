import plotter.plotter as pl
from curves.spirograph import Spirograph
import numpy as np


t_space = np.linspace(0, 100 * np.pi, 10000)
pl.plot_parametric(Spirograph(radius=7, domain_len_frac=-1, fraction=1.5), t_space)

## How about a spiro-spirograph?
s = Spirograph(radius=7, domain_len_frac=1, domain_norm_frac=-1.0)
s1 = Spirograph(domain_func=s, radius=3, domain_len_frac=1, fraction=1.7)
pl.plot_parametric(s1, t_space)


