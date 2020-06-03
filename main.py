import plotter.plotter as pl
from curves.spirograph import Spirograph
from curves.fields import RadialField, DirectionalField, apply_fields
from curves.spiral import spiral

import numpy as np


# t_space = np.linspace(0, 100 * np.pi, 10000)
# pl.plot_parametric(Spirograph(radius=7, domain_len_frac=-1, fraction=1.5), t_space)
#
# ## How about a spiro-spirograph?
# s = Spirograph(radius=7, domain_len_frac=1, domain_norm_frac=-1.0)
# s1 = Spirograph(domain_func=s, radius=3, domain_len_frac=1, fraction=1.7)
# pl.plot_parametric(s1, t_space)


# How about some displacement fields
fields = [
    # RadialField(1.0, [-20.0, -15.0], gaussian(15, 0.0, 30)),
    # RadialField(-1.0, [40.0, 20.0]),
    # RadialField(-1.0, [-20, -15]),

    RadialField(3.0, [20.0, -5], lambda d: np.sin(d / 5)),
    DirectionalField(3.0, [-30.0, 5], [1, 1], lambda d: np.sin(d / 5)),
    DirectionalField(3.0, [0.0, 30], [0, -1], lambda d: np.sin(d / 7)),
]


t_space = np.linspace(0, 100 * np.pi, 10000)
pl.plot_parametric(spiral(3, fields), t_space)
