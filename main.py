from utils import *
from mensagemwpp import *
from mensagemwpp import nave
import pandas as pd
from publico_rotacao import *

#agenda
caminhoagenda = 'Agenda com carteira.xlsx'
agenda = pd.read_excel(caminhoagenda)
agenda_tratada = tratarcontatos(agenda)
agenda_tratada['MCI'] = agenda_tratada['MCI'].astype(int).astype(str)

agenda_tratada
####################

#tratamento do Público para camanhas de crédito

campanha_sel = 'Portabilidade / 04. Endividamento Selic alta (Consig) (18,1%)'
pub = pub_732('rels/relatorio-732.xlsx', campanha_sel)
#####################
pub = rotacionar_peso2('rels/relatorio-2914.xlsx')

#####################
pub = sd_conta_25k('rels/relatorio-2104.xlsx')

pub = [str(pub) for pub in pub]
pub

jarotacionados = ['916928354', '913253923', '506096320', '910799049', '106733911', '927465161']

for i in jarotacionados:
    pub.remove(i)
    
publico_df = agenda_tratada[agenda_tratada['MCI'].isin(pub)] # filtrar em y['mci'] os dados que estão em x
publico_df.drop_duplicates(subset=['MCI'], inplace=True, keep='first') # tirando as duplicadas e mantendo a primeira ocorrencia achada

mcis_atualizar = publico_sem_agenda(agenda_tratada, pub)
print('Os Mcis qe não constam na agendasão os seguintes:')
for i in mcis_atualizar:
    print(i)

publico_df.to_excel('publico para envio.xlsx')

##############################
print(f'o público para envio serão: {publico_df}')
print(f'que são {len(publico_df)} do total de {len(pub)}, faltando cadastrar {len(mcis_atualizar)}' )


##############################
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

########################
'''
# para rodar teste => com data frame com apenas os meus dados

colunas_teste = ['MCI', 'nome', 'Telefone']
teste = pd.DataFrame(columns=colunas_teste)
cassio = [{'MCI':'30', 'nome':'Gemacão','Telefone':'5596981316611', 'MCI':'2'},{'MCI':'30', 'nome':'Gemacão','Telefone':'5596981316611', 'MCI':'2'}]
teste = teste.append(cassio, ignore_index=True)
teste
'''



