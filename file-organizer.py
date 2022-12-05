import os
import shutil

path = input("Enter Path: ")
print(path)
files = os.listdir(path)
for file in files:
    if os.path.isfile(path + '/' + file):
        filename, extension = os.path.splitext(file)
        extension = extension[1:]
        if os.path.exists(path + '/' + extension) and len(extension) != 0:
            shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
            print(f'File {file} was moved to {path}\{extension}')
        elif len(extension) != 0:
            os.makedirs(path + '/' + extension)
            print(f'Folder "{extension}" was created!')
            shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
            print(f'File {file} was moved to {path}\{extension}')
        else:
            if os.path.exists(path + '/' +  '_unsorted_files'):
                shutil.move(path + '/' + file, path + '/' + '_unsorted_files' + '/' + file)
                print(f'File {file} was moved to {path}\\_unsorted_files')
            else:
                os.makedirs(path + '/' + '_unsorted_files')
                print('Folder _unsorted_files was created!')
                shutil.move(path + '/' + file, path + '/' + '_unsorted_files' + '/' + file)
                print(f'File {file} was moved to {path}\\_unsorted_files')






