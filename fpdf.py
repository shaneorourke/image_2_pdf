from PIL import Image
import os
import time

dir = '/home/shane/Downloads/naruto'
pdf_name = 'naruto_'

#Boolean - If this locks up the machine 
#due to lack of resources (it can be hungry), do each loop individually
#just keep running the code until you get the error "IndexError: list index out of range"
#This means that the images list is empty
low_power_mode = True

if not os.path.exists('output'):
    os.makedirs('output')

files_writen = []
#open and read the file after the appending:
files_writen_list = open("files.txt", "r")
for file_writen in files_writen_list.readlines():
    files_writen.append(file_writen.replace('\n',''))


file_breakdowns = []
for a in range(0,10):
    for b in range(0,10):
        c = str(a)+str(b)
        if str(c) not in (files_writen):
            file_breakdowns.append(c)

for i in file_breakdowns:
    file_breakdown = i
    files = []

    for f in os.listdir(dir):
        if f[:2] == file_breakdown:
            files.append(f)

    files.sort()
    images = []
    for f in files:
        img = Image.open(f"{dir}/" + f)
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        images.append(img)
            

    pdf_path = f'./output/{pdf_name}{file_breakdown}.pdf'
    print(pdf_path)
    images[0].save(
        pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:] 
    )

    file_write = open("files.txt", "a")
    file_write.write(file_breakdown+'\n')
    file_write.close()
    
    if low_power_mode != True:
        time.sleep(5)
    else:
        exit()
