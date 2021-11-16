import ezdxf
from PIL import Image

from Matrix import *


class Generator:
    HATCH_NAME = "HATCH"
    OUTLINE_NAME = "OUTLINE"
    OUTLINE_LEFT = "LEFT"
    OUTLINE_RIGHT = "RIGHT"
    OUTLINE_TOP = "TOP"
    OUTLINE_BOTTOM = "BOTTOM"
    OUTLINE_FULL = "FULL"
    FINAL_SIZE = 8

    def __init__(self, matrix: Matrix = None, hatch_angle=0, hatch_density=9):
        """
        :param matrix: input matrix containing the data
        :param hatch_angle: angle of the hatches. 0 -> 45°. Positive is CCW
        :param hatch_density: At powers of 3 the lines are continuous
        """
        self.__matrix = matrix
        self.__hatch_angle = hatch_angle
        self.__hatch_density = hatch_density
        self.__final_size = Generator.FINAL_SIZE

        if matrix is not None:
            self.__sector_width = Generator.FINAL_SIZE / self.__matrix.width

        else:
            self.__sector_width = 0

        self.__doc = None

        self.__hatch = None

    def generate(self):
        """Generates the datamatrix and saves it as a dxf file"""

        self.__doc = ezdxf.new("R2010", setup=True)  # creates a new DXF 2010 drawing

        if self.__matrix is None:
            raise Warning("Generator matrix is None")

        msp = self.__doc.modelspace()  # adds modelspace

        # generate layers
        self.__doc.layers.add(name=Generator.HATCH_NAME)
        self.__doc.layers.add(name=Generator.OUTLINE_NAME)

        self.__generate_blocks()  # generate block references

        sectors = self.__matrix.generate_sectors()  # generate point coordinates from the matrix

        sw = self.__sector_width

        for sector in sectors:
            # add the hatch to the hatch layer
            msp.add_blockref(Generator.HATCH_NAME, (sector.x * sw, sector.y * sw),
                             dxfattribs={
                                 'xscale': 1,
                                 'yscale': 1,
                                 'rotation': 0,
                                 'layer': Generator.HATCH_NAME
                             })

            # add the outlines to the outline layer
            if sector.alone:
                msp.add_blockref(
                    Generator.OUTLINE_FULL,
                    (sector.x * sw, sector.y * sw),
                    dxfattribs={
                        'xscale': 1,
                        'yscale': 1,
                        'rotation': 0,
                        'layer': Generator.OUTLINE_NAME
                    }
                )

            else:
                if not sector.above:
                    msp.add_blockref(
                        Generator.OUTLINE_TOP,
                        (sector.x * sw, sector.y * sw),
                        dxfattribs={
                            'xscale': 1,
                            'yscale': 1,
                            'rotation': 0,
                            'layer': Generator.OUTLINE_NAME
                        }
                    )

                if not sector.below:
                    msp.add_blockref(
                        Generator.OUTLINE_BOTTOM,
                        (sector.x * sw, sector.y * sw),
                        dxfattribs={
                            'xscale': 1,
                            'yscale': 1,
                            'rotation': 0,
                            'layer': Generator.OUTLINE_NAME
                        }
                    )

                if not sector.left:
                    msp.add_blockref(
                        Generator.OUTLINE_LEFT,
                        (sector.x * sw, sector.y * sw),
                        dxfattribs={
                            'xscale': 1,
                            'yscale': 1,
                            'rotation': 0,
                            'layer': Generator.OUTLINE_NAME
                        }
                    )

                if not sector.right:
                    msp.add_blockref(
                        Generator.OUTLINE_RIGHT,
                        (sector.x * sw, sector.y * sw),
                        dxfattribs={
                            'xscale': 1,
                            'yscale': 1,
                            'rotation': 0,
                            'layer': Generator.OUTLINE_NAME
                        }
                    )

        # add the frame to the outline layer
        msp.add_lwpolyline(
            [
                (-sw / 2, -sw / 2),
                (self.__matrix.width * sw - sw / 2, -sw / 2),
                (self.__matrix.width * sw - sw / 2, self.__matrix.height * sw - sw / 2),
                (-sw / 2, self.__matrix.height * sw - sw / 2),
                (-sw / 2, -sw / 2)
            ],
            dxfattribs={
                'layer': Generator.OUTLINE_NAME
            }
        )

        self.__doc.saveas('generated.dxf')

    @staticmethod
    def generate_png(data: str) -> str:
        """Generates a datamatrix and saves it as a pdf file"""
        encoded_data = pylibdmtx.encode(data.encode('utf-8'))
        image = Image.frombytes('RGB', (encoded_data.width, encoded_data.height), encoded_data.pixels)
        filename = 'data/preview.png'
        image.save(filename)
        return filename

    def __generate_blocks(self):
        hatch_block = self.__doc.blocks.new(name=Generator.HATCH_NAME)

        outline_top = self.__doc.blocks.new(name=Generator.OUTLINE_TOP)
        outline_bottom = self.__doc.blocks.new(name=Generator.OUTLINE_BOTTOM)
        outline_left = self.__doc.blocks.new(name=Generator.OUTLINE_LEFT)
        outline_right = self.__doc.blocks.new(name=Generator.OUTLINE_RIGHT)
        outline_full = self.__doc.blocks.new(name=Generator.OUTLINE_FULL)

        hatch = hatch_block.add_hatch()
        hatch.set_pattern_fill('ANSI31', scale=float(self.__sector_width / self.__hatch_density))
        hatch.set_pattern_angle(self.__hatch_angle)
        dist = self.__sector_width / 2
        hatch.paths.add_polyline_path(
            [
                (dist, dist),
                (dist, -dist),
                (-dist, -dist),
                (-dist, dist)
            ],
            is_closed=True
        )

        outline_top.add_lwpolyline(
            [
                (-dist, dist),
                (dist, dist)
            ]
        )

        outline_bottom.add_lwpolyline(
            [
                (-dist, -dist),
                (dist, -dist)
            ]
        )

        outline_left.add_lwpolyline(
            [
                (-dist, dist),
                (-dist, -dist)
            ]
        )

        outline_right.add_lwpolyline(
            [
                (dist, dist),
                (dist, -dist)
            ]
        )

        outline_full.add_lwpolyline(
            [
                (dist, dist),
                (dist, -dist),
                (-dist, -dist),
                (-dist, dist),
                (dist, dist)
            ]
        )

    """ PROPERTIES ----------------------------------------------------------------------------------------------"""
    @property
    def matrix(self):
        return self.__matrix

    @matrix.setter
    def matrix(self, value):
        self.__matrix = value
        self.__sector_width = Generator.FINAL_SIZE / self.__matrix.width

    @property
    def size(self):
        return self.__final_size

    @size.setter
    def size(self, value):
        self.__final_size = value


if __name__ == '__main__':
    DATA = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"
    _encoded_data = pylibdmtx.encode(DATA.encode('utf-8'))
    img = Image.frombytes('RGB', (_encoded_data.width, _encoded_data.height), _encoded_data.pixels)
    img.save("generated.png")
    _matrix = Matrix(width=_encoded_data.width, height=_encoded_data.height)
    m = load_from_encoded_data(_encoded_data)
    m2 = m.conv()

    print(m2)

    g = Generator(matrix=m2, hatch_angle=0, hatch_density=20)
    g.generate()
