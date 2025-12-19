from selenium.webdriver.chrome.options import Options
from scraper.scraper import WebScraper

from config import GENERAL_URL


if __name__ == "__main__":
    scraper = WebScraper(GENERAL_URL)

    """    
    TIME OPTIONS                    MAGNITUDE OPTIONS
    1 = Ultimi 7 giorni             1 = Magnitudo 2+
    2 = Ultimi 30 giorni            2 = Magnitudo 3+
    3 = Ultimi 90 giorni            3 = Magnitudo 4+
    4 = Ultimi 365 giorni           4 = Magnitudo 5.5+
    5 = Dal 1985-01-01              0 = Tutte le magnitudo
    """
    scraper.find_earthquakes_magnitude_higher_than(2, 4)