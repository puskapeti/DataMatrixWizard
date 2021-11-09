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



def load_from_encoded_data(encoded_data: pylibdmtx.Encoded, matrix: Matrix):
    height = encoded_data.height
    width = encoded_data.width
    bits_per_pixel = encoded_data.bpp
    raw_bytes = encoded_data.pixels

    if bits_per_pixel % 4 != 0:
        raise TypeError(f"Bits per pixel ratio invalid: {bits_per_pixel} / 8 = {bits_per_pixel/8}")

    bytes_per_pixel = bits_per_pixel / 8
    row = list()

    if len(raw_bytes) != bytes_per_pixel * width * height:
        raise ValueError(f"Pixel size error: total size = {len(raw_bytes)} != bpp*width*height = {bits_per_pixel*width*height}")

    for row in range(height):
        for col in range(width):
            i = row*width + col
            pixel = raw_bytes[i: i+bytes_per_pixel]

            prev_byte = pixel[0]
            for byte in pixel:
                if byte != prev_byte:
                    raise TypeError(f"Multiple values inside pixel {i}")
                prev_byte = byte



if __name__ == '__main__':
    m = Matrix(5, 5)
    print(m)
    print(m[1])
    print(m[1][1])
    m[1][0] = 0
    print(m)
    pass
