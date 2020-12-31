from OpenGL.GL import *
from OpenGL.GL import glBegin
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import glm

# tamanho da tela
WINDOW_WIDHT = 1000
WINDOW_HEIGHT = 1000

# camera
cameraPos = glm.vec3(0, 3.5, 30)
cameraFront = glm.vec3(0, 0, -1)
cameraUp = glm.vec3(0, 1, 0)
angle = 0

# mouse
old_mouse_x = 0
old_mouse_y = 0
angle_x = -1.57
angle_y = 1.57
mouse_speed = 0.1
mouse_sensitivity = 0.001

half_width = WINDOW_WIDHT / 2
half_height = WINDOW_HEIGHT / 2


def draw_wall(x0, y0, z0, x1, y1, z1):
    glBegin(GL_QUADS)
    glVertex3f(x0, y0, z0)
    glVertex3f(x1, y0, z1)
    glVertex3f(x1, y1, z1)
    glVertex3f(x0, y1, z0)
    glEnd()


def draw_floor(x, y, z, width, length):
    glBegin(GL_QUADS)
    glVertex3f(x, y, z)
    glVertex3f(x, y, z + length)
    glVertex3f(x + width, y, z + length)
    glVertex3f(x + width, y, z)
    glEnd()

def draw_block(x, y, z, width, length, height):
    glColor3f(0.293, 0.211, 0.13)
    draw_wall(x, y, z, x, y + height, z+length)
    glColor3f(0.486, 0.293, 0)
    draw_wall(x, y, z, x+width, y + height, z)
    draw_wall(x+width, y, z, x + width, y + height, z + length)
    glColor3f(0.36, 0.2, 0.09)
    draw_wall(x, y, z+length, x + width, y + height, z + length)
    draw_floor(x, y, z, width, length)
    glColor3f(0.37, 0.15, 0.07)
    draw_floor(x, y+height, z, width, length)


def draw_cylinder(x, y, z, radius, height):
    px = 0
    pz = 0
    c_angle = 0
    angle_stepsize = 0.1

    glBegin(GL_QUAD_STRIP)
    c_angle = 0
    while c_angle < 2*glm.pi() + 1:
        px = radius * glm.cos(c_angle)
        pz = radius * glm.sin(c_angle)
        glVertex3f(x + px, y + height, z + pz)
        glVertex3f(x + px, y, z + pz)
        c_angle += angle_stepsize
    glEnd()

    glBegin(GL_POLYGON)
    c_angle = 0
    while c_angle < 2*glm.pi():
        px = radius * glm.cos(c_angle)
        pz = radius * glm.sin(c_angle)
        glVertex3f(x + px, y + height, z + pz)
        c_angle += angle_stepsize
    glEnd()

    glBegin(GL_POLYGON)
    c_angle = 0
    while c_angle < 2*glm.pi():
        px = radius * glm.cos(c_angle)
        pz = radius * glm.sin(c_angle)
        glVertex3f(x + px, y + height, z + pz)
        c_angle += angle_stepsize
    glEnd()

    glBegin(GL_POLYGON)
    c_angle = 0
    while c_angle < 2 * glm.pi():
        px = radius * glm.cos(c_angle)
        pz = radius * glm.sin(c_angle)
        glVertex3f(x + px, y, z + pz)
        c_angle += angle_stepsize
    glEnd()



def draw_bed(x, y, z):
    glPushMatrix()
    glTranslatef(x,y,z)
    draw_block(0, 0, 0, 5.5, 0.1, 2.5)
    draw_block(0.5, 0.4, 0.1, 4, 8, 1)
    draw_cylinder(0.5+0.2, 0, 0.2, 0.1, 0.4)
    draw_cylinder(0.5+0.2, 0, 4, 0.1, 0.4)
    draw_cylinder(0.5+0.2, 0, 7.8, 0.1, 0.4)
    draw_cylinder(0.5+3.8, 0, 0.2, 0.1, 0.4)
    draw_cylinder(0.5+3.8, 0, 7.8, 0.1, 0.4)
    glPopMatrix()


