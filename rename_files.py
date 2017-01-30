import os
def rename_files():
    #1 get file names from a folder
    file_list = os.listdir(r"C:\Users\Owner\Documents\prank\prank")
    print(file_list)
    
    #2 for each file, rename file
    for photo in file_list:
        os.rename(photo,
rename_files()
