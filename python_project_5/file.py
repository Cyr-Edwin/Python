# import modules
import os

# list files in folders
def listed_files(path):
    
    try:
        # list folders present in the directory
        fls = os.listdir(path)
        return fls, None

    except FileNotFoundError as error:
        return None,"File not found"

    except PermissionError as error:
        return None,"Permission denied"
    except NotADirectoryError as error:
        return None , "Not a directory"


def files():

    # enter folder name path
    folder_names_path = input("Enter your folder names here, separeted by comma  :")

    # convert the string to list of folder name
    list_folder_path = folder_names_path.split(",")

    for folder_path in list_folder_path:
        files , error = listed_files(folder_path)
        #list files name
        if files:
             print (f"Folder path:\n{folder_path}\n")
             print (f"File names:")
             for file in files:
                print (file)
        else:
            print (f"{error}")

if __name__ == "__main__":
    files()
