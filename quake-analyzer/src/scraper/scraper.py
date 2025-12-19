from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC

import time


options = Options()
options.add_argument("--incognito")
# options.add_argument("--headless=new") # modalità senza interfaccia grafica


class WebScraper():
    def __init__(self, url, max_wait = 10):
        self.url = url
        self.driver = webdriver.Firefox(options = options)
        self.wait = WebDriverWait(self.driver, max_wait)


    def find_earthquakes_magnitude_higher_than(self, time_option, min_magnitude = 0):
        """
        Trova i terremoti con magnitudo > min_magnitude nell'intervallo di tempo specificato
        
        TIME OPTIONS                    MAGNITUDE OPTIONS
        1 = Ultimi 7 giorni             1 = Magnitudo 2+
        2 = Ultimi 30 giorni            2 = Magnitudo 3+
        3 = Ultimi 90 giorni            3 = Magnitudo 4+
        4 = Ultimi 365 giorni           4 = Magnitudo 5.5+
        5 = Dal 1985-01-01              0 = Tutte le magnitudo
        """
        try:
            self.driver.get(self.url) # apre la pagina terremoti di INGV
            
            time_dropdown = self.wait.until(EC.element_to_be_clickable((By.ID, "dropdown_last_nd")))
            time_dropdown.click() # apre il menù dropdown per selezionare l'intervallo temporale

            time_menu = self.driver.find_element(By.XPATH, '//*[@id="totop"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/ul')

            time_options = time_menu.find_elements(By.CLASS_NAME, "btn.btn-margin-bottom ")

            time_urls = []

            for option in time_options:
                href = option.get_attribute("href") # salva il link se le opzioni lo presentano

                if href:
                    time_urls.append(href)

            # print(time_urls)

            match time_option: # seleziona il percorso in base all'attributo di tempo passato alla funzione
                case 1:
                    print("Selezionato filtro 'Ultimi 7 giorni'")
                    self.driver.get(time_urls[0])
                case 2:
                    print("Selezionato filtro 'Ultimi 30 giorni'")
                    self.driver.get(time_urls[1])
                case 3:
                    print("Selezionato filtro 'Ultimi 90 giorni'")   
                    self.driver.get(time_urls[2])
                case 4:
                    print("Selezionato filtro 'Ultimi 365 giorni'")
                    self.driver.get(time_urls[3])
                case 5:
                    print("Selezionato filtro 'Dal 1985-01-01'")
                    self.driver.get(time_urls[4])

            time.sleep(2)

            magnitude_dropdown = self.driver.find_element(By.ID, "dropdown_magnitudo")
            magnitude_dropdown.click() # apre il menù dropdown per selezionare la magnitudine minima

            magnitude_menu = self.driver.find_element(By.XPATH, '//*[@id="totop"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/ul')

            magnitude_options = magnitude_menu.find_elements(By.CLASS_NAME, "btn.btn-margin-bottom ")

            magnitude_urls = []

            for option in magnitude_options:
                href = option.get_attribute("href")

                if href:
                    magnitude_urls.append(href)
            
            match min_magnitude:
                case 0:
                    print("Selezionato filtro 'Tutte le magnitudo'")
                    self.driver.get(magnitude_urls[0])
                case 1:
                    print("Selezionato filtro 'Magnitudo 2+'")
                    self.driver.get(magnitude_urls[1])
                case 2:
                    print("Selezionato filtro 'Magnitudo 3+'")   
                    self.driver.get(magnitude_urls[2])
                case 3:
                    print("Selezionato filtro 'Magnitudo 4+'")
                    self.driver.get(magnitude_urls[3])
                case 4:
                    print("Selezionato filtro 'Magnitudo 5.5+'")
                    self.driver.get(magnitude_urls[4])
            
            time.sleep(5)


        except Exception as e:
            print(f"Errore durante l'apertura della pagina: {e}")

        finally:
            self.driver.quit()