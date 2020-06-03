import numpy as np
from curves.fields import apply_fields


def spiral(spacing=3, fields=[]):
    def inner(t):
        phase, dist = np.modf(t / (2.0 * np.pi))
        phase *= 2.0 * np.pi
        normal = np.array([np.cos(t), np.sin(t)])
        R = spacing
        depth = R + t/(2.0 * np.pi) * spacing
        pt = normal * depth

        vf = apply_fields(pt, fields)
        R = depth

        return normal * R + vf, R * t

    return inner

