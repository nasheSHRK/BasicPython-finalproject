import pgzrun
#pgzero
import random

cell = Actor('border')
size_w = 10
size_h = 10
FPS=30
HEIGHT=640
WIDTH=640
gm = 'm'
char = 0
enemys = []
lvln = 21
lv0 = 'lv0'
lv1 = 'lv1'
lv2 = 'lv2'
lv3 = 'lv3'
lv4 = 'lv4'
lv5 = 'lv5'
lv6 = 'lv6'

def create_enemies():
    for i in range(5):
        x = random.randint(2,7)* cell.width
        y = random.randint(2,7)* cell.height
        skin = 0
        if lvln < 3:
            skin = 0
        elif lvln >= 3 and lvln < 6:
            skin = random.randint(0,7)
        elif lvln >= 6 and lvln < 9:
            skin = random.randint(0,13)
        elif lvln >= 9 and lvln < 12:
            skin = random.randint(3,16)
        elif lvln >= 12 and lvln < 15:
            skin = random.randint(5,21)
        elif lvln >= 15 and lvln < 18:
            skin = random.randint(15,20)
        elif lvln >= 18 and lvln < 21:
            skin = random.randint(15,25)
        elif lvln >= 21:
            skin = random.randint(18,25)
            
        if skin <= 5:
            enemy = Actor(lv0, topleft = (x,y))
            enemy.hp = 30
            enemy.att = 10
            enemy.bonus = random.randint(0,2)
        elif skin <= 10 and skin > 5:
            enemy = Actor(lv1, topleft = (x,y))
            enemy.hp = random.randint(30,50)
            enemy.att = random.randint(10,15)
            enemy.bonus = random.randint(0,2)
        elif skin <= 14 and skin > 10 :
            enemy = Actor(lv2, topleft = (x,y))
            enemy.hp = random.randint(60,80)
            enemy.att = random.randint(15,20)
            enemy.bonus = random.randint(0,2)
        elif skin <= 17 and skin > 14 :
            enemy = Actor(lv3, topleft = (x,y))
            enemy.hp = random.randint(70,100)
            enemy.att = random.randint(20,25)
            enemy.bonus = random.randint(0,2)
        elif skin <= 20 and skin > 17 :
            enemy = Actor(lv4, topleft = (x,y))
            enemy.hp = random.randint(90,125)
            enemy.att = random.randint(25,30)
            enemy.bonus = random.randint(0,2)
        elif skin <= 23 and skin > 20 :
            enemy = Actor(lv5, topleft = (x,y))
            enemy.hp = random.randint(125,175)
            enemy.att = random.randint(30,35)
            enemy.bonus = random.randint(0,2)
        elif skin <= 25 and skin > 23 :
            enemy = Actor(lv6, topleft = (x,y))
            enemy.hp = random.randint(170,200)
            enemy.att = random.randint(40,50)
            enemy.bonus = random.randint(0,2)
        enemys.append(enemy)

lvl =[[0,0,0,0,0,0,0,0,0,0],
      [0,5,1,1,2,1,1,1,1,0],
      [0,1,1,1,1,1,1,1,1,0],
      [0,1,1,1,1,1,1,2,1,0],
      [0,1,1,1,1,3,1,1,1,0],
      [0,1,1,1,1,1,1,1,1,0],
      [0,1,1,1,1,1,1,1,1,0],
      [0,1,1,1,1,1,1,3,4,0],
      [0,0,0,0,0,0,0,0,0,0]]

menu=[[0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0]]
      
cell1=Actor('floor')
cell2=Actor('decor_cross')
cell3=Actor('decor_dagger')
cell4=Actor('decor_hammer')
cell5=Actor('decor_skull')

########### GUI ###########
hp_ico = Actor('hp', topleft= (0,580))
att_ico= Actor('att', topleft= (0,600))

skelly_small = Actor('skelly_icon', bottomright=(640,637))
#################################

########### MENU ###########
skelly_ico = Actor('skelly_icon', (100,200))
engi_ico = Actor('engi_icon', (100,300))
tux_ico = Actor('tux_icon', (100,400))
bike_ico = Actor('bike_icon', (100,500))
menuchar = Actor('p1', bottomright = (600, 637))
dialog = Actor('dialog', bottomleft= (0, 620))
bigMode = Actor('off_button', bottomright= (640,500))
bigMode.state = False
#################################

