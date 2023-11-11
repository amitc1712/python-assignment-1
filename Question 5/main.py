import requests
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(name)s - %(levelname)s - %(asctime)s - %(message)s")
file_handler = logging.FileHandler("app.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def anti_html(url):
    try:
        response = requests.get(url)
        html = response.content

        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()

        print(text)
        logger.info(
            "Successfully retrieved and parsed HTML content from {}".format(url)
        )
        return text

    except requests.exceptions.RequestException as e:
        logger.error("Failed to retrieve content from {}. Error: {}".format(url, e))
        return None

    except Exception as e:
        logger.error("An unexpected error occurred. Error: {}".format(e))
        return None


if __name__ == "__main__":
    url = "https://www.example.com"
    anti_html(url)
