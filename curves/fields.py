import numpy as np


def softplus(softness=1.0):
    return lambda x: np.log(softness + np.exp(x))


def gaussian(amplitude=1.0, median=0.0, var=1.0):
    return lambda x: amplitude * np.exp(-0.5 * np.square((x - median) / var))


def sigmoid(top=1.0, soft=1.0, yoffset=0.0):
    return lambda x: top / (1.0 + np.exp(-x/soft)) + yoffset


class DirectionalField:
    def __init__(self, strength, center, direction, dist_fn=lambda dist: gaussian(5, 0.0, 30)(dist)): #np.power(softplus(100)(dist), 0.5)):
        self.strength = strength
        self.center = center
        self.direction = direction
        self.dist_fn = dist_fn

    def __call__(self, point):
        normal = point - self.center
        norm = np.linalg.norm(normal)
        direction_norm = np.dot(self.direction, normal)
        normal /= norm
        return self.strength * self.dist_fn(direction_norm), normal


class RadialField:
    def __init__(self, strength, center, dist_fn=lambda dist: gaussian(5, 0.0, 30)(dist)): #np.power(softplus(100)(dist), 0.5)):
        self.strength = strength
        self.center = center
        self.dist_fn = dist_fn

    def __call__(self, point):
        normal = point - self.center
        norm = np.linalg.norm(normal)
        normal /= norm
        return self.strength * self.dist_fn(norm), normal


def apply_fields(pt, fs):
    pts = [p * f for f, p in [f(pt) for f in fs]]
    vf = np.sum(pts, axis=0)
    return vf
