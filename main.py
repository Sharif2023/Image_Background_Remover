from rembg import remove
from PIL import Image #PIL = Python Imaging Library
input_path = 'F:/Python/BG Remover/me.jpg'
output_path = 'F:/Python/BG Remover/output.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)