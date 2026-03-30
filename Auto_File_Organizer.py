import os
import shutil

folder_path = "C:\\Users\\17284\Desktop\\test_folder"

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isdir(file_path):
        continue

    if filename.endswith(".pdf"):
        target_folder = os.path.join(folder_path, "PDF")
    elif filename.endswith(".jpg") or filename.endswith(".png"):
        target_folder = os.path.join(folder_path, "Images")
    elif filename.endswith(".mp4"):
        target_folder = os.path.join(folder_path, "Videos")
    else:
        target_folder = os.path.join(folder_path, "Others")

    os.makedirs(target_folder, exist_ok=True)

    shutil.move(file_path, os.path.join(target_folder, filename))

print("Organization Complete")
