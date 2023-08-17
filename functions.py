import requests
from loguru import logger
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import platform
import pathlib


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


def check_os() -> pathlib.Path:
    return platform.system()

def save_image_from_internet(platform: platform.system, response: requests.Response) -> None:
    with open(pathlib.Path(pathlib.Path.cwd(), '1.jpg'), 'wb') as file:
        file.write(response.content)
    return pathlib.Path(pathlib.Path.cwd(), '1.gpg')