# Calculadora de `Fração geratriz`!
Este é um projeto em Python que recebe uma dízima periódica qualquer e retorna para o usuário qual a fração geratriz da dízima!

## Como utilizar a partir do código fonte?
- Este repositório possui o código fonte necessário para rodar a aplicação.
- Se deseja utilizar no "prompt de comando" de qualquer IDE de sua preferência, basta copiar o código e colar lá!
- Se deseja utilizar a partir de um executável, é necessário seguir os seguintes passos:
    - Copiar o código fonte (ou baixar o arquivo `decimal_to_fraction.py`)
    - Baixar a biblioteca `pyinstaller` caso você não possua:
       
       ```
       pip install pyinstaller
       ```
       
    - Abrir a pasta em que o arquivo `decimal_to_fraction.py` está localizado e executar o seguinte comando:
       
       ```
       pyinstaller --onefile <nome do arquivo que contém o código fonte>.py
       ```
       
    - Abrir a pasta `dist` que foi criada
    - Executar o programa!

## Como utilizar a partir do executável?
- Basta abrir a pasta `dist`
- Executar o `decimal_to_fraction.exe`
