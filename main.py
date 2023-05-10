import os
import random


def mp3_scrambler():
    folder = input("What directory full of mp3 files, should I scramble: ")
    funny_word = input("Please enter a random word: ")

    # Check if the directory actually exists
    try:
        os_list = os.listdir(folder)
    except FileNotFoundError:
        print("ERROR: invalid directory")
        return
    random.shuffle(os_list)
    random.shuffle(os_list)

    for filename in os_list:
        old = folder + filename
        new = folder + str(os_list.index(filename)) + "_" + funny_word + ".mp3"

        # Extract extension from filename
        file_type = filename.split(".")
        if file_type[-1] != "mp3":
            continue
        # Check if the filename is already in the folder
        try:
            os.rename(old, new)
        except FileExistsError:
            print("ERROR: used this word in directory already")
            break
    print("DONE")


if __name__ == '__main__':
    mp3_scrambler()
