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

#### As imagens para analise foram obtidas a partir da elaboração de pães e após a sua realização, uma fatia vertical é feita.

#### As faces das duas partes do pão cortado são escaneadas.

#### Após o scan, cada experimento é recortado individualmente, caso necessário, é corrigido o brilho, saturação e nitidez e, após isso, é recortada uma amostra de cada experimento corrigido.

#### Essa correção é realizada a fim de facilitar a analise propriamente dita, que será explicada posteriormente.

### 1.1 A análise

#### A analise propriamente dita é realizada em partes:

#### - Obtenção da imagem a ser analisada(scanner);
#### - Correção da imagem(software de edição de imagem);
#### - Trichute (binarização dos dados e cores atraves de função da biblioteca OpenCv);
#### - Obtenção da imagem preta e branca;
#### - Obtenção de uma imagem com os clusters visiveis;
#### - Contagem e analise dos clusters;

#### O trichute é realizado a partir de que, os clusters possuem, em média uma coloração mais escura o resto do pão. Dessa forma, um trichute é feito: de um valor médio minimo até um valor médio máximo dos canais RGBA, os pixeis que estiverem dentro desse minimo e máximo serão pretos e, dado outro valor médio minimo até outro valor médio mínimo dos canais RGBA, os pixeis dentro desses valores serão brancos.

#### A partir dessa nova imagem, preta e branca, com os clusters nitidos, de maneira constratada, a analise é realizada.

### 2. Implementação

### 2.1. Python

#### A linguagem escolhida para o projeto foi Python, dada a sua facilidade para tratamento de dados e imagens, possuido boas bibliotecas para o projeto.

### 2.1.1 Ambiente Virtual

#### Python depende de um ambiente virtual para desenvolvimento. Isso permite um gerenciamento total e completo das bibliotecas e dependencias do projeto, além de permitir as suas instalações propriamente ditas.

#### Para iniciar um "venv", esteja na raiz do seu projeto e digite : python -m venv "nome_do_ambiente"

#### Depois isso, para ativa-lo: source venv/bin/activate

#### Dessa forma, o ambiente estará ativado e voce estará pronto para instalar as dependencias e gerenciar o seu projeto.

### 2.1.3 Bibliotecas e dependencias

#### São usadas 3 bibliotecas de analises de imagens: opencv-python, scikit-image e Pillow;

#### para baixar cada: pip install "pacote"

### 2.2 Estruturação do projeto
 
#### O projeto, a grosso modo, é dividido em :

#### venv, o arquivo do ambiente virtual que estamos. Não iremos mudar, mexer ou alterar muitas coisas nessa diretorio, sendo praticamente 100% usando só para instalação, gerenciamente e ativação do ambiento e dependencias. 

#### Src é o source, onde teremos nosso código, ou se necessário, codigos.

#### Models, que será onde teremos cada uma das nossas imagens que serão tratadas. Irá possuir os scans originais, cada recorte de cada experimento individual, os experimentos corrigidos e as amostras dos experimentos corrigidos.

#### Resources, um diretório para armazenamento de de recursos a serem utilizados ou aqueles que ja foram e são interessantes de serem armazenados.

#### Tests, onde estão os recursos para realização dos testes do código.


### 2.3 index.ipynb

### 2.3.1 Incluindo bibliotecas

#### Inicialmente é realizada a inclusão das bibliotecas necessarias. Deve-se também, já compilar a célula, para ver se há algum erro de compilação. No meu caso, utilizando a o ambiente Jupyter Notebook, eu tive que instalar algumas dependencias do kernel jupyter para que compilasse o ambiente virtual.

### 2.3.2 Caminho das dependencias

#### Quando trabalhamos com Python, sempre trabalhamos com um ambiente virtual, o que nos permite a inportação e utilização de bibliotecas e dependencias. Só que, para garantirmos que o Kernel Python do projeto irá utilizar as importações do nosso ambiente, temos que deixarmos explicito para o projeto o caminho do ambiente que será utilizado. Observa-se que, apesar de o código como está implementado permitir que qualquer máquina, ao clonar o repositório, utilize o caminho normalmente, pode haver algum conflito e por isso, você terá de configurar e passar manualmente o caminho do ambiente.

### 2.3.3 Importação das bibliotecas

#### Após a instalação das bibliotecas no ambiente virtual, podemos importa-las no nosso código.

### 2.3.4 - Código principal

#### Uma variavel img é definida que le uma imagem que você definir. Após isso, são definidas variaveis auxiliares gray e blurred, que serviram que auxilio para a realização do trichute. Após a definição dessas variáveis, é criada a mascará, o filtro da imagem. A mascara recebe como valor a função adaptiveThreshold(trichute adaptativo) da biblioteca opencv. A função recebe como parametros o valor da variavel blurred, o valor maximo de um rgb, duas funções da biblioteca opencv, a primeira ADAPTIVE_THRESH_MEAN_C e a segunda THRESH_BINARY, por fim, os valores 31 e 10.

#### Após a mascara ter sido criada, são definidas duas variaveis que irão plotar a imagem resultante. 

#### Com isso, um laço de repetição é criado a fim de  











   
