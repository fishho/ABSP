#! python3
# selectiveCopy.py - A grogram that walks through a folder tree and searches for
# files with a certain file extension(such as .pdf or.jpg).Copy these files from
# whatever location they are in to a new folder
import os, shutil

def moveFileType(folder):
    print("Done1")
    for root, dirs ,files in os.walk(folder):
        print("Done1")
        for file in files:
            print("Done1")
            if file.endswith('.txt'):
                image_path = os.path.join(root, file) # get hte path location of each txt
                print('location:',image_path)
                shutil.copy(image_path,'D:\\workspace\\ABSP\\chapter9\\back\')
                print("Done")

moveFileType('D:\\workspace\\ABSP\\chapter9')