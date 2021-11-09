import ezdxf

from Matrix import Matrix


class Generator:
    def __init__(self, matrix: Matrix):
        self.__matrix = matrix


    def generate(self):
        doc = ezdxf.new('R2010')  # creates a new DXF 2010 drawing

        msp = doc.modelspace()  # adds modelspace

        
