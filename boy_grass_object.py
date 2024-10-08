from cgitb import reset

from pico2d import *
import random
# Game object class here
class Grass:
    # 생성자를 이용해서 객체의 초기 상태를 정의 상태를 정의함
    def __init__(self):
        self.image = load_image('grass.png')
    def update(self):
        pass
    def draw(self):
        self.image.draw(400,30)
    pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 90
        self.frame = random.randint(0,7) # 각 캐릭터 동기화 X
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 599), 900
        self.num = random.randint(1, 2)
        if self.num == 1:
            self.image = load_image('ball21x21.png')
        elif self.num == 2:
            self.image = load_image('ball41x41.png')

        self.i = random.randint(4, 14)
    def update(self):
        if self.num == 1:
            if self.y > 40:
                self.y -= self.i
        elif self.num == 2:
            if self.y > 50:
                self.y -= self.i
    def draw(self):
        if self.num == 1:
            self.image.clip_draw(0, 0, 21, 21, self.x, self.y)
        elif self.num == 2:
            self.image.clip_draw(0, 0, 41, 41, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def update_world():
    grass.update()
    for boy in team:
        boy.update()
    for ball in team2:
        ball.update()
    for o in world:
        o.update()
    pass

def render_world():
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in team2:
        ball.draw()
    for o in world:
        o.draw()
    update_canvas()

def reset_world(): # 초기화하는 함수
    global running
    global grass
    global team
    global team2
    global world

    running = True
    world = []
    grass = Grass() # Grass 클래스를 이용해서 grass 객체 생성
    world.append(grass)
    team = [ Boy() for i in range(11)] # 소년 11명으로 된 팀 생성
    team2 = [ Ball() for i in range(21)]
    world += team
    world += team2

open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)


# finalization code

close_canvas()
