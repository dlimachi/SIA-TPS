import numpy as np
from Autoencoder import Autoencoder
import matplotlib.pyplot as plt

def convert_font_to_binary(font_data):
    binary_data = []
    for char in font_data:
        binary_char = []
        for row in char:
            binary_row = [int(bit) for bit in format(row, '05b')]
            binary_char.extend(binary_row)
        binary_data.append(binary_char)
    binary_data = np.array(binary_data)
    return binary_data

def normalize_data(data):
    return data / 1.0  # Assure que les valeurs sont déjà 0 ou 1

def visualize_latent_space(encoded_data, labels):
    plt.scatter(encoded_data[:, 0], encoded_data[:, 1], c=labels)
    plt.xlabel('Latent Dimension 1')
    plt.ylabel('Latent Dimension 2')
    plt.title('2D Latent Space Visualization')
    plt.colorbar()
    plt.show()

if __name__ == "__main__":
    # Données extraites de font.h
    font_data = [
       [0x04, 0x04, 0x02, 0x00, 0x00, 0x00, 0x00],   # 0x60, `
       [0x00, 0x0e, 0x01, 0x0d, 0x13, 0x13, 0x0d],   # 0x61, a
       [0x10, 0x10, 0x10, 0x1c, 0x12, 0x12, 0x1c],   # 0x62, b
       [0x00, 0x00, 0x00, 0x0e, 0x10, 0x10, 0x0e],   # 0x63, c
       [0x01, 0x01, 0x01, 0x07, 0x09, 0x09, 0x07],   # 0x64, d
       [0x00, 0x00, 0x0e, 0x11, 0x1f, 0x10, 0x0f],   # 0x65, e
       [0x06, 0x09, 0x08, 0x1c, 0x08, 0x08, 0x08],   # 0x66, f
       [0x0e, 0x11, 0x13, 0x0d, 0x01, 0x01, 0x0e],   # 0x67, g
       [0x10, 0x10, 0x10, 0x16, 0x19, 0x11, 0x11],   # 0x68, h
       [0x00, 0x04, 0x00, 0x0c, 0x04, 0x04, 0x0e],   # 0x69, i
       [0x02, 0x00, 0x06, 0x02, 0x02, 0x12, 0x0c],   # 0x6a, j
       [0x10, 0x10, 0x12, 0x14, 0x18, 0x14, 0x12],   # 0x6b, k
       [0x0c, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04],   # 0x6c, l
       [0x00, 0x00, 0x0a, 0x15, 0x15, 0x11, 0x11],   # 0x6d, m
       [0x00, 0x00, 0x16, 0x19, 0x11, 0x11, 0x11],   # 0x6e, n
       [0x00, 0x00, 0x0e, 0x11, 0x11, 0x11, 0x0e],   # 0x6f, o
       [0x00, 0x1c, 0x12, 0x12, 0x1c, 0x10, 0x10],   # 0x70, p
       [0x00, 0x07, 0x09, 0x09, 0x07, 0x01, 0x01],   # 0x71, q
       [0x00, 0x00, 0x16, 0x19, 0x10, 0x10, 0x10],   # 0x72, r
       [0x00, 0x00, 0x0f, 0x10, 0x0e, 0x01, 0x1e],   # 0x73, s
       [0x08, 0x08, 0x1c, 0x08, 0x08, 0x09, 0x06],   # 0x74, t
       [0x00, 0x00, 0x11, 0x11, 0x11, 0x13, 0x0d],   # 0x75, u
       [0x00, 0x00, 0x11, 0x11, 0x11, 0x0a, 0x04],   # 0x76, v
       [0x00, 0x00, 0x11, 0x11, 0x15, 0x15, 0x0a],   # 0x77, w
       [0x00, 0x00, 0x11, 0x0a, 0x04, 0x0a, 0x11],   # 0x78, x
       [0x00, 0x11, 0x11, 0x0f, 0x01, 0x11, 0x0e],   # 0x79, y
       [0x00, 0x00, 0x1f, 0x02, 0x04, 0x08, 0x1f],   # 0x7a, z
       [0x06, 0x08, 0x08, 0x10, 0x08, 0x08, 0x06],   # 0x7b, {
       [0x04, 0x04, 0x04, 0x00, 0x04, 0x04, 0x04],   # 0x7c, |
       [0x0c, 0x02, 0x02, 0x01, 0x02, 0x02, 0x0c],   # 0x7d, }
       [0x08, 0x15, 0x02, 0x00, 0x00, 0x00, 0x00],   # 0x7e, ~
       [0x1f, 0x1f, 0x1f, 0x1f, 0x1f, 0x1f, 0x1f]    # 0x7f, DEL
    ]

    binary_font_data = convert_font_to_binary(font_data)
    binary_font_data = normalize_data(binary_font_data)

    encoder_layers = [35, 16, 8, 2]
    decoder_layers = [2, 8, 16, 35]

    autoencoder = Autoencoder(encoder_layers, decoder_layers, learning_rate=0.01)
    autoencoder.train(binary_font_data, epochs=10000)

    encoded_data = autoencoder.encode(binary_font_data)
    decoded_data = autoencoder.decode(encoded_data)

    print("Encoded Data:\n", encoded_data)
    print("Decoded Data:\n", decoded_data)

    # Visualisation de l'espace latent
    labels = np.arange(len(binary_font_data))  # Utiliser des labels pour identifier chaque caractère
    visualize_latent_space(encoded_data, labels)

    # Génération d'une nouvelle lettre (par exemple, en interpolant dans l'espace latent)
    new_latent_point = np.array([0.5, -0.5])  # Exemple de point dans l'espace latent
    new_letter = autoencoder.decode([new_latent_point])
    print("New Letter:\n", new_letter)