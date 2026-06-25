from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import json

def extrair_tendencias_imdb():
    print("Iniciando navegador automatizado...")
    
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=True)
        pagina = navegador.new_page(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        
        print("Acessando o IMDb de forma realista...")
        pagina.goto("https://www.imdb.com/chart/moviemeter/", wait_until="networkidle")
        
        # Aguarda que a estrutura principal da página esteja visível
        pagina.wait_for_selector("main")
        
        html_da_pagina = pagina.content()
        navegador.close()
        
    soup = BeautifulSoup(html_da_pagina, "html.parser")
    
    # Buscando a tag de dados brutos que o IMDb usa
    script_dados = soup.find("script", id="__NEXT_DATA__")
    
    if not script_dados:
        print("Erro: Não foi possível mapear os dados do IMDb. Tentando método alternativo...")
        # Fallback rápido buscando por tags h3 genéricas de títulos caso o JSON falhe
        titulos = soup.find_all("h3", class_=lambda x: x and "title" in x.lower())
        if titulos:
            print(f"\n--- TOP 10 FILMES MAIS POPULARES NO IMDB (Método 2) ---\n")
            for i, t in enumerate(titulos[:10], start=1):
                print(f"{i}. {t.text.strip()}")
        else:
            print("Layout completamente protegido ou modificado.")
        return

    print(f"\n--- TOP 10 FILMES MAIS POPULARES NO IMDB ---\n")
    
    try:
        # Transforma o texto do script em um dicionário Python útil
        dados_json = json.loads(script_dados.string)
        
        # Navega pela estrutura do JSON do IMDb para encontrar a lista de filmes
        lista_filmes = dados_json["props"]["pageProps"]["pageData"]["chartTitles"]["edges"]
        
        for i, item in enumerate(lista_filmes[:10], start=1):
            filme = item["node"]
            titulo = filme["titleText"]["text"]
            
            # Tenta buscar a nota dentro do objeto de avaliações
            try:
                nota = filme["ratingsSummary"]["aggregateRating"]
                nota = str(nota) if nota else "Sem nota"
            except:
                nota = "Sem nota"
                
            print(f"{i}. {titulo} | Nota: {nota}")
            
    except Exception as e:
        print(f"Erro ao processar os dados estruturados: {e}")

if __name__ == "__main__":
    extrair_tendencias_imdb()