import time
from typing import List, Tuple
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BrowserManager:

  @staticmethod
  def install_driver() -> webdriver.Chrome:
    """
        Install and return a Chrome WebDriver.

        Returns:
        - webdriver.Chrome: The Selenium WebDriver for Chrome.
        """
    # Note: The executable_path parameter is unnecessary in this context.
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service)

  @staticmethod
  def login_codata(driver: webdriver, login: Tuple[str, str]) -> None:
    """
            Logs into the Codata website.

            Parameters:
            - driver (WebDriver): The Selenium WebDriver.
            - login (Tuple[str, str]): A tuple containing the username and password.

            Usage:
            ```python
            driver = BrowserManager.install_driver()
            BrowserManager.login_codata(driver, ("your_username", "your_password"))
            ```

            Note:
            Make sure to replace "your_username" and "your_password" with actual login credentials.
            """
    codata_url = "https://apx.sead.pb.gov.br/SEADApxPrd/hostLogin.jsp"
    driver.get(codata_url)

    driver.find_element(By.XPATH, '//*[@id="GXUser"]').send_keys(login[0])

    driver.find_element(By.XPATH, '//*[@id="GXPassword"]').send_keys(login[1])

    driver.find_element(By.XPATH, '//*[@id="GXLoginBtn"]').click()

  @staticmethod
  def login_srh(driver: webdriver, login: Tuple[str, str]):
    wait = WebDriverWait(driver, 10)

    frames = wait.until(
        EC.presence_of_all_elements_located((By.TAG_NAME, 'frame')))

    driver.switch_to.frame(frames[1])
    srh = wait.until(EC.element_to_be_clickable((By.ID, 'POS581')))
    srh.send_keys('X')
    srh.send_keys(Keys.ENTER)

    driver.switch_to.default_content()  # Switch back to the default content
    driver.switch_to.frame(frames[0])

    # Add an explicit wait for elements inside the frame if needed
    wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*')))
    driver.find_element(By.NAME, 'POS1492').send_keys(login[0])
    srh = driver.find_element(By.NAME, 'POS1572')
    srh.send_keys(login[1])
    srh.send_keys(Keys.ENTER)

    driver.switch_to.default_content()
    driver.switch_to.frame(frames[1])
    wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*')))
    srh = driver.find_element(By.ID, 'POS1403')
    srh.send_keys('01')
    srh.send_keys(Keys.ENTER)

    driver.switch_to.default_content()
    driver.switch_to.frame(frames[0])
    wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*')))
    srh = driver.find_element(By.ID, 'POS1228')
    srh.send_keys('01')
    srh.send_keys(Keys.ENTER)

    driver.switch_to.default_content()
    driver.switch_to.frame(frames[1])
    wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*')))
    srh = driver.find_element(By.ID, 'POS1643')
    srh.send_keys('01')
    srh.send_keys(Keys.ENTER)

    driver.switch_to.default_content()
    driver.switch_to.frame(frames[0])
    wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*')))
    srh = driver.find_element(By.ID, 'POS1152')
    srh.send_keys('02')
    srh.send_keys(Keys.ENTER)

  @staticmethod
  def search_matricula(driver: webdriver, matricula: str):
    try:
      wait = WebDriverWait(driver, 10)
      driver.switch_to.default_content()
      frames = wait.until(
          EC.presence_of_all_elements_located((By.TAG_NAME, 'frame')))

      driver.switch_to.frame(frames[1])

      srh = wait.until(EC.element_to_be_clickable((By.ID, 'POS1631')))
      srh.send_keys('02')
      srh = driver.find_element(By.NAME, 'POS1646')
      time.sleep(1)
      srh.send_keys(matricula)
      srh.send_keys(Keys.ENTER)

    except Exception as e:
      print(f"An error occurred in search_matricula: {e}")

  @staticmethod
  def get_data(driver: webdriver, data: List[str]):
    try:
      wait = WebDriverWait(driver, 10)
      driver.switch_to.default_content()
      frames = wait.until(
          EC.presence_of_all_elements_located((By.TAG_NAME, 'frame')))
      driver.switch_to.frame(frames[0])

      srh = wait.until(EC.element_to_be_clickable((By.ID, 'POS597')))
      regime = "COMISSIONADO"
      sexo = srh.text
      jornada_de_trabalho = "8 HORAS / DIA"
      trbalho_noturno = "NÃO"
      atividade_insalubre = "NÃO"
      grau_insalubre = "NÃO"
      cpf = driver.find_element(By.ID,
                                'POS896').text.replace(".",
                                                       "").replace("-", "")
      rg = driver.find_element(By.ID, 'POS666').text.rstrip()
      pasep = driver.find_element(By.ID, 'POS923').text
      time.sleep(0.5)
      ActionChains(driver).send_keys(Keys.RETURN).perform()

      driver.switch_to.default_content()
      driver.switch_to.frame(frames[1])
      data_admissao = driver.find_element(By.ID,
                                          'POS1102').text.replace("/",
                                                                  "").rstrip()

      driver.switch_to.default_content()
      driver.switch_to.frame(frames[0])
      ActionChains(driver).send_keys(Keys.RETURN).perform()

      driver.switch_to.default_content()
      driver.switch_to.frame(frames[1])
      ActionChains(driver).send_keys(Keys.RETURN).perform()

      data.extend(
          (regime, sexo, jornada_de_trabalho, trbalho_noturno,
           atividade_insalubre, grau_insalubre, cpf, rg, pasep, data_admissao))
      time.sleep(0.5)
    except Exception as e:
      print(f"An error occurred in get_data: {e}")

  @staticmethod
  def close_driver(driver):
    driver.quit()
