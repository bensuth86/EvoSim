from settings import *

"""Evolution Sim"""

class Cell:

    def __init__(self, area, weight, elasticity, subdiv_rate,):

        self.area = area
        self.weight = weight
        self.elasticity = elasticity  # Force / extension (or compression)
        self.subdiv_rate = subdiv_rate  # e.g. subdiv_rate = 5 => subdivides every 5 turns
        # self.drag # whilst travelling

    def subdivide(self):

        pass


class Organism:

    def __init__(self, *cells):

        self.cells = cells  # list of cell objects

    def reproduce(self):

        for cell in self.cells:

            pass


class PhytoPatch:
    """ Area of plankton for orgsms feeding zones"""

    def __init__(self, radius):

        self.radius = radius


class Simulator:

    def __init__(self, total_patches, total_orgns):

        self.total_patches = total_patches
        self.total_orgns = total_orgns
        self.phyPatches = self.create_patches()

    def create_patches(self):

        return []

    def create_organism(self):

        pass

    def run(self):
        pass
