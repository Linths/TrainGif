# Visualizing the training process of a convolutional neural network over time.
# Copyright (C) 2019  Michelle Peters & Lindsay Kempen

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import os
import random
from PIL import Image
import matplotlib.pyplot as plt

#folders = ["bear (animal)", "car (sedan)", "cloud", "panda", "pigeon", "seagull", "sheep", "suv", "teddy-bear", "van"]
folders = ["airplane","alarm clock","angel","ant","apple","banana","basket","bed","bell","calculator"]
for folder in folders:
    folder_path = os.path.join('data/train_diff_trans', folder)
    
    # find all files paths from the folder
    images = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    for image in images:
        #print(image)
        
        #normal image
        img = Image.open(image)
        #plt.imshow(img)
        #plt.show()
        
        #flipped image
        flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
        #plt.imshow(flipped_img)
        #plt.show()
        
        #rotated image
        k = random.choice([int(random.uniform(-20.5,-3.5)),int(random.uniform(3.5,20.5))])
        rotated_img = img.rotate(k, fillcolor="white")
        #plt.imshow(rotated_img)
        #plt.show()    
        
        #shifted image
        l = random.choice([random.uniform(-100,-20),random.uniform(20,100)])
        m = random.choice([random.uniform(-100,-20),random.uniform(20,100)]) 
        shifted_img = img.rotate(0, translate=(l,m), fillcolor="white")
        #plt.imshow(shifted_img)
        #plt.show()  
        
        #scaled image
        n = int(random.choice([random.uniform(0.75,0.9),random.uniform(1.1,1.25)])*img.width)
        scaled_img = img.resize((n,n))
        if scaled_img.width>img.width: #bigger
            padd_needed = scaled_img.width-img.width
            padd = int(padd_needed/2)
            padd_r = padd+img.width
            scaled_img_2 = scaled_img.crop((padd, padd, padd_r, padd_r))
        else: #smaller
            padd = (img.width-scaled_img.width)/2
            if (padd%2==0):
                padd_1 = int(padd)
                padd_2 = padd_1
            else:
                padd_1 = int(padd)
                padd_2 = padd_1+1
            scaled_img_2 = Image.new(scaled_img.mode, (img.width,img.height), (255))
            scaled_img_2.paste(scaled_img, box=(padd_1,padd_2))
        #plt.imshow(scaled_img_2)
        #plt.show()
        
        file, ext = os.path.splitext(image)
        flipped_img.save(file + "_flipped.png", "PNG")
        rotated_img.save(file + "_rotated.png", "PNG")
        shifted_img.save(file + "_shifted.png", "PNG")
        scaled_img_2.save(file + "_scaled.png", "PNG")