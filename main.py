from loguru import logger
import sys
import ctypes, os
from functions import *



logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")


def main():
    url = 'https://wallscloud.net/ru/wallpapers/random'
    page_from_url = get_page_by_url(url)
    soup_from_page = get_soup_from_page(page_from_url)
    link = soup_from_page.find('a', class_='wall_link')
    link = link.get('href')

    page_for_download = get_page_by_url(link)
    soup_for_download = get_soup_from_page(page_for_download)
    link = soup_for_download.find('button', class_='btn btn-default res_down search_available_res hide')
    print(link.get('href'))
    
    
    resolution = f'{ctypes.windll.user32.GetSystemMetrics(0)}x{ctypes.windll.user32.GetSystemMetrics(1)}'
    link = str(link.get('href'))
    link = link.replace('{R_WIDTH}x{R_HEIGHT}', resolution)
    image_by_url = get_page_by_url(link)
    path = save_image_from_internet(image_by_url)
    # with open(f'1.jpg', 'wb') as file:
    #     file.write(image_by_url.content)
    if check_os == 'Linux':
        command = f"gsettings set org.gnome.desktop.background picture-uri file:{path}"
        os.system(command)
    else:
        folder = r"E:\Python_projects\wallpaper_to_background"
        file_name = r"1.jpg"

        full_path = os.path.join(folder, file_name)
        img = bytes(full_path, 'utf-8')

        ctypes.windll.user32.SystemParametersInfoA(20, 0, img , 0)


if __name__ == '__main__':
    main()
    def aa():
        pass