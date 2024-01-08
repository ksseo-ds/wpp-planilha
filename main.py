from utils import *
from mensagemwpp import *
from mensagemwpp import nave
import pandas as pd
from publico_rotacao import *






############################## Mensagem e envio pela classe ################################
msg = """ Boa Dia, Cássio teu gerente de relacionamento do BB falando.

Estava verificando que possui algumas operações de consignado, no BB e fora, e provavelmente com uma taxa mais alta que a que comercializamos hoje, e existe uma chance boa de conseguir um troco na renovação, e ainda baixar a taxa um pouco.

Vamos fazer uma simulação de portabilidade ou de renovação ?



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
