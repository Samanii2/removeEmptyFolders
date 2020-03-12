"""Remove empty folders program"""
import os

def removeEmptyFolders():
    path = r"C:\utv\Projects\FileSorter\testdata"
    os.chdir(path)
    filesToRemove = os.listdir(path)
    
    print("Removing empty folders...")
    if len(filesToRemove):
        for files in filesToRemove:
            filePath = os.path.join(path, files)              
            if os.path.isdir(filePath) and len(os.listdir(filePath)) == 0:
                os.rmdir(filePath)

    print("Removal complete.")
    
removeEmptyFolders()
