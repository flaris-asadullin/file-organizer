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
            print(f'The file {file} has been moved to {path}\{extension}')
        elif len(extension) != 0:
            os.makedirs(path + '/' + extension)
            print(f'Folder "{extension}" has been created!')
            shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
            print(f'The file {file} has been moved to {path}\{extension}')
        else:
            if os.path.exists(path + '/' + 'without_extension'):
                shutil.move(path + '/' + file, path + '/' + 'without_extension' + '/' + file)
                print(f'The file {file} has been moved to {path}\\without_extension')
            else:
                os.makedirs(path + '/' + 'without_extension')
                print('Folder without_extension has been created!')
                shutil.move(path + '/' + file, path + '/' + 'without_extension' + '/' + file)
                print(f'The file {file} has been moved to {path}\\without_extension')
                





