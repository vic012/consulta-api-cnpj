Um script python para consumir a Api pública da Receita para consulta do Cartão CNPJ
Como funciona:
Baixe o módulo "cnpj.py" no seu pc. Exceute-o com o python:

Você pode selecionar quais informações serão mostradas, para isso: Abra o módulo "cnpj.py" com um editor de texto o método(pyg.alert) dentro da função "demonstra(self)", altere dentro da propriedade {texto['O campo que deseja exibir a informação']}, por exemplo: {texto['nome']} Que mostrará o nome da empresa.

Atenção, o script usa duas bibliotecas:
1)PyAutogui; 2)Requests;

Você vai precisar instalar elas em seu PC:

Instalando pelo PIP:
1)PyAutogui: pip install pyautogui

Para mais detalhes consulte https://pypi.org/project/PyAutoGUI/

2)Requests: pip install requests

Para mais detalhes consulte https://pypi.org/project/requests/

Versão do python: 3.7.2