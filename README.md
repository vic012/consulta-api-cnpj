Um script python para consumir a Api p�blica da Receita para consulta do Cart�o CNPJ
Como funciona:
Baixe o m�dulo "cnpj.py" no seu pc. Exceute-o com o python:

Voc� pode selecionar quais informa��es ser�o mostradas, para isso: Abra o m�dulo "cnpj.py" com um editor de texto o m�todo(pyg.alert) dentro da fun��o "demonstra(self)", altere dentro da propriedade {texto['O campo que deseja exibir a informa��o']}, por exemplo: {texto['nome']} Que mostrar� o nome da empresa.

Aten��o, o script usa duas bibliotecas:
1)PyAutogui; 2)Requests;

Voc� vai precisar instalar elas em seu PC:

Instalando pelo PIP:
1)PyAutogui: pip install pyautogui

Para mais detalhes consulte https://pypi.org/project/PyAutoGUI/

2)Requests: pip install requests

Para mais detalhes consulte https://pypi.org/project/requests/

Vers�o do python: 3.7.2