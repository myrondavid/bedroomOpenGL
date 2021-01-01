from OpenGL.GL import *
from OpenGL.GL import glBegin
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import numpy
import glm
from PIL import Image
import pygame

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

#textures
textures = {
    'brick': None,
    'ceramica': None,
    'guardaroupa': None,
    'ednaldo': None,
    'gavetas_comoda': None,
    'portas_comoda': None,
    'teto': None,
    'parede': None
}


half_width = WINDOW_WIDHT / 2
half_height = WINDOW_HEIGHT / 2


def draw_wall(x0, y0, z0, x1, y1, z1):
    glBegin(GL_QUADS)
    glVertex3f(x0, y0, z0)
    glVertex3f(x1, y0, z1)
    glVertex3f(x1, y1, z1)
    glVertex3f(x0, y1, z0)
    glEnd()

def draw_textured_wall(x0, y0, z0, x1, y1, z1, texture):

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture)
    # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(x0, y0, z0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(x1, y0, z1)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(x1, y1, z1)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(x0, y1, z0)
    glEnd()
    glDisable(GL_TEXTURE_2D)


def draw_floor(x, y, z, width, length):
    glBegin(GL_QUADS)
    glVertex3f(x, y, z)
    glVertex3f(x, y, z + length)
    glVertex3f(x + width, y, z + length)
    glVertex3f(x + width, y, z)
    glEnd()


def draw_textured_floor(x, y, z, width, length, texture):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture)
    # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(x, y, z)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(x, y, z + length)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(x + width, y, z + length)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(x + width, y, z)
    glEnd()

    glDisable(GL_TEXTURE_2D)


def draw_block(x, y, z, width, length, height):
    draw_wall(x, y, z, x, y + height, z+length)
    draw_wall(x, y, z, x+width, y + height, z)
    draw_wall(x+width, y, z, x + width, y + height, z + length)
    draw_wall(x, y, z+length, x + width, y + height, z + length)
    draw_floor(x, y, z, width, length)
    draw_floor(x, y+height, z, width, length)

def draw_texturized_block_right(x, y, z, width, length, height, texture):
    #left side
    draw_wall(x, y, z, x, y + height, z+length)
    #back side
    draw_wall(x, y, z, x+width, y + height, z)
    #right side
    # draw_wall(x+width, y, z, x + width, y + height, z + length)
    draw_textured_wall(x+width, y, z, x + width, y + height, z + length, texture)
    #front side
    draw_wall(x, y, z+length, x + width, y + height, z + length)
    #down side
    draw_floor(x, y, z, width, length)
    #up side
    draw_floor(x, y+height, z, width, length)

def draw_texturized_block_front(x, y, z, width, length, height, texture):
    #left side
    draw_wall(x, y, z, x, y + height, z+length)
    #back side
    draw_wall(x, y, z, x+width, y + height, z)
    #right side
    draw_wall(x+width, y, z, x + width, y + height, z + length)
    #front side
    draw_textured_wall(x, y, z+length, x + width, y + height, z + length, texture)
    #down side
    draw_floor(x, y, z, width, length)
    #up side
    draw_floor(x, y+height, z, width, length)


def draw_colored_block(x, y, z, width, length, height, front_color, back_color, left_color, right_color, up_color, down_color):
    #left side
    glColor3f(left_color.x, left_color.y, left_color.z)
    draw_wall(x, y, z, x, y + height, z+length)
    #back side
    glColor3f(back_color.x, back_color.y, back_color.z)
    draw_wall(x, y, z, x+width, y + height, z)
    #right side
    glColor3f(right_color.x, right_color.y, right_color.z)
    draw_wall(x+width, y, z, x + width, y + height, z + length)
    #front side
    glColor3f(front_color.x, front_color.y, front_color.z)
    draw_wall(x, y, z+length, x + width, y + height, z + length)
    #down side
    glColor3f(down_color.x, down_color.y, down_color.z)
    draw_floor(x, y, z, width, length)
    #up side
    glColor3f(up_color.x, up_color.y, up_color.z)
    draw_floor(x, y+height, z, width, length)


def draw_colored_block_fixed(x, y, z, width, length, height):
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



