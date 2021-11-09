import ezdxf
from PIL import Image

from Matrix import *


class Generator:
    SECTOR_NAME = "SECTOR"
    SECTOR_WIDTH = 2

    def __init__(self, matrix: Matrix, hatch_angle=0, hatch_density=10):
        self.__matrix = matrix
        self.__hatch_angle = hatch_angle
        self.__hatch_density = hatch_density

        self.__doc = ezdxf.new("R2010")  # creates a new DXF 2010 drawing

        self.__hatch = None

    def generate(self):
        msp = self.__doc.modelspace()  # adds modelspace

        self.__generate_block()  # generate block references

        points = self.__matrix.generate_points()  # generate point coordinates from the matrix

        sw = Generator.SECTOR_WIDTH

        for point in points:
            msp.add_blockref("SECTOR", (point.x * sw, point.y * sw),
                             dxfattribs={
                                 'xscale': 1,
                                 'yscale': 1,
                                 'rotation': 0
                             })

        # generate frame
        msp.add_lwpolyline(
            [
                (-sw/2, -sw/2),
                (self.__matrix.width * sw - sw/2, -sw/2),
                (self.__matrix.width * sw - sw/2, self.__matrix.height * sw - sw/2),
                (-sw/2, self.__matrix.height * sw - sw/2),
                (-sw / 2, -sw / 2)
            ]
        )

        self.__doc.saveas('generated.dxf')

    def __generate_block(self):
        sector = self.__doc.blocks.new(name=Generator.SECTOR_NAME)  # generate block named SECTOR

        hatch = sector.add_hatch()
        hatch.set_pattern_fill('ANSI31', scale=1/self.__hatch_density)
        hatch.set_pattern_angle(self.__hatch_angle)
        dist = Generator.SECTOR_WIDTH / 2
        hatch.paths.add_polyline_path(
            [
                (dist, dist),
                (dist, -dist),
                (-dist, -dist),
                (-dist, dist)
            ],
            is_closed=True
        )
        sector.add_lwpolyline(
            [
                (dist, dist),
                (dist, -dist),
                (-dist, -dist),
                (-dist, dist),
                (dist, dist)
            ]
        )


if __name__ == '__main__':
    DATA = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"
    _encoded_data = pylibdmtx.encode(DATA.encode('utf-8'))
    img = Image.frombytes('RGB', (_encoded_data.width, _encoded_data.height), _encoded_data.pixels)
    img.save("generated.png")
    _matrix = Matrix(width=_encoded_data.width, height=_encoded_data.height)
    m = load_from_encoded_data(_encoded_data)
    m2 = m.conv()

    print(m2)

    g = Generator(matrix=m2, hatch_angle=0, hatch_density=10)
    g.generate()
