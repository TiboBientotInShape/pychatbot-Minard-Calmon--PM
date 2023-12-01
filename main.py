from function import *
if __name__ == '__main__':
    directory = "./Speeches"
    files_name = list_of_files(directory, ".txt")
    print(files_name)