def draw_bed1(x, y, z):
    glPushMatrix()
    glTranslatef(x,y,z)
    #cabeceira da cama
    draw_colored_block(0, 0, 0, 6.2, 0.1, 2.5,
                       glm.vec3(0.8, 0.8, 0.8), glm.vec3(1, 1, 1),
                       glm.vec3(0.6, 0.6, 0.6), glm.vec3(1, 1, 1),
                       glm.vec3(1, 1, 1), glm.vec3(1, 1, 1))
    draw_colored_block(4.6, 0, 0.1, 0.1, 1, 1.4,
                       glm.vec3(0.12, 0.12, 0.12), glm.vec3(0.10, 0.10, 0.10),
                       glm.vec3(0.14, 0.14, 0.14), glm.vec3(0.10, 0.10, 0.10),
                       glm.vec3(0.10, 0.10, 0.10), glm.vec3(0.10, 0.10, 0.10))
    draw_colored_block(4.65, 1.3, 0.1, 1.3, 1, 0.1,
                       glm.vec3(0.12, 0.12, 0.12), glm.vec3(0.10, 0.10, 0.10),
                       glm.vec3(0.14, 0.14, 0.14), glm.vec3(0.10, 0.10, 0.10),
                       glm.vec3(0.10, 0.10, 0.10), glm.vec3(0.10, 0.10, 0.10))
    draw_colored_block(4.65, 0.7, 0.1, 1.3, 1, 0.1,
                       glm.vec3(0.12, 0.12, 0.12), glm.vec3(0.10, 0.10, 0.10),
                       glm.vec3(0.14, 0.14, 0.14), glm.vec3(0.10, 0.10, 0.10),
                       glm.vec3(0.10, 0.10, 0.10), glm.vec3(0.10, 0.10, 0.10))
    draw_colored_block(4.65, 0.2, 0.1, 1.3, 1, 0.1,
                       glm.vec3(0.12, 0.12, 0.12), glm.vec3(0.10, 0.10, 0.10),
                       glm.vec3(0.14, 0.14, 0.14), glm.vec3(0.10, 0.10, 0.10),
                       glm.vec3(0.10, 0.10, 0.10), glm.vec3(0.10, 0.10, 0.10))
    #cama
    draw_colored_block(0.5, 0.4, 0.1, 4, 8, 0.5,
                       glm.vec3(0.8, 0.8, 0.8), glm.vec3(1, 1, 1),
                       glm.vec3(0.6, 0.6, 0.6), glm.vec3(1, 1, 1),
                       glm.vec3(1, 1, 1), glm.vec3(1, 1, 1))
    #colchão
    glColor3f(0.212, 0.205, 0.205)
    draw_block(0.5, 0.9, 0.1, 4, 8, 0.6)
    #pés da cama
    glColor3f(0.18, 0.16, 0.16)
    draw_cylinder(0.5+0.2, 0, 0.2, 0.1, 0.4)
    draw_cylinder(0.5+0.2, 0, 4, 0.1, 0.4)
    draw_cylinder(0.5+0.2, 0, 7.8, 0.1, 0.4)
    draw_cylinder(0.5+3.8, 0, 0.2, 0.1, 0.4)
    draw_cylinder(0.5+3.8, 0, 7.8, 0.1, 0.4)
    glPopMatrix()


def draw_bed2(x, y, z):
    glPushMatrix()
    glTranslatef(x,y,z)
    #cama
    draw_colored_block(0.5, 0.4, 0.1, 4, 8, 0.5,
                       glm.vec3(0.8, 0.8, 0.8), glm.vec3(1, 1, 1),
                       glm.vec3(0.6, 0.6, 0.6), glm.vec3(1, 1, 1),
                       glm.vec3(1, 1, 1), glm.vec3(1, 1, 1))
    #colchão
    glColor3f(0.212, 0.205, 0.205)
    draw_block(0.5, 0.9, 0.1, 4, 8, 0.6)
    #pés da cama
    glColor3f(0.18, 0.16, 0.16)
    draw_cylinder(0.5+0.2, 0, 0.2, 0.1, 0.4)
    draw_cylinder(0.5+0.2, 0, 4, 0.1, 0.4)
    draw_cylinder(0.5+0.2, 0, 7.8, 0.1, 0.4)
    draw_cylinder(0.5+3.8, 0, 0.2, 0.1, 0.4)
    draw_cylinder(0.5+3.8, 0, 7.8, 0.1, 0.4)
    glPopMatrix()

def draw_wardrobe(x, y, z):
    glPushMatrix()
    glTranslatef(x, y, z)
    glColor3ub(250, 250, 250)
    # draw_colored_block(0, 0, 0, 2.5, 12, 5,
    #                    glm.vec3(0.8, 0.8, 0.8), glm.vec3(1, 1, 1),
    #                    glm.vec3(0.6, 0.6, 0.6), glm.vec3(1, 1, 1),
    #                    glm.vec3(1, 1, 1), glm.vec3(1, 1, 1))
    draw_texturized_block_right(0, 0, 0, 2.5, 12, 5, textures['guardaroupa'])
    glPopMatrix()


