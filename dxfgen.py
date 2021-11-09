from pylibdmtx import pylibdmtx


class Matrix:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        self.__matrix = [[1 for w in range(self.__width)] for h in range(self.__height)]

    def __getitem__(self, item):
        return self.__matrix[item]

    def __setitem__(self, key, value):
        self.__matrix[key] = value

    def __str__(self):
        string = ""
        for row in self.__matrix:
            string += str(row) + '\n'

        return string

    def conv(self, kernel_size: int):
        """
        Applies a convolution-like method to the matrix. Each sector is 5x5 pixels. Returns a matrix containing
        only the sectors
        :param kernel_size:
        :return:
        """

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
    print(m)
