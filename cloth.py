import os
import glob
import random

clothes_path = "G:\CN5\AIP391\VIRTUAL_TRY_ON\FashionTryon\FashionTryon\clothes"
img_path = "G:\CN5\AIP391\VIRTUAL_TRY_ON\FashionTryon\FashionTryon\img"

img_name = sorted(os.listdir(img_path))
clothes_name = os.listdir(clothes_path)
random.shuffle(clothes_name)

print(img_name)
print(clothes_name)
print(len(img_name), len(clothes_name))
demo_shuffle = open("G:\CN5\AIP391\VIRTUAL_TRY_ON\FashionTryon\FashionTryon\demo_shuffle\demo.txt", "w")
for i in range(len(img_name)):
    demo_shuffle.write(img_name[i]+" "+clothes_name[i]+"\n")
demo_shuffle.close()