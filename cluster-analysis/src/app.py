import os
import sys
import cv2
import matplotlib.pyplot as plt
import numpy as np
import csv
from tkinter import filedialog, Tk

####################################
####################################
####################################

# cria o csv
csv_file_path = os.path.join(f'analise_cluster_face_1.csv')

with open(csv_file_path, 'a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['EXPERIMENTO', 'NUMERO DE CLUSTERS', 'AREA', '% DA AREA', "N.C(2.3 - 3.3)", "AREA(2.3 - 3.3)", "% da area (2.3 - 3.3)", "N.C(3.3 - 4.3)", "AREA(3.3 - 4.3)", "% da area (3.3 - 4.3)", "N.C(4.3 - 5.3)", "AREA(4.3 - 5.3)", "% da area (4.3 - 5.3)", "N.C(5.3 - 6.3)", "AREA(5.3 - 6.3)", "% da area (5.3 - 6.3)"])

root = Tk()
root.withdraw()  # Esconde a janela principal
models_path = filedialog.askdirectory(title="Selecione o diretório dos modelos")
root.destroy()

####################################
####################################
####################################

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
                #if img_file.lower().endswith('2.jpg'):
                    #print(f"Pular imagem: {img_path}")
                    #continue

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

                ####################################
                ####################################
                ####################################

                gray_bin = cv2.cvtColor(img_bin, cv2.COLOR_BGR2GRAY)
                ret, thresh_bin = cv2.threshold(gray_bin, 127, 255, 1)
                contours_bin, _ = cv2.findContours(thresh_bin, 1, 2)

                # Itera sobre cada contorno na imagem binária
                for cnt in contours_bin:
                    cv2.drawContours(img_bin, [cnt], 0, (0, 0, 255), 1)

                    # Calcula a área (número de pixels) para cada contorno
                    # Pula os ruídos
                    if cv2.contourArea(cnt) < 10 or cv2.contourArea(cnt) > 1000:
                        continue
                    area = cv2.contourArea(cnt)
                    areas.append(area)

                areas.sort()

                ####################################
                ####################################
                ####################################

                # Salva a imagem binária com contornos
                plt.imshow(cv2.cvtColor(img_bin, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.tight_layout()
                bin_contours_image_path = os.path.join(exp_path, f'{img_file[:-4]}_bin_contours.jpg')
                plt.savefig(bin_contours_image_path, bbox_inches='tight', pad_inches=0)
                plt.close()  # Fecha a figura

                ####################################
                ####################################
                ####################################

                faixas = [np.log(10), np.log(27), np.log(73), np.log(200), np.log(550)]

                len_1 = 0
                len_2 = 0
                len_3 = 0
                len_4 = 0

                sum_1 = 0
                sum_2 = 0
                sum_3 = 0
                sum_4 = 0

                for area in areas:
                    if (np.log(area) >= faixas[0] and np.log(area) <= faixas[1]):
                        len_1 = len_1 + 1
                        sum_1 = sum_1 + area
                    if (np.log(area) >= faixas[1] and np.log(area) <= faixas[2]):
                        len_2 = len_2 + 1
                        sum_2 = sum_2 + area
                    if (np.log(area) >= faixas[2] and np.log(area) <= faixas[3]):
                        len_3 = len_3 + 1
                        sum_3 = sum_3 + area
                    if (np.log(area) >= faixas[3] and np.log(area) <= faixas[4]):
                        len_4 = len_4 + 1
                        sum_4 = sum_4 + area

                percent_1 = "aaaaaaa"
                percent_2 = "aaaaaaa"
                percent_3 = "aaaaaaa"
                percent_4 = "aaaaaaa"

                with open(csv_file_path, 'a', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)

                    csv_writer.writerow([img_path, len(areas), sum(areas), "A+b", len_1, sum_1, percent_1, len_2, sum_2, percent_2, len_3, sum_3, percent_3, len_4, sum_4, percent_4])
