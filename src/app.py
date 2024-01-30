import os
os.sys.path
import sys
path_to_module = "../venv/lib/python3.11/site-packages/"
sys.path.append(path_to_module)

import cv2
import matplotlib.pyplot as plt
import numpy as np
import csv
from tkinter import filedialog, Tk

# Define the path to the models directory
root = Tk()
root.withdraw()  # Hide the main window
models_path = filedialog.askdirectory(title="Select the models directory")
root.destroy()

# Iterate over each experiment directory
for exp_dir in os.listdir(models_path):
    exp_path = os.path.join(models_path, exp_dir)
    
    # Check if it's a directory
    if os.path.isdir(exp_path):
        # Iterate over each image in the experiment directory
        for img_file in os.listdir(exp_path):
            img_path = os.path.join(exp_path, img_file)
            
            # Check if it's an image file
            if os.path.isfile(img_path) and img_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                print(f"Processing image: {img_path}")

                # Read and prepare the image
                img = cv2.imread(img_path)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                blurred = cv2.GaussianBlur(gray, (7, 7), 0)

                # Apply adaptive thresholding
                mask = cv2.adaptiveThreshold(blurred,
                                              255,
                                              cv2.ADAPTIVE_THRESH_MEAN_C,
                                              cv2.THRESH_BINARY,
                                              31,
                                              10)

                # Plot results
                

                ax = plt.subplots(1, figsize=(12,5))
                ax[1].imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
                ax[1].axis('off')
                plt.tight_layout()
                # Save the plotted image
                bin_image_path = os.path.join(exp_path, f'{img_file[:-4]}_bin.jpg')
                plt.savefig(bin_image_path, bbox_inches='tight', pad_inches=0)
                
                #Define variable to receive the binary image
                img_bin = cv2.imread(bin_image_path)

                areas = []
                csv_file_path = os.path.join(exp_path, f'cluster_data_{img_file[:-4]}.csv')

                gray_bin = cv2.cvtColor(img_bin, cv2.COLOR_BGR2GRAY)
                ret, thresh_bin = cv2.threshold(gray_bin, 127, 255, 1)
                contours_bin, _ = cv2.findContours(thresh_bin, 1, 2)
                counter = 0

                # Iterate over each contour in the binary image
                for cnt in contours_bin:
                    cv2.drawContours(img_bin, [cnt], 0, (0, 0, 255), 1)
                    counter += 1

                    # Calculate the area (number of pixels) for each contour
                    area = cv2.contourArea(cnt)
                    areas.append(area)

                areas.sort()

                with open(csv_file_path, 'w', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow([f'{exp_dir}_{img_file[:-4]}', 'Number of Total Clusters'])
                    csv_writer.writerow([counter])

                    for i, area in enumerate(areas, start=1):
                        csv_writer.writerow([f'Area of Cluster{i}', area])

                # Plot the binary image with contours
                plt.imshow(cv2.cvtColor(img_bin, cv2.COLOR_BGR2RGB))
                plt.axis('off')  # Turn off axis labels and ticks
                plt.tight_layout()

                # Save the binary image with contours
                bin_contours_image_path = os.path.join(exp_path, f'{img_file[:-4]}_bin_contours.jpg')
                plt.savefig(bin_contours_image_path, bbox_inches='tight', pad_inches=0)
                plt.show()