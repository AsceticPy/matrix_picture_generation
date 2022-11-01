import numpy as np
from pathlib import Path
from PIL import Image, ImageDraw

class Matrix:
    def __init__(self, size: int, n_square: int) -> None:
        self.size: int = size
        self.n_square: int = n_square
        self.size_square: int = size / n_square
        self.matrix: np.zeros = np.zeros((self.size, self.size), dtype=np.uint8)
        self.squares: int = {}
        self.clear_matrix()
        self.calc_coord_squares()

    def calc_coord_squares(self):
        x = 0
        x_zero, y_zero = 0, 0
        x_one, y_one = self.size_square, self.size_square
        for n in range(self.n_square ** 2):
            self.squares[n] = [[y_zero, y_one],[x_zero, x_one]]
            x_zero += self.size_square
            x_one += self.size_square
            x += 1
            if x % self.n_square == 0:
                x_zero, x_one = 0, self.size_square
                y_zero += self.size_square
                y_one += self.size_square
                x = 0
    
    def color_square(self, n):
        self.matrix[int(self.squares[n][0][0]) : int(self.squares[n][0][1]), int(self.squares[n][1][0]) : int(self.squares[n][1][1])] = [0]
    
    def clear_matrix(self):
        self.matrix[0 : self.size, 0 : self.size] = [255]


def get_bin(n, length):
    return str(format(n, 'b').zfill(length * length))


def generate_fixed_matrix_picture(img_length: int = 100, n_square: int = 3, format: str = 'PNG'):
    img_path = Path.joinpath(Path(__file__).parent, 'Images', 'Fixed', str(n_square))
    Path(img_path).mkdir(parents=True, exist_ok=True)
    matrix = Matrix(size=img_length, n_square=n_square)
    for n in range(int(('').join(['1' for i in range(n_square * n_square)]), 2)):
        n_bin = get_bin(n, n_square)
        for count, i in enumerate(n_bin):
            if i == '1':
                matrix.color_square(count)
        img = Image.fromarray(matrix.matrix, mode='L')
        img.save(Path.joinpath(img_path, str(n_bin)), format)
        matrix.clear_matrix()


if __name__ == '__main__':
    generate_fixed_matrix_picture(n_square=3, img_length=100)
    print('Done')
