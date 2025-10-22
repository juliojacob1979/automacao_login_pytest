# tests/test_login.py

import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage

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


# ---------- Testes Positivos ----------
@pytest.mark.positivo
def test_login_sucesso(driver_setup):
    page = LoginPage(driver_setup)
    page.load()
    page.login("student", "Password123")
    assert "Logged In Successfully" in page.get_success_message()


# ---------- Testes Negativos ----------
@pytest.mark.negativo
def test_login_usuario_invalido(driver_setup):
    page = LoginPage(driver_setup)
    page.load()
    page.login("invalid_user", "Password123")
    assert "Your username is invalid!" in page.get_error_message()


@pytest.mark.negativo
def test_login_senha_invalida(driver_setup):
    page = LoginPage(driver_setup)
    page.load()
    page.login("student", "wrongpass")
    assert "Your password is invalid!" in page.get_error_message()


@pytest.mark.negativo
def test_login_usuario_vazio(driver_setup):
    page = LoginPage(driver_setup)
    page.load()
    page.login("", "Password123")
    assert "Your username is invalid!" in page.get_error_message()


@pytest.mark.negativo
def test_login_senha_vazia(driver_setup):
    page = LoginPage(driver_setup)
    page.load()
    page.login("student", "")
    assert "Your password is invalid!" in page.get_error_message()



        