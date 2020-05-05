import pyglet
import math
from random import choice
from random import randint
from pyglet import gl
from pyglet.window import key
batch = pyglet.graphics.Batch()

ACCELERATION = 250
ROTATION_SPEED = 150
MAX_SPEED = 800

window = pyglet.window.Window()

def load_picture(name):
    picture = pyglet.image.load('obrazky/PNG/' + name)
    picture.anchor_x = picture.width // 2 # otáčení kolem středu
    picture.anchor_y = picture.height // 2
    return picture

picture_ship = load_picture('playerShip1_green.png')
picture_meteor = [
        load_picture('Meteors/meteorGrey_big1.png'),
        load_picture('Meteors/meteorGrey_big2.png'),
        load_picture('Meteors/meteorGrey_med1.png'),
        load_picture('Meteors/meteorGrey_med2.png')] # seznam obsahující 4 obrázky

class SpaceObject:

    def __init__(self,x,y,rotation,picture):
        self.x = x      # údaje o lodi
        self.y = y
        self.rotation = 90 - rotation
        self.speed_x = 0
        self.speed_y = 0
        self.rotation_speed = 0
        self.sprite = pyglet.sprite.Sprite(picture, batch = batch)
        self.radius = 30

    def tick(self, dt):
        if self.x > window.width:    #vyletění z okna - objeví se na druhé straně
                self.x -= window.width
        if self.x < 0:
                self.x += window.width
        if self.y > window.height:
                self.y -= window.height
        if self.y < 0:
                self.y += window.height

        self.x = self.x + dt * self.speed_x # aktualizace polohy
        self.y = self.y + dt * self.speed_y
        self.rotation = self.rotation + dt * self.rotation_speed

        self.sprite.x = self.x              # nastavení parametru obrazku na danou polohu
        self.sprite.y = self.y              # nové souřadnce
        self.sprite.rotation = 90 - self.rotation

    def delete(self):
        objects = objects[1:]
        delete(Spaceship.sprite)


class Spaceship(SpaceObject):
    def __init__(self,x,y,rotation):
        super().__init__(x, y, rotation, picture_ship) # do initu SpaceObjectu dá jako obrázek picture_lod

    def tick(self, dt): # nastavení kláves a
        self.rotation_speed = 0
        if pyglet.window.key.LEFT in pressed_keys: # kontrola, jestli zmáčknuté tlačítko - otáčení
            self.rotation_speed += ROTATION_SPEED
        if pyglet.window.key.RIGHT in pressed_keys:
            self.rotation_speed -= ROTATION_SPEED

        rotation_radians = math.radians(self.rotation)
        if pyglet.window.key.UP in pressed_keys:
            self.speed_x += dt * ACCELERATION * math.cos(rotation_radians) # akcelerace dopředu
            self.speed_y += dt * ACCELERATION * math.sin(rotation_radians)
        if pyglet.window.key.DOWN in pressed_keys:
            self.speed_x -= dt * ACCELERATION * math.cos(rotation_radians) # akcelerace dozadu
            self.speed_y -= dt * ACCELERATION * math.sin(rotation_radians)

        self.speed_x = min(self.speed_x, MAX_SPEED)    #pokud bude rychlost menší než MAX_SPEED tak se vezme, pokud větší
        self.speed_x = max(self.speed_x, -MAX_SPEED)   # tak se vezme MAX_SPEED
        self.speed_y = min(self.speed_y, MAX_SPEED)
        self.speed_y = max(self.speed_y, -MAX_SPEED)

        super().tick(dt)


class Asteroid(SpaceObject):
    def __init__(self,x,y,rotation):
        super().__init__(x,y,rotation,choice(picture_meteor))
        self.speed_x = randint(-50,50)
        self.speed_y = randint(-50,50)
        self.rotation_speed = randint(-50,50)

objects = []
objects.append(Spaceship(window.width // 2, window.height //2, 0))
for i in range(4):
    objects.append(Asteroid(window.width // 2, window.height //2, 0))

def distance(a, b, wrap_size):
   """Distance in one direction (x or y)"""
   result = abs(a - b)
   if result > wrap_size / 2:
       result = wrap_size - result
       return result

def overlaps(a, b):
    """Returns true iff two space objects overlap"""
    distance_squared = (distance(a.x, b.x, window.width) ** 2 +
                        distance(a.y, b.y, window.height) ** 2)
    max_distance_squared = (a.radius + b.radius) ** 2
    return distance_squared < max_distance_squared



def tick(dt):
    for item in objects:
        item.tick(dt)
pyglet.clock.schedule_interval(tick,1/30)

def draw_circle(x, y, radius):
    iterations = 20
    s = math.sin(2*math.pi / iterations)
    c = math.cos(2*math.pi / iterations)

    dx, dy = radius, 0

    gl.glBegin(gl.GL_LINE_STRIP)
    for i in range(iterations+1):
        gl.glVertex2f(x+dx, y+dy)
        dx, dy = (dx*c - dy*s), (dy*c + dx*s)
    gl.glEnd()

def draw():
    window.clear()

    for x_offset in (-window.width, 0, window.width):
        for y_offset in (-window.height, 0, window.height):
              # Remember the current state
              gl.glPushMatrix()
              # Move everything drawn from now on by (x_offset, y_offset, 0)
              gl.glTranslatef(x_offset, y_offset, 0)
              # Draw
              batch.draw()
              # Restore remembered state (this cancels the glTranslatef)
              for item in objects:
                  draw_circle(item.x,item.y,item.radius)
              gl.glPopMatrix()

pressed_keys = set() # v proměnné všechna tlačítka, která držím

def on_key_press(symbol, modifiers): #symbol je daná klávesa
    pressed_keys.add(symbol)


def on_key_release(symbol, modifiers):
    pressed_keys.discard(symbol)


window.push_handlers(on_key_press =on_key_press,on_key_release =on_key_release, on_draw=draw)

pyglet.app.run()
