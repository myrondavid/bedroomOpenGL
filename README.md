# bedroomOpenGL
## Quarto modelado com PyOpenGL

### Projeto da disciplina de Computação Gráfica do curso de Ciência da Computação IC-UFAL
### Professor: Marcelo Costa Oliveira
### Dupla: Myron e Cristiano
#### PLE 2020

Demonstração: https://www.youtube.com/watch?v=rVtttBJ74V4


#### Requisitos para rodar:
- python3 instalado
- PyOpenGL e PyOpenGL_accelerate
- pygame e pyglm

#### Instalação dos Requisitos:
- download e instalação do Python3 em https://www.python.org/downloads/
- PyOpenGL e PyOpenGL_accelerate podem ser instalados via PIP, para isto basta usar o comando:

`pip install PyOpenGL PyOpenGL_accelerate`

Mais informações em: https://pypi.org/project/PyOpenGL/

No entanto, há diversos relatos de erro ao instalar dessa forma, então é recomendado baixar o pacote externamente e instalá-lo via PIP, para isto:
- acessar https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopengl

- baixar os seguintes pacotes:
PyOpenGL_accelerate-3.1.5-cp39-cp39-win_amd64.whl
PyOpenGL-3.1.5-cp39-cp39-win_amd64.whl

fique atento a versão do seu python, se for 32 bits,
baixar os pacotes sendo win32 no lugar de win_amd64

- após o download, basta instalá-los com o PIP, exemplo:

`pip install PyOpenGL_accelerate-3.1.5-cp39-cp39-win_amd64.whl`

`pip install PyOpenGL-3.1.5-cp39-cp39-win_amd64.whl`

- instalar pygame e pyglm utilizando o PIP:

`pip install pygame`

`pip install PyGLM`

Mais informações em: https://pypi.org/project/PyGLM/ e https://pypi.org/project/pygame/

#### Executando:
- Para rodar basta entrar na pasta do projeto e executar com: `py main.py`
- Caso utilize o PyCharm para importar o projeto, basta executar(Shift+F10)

#### Controles:
- wasd movimentam a câmera
- clicar e arrastar o mouse mudam o angulo da câmera
- 'i' ativa a iluminação, 'I' desativa
- 'l' ativa spotlight, 'L' desativa
- 'o' abre a porta, 'O' fecha
- 'j' abre as janelas, 'J' fecha as janelas

O projeto foi desenvolvido com a IDE PyCharm, logo, recomendo o uso do mesmo para modificação ou execução.


#### Referências:
- Movimentação da câmera baseada em: 

http://www.lighthouse3d.com/tutorials/glut-tutorial/keyboard-example-moving-around-the-world/ 

https://learnopengl.com/Getting-started/Camera

- Código das texturas baseado em: 

https://github.com/mdrkb/3D-House-using-OpenGL-and-C-/ 

https://open.gl/textures

https://stackoverflow.com/questions/39194862/opengl-how-do-i-apply-a-texture-to-this-cube

- Iluminação baseada em: 

https://stackoverflow.com/questions/26032332/opengl-glut-spot-light/26033305 

https://github.com/mgleysson/CG_UFAL/tree/master/Projeto_MuseuZG
