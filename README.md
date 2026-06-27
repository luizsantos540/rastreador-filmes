# 🎬 Movie Tracker & Streaming Finder / Rastreador de Filmes e Localizador de Streaming

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Playwright-Automated-green.svg" alt="Playwright">
  <img src="https://img.shields.io/badge/BeautifulSoup-4-orange.svg" alt="BeautifulSoup">
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen.svg" alt="Status">
</p>

---

### 🌐 Language / Idioma
* [Read in English (Default)](#english-version)
* [Ler em Português](#versão-em-português)

---

## English Version

### 📄 Description
An automated web scraper built in Python that captures the top 5 trending movies from **IMDb** and dynamically cross-references them with **JustWatch** to find which streaming platforms (Netflix, Prime Video, Disney+, etc.) they are currently available on in Brazil. 

To bypass aggressive anti-bot protections, the script uses **Playwright** to simulate a real browser environment, waiting for the structural DOM to load (`domcontentloaded`) instead of heavy background tracking scripts, ensuring speed and reliability.

### 🛠️ Technologies
* **Python 3**
* **Playwright** (Browser Automation)
* **BeautifulSoup4** (HTML Parsing)
* **JSON** (Internal Data Extraction)

### 🚀 How to Run

#### Prerequisites
Ensure you have **Python 3.8+** installed on your system.

#### 1. Clone the Repository
```bash
git clone [https://github.com/luizsantos540/rastreador_filmes.git](https://github.com/luizsantos540/rastreador_filmes.git)
cd rastreador_filmes
2. Setup Virtual Environment
Bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Linux/macOS
source venv/bin/activate
3. Install Dependencies
Bash
pip install playwright beautifulsoup4
4. Install Playwright Browsers
Bash
python -m playwright install chromium
5. Run the Script
Bash
python main.py
🧠 Architecture Details
Resilience: Instead of relying on CSS classes that change constantly, the script targets the internal script tag __NEXT_DATA__ on IMDb to extract pure structured JSON.

Timeout Fix: Uses wait_until="domcontentloaded" to bypass endless analytics and ads scripts that usually trigger TimeoutError in standard automation.

 Português
📄 Descrição
Um web scraper automatizado desenvolvido em Python que captura os 5 principais filmes em alta no IMDb e cruza esses dados dinamicamente com o JustWatch para descobrir em quais plataformas de streaming (Netflix, Prime Video, Disney+, etc.) eles estão disponíveis no Brasil.

Para burlar proteções agressivas contra robôs, o script utiliza o Playwright para simular um navegador real, aguardando o carregamento estrutural do DOM (domcontentloaded) em vez de scripts pesados de rastreamento em segundo plano, garantindo velocidade e confiabilidade.

🛠️ Tecnologias
Python 3

Playwright (Automação de Navegador)

BeautifulSoup4 (Extração de Dados HTML)

JSON (Extração de Dados Estruturados)

🚀 Como Executar
Pré-requisitos
Certifique-se de ter o Python 3.8+ instalado no seu sistema.

1. Clonar o Repositório
Bash
git clone [https://github.com/luizsantos540/rastreador_filmes.git](https://github.com/luizsantos540/rastreador_filmes.git)
cd rastreador_filmes
2. Configurar o Ambiente Virtual
Bash
python -m venv venv
# No Windows
venv\Scripts\activate
# No Linux/macOS
source venv/bin/activate
3. Instalar Dependências
Bash
pip install playwright beautifulsoup4
4. Instalar os Navegadores do Playwright
Bash
python -m playwright install chromium
5. Executar o Script
Bash
python main.py
🧠 Detalhes de Arquitetura
Resiliência: Em vez de depender de classes CSS que mudam constantemente, o script alveja a tag de script interna __NEXT_DATA__ do IMDb para extrair JSON estruturado puro.

Correção de Timeout: Utiliza wait_until="domcontentloaded" para ignorar scripts infinitos de analytics e anúncios que costumam disparar TimeoutError em automações comuns.

📊 Sample Output / Exemplo de Saída
Plaintext
Iniciando navegador automatizado...
Acessando o IMDb para coletar os filmes em alta...

--- TOP 5 FILMES + ONDE ASSISTIR ---
Cruzando dados com o JustWatch em tempo real...

Buscando: Inside Out 2...
1. Inside Out 2
   ⭐ Nota IMDb: 7.9
   📺 Onde assistir: Disney Plus

Buscando: Furiosa: A Mad Max Saga...
2. Furiosa: A Mad Max Saga
   ⭐ Nota IMDb: 7.6
   📺 Onde assistir: Max, Prime Video