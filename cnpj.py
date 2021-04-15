import pyautogui as pyg
import requests as http

class CNPJ:

	def __init__(self):
		self.__cnpj = pyg.prompt('Digite o Nº do CNPJ que você deseja consultar (14 dígitos, sem (. / ou -)')

	def valida(self):
		if (not len(self.__cnpj) == 14):
			pyg.alert('Por favor, digite um número de CNPJ válido!')
			self.__cnpj = None
			exit()
		else:
			return self.__cnpj

	def demonstra(self, link):
		#O parâmetro link é um objeto json
		texto = link.json()
		pyg.alert(f"O cnpj informado pertence a empresa: {texto['nome']}"
			f" Nome fantasia: {texto['fantasia']}"
			f" Capital Social: {texto['capital_social']}"
			f" Ultima atualização do CNPJ: {texto['ultima_atualizacao']}"
			f" O caiptal é composto por: {texto['qsa']}")

	def consulta(self):
		api = http.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(self.valida()))
		status = api.json()['status']
		if (status == 'ERROR'):
			pyg.alert('O CNPJ informado é invalido!')
		else:
			return self.demonstra(api)#Passa como parâmetro um objeto Json

teste = CNPJ()
teste.consulta()