p1 = Actor('p1', topleft= (64,64))
p1.startpos = (96, 96)
p1.hp = 300
p1.maxhp = 300
p1.att = 50

def data_draw(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 0:
                cell.left = cell.width*j
                cell.top = cell.height*i
                cell.draw()
            elif data[i][j] == 1:
                cell1.left = cell.width*j
                cell1.top = cell.height*i
                cell1.draw()
            elif data[i][j] == 2:
                cell2.left = cell.width*j
                cell2.top = cell.height*i
                cell2.draw()
            elif data[i][j] == 3:
                cell3.left = cell.width*j
                cell3.top = cell.height*i
                cell3.draw()
            elif data[i][j] == 4:
                cell4.left = cell.width*j
                cell4.top = cell.height*i
                cell4.draw()
            elif data[i][j] == 5:
                cell5.left = cell.width*j
                cell5.top = cell.height*i
                cell5.draw()
        
def draw():
    screen.fill('black')
    global gm
    global lvln
    if gm == 'p':
        screen.draw.text('level '+str(lvln), center = (WIDTH/2, 605), fontsize = 25)
        data_draw(lvl)
        skelly_small.draw()
        p1.draw()
            
        for i in enemys:
            i.draw()
        if len(enemys) == 0 :
            lvln = lvln + 1
            p1.pos = topleft=(96,96)
            create_enemies()
            if lvln == 3 or lvln == 6 or lvln == 9 or lvln == 12 or lvln == 15 or lvln == 18 or lvln == 21:
                p1.maxhp += 25
            p1.hp = p1.maxhp

        screen.draw.text('        :' + str(p1.hp), topleft = (0,590), fontsize=20)
        hp_ico.draw()
        screen.draw.text('        :' + str(p1.att), topleft = (0,615), fontsize=20)
        att_ico.draw()
        
    elif gm == 'm':
        data_draw(menu)
        p1.hp = 100
        p1.att = 15
        p1.maxhp=100
        p1.pos = p1.startpos
        enemys.clear()
        lvln = 0
        screen.draw.text('Skeletons and Ninjas', center= (320,50), fontsize=30)
        screen.draw.text('Press enter to play', center=(320,75), fontsize=20)
        screen.draw.text('Choose your skin:', center=(100, 150),fontsize = 20)
        skelly_small.draw()
        screen.draw.text('Current skin:', bottomright=(640, 575))
        skelly_ico.draw()
        engi_ico.draw()
        tux_ico.draw()
        bike_ico.draw()
        screen.draw.text('1.Skelly', center = (100, 235), fontsize=15)
        screen.draw.text('2.Engineer', center = (100, 335), fontsize=15)
        screen.draw.text('3.Tuxedo', center = (100, 435), fontsize=15)
        screen.draw.text('4.Biker', center = (100, 535), fontsize=15)
        dialog.draw()
        screen.draw.text('Controls: WASD or Arrows, enter to start, delete to pause, p to unpause', bottomleft= (86,595), fontsize= 17)
        menuchar.draw()
        screen.draw.text('eldelgas31', bottomleft = (15, 630), fontsize= 17)
        bigMode.draw()
        screen.draw.text('"High Contrast" mode:', bottomright= (560,490))

    elif gm == 'pause':
        screen.draw.text('level '+str(lvln), center = (WIDTH/2, 605), fontsize = 25)
        data_draw(lvl)
        skelly_small.draw()
        p1.draw()
        for i in enemys:
            i.draw()
        if len(enemys) == 0 :
            lvln = lvln + 1
            p1.pos = topleft=(96,96)
            create_enemies()
        screen.draw.text('PAUSED', center = (WIDTH/2, 300), fontsize = 35)
        screen.draw.text('Press the "P" key to continue', center = (WIDTH/2, 350), fontsize = 25)
        dialog.draw()
        screen.draw.text('eldelgas31', bottomleft = (15, 630), fontsize= 17)
        tip = random.randint(1,6)
        if tip == 1:
            screen.draw.text('Test', bottomleft= (86,595), fontsize= 17)
        elif tip == 2:
            screen.draw.text('Fun Fact: I didnt have a drawing style before this game', bottomleft= (86,595), fontsize= 17)
        elif tip == 3:
            screen.draw.text('Tip: if youre low on health, kill the lower level enemies first', bottomleft= (86, 595), fontsize = 17)
        elif tip == 4:
            screen.draw.text('If you use the Esc key in this menu you will restart your game', bottomleft= (86,595), fontsize= 17)
        elif tip == 5:
            screen.draw.text('Kodland!!1!!1!', bottomleft= (86,595), fontsize= 17)
        elif tip == 6:
            screen.draw.text('White: lvl0, Yellow: lvl1, Orange: lvl2, Green: lvl3, Blue: lvl4, Brown: lvl5, Black: lvl6', bottomleft= (86,595), fontsize= 17)

        
def on_key_down(key):
    global gm
    if gm == 'pause':
        if keyboard.p:
            gm = 'p'
        if keyboard.ESCAPE:
            gm = 'm'
        
    if gm == 'm':
        if keyboard.RETURN:
            gm = 'p'
        if keyboard.k_1:
            p1.image = 'p1'
            skelly_small.image = 'skelly_icon'
        if keyboard.k_2:
            p1.image = 'p1_engi'
            skelly_small.image = 'engi_icon'
        if keyboard.k_3:
            p1.image = 'p1_tux'
            skelly_small.image = 'tux_icon'
        if keyboard.k_4:
            p1.image = 'p1_bike'
            skelly_small.image = 'bike_icon'

    if gm == 'p':
        old_x = p1.x
        old_y = p1.y
        
        if (keyboard.right or keyboard.d) and p1.x <= 576-cell.width :
            p1.x += cell.width
        if (keyboard.left or keyboard.a) and p1.x >= 33+cell.width :
            p1.x -= cell.width
        if (keyboard.up or keyboard.w) and p1.y > 33+cell.width:
            p1.y -= cell.height
        if (keyboard.down or keyboard.s) and p1.y <= 543-cell.height :
            p1.y += cell.height 
        if keyboard.Backspace:
            gm = 'pause'  
        enemy_index = p1.collidelist(enemys)
        if enemy_index != -1:
            p1.x = old_x
            p1.y = old_y
            enemy = enemys[enemy_index]
            enemy.hp -= p1.att
            p1.hp -= enemy.att
            if enemy.hp <= 0 :  
                if enemy.bonus == 1:
                    p1.hp += 30
                    if p1.hp > p1.maxhp:
                        p1.hp = p1.maxhp
                elif enemy.bonus == 2:
                    p1.att +=1
                enemys.pop(enemy_index)
            if p1.hp <= 0:
                gm = 'm'
    
def on_mouse_down(button, pos):
    global gm
    global bigMode
    global lv0
    global lv1
    global lv2
    global lv3
    global lv4
    global lv5
    global lv6
    if skelly_ico.collidepoint(pos):
        p1.image = 'p1'
        skelly_small.image = 'skelly_icon'
        menuchar.image = 'p1'
    if engi_ico.collidepoint(pos):
        p1.image = 'p1_engi'
        skelly_small.image = 'engi_icon'
        menuchar.image = 'p1_engi'
    if tux_ico.collidepoint(pos):
        p1.image = 'p1_tux'
        menuchar.image = 'p1_tux'
        skelly_small.image = 'tux_icon'
    if bike_ico.collidepoint(pos):
        p1.image = 'p1_bike'
        menuchar.image = 'p1_bike'
        skelly_small.image = 'bike_icon'
    if bigMode.collidepoint(pos) and bigMode.state == False:
        bigMode.image = 'on_button'
        bigMode.state = True
        lv0 = 'lvl0_big'
        lv1 = 'lvl1_big'
        lv2 = 'lvl2_big'
        lv3 = 'lvl3_big'
        lv4 = 'lvl4_big'
        lv5 = 'lvl5_big'
        lv6 = 'lvl6_big'

pgzrun.go()        