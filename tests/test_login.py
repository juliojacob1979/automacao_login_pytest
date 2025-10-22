# tests/test_login.py

import os
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pytest_bdd import scenarios, given, when, then, parsers

# Conecta o arquivo feature
scenarios('../features/login.feature')

# Fixture para abrir/fechar o navegador
@pytest.fixture
def driver_setup():
    # Configurações do Chrome
    chrome_options = Options()
    
    # Se estiver rodando no GitHub Actions
    if os.environ.get("CI") == "true":
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-gpu")
    else:
        # Local: Chrome normal
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    
    # Inicializa o driver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    
    yield driver
    driver.quit()


# ---------- Fixture da página ----------
@pytest.fixture
def login_page(driver_setup):
    page = LoginPage(driver_setup)
    page.load()
    return page

# ---------- Steps ----------
@given("que o usuario esta na pagina de login")
def step_given_login_page(login_page):
    # Só chama a fixture, não precisa retornar nada
    pass

@when(parsers.cfparse('ele informa usuario "{usuario}" e senha "{senha}"'))
def step_when_login(login_page, usuario, senha):
    # Converte "<vazio>" para string vazia
    if usuario == "<vazio>":
        usuario = ""
    if senha == "<vazio>":
        senha = ""
    login_page.login(usuario, senha)

@then(parsers.parse('ele deve ver a mensagem de sucesso "{mensagem}"'))
def step_then_sucesso(login_page, mensagem):
    assert mensagem in login_page.get_success_message()

@then(parsers.parse('ele deve ver a mensagem de erro "{mensagem}"'))
def step_then_erro(login_page, mensagem):
    assert mensagem in login_page.get_error_message()



        