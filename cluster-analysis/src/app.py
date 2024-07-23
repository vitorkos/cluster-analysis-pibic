import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import csv
from tkinter import filedialog, Tk

# Define as faixas de logaritmos
faixas = [np.log(10), np.log(27), np.log(73), np.log(200), np.log(550)]

# Cria o csv
csv_file_path = os.path.join('vitor_analise_cluster_face_2.csv')

with open(csv_file_path, 'a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['EXPERIMENTO', 'NUMERO DE CLUSTERS', 'AREA', '% DA AREA',
                         "N.C(2.3 - 3.3)", "AREA(2.3 - 3.3)", "% da area (2.3 - 3.3)",
                         "N.C(3.3 - 4.3)", "AREA(3.3 - 4.3)", "% da area (3.3 - 4.3)",
                         "N.C(4.3 - 5.3)", "AREA(4.3 - 5.3)", "% da area (4.3 - 5.3)",
                         "N.C(5.3 - 6.3)", "AREA(5.3 - 6.3)", "% da area (5.3 - 6.3)"])

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
                # Pular arquivos que terminam com '2.jpg'
                if img_file.lower().endswith('1.jpg'):
                     print(f"Pular imagem: {img_path}")
                     continue

                print(f"Processando imagem: {img_path}")

                # Lê e prepara a imagem
                img = cv2.imread(img_path)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                blurred = cv2.GaussianBlur(gray, (7, 7), 0)

                # Aplica threshold adaptativo
                mask = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 31, 10)

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

                # Extrai contornos
                gray_bin = cv2.cvtColor(img_bin, cv2.COLOR_BGR2GRAY)
                ret, thresh_bin = cv2.threshold(gray_bin, 127, 255, 1)
                contours_bin, _ = cv2.findContours(thresh_bin, 1, 2)

                # Itera sobre cada contorno na imagem binária
                for cnt in contours_bin:
                    cv2.drawContours(img_bin, [cnt], 0, (0, 0, 255), 1)

                    # Calcula a área (número de pixels) para cada contorno
                    # Pula os ruídos
                    area = cv2.contourArea(cnt)
                    if area >= 10 and area <= 1000:
                        areas.append(area)

                areas.sort()

                # Inicia as contagens e somas das áreas das faixas
                len_1 = len_2 = len_3 = len_4 = 0
                sum_1 = sum_2 = sum_3 = sum_4 = 0

                # Calcula as áreas e contagens para cada faixa
                for area in areas:
                    log_area = np.log(area)
                    if faixas[0] <= log_area < faixas[1]:
                        len_1 += 1
                        sum_1 += area
                    elif faixas[1] <= log_area < faixas[2]:
                        len_2 += 1
                        sum_2 += area
                    elif faixas[2] <= log_area < faixas[3]:
                        len_3 += 1
                        sum_3 += area
                    elif faixas[3] <= log_area <= faixas[4]:
                        len_4 += 1
                        sum_4 += area

                # Calcula a porcentagem da área ocupada pelos clusters
                h, w, c = img.shape
                total = h * w

                percent_1 = (100 * sum_1) / total
                percent_2 = (100 * sum_2) / total
                percent_3 = (100 * sum_3) / total
                percent_4 = (100 * sum_4) / total
                porcent_total = (100 * sum(areas)) / total

                # Salva os resultados no CSV
                with open(csv_file_path, 'a', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow([img_file, len(areas), sum(areas), porcent_total,
                                         len_1, sum_1, percent_1,
                                         len_2, sum_2, percent_2,
                                         len_3, sum_3, percent_3,
                                         len_4, sum_4, percent_4])


print("Análise concluída e salva no arquivo CSV.")
