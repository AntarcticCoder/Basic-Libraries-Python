from rembg import remove
from PIL import Image

input_path = 'test2.webp'
output_path = 'omg2.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)