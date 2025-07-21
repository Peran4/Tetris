from PIL import Image, ImageEnhance
from paths import *

image_path = root_path / "Graphics" / "exit_button.png"
brighten_path = root_path / "Graphics" / "exit_button_brighten.png"


def BrightenImage(input_path, output_path, factor):
    img = Image.open(input_path).convert("RGBA")
    r, g, b, a = img.split()

    rgb_image = Image.merge("RGB", (r, g, b))
    enhancer = ImageEnhance.Brightness(rgb_image)
    brightened_rgb = enhancer.enhance(factor)

    result = Image.merge("RGBA", (*brightened_rgb.split(), a))
    result.save(output_path)


BrightenImage(image_path, brighten_path, 1.5)
