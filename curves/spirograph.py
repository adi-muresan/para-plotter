import numpy as np


def ellipse(t):
    return (10 * np.cos(t), 15 * np.sin(t)),


def circle(t):
    nx, ny = np.cos(t), np.sin(t)
    R = 30
    return (nx * R, ny * R), (nx, ny), R * t


class Spirograph:
    def __init__(self, radius=5.0, fraction=1.0, domain_func=circle, domain_len_frac=-1.0, domain_norm_frac=-1.0):
        """

        :param radius: Radius of small circle

        :param fraction: Fraction along the small radius to put the moving dot. Only positive values make sense.
            When 0, the dot will be in the center of the small circle; when 1 it will be on the edge, when > 1 outside.

        :param domain_func: Function that generates the domain we will be moving around

        :param domain_len_frac: Multiplies domain length by this.
            If -1 then rotating against the domain, if 1 then rotating with the domain.

            Ex: when rotating on the inside of a larger circle, the small circle rotates against the larger circle.

        :param domain_norm_frac: Multiply domain normals by this.
            When +1 we rotate on the outside of the domain; when -1 we rotate on the inside of the domain.
        """
        self.domain_func = domain_func
        self.domain_norm_frac = domain_norm_frac
        self.domain_len_frac = domain_len_frac
        self.radius = radius
        self.fraction = fraction

    def __call__(self, t):
        (domain_x, domain_y), (domain_nx, domain_ny), domain_len = self.domain_func(t)
        len = self.domain_len_frac * domain_len / self.radius

        cx = domain_x + self.domain_norm_frac * domain_nx * self.radius
        cy = domain_y + self.domain_norm_frac * domain_ny * self.radius

        nx, ny = np.cos(- len), np.sin(- len)
        x, y = cx + self.fraction * self.radius * nx, cy + self.fraction * self.radius * ny

        return (x, y), (nx, ny), len

