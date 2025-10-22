# 🧪 Automação de Testes com Pytest — Exemplo Login

## 🎯 Objetivo

Este projeto é um **exemplo didático de automação de testes**, demonstrando o fluxo completo de criação, execução e registro de resultados de testes automatizados.
O foco é em **casos de teste de login**, cobrindo cenários positivos e negativos, seguindo boas práticas de automação.

O projeto atende à solicitação da **Invent Software**, mostrando:

* Automação de testes com **Python** e **Selenium**
* Estrutura de testes organizada com **Pytest** e **Pytest-BDD**
* Geração de **relatórios HTML** para visualização dos resultados
* Execução **local** e em **CI/CD (GitHub Actions)**

## 🛠 Tecnologias Utilizadas

* **Python 3.11+**
* **Pytest** — Framework de testes
* **Pytest-BDD** — Suporte a testes BDD (Gherkin)
* **Selenium** — Automação de navegadores
* **Webdriver Manager** — Gerenciamento automático do ChromeDriver
* **Faker** — Dados falsos para testes
* **Pytest-HTML** — Relatórios em HTML

## ⚙️ Pré-requisitos

* Python 3.11+ instalado
* Google Chrome instalado (para execução local)
* Clonar o repositório:

```bash
git clone <url-do-repositorio>
cd automacao_login_pytest
```

## 📦 Instalação

Instalar todas as dependências do projeto:

```bash
pip install -r requirements.txt
```

> **Observação:** `selenium` e `webdriver-manager` são necessários para executar testes de interface web.

## 🗂 Estrutura do Projeto

```
automacao_login_pytest/
├─ features/           # Arquivos .feature (cenários BDD)
├─ pages/              # Page Objects (LoginPage)
├─ tests/              # Scripts de testes
├─ reports/            # Relatórios gerados pelo Pytest
├─ requirements.txt    # Dependências do projeto
├─ README.md
```

## ▶️ Como Executar

### 💻 Local

Abrir terminal na pasta do projeto e executar testes:

```bash
pytest --html=reports/report.html --self-contained-html -v
```

O relatório será gerado em: `reports/report.html`

### 🌐 CI/CD (GitHub Actions)

* Testes configurados para rodar automaticamente ao dar push ou abrir pull request na branch `main`
* Executados em **headless Chrome**
* Relatório HTML gerado como **artifact**

## ✅ Casos de Teste Cobertos

* Login válido (positivo)
* Login com usuário inválido
* Login com senha inválida
* Login com usuário vazio
* Login com senha vazia

## 📊 Visualização do Resultado

* Relatório HTML detalhado (`reports/report.html`)
* Indica testes **passados**, **falhados** e logs do Selenium

## 🚀 Próximos Passos / Evolução

* Adicionar mais páginas e fluxos de teste
* Integração com outros navegadores (Firefox, Edge)
* Executar testes em **paralelismo**
* Gravar vídeo mostrando **execução** e **relatório**