import os
from PIL import Image

def read_image(file_path):
    with open(file_path, 'rb') as f:
        return f.read()

def write_image(file_path, data):
    with open(file_path, 'wb') as f:
        f.write(data)

def create_output_folder(folder_name="output"):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return folder_name

def convert_to_grayscale(image_data, width, height):
    grayscale = []
    index = 0
    for y in range(height):
        for x in range(width):
            r = image_data[index]
            g = image_data[index + 1]
            b = image_data[index + 2]
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            grayscale.extend([gray, gray, gray])
            index += 3
    return bytes(grayscale)

def binarize(grayscale_data, width, height, threshold=128):
    binary = []
    index = 0
    for y in range(height):
        for x in range(width):
            gray = grayscale_data[index]
            value = 255 if gray > threshold else 0
            binary.extend([value, value, value])
            index += 3
    return bytes(binary)

def convert_png_to_bmp(input_path, output_path):
    with Image.open(input_path) as img:
        img.convert("RGB").save(output_path, format="BMP")
        print(f"Imagem convertida para BMP e salva em: {output_path}")

def get_image_dimensions(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
        print(f"Largura: {width} pixels")
        print(f"Altura: {height} pixels")
        return width, height

def main():
    
    # Caminho do arquivo PNG de entrada
    input_png = "imagem.png"

    # Caminho para salvar o arquivo BMP convertido
    output_bmp = "imagem_convertida.bmp"  

    # Realizar a conversão
    convert_png_to_bmp(input_png, output_bmp)

    # Caminho do arquivo BMP
    input_file = "imagem_convertida.bmp"   
    width, height = get_image_dimensions(input_file)

    # Lendo a image
    image_data = read_image(input_file)
    
    # Extraindo o cabeçalho BMP e os pixels
    header = image_data[:54]  
    pixel_data = image_data[54:]
    
    # Convertendo para escala de cinza
    grayscale_data = convert_to_grayscale(pixel_data, width, height)
    grayscale_image = header + grayscale_data
    
    # Convertendo em binario preto e branco
    binary_data = binarize(grayscale_data, width, height)
    binary_image = header + binary_data
    
    # Salvando as saidas
    output_folder = create_output_folder()
    write_image(os.path.join(output_folder, "grayscale.bmp"), grayscale_image)
    write_image(os.path.join(output_folder, "binary.bmp"), binary_image)

if __name__ == "__main__":
    main()
