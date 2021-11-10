from pylibdmtx import pylibdmtx

from Sector import Sector

WHITE_VALUE = 255
BLACK_VALUE = 0


class Matrix:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        self.__matrix = [[1 for _ in range(self.__width)] for _ in range(self.__height)]

    """ OVERRIDES ---------------------------------------------------------------------------------------------------"""

    def __getitem__(self, item):
        return self.__matrix[item]

    def __setitem__(self, key, value):
        self.__matrix[key] = value

    def __str__(self):
        string = ""
        for row in self.__matrix:
            string += str(row) + '\n'

        return string

    """ METHODS -----------------------------------------------------------------------------------------------------"""

    def conv(self):
        """
        Applies a convolution-like method to the matrix. Each sector is 5x5 pixels. Returns a matrix containing
        only the sectors
        :return:
        """
        kernel_size = self.get_sector_size()

        if kernel_size == 0:
            return ValueError("Kernel size cannot be zero")

        if self.height % kernel_size != 0 or self.width % kernel_size != 0:
            return ValueError("Size or width not multiple of kernel size")

        res = Matrix(width=self.width // kernel_size, height=self.height // kernel_size)
        for row in range(res.height):
            for col in range(res.width):
                res.__matrix[row][col] = self.__matrix[5 * row][5 * col]

        return res

    def get_sector_size(self):
        min_white_size = self.__width
        min_black_size = self.__width

        for i, row in enumerate(self.__matrix):
            whites = 0
            blacks = 0
            prev_pixel = row[0]  # start pixel in the row
            for pixel in row:
                # increment the color values accordingly
                if pixel == WHITE_VALUE:
                    whites += 1
                if pixel == BLACK_VALUE:
                    blacks += 1

                if pixel != prev_pixel:  # color change
                    if pixel == BLACK_VALUE:  # white -> black
                        if whites < min_white_size:
                            min_white_size = whites

                        whites = 0

                    if pixel == WHITE_VALUE:  # black -> white
                        if blacks < min_black_size:
                            min_black_size = blacks

                        blacks = 0

                prev_pixel = pixel

        if min_white_size == 0:
            return min_black_size

        if min_black_size == 0:
            return min_white_size

        return min(min_white_size, min_black_size)

    def generate_sectors(self):
        """
        Generates a sector for each black value
        :return:
        """
        sectors = list()  # type: list[Sector]

        for row in range(self.__height):
            for col in range(self.__width):

                if self.__matrix[row][col] == BLACK_VALUE:
                    sector = Sector(col, self.__height - row - 1)  # generate sector

                    """ check if surrounding sectors are black"""
                    if col > 0 and self.__matrix[row][col - 1] == BLACK_VALUE:
                        sector.left = True

                    if col < self.__width - 1 and self.__matrix[row][col + 1] == BLACK_VALUE:
                        sector.right = True

                    if row > 0 and self.__matrix[row - 1][col] == BLACK_VALUE:
                        sector.above = True

                    if row < self.__height - 1 and self.__matrix[row + 1][col] == BLACK_VALUE:
                        sector.below = True

                    # append the sector to the list
                    sectors.append(sector)

        return sectors

    """ PROPERTIES --------------------------------------------------------------------------------------------------"""

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height


def load_from_encoded_data(encoded_data: pylibdmtx.Encoded) -> Matrix:
    """
    Loads the data matrix from the raw bytes
    :param encoded_data: pixel data
    """
    height = encoded_data.height
    width = encoded_data.width
    bits_per_pixel = encoded_data.bpp
    raw_bytes = encoded_data.pixels

    if bits_per_pixel % 8 != 0:
        raise TypeError(f"Bits per pixel ratio invalid: {bits_per_pixel} / 8 = {bits_per_pixel / 8}")

    bytes_per_pixel = int(bits_per_pixel / 8)

    matrix = Matrix(width=width, height=height)

    if len(raw_bytes) != bytes_per_pixel * width * height:
        raise ValueError(
            f"Pixel size error: total size = {len(raw_bytes)} != bpp*width*height = {bits_per_pixel * width * height}")

    # read the raw bytes
    raw_pixels = list()

    for i in range(0, len(raw_bytes), bytes_per_pixel):
        pixel = raw_bytes[i: i + bytes_per_pixel]

        # check if all elements in the pixel are the same
        first = pixel[0]
        for byte in pixel:
            if byte != first:
                raise TypeError(f"Multiple values inside pixel {i}")

        raw_pixels.append(first)

    # convert the raw bytes into a matrix
    for row in range(matrix.height):
        for col in range(matrix.width):
            i = row * matrix.width + col
            matrix[row][col] = raw_pixels[i]

    return matrix


if __name__ == '__main__':
    DATA = "H-1234-5678"
    _encoded_data = pylibdmtx.encode(DATA.encode('utf-8'))
    _matrix = Matrix(width=_encoded_data.width, height=_encoded_data.height)
    m = load_from_encoded_data(_encoded_data)
    print(m.get_sector_size())
    print(m)
    m2 = m.conv()
    print(m2)
    pass