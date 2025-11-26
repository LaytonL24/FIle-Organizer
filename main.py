import os
import shutil

source_dir = "/Users/laytonlin/Downloads"

# To move - Extensions
extensions_move_map = {
    ".jpg": "Pictures", 
    ".png": "Pictures", 
    ".docx": "Docs", 
    ".txt": "Docs", 
    ".pdf": "Docs", 
    ".mp4": "Movies",
    ".mov": "Movies",
}

# To Delete - Extensions
extensions_delete_map = {
    ".zip",
    ".dmg"
}

for file in os.listdir(source_dir):
    file_path = os.path.join(source_dir, file)
    
    if os.path.isfile(file_path):
        extension = os.path.splitext(file)[1].lower()
        
        if extension in extensions_move_map:
            destination_name = extensions_move_map[extension]
            destination_folder = os.path.join(source_dir, destination_name)

            # Creates folder if it doesn't exist
            os.makedirs(destination_folder, exist_ok=True)  

            destination_path = os.path.join(destination_folder, file)
            shutil.move(file_path, destination_path)

            print("Moved " + file + " to " + destination_path)
    
        elif extension in extensions_delete_map:
            os.remove(file)

            print("Deleted " + file)
        else:
            print("Unknown extension for " + file)
    else:
        print("Skipped " + file)
