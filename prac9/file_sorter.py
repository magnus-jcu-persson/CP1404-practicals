import os
import shutil

def main():
    os.chdir('FilesToSort')
    directories = {}

    for filename in os.listdir('.'):
        ext_list = filename.split('.')
        ext = ext_list[-1].lower()

        if ext not in directories:
            directory = input("What category would you like to sort {} files into?".format(ext)).title()
            directories[ext] = directory

        try:
            os.mkdir(directories[ext])
        except FileExistsError:
            pass

        shutil.move(filename, os.path.join(directories[ext], filename))

main()