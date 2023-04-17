import os

# define the folder name and directory
folder_Name = input("Folder name ? ")
parent_folder = "C:/Users/Pedro/Desktop/i/Projects"
parent_path = os.path.join(parent_folder, folder_Name)

file_Name = folder_Name + ".py"
file_path = os.path.join(parent_path, file_Name)

# check if the foler already exists or not
if os.path.exists(parent_path):
    print("Folder Already Exists!")
# Creates the folder
else:
    try:
        os.mkdir(parent_path)
        print("Folder created")
# Creates a python file inside the folder
        with open(file_path, 'w') as f:
            f.write("import ")
        print("File created inside the folder")
    except OSError:
        print("Folder was NOT created")