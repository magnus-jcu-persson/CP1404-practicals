"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def main():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))

            os.rename(os.path.join(directory_name, filename), os.path.join(directory_name, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(".TXT", ".txt")
    next_new_name = ''
    for i, letter in enumerate(new_name):
        if i == 0:
            next_new_name += letter.upper()
        elif letter.isupper():
            next_new_name += "_" + letter
        elif letter == ' ':
            pass
        elif new_name[i-1] == " ":
            next_new_name += "_" + letter.upper()
        else:
            next_new_name += letter


    return next_new_name

main()