# PIBIC - AVALIAÇÕES DAS PROPRIEDADES FÍSICAS DA MASSA E DE PÃES ELABORADOS COM ADIÇÃO DE FARINHAS DE BIOMASSA DE BANANA E DE SOJA

### Grande área de conhecimento: Ciências Exatas e dda Terra

### Subárea do conhecimento: Química

### Orientado: Vitor Kauã Oliveira de Souza, Segundo ano de Ciência da Computação, Universidade Estadual do Norte do Paraná

### Orientador: Professor Doutor Luís Guilherme Sachs

### 11,30,2023
---

## Documentação 

#### O seguinte arquivo se trata da documentação da implementação de um analizador de cluster de imagens de fatias de pães.

### 1. As imagens

#### As imagens para analise foram obtidas a partir da elaboração dos pães propriamente ditos e após a sua realização, uma fatia horizontal é retirada.

#### Essa fatia é escaneada e pelo próprio software na impressora/ scanner é realizada uma correção de brilho, saturação e contraste.

#### Essa correção é realizada a fim de facilitar a analise propriamente dita, que será explicada posteriormente.

### 1.1 A análise

#### A analise propriamente dita é realizada em partes:

#### - Obtenção da imagem a ser analisada(scanner);
#### - Correção da imagem(software do scanner);
#### - Trichute (binarização dos dados e cores);
#### - Obtenção da imagem preta e branca;
#### - Obtenção de uma imagem com os clusters visiveis;
#### - Contagem e analise dos clusters;

#### O trichute é realizado a partir de que, os clusters possuem, em média uma coloração mais escura o resto do pão. Dessa forma, um trichute é feito: de um valor médio minimo até um valor médio máximo dos canais RGBA, os pixeis que estiverem dentro desse minimo e máximo serão pretos e, dado outro valor médio minimo até outro valor médio mínimo dos canais RGBA, os pixeis dentro desses valores serão brancos.

#### A partir dessa nova imagem, preta e branca, com os clusters nitidos, de maneira constratada, a imagem é realizada.

### 2. Implementação

### 2.1. Python

#### A linguagem escolhida para o projeto foi Python, dada a sua facilidade para tratamento de dados e imagens, possuido boas bibliotecas.

### 2.1.1 Ambiente Virtual

#### Python depende de um ambiente virtual para desenvolvimento. Isso permite um gerenciamento total e completo das bibliotecas e dependencias do projeto, além de permitir as suas instalações propriamente ditas.

#### Para iniciar um "venv", esteja na raiz do seu projeto e digite : python -m venv "nome_do_ambiente"

#### Depois isso, para ativa-lo: source venv/bin/activate

#### Dessa forma, o ambiente estará ativado e voce estará pronto para instalar as dependencias e gerenciar o seu projeto.

### 2.1.3 Bibliotecas e dependencias

#### São usadas 3 bibliotecas de analises de imagens: opencv-python, scikit-image e Pillow;

#### para baixar cada: pip install "pacote"

### 2.2 Estruturação do projeto
 
#### O projeto, a grosso modo, é dividido em .venv, o arquivo do ambiente virtual que estamos. Não iremos mudar, mexer ou alterar muitas coisas nessa diretorio, sendo praticamente 100% usando só para instalação, gerenciamente e ativação do ambiento e dependencias. 

#### Src é o source, onde teremos nosso código, ou se necessário, codigos.

#### Models, que será onde teremos cada uma das nossas imagens que serão tratadas

#### E por fim, um diretorio final, para armazenamento das novas imagens e analises.