from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import json
import time

def buscar_streaming_no_justwatch(pagina, titulo_filme):
    try:
        url_busca = f"https://www.justwatch.com/br/busca?q={titulo_filme.replace(' ', '%20')}"
        
        # Mudado para domcontentloaded para não travar com scripts lentos de terceiros
        pagina.goto(url_busca, wait_until="domcontentloaded")
        
        # Espera o container de resultados aparecer na tela
        pagina.wait_for_selector(".title-list-row__offers", timeout=5000)
        
        html_busca = pagina.content()
        soup_busca = BeautifulSoup(html_busca, "html.parser")
        
        provedores = soup_busca.find_all("img", class_="provider-icon")
        if not provedores:
            cartao_filme = soup_busca.find("div", class_="title-list-row__offers")
            if cartao_filme:
                provedores = cartao_filme.find_all("img")
        
        plataformas = []
        for prov in provedores:
            nome_plataforma = prov.get("alt", "").strip()
            if nome_plataforma and nome_plataforma not in plataformas:
                if json.dumps(nome_plataforma).lower() not in ["compra", "aluguel", "cinema"]:
                    plataformas.append(nome_plataforma)
                    
        if plataformas:
            return ", ".join(plataformas[:3])
            
        return "Disponível apenas para Aluguel/Compra ou Não listado"
        
    except Exception:
        return "Disponível apenas para Aluguel/Compra ou Não listado"

def executar_rastreador():
    print("Iniciando navegador automatizado...")
    
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=True)
        pagina = navegador.new_page(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        
        print("Acessando o IMDb para coletar os filmes em alta...")
        # CORREÇÃO AQUI: Mudado para domcontentloaded
        pagina.goto("https://www.imdb.com/chart/moviemeter/", wait_until="domcontentloaded")
        
        # Em vez de esperar a rede, esperamos especificamente a tag principal que segura a lista aparecer
        pagina.wait_for_selector("main", timeout=10000)
        
        html_imdb = pagina.content()
        soup_imdb = BeautifulSoup(html_imdb, "html.parser")
        script_dados = soup_imdb.find("script", id="__NEXT_DATA__")
        
        if not script_dados:
            print("Erro: Não foi possível ler os dados do IMDb.")
            navegador.close()
            return

        try:
            dados_json = json.loads(script_dados.string)
            lista_filmes = dados_json["props"]["pageProps"]["pageData"]["chartTitles"]["edges"]
            
            print(f"\n--- TOP 5 FILMES + ONDE ASSISTIR ---")
            print("Cruzando dados com o JustWatch em tempo real...\n")
            
            for i, item in enumerate(lista_filmes[:5], start=1):
                filme = item["node"]
                titulo = filme["titleText"]["text"]
                
                try:
                    nota = filme["ratingsSummary"]["aggregateRating"]
                    nota = str(nota) if nota else "Sem nota"
                except:
                    nota = "Sem nota"
                
                print(f"Buscando: {titulo}...")
                streaming = buscar_streaming_no_justwatch(pagina, titulo)
                
                print(f"{i}. {titulo}")
                print(f"   ⭐ Nota IMDb: {nota}")
                print(f"   📺 Onde assistir: {streaming}\n")
                
        except Exception as e:
            print(f"Erro ao processar a lista: {e}")
            
        navegador.close()

if __name__ == "__main__":
    executar_rastreador()