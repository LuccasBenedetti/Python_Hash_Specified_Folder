import hashlib
import os


def hash_files():
    directory = input("Enter the full directory path: ")
    while not (os.path.isdir(directory)):
        directory = input("Invalid directory, try again: ")

    if os.path.isfile("hash_file_old.txt"):
        os.remove("hash_file_old.txt")
    if os.path.isfile("hash_file.txt"):
        os.rename("hash_file.txt", "hash_file_old.txt")
        hash_file = open("hash_file.txt", "w")
    else:
        hash_file = open("hash_file.txt", "w")
    hash_file.write(directory + "\n\n")

    for root, dirs, files in os.walk(directory, topdown=True):

        for name in files:
            print(os.path.join(root, name))
            FileName = (os.path.join(root, name))

            hasher = hashlib.sha256()
            with open(str(FileName), 'rb') as afile:
                hasher.update(afile.read())
                print(hasher.hexdigest() + "\n")
                hash_file.write(os.path.join(root, name) + " ; " + hasher.hexdigest() + "\n")


def check_hash():
    with open("hash_file.txt") as file1:
        file_directory1 = file1.readline().rstrip()
    with open("hash_file_old.txt") as file2:
        file_directory2 = file2.readline().rstrip()

    if file_directory1 == file_directory2:
        f1 = open("hash_file.txt")
        i = 0
        for line1 in f1:
            i += 1
            if i == 1 or i == 2:
                continue
            list_comp = line1.split(" ; ")
            flag = 0
            j = 0
            f2 = open("hash_file_old.txt")
            for line2 in f2:
                j += 1
                if j == 1 or j == 2:
                    continue
                list_comp2 = line2.split(" ; ")
                if list_comp[0] == list_comp2[0]:
                    flag = 1
                    if list_comp[1] == list_comp2[1]:
                        print("Line: " + str(i) + "- Hash confirmed")
                    else:
                        print("Line: " + str(i) + "- File was modified since backup")
                    break
            if flag == 0:
                print("Line: " + str(i) +"- File not found on backup")

    else:
        print("Incoherent directories!")


def options_menu():
    options = ["Hash Files", "Check Files", "Exit Program"]
    for i in range(len(options)):
        print(str(i + 1) + ":", options[i])

    inp = int(input("Choose an option: "))
    if inp == 1:
        os.system('cls')
        hash_files()
        another_operation()
    elif inp == 2:
        os.system('cls')
        check_hash()
        another_operation()
    elif inp == 3:
        exit()
    else:
        os.system('cls')
        print("Invalid Input!\n")
        options_menu()


def another_operation():
    anthr_op = input("Do you wish to make another operation? Y/N: ")
    if anthr_op.upper() == 'Y':
        options_menu()
    elif anthr_op.upper() == 'N':
        exit()
    else:
        another_operation()


print("-_ Program to generate and compare the Hash on my files _-\n")
options_menu()