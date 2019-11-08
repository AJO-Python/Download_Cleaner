import os
import shutil
import time

def sort_files(path="~/Downloads"):
    """
    Sorts all files in "path" into folders by filetype
    Default path is current users downloads folder
    """
    # Gets list of files in directory
    # Ignores folders, looks only for files
    FILES = [file for file in os.listdir(path) if os.path.isfile(join(path, file))]
    FOLDER_CATEGORIES = {
        "Images": ["png", "jpeg", "jpg", "bmp", "dds", "gif", "psd", "thm", "tif", "tiff",
            "yuv", "svg"],
        "Documents": ["pdf", "doc", "xlr", "xls", "docx", "log", "msg", "odt", "rtf",
            "pages", "tex", "txt", "wpd", "wps"],
        "Data": ["csv", "dat", "ged", "sdf", "xml"],
        "Media": ["aif", "iff", "m3u", "m4a", "mid", "mp3", "mpa", "wav", "wma", "wmv",
            "asf", "avi", "flv", "m4v", "mov", "mp4", "mpg", "rm", "srt",
            "swf", "vob"],
        "Programs": ["sh", "exe", "bash", "tar", "apk", "app", "bat", "com", "jar"]
        }

    #Checking and creating destination folders according to folder
    for key in FOLDER_CATEGORIES:
        if os.path.isdir(path + "/" + key):
            continue
        else:
            os.mkdir(path + "/" + key)

    # Moving files into the folders
    for file in FILES:
        # Gets filetype for each file
        filetype = file.split(".")[1]
        
        # Checks filetype and moves to correct folder
        for key in FOLDER_CATEGORIES:
            if filetype in FOLDER_CATEGORIES[key]:
                new_path = path + "/" + key + "/" + file
                shutil.move(join(path,file), new_path)

if __name__=="__main__":
    """
    If run as main will default to current users default downloads - Linux only
    Can leave running and will automatically sort every 5 mins
    """
    while True:
        path="~/Downloads"
        sort_files(path)
        time.sleep(300)
