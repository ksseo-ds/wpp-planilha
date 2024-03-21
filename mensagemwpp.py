import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib.parse
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm
from random import randint

class nave:
    def __init__(self,navegador):
        
        self.navegador = navegador

    def Modulo_wpp(self): 
        
#        servico = ChromeService(ChromeDriverManager().install())
#        options = webdriver.ChromeOptions()
#       navegador = webdriver.Chrome(service=servico, options=options)  # Use o ChromeDriverManager para inicializar o driver do Chrome
        
        time.sleep(3)
        self.navegador.get("https://web.whatsapp.com/")
        
        return self.navegador
        
    def Enviar_mensagens(self,contatos_df, mensagem):   
        contatos_df.reset_index(drop=True, inplace=True)
        enviados = []
        erros = []
        for i, Cod_Cliente in enumerate(tqdm(contatos_df['Cod_Cliente'])):
            try:
                sleeprange = randint(19,33)
                pessoa = contatos_df.loc[i, "nome"]
                numero = contatos_df.loc[i, "Telefone"]
                texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
                link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"

                self.navegador.get(link)
                time.sleep(sleeprange)

                # Aguarde até que o campo de entrada de mensagem seja visível
                mensagem_input = WebDriverWait(self.navegador, 10).until(
                    EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span'))
                )
                mensagem_input.send_keys(Keys.ENTER)
                enviados.append(Cod_cliente) # criando lista de enviados 30/10/2023
                time.sleep(3)
                
        
            except Exception as e:
                erros.append(Cod_cliente) # criando lista de erros de envio 30/10/2023
                print(f"Erro ao enviar mensagem para {pessoa}: {str(e)}")
                continue
        return enviados, erros
    
    def testee(navegador):
        link = 'www.google.com'
        navegador.get(link)
