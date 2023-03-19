import os


directory = "D:/Data/newdata/"  # Replace with the directory path where your JPG files are located
new_name = "Fire"       # Replace with the new name you want to give to your JPG files
new_directory = "D:/Data/newdata/"  # New directory to save the renamed files
start_index = 1

# Create the new directory if it does not exist
if not os.path.exists(new_directory):
     os.makedirs(new_directory)

# Get all JPG files in the directory
jpg_files = [f for f in os.listdir(directory) if f.endswith('.jpg')]

# Rename each JPG file with a consecutive number as suffix and save in the new directory
for i, jpg_file in enumerate(jpg_files):
    old_path = os.path.join(directory, jpg_file)
    new_path = os.path.join(new_directory, f"{new_name}_{start_index + i}.jpg")
    # Check if the new file name already exists in the directory
    if os.path.exists(new_path):
        new_path = os.path.join(new_directory, f"{new_name}_{start_index + i}.jpg")
    os.rename(old_path, new_path)
