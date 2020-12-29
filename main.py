from OpenGL.GL import *
from OpenGL.GL import glBegin
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# tamanho da tela
WINDOW_WIDHT = 1000
WINDOW_HEIGHT = 1000

# angulo de rotação da camera
x_angle = 0
y_angle = 0
# direção da camera
dx, dy, dz = 0, 0, -1
# posição da camera
X = -5
Y = 2.5
Z = 18

roll = 0

half_width = WINDOW_WIDHT / 2
half_height = WINDOW_HEIGHT / 2



def display():
    global X, Z, dx, dy, dz, x_angle, y_angle, mouse_x, mouse_y, roll
    # limpa cor e buffers de profundidade
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # reseta transformações
    glLoadIdentity()

    # define camera
    # camx camy camz centerx centery centerz upx upy upz
    gluLookAt(X, Y, Z,
              dx, dy, dz,
              roll + 0, Y, 0)

    # piso
    glColor(0.7, 0.7, 0.7)
    glBegin(GL_QUADS)
    glVertex3f(-10, 0, -10)
    glVertex3f(-10, 0, 10)
    glVertex3f(10, 0, 10)
    glVertex3f(10, 0, -10)
    glEnd()

    # parede1
    glColor3f(0.9294, 0.9216, 0.8353)
    glBegin(GL_QUADS)
    glVertex3f(-10, 0, -10)
    glVertex3f(-10, 7, -10)
    glVertex3f(10, 7, -10)
    glVertex3f(10, 0, -10)
    glEnd()

    # parede2
    glColor3f(1, 0.851, 0.702)
    glBegin(GL_QUADS)
    glVertex3f(-10, 0, -10)
    glVertex3f(-10, 7, -10)
    glVertex3f(-10, 7, 10)
    glVertex3f(-10, 0, 10)
    glEnd()

    # parede3 com porta
    glColor3f(1, 0.851, 0.702)
    glBegin(GL_QUADS)
    glVertex3f(-10, 0, 10)
    glVertex3f(-10, 7, 10)
    glVertex3f(-6, 7, 10)
    glVertex3f(-6, 0, 10)
    glEnd()

    glColor3f(1, 0.851, 0.702)
    glBegin(GL_QUADS)
    glVertex3f(-3, 0, 10)
    glVertex3f(-3, 7, 10)
    glVertex3f(10, 7, 10)
    glVertex3f(10, 0, 10)
    glEnd()

    glColor3f(1, 0.851, 0.702)
    glBegin(GL_QUADS)
    glVertex3f(-6, 7, 10)
    glVertex3f(-6, 5, 10)
    glVertex3f(-3, 5, 10)
    glVertex3f(-3, 7, 10)
    glEnd()

    glColor3f(0.4, 0.2, 0)
    glLineWidth(30)
    glBegin(GL_LINES)
    glVertex3f(-6, 5, 10.01)
    glVertex3f(-3, 5, 10.01)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(-6, 5, 10.01)
    glVertex3f(-6, 0, 10.01)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(-3, 0, 10.01)
    glVertex3f(-3, 5, 10.01)
    glEnd()

    # parede4
    glColor3f(1, 0.851, 0.702)
    glBegin(GL_QUADS)
    glVertex3f(10, 0, -10)
    glVertex3f(10, 7, -10)
    glVertex3f(10, 7, 10)
    glVertex3f(10, 0, 10)
    glEnd()

    # teto
    glColor3f(0.95, 0.95, 0.95)
    glBegin(GL_QUADS)
    glVertex3f(-10, 7, -10)
    glVertex3f(10, 7, -10)
    glVertex3f(10, 7, 10)
    glVertex3f(-10, 7, 10)
    glEnd()

    #padrão do piso
    glColor3f(0.149, 0.149, 0.149)
    glLineWidth(3)
    for i in range(0, 20, 2):
        glBegin(GL_LINES)
        glVertex3f(-10 + i, 0.001, -10.01)
        glVertex3f(-10 + i, 0.001, 10.01)
        glEnd()
    for i in range(0, 20, 2):
        glBegin(GL_LINES)
        glVertex3f(-10, 0.001, -10.01 + i)
        glVertex3f(-10, 0.001, 10.01 + i)
        glEnd()


    glutSwapBuffers()
    glutPostRedisplay()


def keyboard_d_keys(key, x, y):
    global x_angle, X, Z, dx, dy, dz

    if not isinstance(key, int):
        key = key.decode("utf-8")

    if key == GLUT_KEY_LEFT:
        print("D_KEYS_L ", key)
        dx -= 1
    elif key == GLUT_KEY_RIGHT:
        print("D_KEYS_R ", key)
        dx += 1
    elif key == GLUT_KEY_UP:
        print("D_KEYS_U ", key)
        dy += 1
    elif key == GLUT_KEY_DOWN:
        print("D_KEYS_D ", key)
        dy -= 1


def keyboard(key, x, y):
    global x_angle, X, Z, dx, dy, dz, roll
    fraction = 0.1
    if not isinstance(key, int):
        key = key.decode("utf-8")

    if key == 'w':
        print("KEYBOARD w", key)
        Z -= 1
    elif key == 'a':
        print("KEYBOARD a", key)
        X -= 1
    elif key == 's':
        print("KEYBOARD s", key)
        Z += 1
    elif key == 'd':
        print("KEYBOARD d", key)
        X += 1
    elif key == 'x':
        print("KEYBOARD x", key)
        roll += 0.5
    elif key == 'z':
        print("KEYBOARD z", key)
        roll -= 0.5


def change_side(w, h):
    global half_width, half_height
    if h == 0:
        h = 1
    ratio = w * 1/h

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    glViewport(0, 0, w, h)

    half_width = w / 2
    half_height = h / 2

    gluPerspective(45, ratio, 0.1, 100)

    glMatrixMode(GL_MODELVIEW)


def main():
    # inicialização
    glutInit()  # inicia glut
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(WINDOW_WIDHT, WINDOW_HEIGHT)
    window = glutCreateWindow("Bedroom")

    glutDisplayFunc(display)
    glutReshapeFunc(change_side)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(keyboard_d_keys)

    glEnable(GL_DEPTH_TEST)

    glutMainLoop()
    print("wasd anda, seta olha")


main()
