from utils import *
from mensagemwpp import *
from mensagemwpp import nave
import pandas as pd
from publico_rotacao import *






############################## Mensagem e envio pela classe ################################
msg = """ 



"""


servico = ChromeService(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
navegador = webdriver.Chrome(service=servico, options=options)
navegador.implicitly_wait(20)
naveg = nave(navegador)

naveg.Modulo_wpp()

envios, erros = naveg.Enviar_mensagens(publico_df,msg) #inclui o instanciamento para tentar o retorno dos erros e dos envios

envios
erros
