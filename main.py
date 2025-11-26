import os
import shutil

source_dir = "/Users/laytonlin/Downloads"

# To 
extensions_map = {
    ".jpg": "Pictures", 
    ".png": "Pictures", 
    ".docx": "Docs", 
    ".txt": "Docs", 
    ".pdf": "Docs", 
    ".mp4": "Movies",
    ".mov": "Movies",
}

for file in os.listdir(source_dir):
    file_path = os.path.join(source_dir, file)
    
    if os.path.isfile(file_path):
        extension = os.path.splitext(file)[1].lower()
        
        if extension in extensions_map:
            destination_name = extensions_map[extension]
            destination_folder = os.path.join(source_dir, destination_name)
            os.makedirs(destination_folder, exist_ok=True)  

            destination_path = os.path.join(destination_folder, file)
            shutil.move(file_path, destination_path)

            print("Moved " + file + " to " + destination_path)
        else:
            print("Unknown extension for " + file)
    else:
        print("Skipped " + file)
