import os
import time
import sys
import ctypes

#this function will change the wall paper...
def main():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    while(True):
        file_names = []
        current_time_of_day = get_time_of_day()
        for (path, dir_name, file_name) in os.walk(current_dir + "/images/" + current_time_of_day):
            file_names = file_name

        for file_name in file_names:
            change(current_time_of_day, file_name)
            time.sleep(30)
            continue

#this function will tell the foldername and goes to the folder
def change(folder_path, image_name):
    current_dir = os.path.dirname(os.path.realpath(__file__))

    os_name = os.name
    if(os_name == "posix"):
        image_path = "file://" + current_dir + "/images/" + folder_path + "/" + image_name
        if(os.path.exists("/usr/bin/gsettings")):
            os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri '" + image_path + "'")
    elif(os_name == "nt"):
        image_path = current_dir + "\\images\\" + folder_path + "\\" + image_name
        SPI_SETDESKWALLPAPER = 20 
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0)

#this function will tell the current time
def get_time_of_day(): 
    current_hour = time.localtime().tm_hour
    
    if(current_hour >= 5 and current_hour <= 11):
        return "morning"
    elif(current_hour >= 12 and current_hour <= 17):
        return "day"
    elif(current_hour >= 18 and current_hour <= 20):
        return "afternoon"
    elif(current_hour >= 21 or current_hour <= 4):
        return "night"

if __name__ == "__main__":
    main()
