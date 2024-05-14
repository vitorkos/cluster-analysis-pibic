import os
os.sys.path
import sys
path_to_module = "Users/vitor/cluster-analysis-pibic/venv/Lib/site-packages"
#path_to_module = "../venv/lib/python3.12/site-packages/"
sys.path.append(path_to_module)
import cv2
import matplotlib.pyplot as plt
import numpy as np
import csv
from tkinter import filedialog, Tk

min = float(input("Enter the cluster min size: "))
max = float(input("Enter the cluster max size: "))

# Define o caminho para o diretório dos modelos
root = Tk()
root.withdraw()  # Esconde a janela principal
models_path = filedialog.askdirectory(title="Selecione o diretório dos modelos")
root.destroy()

# Itera sobre cada diretório de experimento
for exp_dir in os.listdir(models_path):
    exp_path = os.path.join(models_path, exp_dir)

    # Verifica se é um diretório
    if os.path.isdir(exp_path):
        # Itera sobre cada imagem no diretório do experimento
        for img_file in os.listdir(exp_path):
            img_path = os.path.join(exp_path, img_file)

            # Verifica se é um arquivo de imagem
            if os.path.isfile(img_path) and img_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                print(f"Processando imagem: {img_path}")

                # Lê e prepara a imagem
                img = cv2.imread(img_path)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                blurred = cv2.GaussianBlur(gray, (7, 7), 0)

                # Aplica threshold adaptativo
                mask = cv2.adaptiveThreshold(blurred,
                                              255,
                                              cv2.ADAPTIVE_THRESH_MEAN_C,
                                              cv2.THRESH_BINARY,
                                              31,
                                              10)

                # Salva a imagem plotada
                bin_image_path = os.path.join(exp_path, f'{img_file[:-4]}_bin.jpg')
                plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.tight_layout()
                plt.savefig(bin_image_path, bbox_inches='tight', pad_inches=0)
                plt.close()  # Fecha a figura

                # Define a variável para receber a imagem binária
                img_bin = cv2.imread(bin_image_path)

                areas = []
                csv_file_path = os.path.join(exp_path, f'cluster_data_{img_file[:-4]}.csv')

                gray_bin = cv2.cvtColor(img_bin, cv2.COLOR_BGR2GRAY)
                ret, thresh_bin = cv2.threshold(gray_bin, 127, 255, 1)
                contours_bin, _ = cv2.findContours(thresh_bin, 1, 2)
                counter = 0

                # Itera sobre cada contorno na imagem binária
                for cnt in contours_bin:
                    cv2.drawContours(img_bin, [cnt], 0, (0, 0, 255), 1)
                    counter += 1

                    # Calcula a área (número de pixels) para cada contorno
                    area = cv2.contourArea(cnt)
                    areas.append(area)

                areas.sort()

                with open(csv_file_path, 'w', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow([f'{exp_dir}_{img_file[:-4]}', 'Número total de clusters'])
                    csv_writer.writerow([counter])

                    j = 0
                    for i, area in enumerate(areas, start=1):
                        if area >= min and area <= max:
                            if i == counter:
                                continue
                            else:
                                csv_writer.writerow([f'Área do Cluster{j}', area])
                                j = j + 1

                # Salva a imagem binária com contornos
                plt.imshow(cv2.cvtColor(img_bin, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.tight_layout()
                bin_contours_image_path = os.path.join(exp_path, f'{img_file[:-4]}_bin_contours.jpg')
                plt.savefig(bin_contours_image_path, bbox_inches='tight', pad_inches=0)
                plt.close()  # Fecha a figura
