# File Organizer

A Python script that cleans and organizes a folder by **moving** certain file types into folders and **deleting** others.

## What It Does

* Moves files based on extension:

  * **Pictures:** `.jpg`, `.png`
  * **Docs:** `.docx`, `.txt`, `.pdf`
  * **Movies:** `.mp4`, `.mov`
* Deletes unwanted files: `.zip`, `.dmg`
* Creates folders automatically if they don’t exist.

## How to Use

1. Set the folder you want to clean:

   ```python
   source_dir = "/path/to/folder"
   ```
2. Edit which files get **moved** here:

   ```python
   extensions_move_map = {
       ".jpg": "Pictures",
       ".png": "Pictures",
       ".docx": "Docs",
       ".txt": "Docs",
       ".pdf": "Docs",
       ".mp4": "Movies",
       ".mov": "Movies",
   }
   ```
3. Edit which files get **deleted** here:

   ```python
   extensions_delete_map = {
       ".zip",
       ".dmg"
   }
   ```
4. Run the script.

## ⚠️ Note

Files in the delete list are **permanently removed** — review the lists above before running.
