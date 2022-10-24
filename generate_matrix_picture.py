import random
from pathlib import Path
from PIL import Image, ImageDraw


def get_bin(n):
    return str(format(n, 'b').zfill(BITS * BITS))


def generate_fixed_matrix_picture(img_length: int = 100, n_square: int = 3, square_color: str = 'black', background_color = 'white', format: str = 'PNG'):
    img_path = Path.joinpath(Path(__file__).parent, 'Images', 'Fixed', str(n_square))
    Path(img_path).mkdir(parents=True, exist_ok=True)
    length_square = img_length / n_square
    for n in range(1, int(('').join(['1' for i in range(n_square * n_square)]), 2)):
        img = Image.new('RGB', (img_length, img_length), color = background_color)
        draw = ImageDraw.Draw(img)
        n_bin = get_bin(n)
        x_zero, y_zero = 0, 0
        x_one, y_one = length_square, length_square
        x = 0
        for i in n_bin:
            if i == '1':
                draw.rectangle([x_zero, y_zero, x_one, y_one], outline=None, fill=square_color, width=1)
            x_zero += length_square
            x_one += length_square

            x += 1
            if x % n_square == 0:
                x = 0
                x_zero = 0
                y_zero += length_square
                x_one = length_square 
                y_one += length_square
                
            
        img.save(Path.joinpath(img_path, str(n_bin)), format)


def generate_animated_matrix_picture(img_length: int = 100
                                    , n_square: int = 3
                                    , file_name = ''
                                    , rand_order:bool = False
                                    , rand_color_background: bool = False
                                    , rand_color_square: bool = False):
    img_path = Path.joinpath(Path(__file__).parent, 'Images', 'Animated', str(BITS))
    Path(img_path).mkdir(parents=True, exist_ok=True)
    length_square = img_length / n_square
    images = []
    r, g, b = 0, 0, 0
    r_background, g_background, b_background = 255, 255, 255
    for n in range(0, int(('').join(['1' for i in range((n_square * n_square) + 1)]), 2)):
        if rand_color_background:
            r_background, g_background, b_background = random.randint(0,255), random.randint(0,255), random.randint(0,255)
        img = Image.new('RGB', (img_length, img_length), color = (r_background, g_background, b_background))
        draw = ImageDraw.Draw(img)
        n_bin = get_bin(n)
        x_zero, y_zero = 0, 0
        x_one, y_one = length_square, length_square
        x = 0
        for i in n_bin:
            if i == '1':
                if rand_color_square:
                    r, g, b = random.randint(0,255), random.randint(0,255), random.randint(0,255)
                draw.rectangle([x_zero, y_zero, x_one, y_one], outline=None, fill=(r, g, b), width=1)
            x_zero += length_square
            x_one += length_square

            x += 1
            if x % n_square == 0:
                x = 0
                x_zero = 0
                y_zero += length_square
                x_one = length_square 
                y_one += length_square
                
            
        images.append(img)
    if rand_order:
        random.shuffle(images)
    if file_name == '':
        file_name = f'{n_square}'
    images[0].save(Path.joinpath(img_path, f'{file_name}.gif'), save_all = True, append_images = images[1:], optimize = False, duration = 1)


if __name__ == '__main__':
    #generate_animated_matrix_picture()
    #generate_fixed_matrix_picture()
    print('Done')