def draw_dresser(x, y, z):
    glPushMatrix()
    glTranslatef(x, y, z)

    # pés
    glColor3f(0.18, 0.16, 0.16)
    draw_cylinder(0.2, 0, 0.2, 0.1, 0.2)
    draw_cylinder(0.2, 0, 1.8, 0.1, 0.2)
    draw_cylinder(4.8, 0, 0.2, 0.1, 0.2)
    draw_cylinder(4.8, 0, 1.8, 0.1, 0.2)
    #base
    draw_colored_block(0, 0.2, 0, 5, 2, 0.1,
                       glm.vec3(0.8, 0.8, 0.8), glm.vec3(1, 1, 1),
                       glm.vec3(0.6, 0.6, 0.6), glm.vec3(1, 1, 1),
                       glm.vec3(1, 1, 1), glm.vec3(1, 1, 1))
    #gavetas
    # draw_colored_block(0.2, 0.3, 0.2, 2, 1.6, 2.5,
    #                    glm.vec3(0.8, 0.8, 0.8), glm.vec3(1, 1, 1),
    #                    glm.vec3(0.6, 0.6, 0.6), glm.vec3(1, 1, 1),
    #                    glm.vec3(1, 1, 1), glm.vec3(1, 1, 1))
    glColor3ub(250, 250, 250)
    draw_texturized_block_front(0.2, 0.3, 0.2, 2, 1.6, 2.5, textures['gavetas_comoda'])
    #armarinho
    # draw_colored_block(1.8, 0.3, 0.2, 3, 1.6, 1.6,
    #                    glm.vec3(0.8, 0.8, 0.8), glm.vec3(1, 1, 1),
    #                    glm.vec3(0.6, 0.6, 0.6), glm.vec3(1, 1, 1),
    #                    glm.vec3(1, 1, 1), glm.vec3(1, 1, 1))
    draw_texturized_block_front(2.2, 0.3, 0.2, 2.6, 1.6, 1.6, textures['portas_comoda'])
    #pedaço do lado
    draw_colored_block(4.7, 1.9, 0.2, 0.1, 1.6, 0.9,
                       glm.vec3(0.8, 0.8, 0.8), glm.vec3(1, 1, 1),
                       glm.vec3(0.6, 0.6, 0.6), glm.vec3(1, 1, 1),
                       glm.vec3(1, 1, 1), glm.vec3(1, 1, 1))
    # tampo
    draw_colored_block(0, 2.7, 0, 5, 2, 0.1,
                       glm.vec3(0.8, 0.8, 0.8), glm.vec3(1, 1, 1),
                       glm.vec3(0.6, 0.6, 0.6), glm.vec3(1, 1, 1),
                       glm.vec3(1, 1, 1), glm.vec3(1, 1, 1))


    # tv
    glPushMatrix()
    # base tv
    draw_colored_block(2, 2.8, 0.7, 1, 0.6, 0.1,
                       glm.vec3(0.1, 0.1, 0.1), glm.vec3(0.1, 0.1, 0.1),
                       glm.vec3(0.1, 0.1, 0.1), glm.vec3(0.1, 0.1, 0.1),
                       glm.vec3(0.1, 0.1, 0.1), glm.vec3(0.1, 0.1, 0.1))
    glColor3ub(23, 22, 20)
    # pé da base
    draw_cylinder(2.5, 2.9, 1, 0.1, 0.2)
    # base tela
    draw_block(1, 3.1, 0.8, 3, 0.4, 0.1)
    #lateral esquerda tela
    draw_block(1, 3.2, 0.8, 0.1, 0.4, 1.5)
    # lateral direita tela
    draw_block(3.9, 3.2, 0.8, 0.1, 0.4, 1.5)
    #topo tela
    draw_block(1, 4.6, 0.8, 3, 0.4, 0.1)
    #tela
    # draw_colored_block(1.1, 3.2, 0.9, 2.8, 0.3, 1.4,
    #                    glm.vec3(0.3, 0.3, 0.3), glm.vec3(23/255, 22/255, 20/255),
    #                    glm.vec3(0.1, 0.1, 0.1), glm.vec3(0.1, 0.1, 0.1),
    #
    glColor3ub(255, 255, 255)
    draw_texturized_block_front(1.1, 3.2, 0.9, 2.8, 0.3, 1.4, textures['ednaldo'])
    glPopMatrix()


    glPopMatrix()


