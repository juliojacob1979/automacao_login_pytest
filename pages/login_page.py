# pages/login_page.py

from selenium.webdriver.common.by import By
import time

class LoginPage:
    URL = "https://practicetestautomation.com/practice-test-login/"

    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON = (By.ID, "submit")
    ERROR_MESSAGE = (By.ID, "error")
    SUCCESS_MESSAGE = (By.TAG_NAME, "h1")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        # Preenche usuário
        self.driver.find_element(*self.USERNAME_INPUT).clear()
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        time.sleep(1)  # pausa para visualização

        # Preenche senha
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        time.sleep(1)  # pausa para visualização

        # Clica em submit
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
        time.sleep(1)

        # Scrolla para a mensagem de erro ou sucesso
        self.scroll_to_result()
        time.sleep(2)  # pausa para visualização da mensagem

    def scroll_to_result(self):
        try:
            # Prioriza scroll até mensagem de erro ou sucesso
            element = None
            try:
                element = self.driver.find_element(*self.ERROR_MESSAGE)
            except:
                element = self.driver.find_element(*self.SUCCESS_MESSAGE)

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});", element
            )
        except:
            pass  # se não encontrar nenhum, ignora

    def get_error_message(self):
        try:
            return self.driver.find_element(*self.ERROR_MESSAGE).text
        except:
            return ""

    def get_success_message(self):
        try:
            return self.driver.find_element(*self.SUCCESS_MESSAGE).text
        except:
            return ""