def display():
    global angle
    # limpa cor e buffers de profundidade
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # reseta transformações
    glLoadIdentity()

    # define camera
    # camx camy camz centerx centery centerz upx upy upz
    gluLookAt(cameraPos.x, cameraPos.y, cameraPos.z,
              cameraPos.x + cameraFront.x, cameraPos.y + cameraFront.y, cameraPos.z + cameraFront.z,
              cameraUp.x, cameraUp.y, cameraUp.z)
    #fixed cam
    # gluLookAt(0, 5, 35,
    #           0, 0, -5,
    #           0, 1, 0)



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
        glVertex3f(10, 0.001, -10.01 + i)
        glEnd()


    draw_bed(-9, 0, -9)

    glutSwapBuffers()



def keyboard_d_keys(key, dx, y):
    global angle, cameraFront, cameraUp, cameraPos

    if not isinstance(key, int):
        key = key.decode("utf-8")

    front = glm.vec3(0, 0, -1)

    cam_speed = 0.2

    if key == GLUT_KEY_LEFT:
        print("D_KEYS_L ", key)
        angle -= cam_speed
        front.x = glm.sin(angle)
        front.z = -glm.cos(angle)
    elif key == GLUT_KEY_RIGHT:
        print("D_KEYS_R ", key)
        angle += cam_speed
        front.x = glm.sin(angle)
        front.z = -glm.cos(angle)
    elif key == GLUT_KEY_UP:
        print("D_KEYS_U ", key)
        angle += cam_speed
        front.y = glm.sin(angle)
        # front.z = -glm.cos(angle)
    elif key == GLUT_KEY_DOWN:
        print("D_KEYS_D ", key)
        angle -= cam_speed
        front.y = glm.sin(angle)
        # front.z = -glm.cos(angle)

    # cameraFront = glm.normalize(front)
    cameraFront = front
    glutPostRedisplay()


def keyboard(key, x, y):
    global angle, X, Z, dx, dy, dz, roll, cameraFront, cameraUp, cameraPos

    cameraSpeed = 1

    if not isinstance(key, int):
        key = key.decode("utf-8")

    if key == 'w':
        print("KEYBOARD w", key)
        cameraPos += cameraSpeed * cameraFront
    elif key == 'a':
        print("KEYBOARD a", key)
        cameraPos -= glm.normalize(glm.cross(cameraFront, cameraUp)) * cameraSpeed
    elif key == 's':
        print("KEYBOARD s", key)
        cameraPos -= cameraSpeed * cameraFront
    elif key == 'd':
        print("KEYBOARD d", key)
        cameraPos += glm.normalize(glm.cross(cameraFront, cameraUp)) * cameraSpeed
    elif key == 'q':
        print("KEYBOARD q", key)
        cameraPos.y += cameraSpeed
    elif key == 'e':
        print("KEYBOARD e", key)
        cameraPos.y -= cameraSpeed
    glutPostRedisplay()


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


def mouse_click(button, state, x, y):
    global old_mouse_x, old_mouse_y
    old_mouse_x = x
    old_mouse_y = y


def mouse_camera(mouse_x, mouse_y):
    global mouse_sensitivity, mouse_speed, angle_x, angle_y, cameraFront, old_mouse_x, old_mouse_y

    angle_x -= (mouse_x - old_mouse_x) * mouse_sensitivity
    angle_y -= (mouse_y - old_mouse_y) * mouse_sensitivity

    if angle_y > 2:
        angle_y = 2
    if angle_y < 1:
        angle_y = 1

    front = glm.vec3()
    front.x = glm.cos(angle_x) * glm.sin(angle_y)
    front.z = glm.sin(angle_x) * glm.sin(angle_y)
    front.y = glm.cos(angle_y)
    cameraFront = front

    old_mouse_x = mouse_x
    old_mouse_y = mouse_y
    glutPostRedisplay()


def main():
    global dy
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

    glutMouseFunc(mouse_click)
    glutMotionFunc(mouse_camera)


    glEnable(GL_DEPTH_TEST)

    glutMainLoop()
    print("wasd anda, seta olha")


main()
