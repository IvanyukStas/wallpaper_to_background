import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from loguru import logger
import sys
import ctypes, os



logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")


def get_page_by_url(url: str) -> requests.Response:
    user_agent = UserAgent()
    headers = {
        'user-agent': user_agent.random
    }
    
    response = requests.get(url=url, headers=headers)
    logger.info('Get page!')
    return response

def get_soup_from_page(response: requests.Response) -> BeautifulSoup:
    soup = BeautifulSoup(response.text, 'lxml')
    return soup



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
    with open(f'1.jpg', 'wb') as file:
        file.write(image_by_url.content)

    folder = r"E:\Python_projects\wallpaper_to_background"
    file_name = r"1.jpg"

    full_path = os.path.join(folder, file_name)
    img = bytes(full_path, 'utf-8')

    ctypes.windll.user32.SystemParametersInfoA(20, 0, img , 0)


if __name__ == '__main__':
    main()