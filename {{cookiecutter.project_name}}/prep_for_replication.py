# This code is here to help you prepare your data for replication. Run it in the command console with: python prep_for_replication.py

# Import packages
import os
import shutil

#Create the replication folder
for folder in ['code', 'paper', 'appendix']:
    if os.path.exists(folder):
        shutil.rmtree(folder)
        if folder == 'code':
            os.mkdir(folder)

# List of folders to copy
folders_to_copy_code = ['data', 'src', 'notebooks', 'references']
folders_to_copy_paper = ['./output/paper']
folders_to_copy_appendix = ['./output/appendix']
destination_folder_code = 'code'
destination_folder_paper = './'
destination_folder_appendix = './'

# Copy each folder
for folder in folders_to_copy_code:
    # Determine the name of the folder
    folder_name = os.path.basename(folder)
    # Create full path for the destination
    dest_path = os.path.join(destination_folder_code, folder_name)

    # Copy the folder
    shutil.copytree(folder, dest_path)
    print(f"Copied {folder} to {dest_path}")

for folder in folders_to_copy_paper:
    # Determine the name of the folder
    folder_name = os.path.basename(folder)
    # Create full path for the destination
    dest_path = os.path.join(destination_folder_paper, folder_name)

    # Copy the folder
    shutil.copytree(folder, dest_path)
    print(f"Copied {folder} to {dest_path}")

for folder in folders_to_copy_appendix:
    # Determine the name of the folder
    folder_name = os.path.basename(folder)
    # Create full path for the destination
    dest_path = os.path.join(destination_folder_appendix, folder_name)

    # Copy the folder
    shutil.copytree(folder, dest_path)
    print(f"Copied {folder} to {dest_path}")

print("All folders have been copied.")

# We remove the older files
for file in ["data", "notebooks", "references", "src", "output"]:
    if os.path.exists(file):
        shutil.rmtree(file)

print("==========================")
print("Formating for replication complete")
print("==========================")

