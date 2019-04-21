# DropsBot

Bot para RagnarokOnline usando processamento de imagem e simulação de clicks para jogar como se fosse um player.
Para conseguir gerar eventos visíveis para outros processos, você precisa rodar os script como administrador.

## Versão do Python: 3.6.6 (tensorflow não suporta 3.7)

## Windows Low Level API:

  - Windows API Index: https://docs.microsoft.com/en-us/windows/desktop/apiindex/windows-api-list
  - winuser.h: https://docs.microsoft.com/en-us/windows/desktop/api/winuser/
  - ctype.h: https://docs.python.org/3/library/ctypes.html
  - pywin32 (Windows API binding for python): http://timgolden.me.uk/pywin32-docs/contents.html

## TODO Tesseract
## TODO Tensorflow
## TODO GRFTool
## Sprites data
http://rosprites.blogspot.com/2009/10/if-you-cant-access-110mbcom-website.html

## Virtual Enviroment

Você pode criar um ambiente virtual de python para desenvolver e rodar o bot num ambiente limpo. Para criar o ambiente virtual, crie uma pasta na raíz do projeto chamada `virtual_env` e rode `python -m venv virtual_env`. Para ativar o ambiente virtual, entre na pasta do embiente e rode `.\Scripts\activate`. Para desativar, rode `.\Scripts\deactivate.bat`.

## Roadmap (em ordem de prioridade)
   
  - Tirar screenshots da janela do jogo a cada X frames
  - Conseguir uma bounding box nas janelas de UI do rag
  - Conseguir identificar qual janela é qual
  - Implementar evento de mouse wheel scroll up/down
  - Ler eventos de teclado para (des)pausar o bot (como ele cria eventos de mouse, fica impossível de usar o mouse normalmente enquanto o bot roda)
  - Manipular janela de itens
    * Mover entre consumíveis, equipamentos e misc
    * Scroll up & down
  - Extrair informações:
    * HP
    * SP
    * Zeny
    * Peso
    * Quantidade de itens no inventório
    * Classe
    * Munição
    * Consumíveis
    * Buffs
    * Debuffs
  - Manipular storage
    * Conseguir abrir storage primário e secundário
    * Extrair informação da quantidade de itens armazenados
    * Mover itens entre inventório e storage
    * Usar @restock
  - Implementar @autoloot e @alootid
  - Identificar e construir bounding box nos mobs
    * Precisa identificar qual mob é qual
      - Montar uma rede neural convolucional no TensorFlow
      - Preparar dataset
        * Extrair sprites do rag
        * Gerar sprites RGB e grayscale para todos os mobs

    * Usar skills
      - Buffs
      - Ataques single target
      - Ataques AoE
      - Teleporte
    * Talvez implementar mobar
    * Arquivo de configuração com alguns behaviours
      - Lista de skills (com atalhos); também dá para colocar consumíveis
      - Quais consumíveis usar (talvez só configurar os atalhos)
    * __Precisa achar uma forma de lidar com hallucination! Quando a tela inverte, a posição do sprite não é a mesma posição que o mob realmente está, isso precisa ser tratado (seja usando Royal Jelly ou colocando uma correção na posição y do mouse)__
  - Implementar mapas e waypoints
    * Extrair informações de coordenadas embaixo do minimap ou do /where
    * Talvez criar uma nova aba de chat com tudo desligado para conseguir informações de comandos (tipo /where)
    * Arquivos de configuração de waypoints por mapa
  - Vender itens?
    * Identificar os itens antes de vender?
    * NÃO VENDER ANÉIS DE MORAAAAA
    * não vender itens de 10z?
    * Trocar de personagem para vender?
    * ou deixa isso pro player se virar?