def display():
    global angle, texture_brick
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


    glPushMatrix()
    # piso
    glColor(1, 1, 1)
    draw_textured_floor(-10, 0, -10, 20, 20, textures['ceramica'])

    #teste parede com textura
    draw_textured_wall(-10, 0, -20, 10, 7, -20, textures['brick'])
    draw_textured_floor(-10, 0, -20, 10, 5, textures['ceramica'])

    # parede de trás
    # glColor3f(0.9294, 0.9294, 0.9294)
    glColor3ub(255, 255, 255)
    draw_textured_wall(-10, 0, -10, 10, 7, -10, textures['parede'])
    # draw_wall(-10, 0, -10, 10, 7, -10)

    # parede esquerda
    glColor3ub(181, 177, 163)
    # draw_wall(-10, 0, -10, -10, 7, 10)
    draw_textured_wall(-10, 0, -10, -10, 7, 10, textures['parede'])

    # parede da frente com portas e janelas
    glColor3f(1, 0.851, 0.702)
    #part1
    draw_block(-10, 0, 10, 2, 0.4, 7)
    # part 2
    draw_block(-8, 5, 10, 3, 0.4, 2)
    # part3
    draw_block(-5, 0, 10, 2, 0.4, 7)
    # part4
    draw_block(-3, 6, 10, 13, 0.4, 1)
    # part5
    draw_block(-3, 0, 10, 4, 0.4, 5)
    # part6
    draw_block(1, 0, 10, 3, 0.4, 6)
    # part7
    draw_block(4, 5, 10, 6, 0.4, 1)
    # part8
    draw_block(4, 0, 10, 3, 0.4, 4)
    # part9
    draw_block(7, 0, 10, 3, 0.4, 5)

    # alisais esquerdo
    draw_colored_block_fixed(-8, 0, 10, 0.1, 0.4, 5)
    # alisais direito
    draw_colored_block_fixed(-5.1, 0, 10, 0.1, 0.4, 5)
    # alisais topo
    draw_colored_block_fixed(-7.9, 4.9, 10, 2.8, 0.4, 0.1)

    # parede direita
    glColor3ub(201, 197, 183)
    draw_textured_wall(10, 0, -10, 10, 7, 10, textures['parede'])
    # draw_wall(10, 0, -10, 10, 7, 10)

    # teto
    glColor3ub(250, 250, 250)
    # draw_floor(-10, 7, -10, 20, 20)
    draw_textured_floor(-10, 7, -10, 20, 20, textures['teto'])

    #padrão do piso
    # glColor3f(0.149, 0.149, 0.149)
    # glLineWidth(3)
    # for i in range(0, 20, 2):
    #     glBegin(GL_LINES)
    #     glVertex3f(-10 + i, 0.001, -10.01)
    #     glVertex3f(-10 + i, 0.001, 10.01)
    #     glEnd()
    # for i in range(0, 20, 2):
    #     glBegin(GL_LINES)
    #     glVertex3f(-10, 0.001, -10.01 + i)
    #     glVertex3f(10, 0.001, -10.01 + i)
    #     glEnd()
    glPopMatrix()

    #cama 1 com cabeceira
    draw_bed1(-6, 0, -9.99)
    #cama 2
    draw_bed2(5.3, 0, -9.99)

    #guarda-roupas grande
    draw_wardrobe(-9.99, 0, -9.99)


    #comoda e tv
    glPushMatrix()
    glTranslatef(4, 0, 9.99)
    glRotatef(180, 0, 1, 0)
    draw_dresser(0, 0, 0)
    glPopMatrix()

    # guarda-roupas pequeno
    glPushMatrix()
    glScalef(0.6, 1, 0.3)
    glTranslatef(16.2, 0, 33)
    glRotatef(180, 0, 1, 0)
    draw_wardrobe(0,0,0)
    glPopMatrix()


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
        cameraPos.y += cameraSpeed/2
    elif key == 'e':
        print("KEYBOARD e", key)
        cameraPos.y -= cameraSpeed/2
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


def load_texture(image):
    texid = 0
    textureSurface = pygame.image.load(image)
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()
    # glGenTextures(1, texid)
    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texid)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_MIRRORED_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_MIRRORED_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)

    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glGenerateMipmap(GL_TEXTURE_2D)

    return texid

def main():
    global textures
    # inicialização
    glutInit()  # inicia glut
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(WINDOW_WIDHT, WINDOW_HEIGHT)
    window = glutCreateWindow("Myron's Bedroom")

    #callbacks
    glutDisplayFunc(display)
    glutReshapeFunc(change_side)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(keyboard_d_keys)
    glutMouseFunc(mouse_click)
    glutMotionFunc(mouse_camera)

    glEnable(GL_DEPTH_TEST)

    #textures
    textures['brick'] = load_texture("textures/wall.png")
    textures['ceramica'] = load_texture("textures/ceramica.png")
    textures['guardaroupa'] = load_texture("textures/guarda-roupa.png")
    textures['ednaldo'] = load_texture("textures/ednaldo.png")
    textures['gavetas_comoda'] = load_texture("textures/gavetas_comoda.png")
    textures['portas_comoda'] = load_texture("textures/portas_comoda.png")
    textures['teto'] = load_texture("textures/teto-pvc.png")
    textures['parede'] = load_texture("textures/parede.png")

    glutMainLoop()


main()
