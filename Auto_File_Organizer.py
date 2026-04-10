import os
import shutil

folder_path = os.path.normpath(input("please enter the folder name: ").strip().strip('"').strip("'"))
if not os.path.exists(folder_path):
    print("Folder not found")
    exit()

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
    elif filename.endswith(".py"):
        target_folder = os.path.join(folder_path, "programmes")
    elif filename.endswith(".xlsx"):
        target_folder = os.path.join(folder_path, "charts")
    else:
        target_folder = os.path.join(folder_path, "Others")

    os.makedirs(target_folder, exist_ok=True)

    target_path = os.path.join(target_folder, filename)

    count = 1
    while os.path.exists(target_path):
        name, ext = os.path.splitext(filename)
        new_filename = f"{name}_{count}{ext}"
        target_path = os.path.join(target_folder, new_filename)
        count += 1

    shutil.move(file_path, target_path)

print("Organization Complete")
