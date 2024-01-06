#
# MiniMetroid.py 2024/1/6
#
DEBUG_MODE = False
import pyxel
import pict
TM = 0  # TileMap
WIDTH,HEIGHT = 8*16,8*16  # ウインドウサイズ
SCRN_X,SCRN_Y,SCRN_W,SCRN_H,CNTR_X,CNTR_Y = 0,0,16*8,16*8,8*8,7*8  # 表示画面サイズ,中心
NO_DIR,LEFT,RIGHT,UP,DOWN = 0,1,2,3,4
BTN_ON,BTN_OFF,BTN_FORCE = 0,1,2
RET_NONE,RET_DEL,RET_BURST,RET_HIT,RET_SCREENIN,RET_SCREENOUT,RET_ATTACK,RET_ATKLEFT,RET_ATKRIGHT,RET_EXPLOTION = 0,101,102,103,104,105,106,107,108,109
RET_GLASSBREAK,RET_BRAINBREAK,RET_RIDLEYBEAT,RET_KRAIDBEAT = 201,202,203,204
RET_FIRE,RET_NEEDLE_UP,RET_NEEDLE_MID,RET_NEEDLE_LOW,RET_PLATE = 401,402,403,404,405
RET_DROPENERGY = 501
ZN_START = 0
ZN_ENDING = 15
ZN_NOBGM = (13,36,37)
ZN = { # Left,   Up,Right, Down, StartX, StartY
     0:(    0, 80*8, 48*8, 96*8, 24*8*4, 91*8*4),  # Start
     1:( 48*8, 80*8, 64*8,112*8, 50*8*4, 87*8*4),
     2:( 64*8, 80*8, 96*8, 96*8, 66*8*4, 87*8*4),
     3:( 96*8,    0,112*8, 96*8, 98*8*4, 87*8*4),
     4:( 64*8, 32*8, 96*8, 48*8, 93*8*4, 39*8*4),
     5:( 48*8, 32*8, 64*8, 48*8, 61*8*4, 39*8*4),
     6:( 48*8,    0, 96*8, 16*8, 93*8*4,  7*8*4),
     7:( 32*8,    0, 48*8, 48*8, 45*8*4,  7*8*4),
     8:( 16*8,    0, 32*8, 16*8, 29*8*4,  7*8*4),
     9:( 16*8, 16*8, 32*8, 64*8, 22*8*4, 22*8*4),
    10:( 32*8, 48*8, 80*8, 64*8, 34*8*4, 55*8*4),
    11:( 80*8, 48*8, 96*8, 80*8, 82*8*4, 55*8*4),
    12:( 48*8, 64*8, 80*8, 80*8, 77*8*4, 71*8*4),
    13:( 16*8, 64*8, 48*8, 80*8, 45*8*4, 71*8*4),
    14:(    0, 16*8, 16*8, 80*8, 13*8*4, 71*8*4),
    15:(    0,    0, 16*8, 16*8,  8*8*4, 11*8*4),  # Ending
    16:(112*8, 48*8,160*8, 64*8,114*8*4, 55*8*4),
    17:(160*8, 48*8,176*8, 80*8,162*8*4, 55*8*4),
    18:(176*8, 48*8,224*8, 64*8,178*8*4, 55*8*4),
    19:(224*8, 16*8,240*8, 64*8,226*8*4, 55*8*4),
    20:(192*8, 32*8,224*8, 48*8,221*8*4, 39*8*4),
    21:(176*8, 32*8,192*8, 48*8,189*8*4, 39*8*4),
    22:(112*8, 80*8,176*8, 96*8,114*8*4, 87*8*4),
    23:(176*8, 80*8,192*8, 96*8,178*8*4, 87*8*4),
    24:(112*8, 16*8,160*8, 32*8,114*8*4, 23*8*4),
    25:(160*8,    0,176*8, 32*8,162*8*4, 23*8*4),
    26:(176*8, 16*8,224*8, 32*8,178*8*4, 23*8*4),
    27:(128*8,    0,160*8, 16*8,157*8*4,  7*8*4),
    28:(112*8,    0,128*8, 16*8,125*8*4,  7*8*4),
    29:(128*8, 64*8,160*8, 80*8,157*8*4, 71*8*4),
    30:(112*8, 64*8,128*8, 80*8,125*8*4, 71*8*4),
    31:( 64*8, 96*8, 80*8,112*8, 66*8*4,103*8*4),
    32:( 64*8,112*8, 80*8,176*8, 70*8*4,119*8*4),
    33:(176*8, 96*8,192*8,128*8,182*8*4,103*8*4),
    34:(    0, 96*8, 32*8,128*8,  3*8*4,100*8*4),  # DEBUG
    35:( 48*8,160*8, 64*8,176*8, 61*8*4,167*8*4),
    36:( 32*8,160*8, 48*8,176*8, 44*8*4,169*8*4),
    37:(160*8,112*8,176*8,128*8,173*8*4,121*8*4),
    38:(128*8,112*8,160*8,128*8,157*8*4,119*8*4),
}
SCRL_MAP = {
        ( 46, 88):(RIGHT, 1), ( 49, 88):(LEFT, 0),
        ( 62, 88):(RIGHT, 2), ( 65, 88):(LEFT, 1),
        ( 94, 88):(RIGHT, 3), ( 97, 88):(LEFT, 2),
        ( 94, 40):(RIGHT, 3), ( 97, 40):(LEFT, 4),
        ( 62, 40):(RIGHT, 4), ( 65, 40):(LEFT, 5),
        ( 94,  8):(RIGHT, 3), ( 97,  8):(LEFT, 6),
        ( 46,  8):(RIGHT, 6), ( 49,  8):(LEFT, 7),
        ( 30,  8):(RIGHT, 7), ( 33,  8):(LEFT, 8),
        ( 30, 56):(RIGHT,10), ( 33, 56):(LEFT, 9),
        ( 78, 56):(RIGHT,11), ( 81, 56):(LEFT,10),
        ( 78, 72):(RIGHT,11), ( 81, 72):(LEFT,12),
        ( 46, 72):(RIGHT,12), ( 49, 72):(LEFT,13),
        ( 14, 72):(RIGHT,13), ( 17, 72):(LEFT,14),
        (110, 56):(RIGHT,16), (113, 56):(LEFT, 3),
        (158, 56):(RIGHT,17), (161, 56):(LEFT,16),
        (174, 56):(RIGHT,18), (177, 56):(LEFT,17),
        (222, 56):(RIGHT,19), (225, 56):(LEFT,18),
        (222, 40):(RIGHT,19), (225, 40):(LEFT,20),
        (190, 40):(RIGHT,20), (193, 40):(LEFT,21),
        (110, 88):(RIGHT,22), (113, 88):(LEFT, 3),
        (174, 88):(RIGHT,23), (177, 88):(LEFT,22),
        (110, 24):(RIGHT,24), (113, 24):(LEFT, 3),
        (158, 24):(RIGHT,25), (161, 24):(LEFT,24),
        (174, 24):(RIGHT,26), (177, 24):(LEFT,25),
        (222, 24):(RIGHT,19), (225, 24):(LEFT,26),
        (158,  8):(RIGHT,25), (161,  8):(LEFT,27),
        (126,  8):(RIGHT,27), (129,  8):(LEFT,28),
        (158, 72):(RIGHT,17), (161, 72):(LEFT,29),
        (126, 72):(RIGHT,29), (129, 72):(LEFT,30),
        ( 62,104):(RIGHT,31), ( 65,104):(LEFT, 1),
        ( 62,168):(RIGHT,32), ( 65,168):(LEFT,35),
        ( 46,168):(RIGHT,35), ( 49,168):(LEFT,36),
        (174,120):(RIGHT,33), (177,120):(LEFT,37),
        (158,120):(RIGHT,37), (161,120):(LEFT,38),
        ( 46, 40):(RIGHT, 5), ( 49, 40):(LEFT, 7),
}
ELEV_POS = {
    (  7*8+4, 22*8):(UP,  15,  7*8+4,    0), (  7*8+3, 22*8):(UP,  15,  7*8+4,    0), (  7*8+5, 22*8):(UP,  15,  7*8+4,    0),
    ( 23*8+4,  7*8):(DOWN, 9, 23*8+4, 22*8), ( 23*8+3,  7*8):(DOWN, 9, 23*8+4, 22*8), ( 23*8+5,  7*8):(DOWN, 9, 23*8+4, 22*8),
    ( 23*8+4, 22*8):(UP,   8, 23*8+4,  7*8), ( 23*8+3, 22*8):(UP,   8, 23*8+4,  7*8), ( 23*8+5, 22*8):(UP,   8, 23*8+4,  7*8),
    ( 71*8+4,103*8):(DOWN,32, 71*8+4,118*8), ( 71*8+3,103*8):(DOWN,32, 71*8+4,118*8), ( 71*8+5,103*8):(DOWN,32, 71*8+4,118*8),
    ( 71*8+4,118*8):(UP,  31, 71*8+4,103*8), ( 71*8+3,118*8):(UP,  31, 71*8+4,103*8), ( 71*8+5,118*8):(UP,  31, 71*8+4,103*8),
    (183*8+4, 87*8):(DOWN,33,183*8+4,102*8), (183*8+3, 87*8):(DOWN,33,183*8+4,102*8), (183*8+5, 87*8):(DOWN,33,183*8+4,102*8),
    (183*8+4,102*8):(UP,  23,183*8+4, 87*8), (183*8+3,102*8):(UP,  23,183*8+4, 87*8), (183*8+5,102*8):(UP,  23,183*8+4, 87*8),
    (    8+4, 92*8):(DOWN,34,    8+4, 99*8), (    8+3, 92*8):(DOWN,34,    8+4, 99*8), (    8+5, 92*8):(DOWN,34,    8+4, 99*8),  # DEBUG
    (    8+4, 99*8):(UP,   0,    8+4, 92*8), (    8+3, 99*8):(UP,   0,    8+4, 92*8), (    8+5, 99*8):(UP,   0,    8+4, 92*8),
}
BRIDGE_POS = ((38,9),(39,9),(40,9),(41,9),(42,9),(43,9),(44,9))

def ugettilemap(ux, uy):  # UserX, UserY
    if 0<=ux<4*8*256 and 0<=uy<4*8*256:
        return pyxel.tilemaps[TM].pget(ux//(4*8), uy//(4*8))
    return -1, -1

def psettilemap(px, py, tile):  # PyxelX, PyxelY
    if 0<=px<8*256 and 0<=py<8*256:
        pyxel.tilemaps[TM].pset(px//8, py//8, tile)

def pgettilemap(px, py):  # PyxelX, PyxelY
    if 0<=px<8*256 and 0<=py<8*256:
        return pyxel.tilemaps[TM].pget(px//8, py//8)
    return -1, -1

def cornertilemap(x, y, pw, ph):  # CornerX, CornerY, PyxelW, PyxelH
    topleft     = pgettilemap(x//4,      y//4     )
    topright    = pgettilemap(x//4+pw-1, y//4     )
    bottomleft  = pgettilemap(x//4,      y//4+ph-1)
    bottomright = pgettilemap(x//4+pw-1, y//4+ph-1)
    return topleft, topright, bottomleft, bottomright

def xy2scrn(x, y, zn, ux, uy):  # X, Y, Zone, UserX, UserY
    sx = x//4-ZN[zn][0]+SCRN_X if ux//4<ZN[zn][0]+CNTR_X else x//4-(ZN[zn][2]-SCRN_W)+SCRN_X if ux//4>ZN[zn][2]-(SCRN_W-CNTR_X) else x//4-(ux//4-CNTR_X)+SCRN_X
    sy = y//4-ZN[zn][1]+SCRN_Y if uy//4<ZN[zn][1]+CNTR_Y else y//4-(ZN[zn][3]-SCRN_H)+SCRN_Y if uy//4>ZN[zn][3]-(SCRN_H-CNTR_Y) else y//4-(uy//4-CNTR_Y)+SCRN_Y
    return sx, sy

def scrn_range(zn, ux, uy):  # Zone, UserX, UserY
    left   = ZN[zn][0] if ux//4<ZN[zn][0]+CNTR_X else ZN[zn][2]-SCRN_W if ux//4>ZN[zn][2]-(SCRN_W-CNTR_X) else ux//4-CNTR_X
    right  = left+SCRN_W
    top    = ZN[zn][1] if uy//4<ZN[zn][1]+CNTR_Y else ZN[zn][3]-SCRN_H if uy//4>ZN[zn][3]-(SCRN_H-CNTR_Y) else uy//4-CNTR_Y
    bottom = top+SCRN_H
    return left, right, top, bottom

def hit(ux, uy, uw, uh, ex, ey, ew, eh):  # UserX, UserY, UserW, UserH, EnemyX, EnemyX, EnemyW, EnemyH,
    return ex-uw<ux<ex+ew and ey-uh<uy<ey+eh

def user_hit(ux, uy, lx, ly, lw, lh, rx, ry, rw, rh, mb):  # UserX, UserY, LeftX, LeftY, LeftW, LeftH, RightX, RightY, RightW, RightH, MorphBall
    if mb:  # MorphBall
        if hit(ux,uy+9*4,3*4,6*4, rx,ry,rw,rh):  # ユーザ左接触
            return RET_ATKLEFT
        elif hit(ux+3*4,uy+9*4,3*4,6*4, lx,ly,lw,lh):  # ユーザ右接触
            return RET_ATKRIGHT
    else:
        if hit(ux,uy,3*4,16*4, rx,ry,rw,rh):  # ユーザ左接触
            return RET_ATKLEFT
        elif hit(ux+3*4,uy,3*4,16*4, lx,ly,lw,lh):  # ユーザ右接触
            return RET_ATKRIGHT

def dir16(x, y, m=1):
    if x==0:
        if y<0:
            return 0, -3*m
        else:
            return 0, 3*m
    else:
        a = pyxel.atan2(y, x)
        if a<-170:
            return -3*m, 0
        elif a<-150:
            return -3*m, -m
        elif a<-120:
            return -2*m, -2*m
        elif a<-100:
            return -m, -3*m
        elif a<-80:
            return 0, -3*m
        elif a<-60:
            return m, -3*m
        elif a<-30:
            return 2*m, -2*m
        elif a<-10:
            return 3*m, -m
        elif a<10:
            return 3*m, 0
        elif a<30:
            return 3*m, m
        elif a<60:
            return 2*m, 2*m
        elif a<80:
            return m, 3*m
        elif a<100:
            return 0, 3*m
        elif a<120:
            return -m, 3*m
        elif a<150:
            return -2*m, 2*m
        elif a<170:
            return -3*m, m
        else:
            return -3*m, 0

TIME_BREAKABLE = 100  # ブロックが元に戻るまでの時間
class Breakable:
    def __init__(self, px, py, tm_broken1, tm_broken2):
        self.px, self.py, self.tm_broken1, self.tm_broken2 = px, py, tm_broken1, tm_broken2
        self.cnt = TIME_BREAKABLE
        self.tm_breakable = pgettilemap(self.px, self.py)
    def update(self):
        self.cnt -= 1
        if self.cnt==TIME_BREAKABLE-1:
            psettilemap(self.px, self.py, self.tm_broken1)
        elif self.cnt==TIME_BREAKABLE-2:
            psettilemap(self.px, self.py, self.tm_broken2)
        elif self.cnt==TIME_BREAKABLE-4:
            psettilemap(self.px, self.py, pict.TM_SPACE)
        elif self.cnt==4:
            psettilemap(self.px, self.py, self.tm_broken2)
        elif self.cnt==2:
            psettilemap(self.px, self.py, self.tm_broken1)
        elif self.cnt<=0:
            return RET_DEL
        return RET_NONE
    def __del__(self):
        psettilemap(self.px, self.py, self.tm_breakable)

TIME_DOOR = 100  # ドアが閉じるまでの時間
class Door:
    def __init__(self, tx, ty, col):
        self.col = col
        self.cnt = TIME_DOOR
        self.txy_list = [(tx,ty),(tx,ty+1),(tx,ty+2),(tx+3,ty),(tx+3,ty+1),(tx+3,ty+2)]
        self.tm_door  = [pyxel.tilemaps[TM].pget(*txy) for txy in self.txy_list]

    def update(self):
        self.cnt -= 1
        if self.cnt==TIME_BREAKABLE-4:
            for txy, tm in zip(self.txy_list, pict.TM_DOOR_AJAR[self.col]):
                pyxel.tilemaps[TM].pset(*txy, tm)
        elif self.cnt==TIME_BREAKABLE-8:
            for txy in self.txy_list:
                pyxel.tilemaps[TM].pset(*txy, pict.TM_SPACE)
        elif self.cnt==4:
            for txy, tm in zip(self.txy_list, pict.TM_DOOR_AJAR[self.col]):
                pyxel.tilemaps[TM].pset(*txy, tm)
        elif self.cnt<=0:
            return RET_DEL
        return RET_NONE

    def __del__(self):
        for txy, tm in zip(self.txy_list, self.tm_door):
            pyxel.tilemaps[TM].pset(*txy, tm)

SCRN_IN, SCRN_OUT = 4*8, 5*8
class BaseEnemy:
    def setscreen(self, zn, ux, uy):  # 画面内敵セット
        lt, rt, tp, bm = scrn_range(zn, ux, uy)
        if lt-SCRN_IN<=self.init_x//4<rt+SCRN_IN and tp-SCRN_IN<=self.init_y//4<bm+SCRN_IN:
            self.reset()
            self.setdxdy(ux, uy)
    def screenin(self, zn, ux, uy):  # スクリーンイン：RETURN
        lt, rt, tp, bm = scrn_range(zn, ux, uy)
        if (lt-SCRN_OUT<=self.init_x//4<lt-SCRN_IN and tp<=self.init_y//4<bm) or (rt+SCRN_IN<=self.init_x//4<rt+SCRN_OUT and tp<=self.init_y//4<bm) or \
                (tp-SCRN_OUT<=self.init_y//4<tp-SCRN_IN and lt<=self.init_x//4<rt) or (bm+SCRN_IN<=self.init_y//4<bm+SCRN_OUT and lt<=self.init_x//4<rt):
            self.reset()
            self.setdxdy(ux, uy)
            return RET_SCREENIN
        return RET_NONE
    def screenout(self, zn, ux, uy):  # スクリーンアウト：RETURN
        lt, rt, tp, bm = scrn_range(zn, ux, uy)
        if self.x//4<lt-SCRN_OUT or rt+SCRN_OUT<=self.x//4 or self.y//4<tp-SCRN_OUT or bm+SCRN_OUT<=self.y//4:
            self.life = 0
            return RET_SCREENOUT
        return RET_NONE
    def damage(self, bx, by, bw, bh, dmg):  # BeamX, BeamY, BeamW, BeamH, Damage：RETURN
        if self.life>0 and hit(bx,by,bw,bh, self.x//4,self.y//4,self.w,self.h):
            self.life -= dmg
            if self.life<=0:
                self.life = -10
            else:
                self.stan = 20
            return RET_HIT
        return RET_NONE

class EnergyBall(BaseEnemy):
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.ptn = 0
    def update(self, zn, ux, uy, udx, udy, mb):  # Zone, UserX, UserY, UserDX, UserDY, MorphBall
        self.ptn += 1
        if self.screenout(zn, ux, uy) or self.ptn>300:
            return RET_DEL
        ret = user_hit(ux,uy, self.x,self.y,self.w//2*4,self.h*4, self.x+self.w//2*4,self.y,self.w//2*4,self.h*4, mb)
        if ret in (RET_ATKLEFT, RET_ATKRIGHT):
            return RET_HIT
        return RET_NONE
    def draw(self, zn, ux, uy):  # Zone, UserX, UserY
        if self.ptn<230 or self.ptn//3%2:
            sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
            pict.energyball(sx, sy, self.ptn//2)

class Zoomer(BaseEnemy):
    def reset(self):
        self.x, self.y, self.cont = self.init_x, self.init_y, self.init_cont 
        self.dx, self.dy, self.ptn, self.stan = 0, 0, 0, 0
        self.life = 6
    def setdxdy(self, ux, uy):
        if self.cont in (DOWN, UP):
            self.dx = -2 if ux<self.x else 2
        else:
            self.dy = -2 if uy<self.y else 2
    def __init__(self, x, y, w, h):
        self.init_x, self.init_y, self.w, self.h = x, y, w, h
        self.atk_pt = 40
        if pgettilemap(x//4+4, y//4+h) in pict.TM_NOMOVE:
            self.init_cont = DOWN
        elif pgettilemap(x//4+4, y//4-1) in pict.TM_NOMOVE:
            self.init_cont = UP
        elif pgettilemap(x//4+w, y//4+4) in pict.TM_NOMOVE:
            self.init_cont = RIGHT
        elif pgettilemap(x//4-1, y//4+4) in pict.TM_NOMOVE:
            self.init_cont = LEFT
        self.reset()
        self.life = 0
    def update(self, zn, ux, uy, udx, udy, mb):  # Zone, UserX, UserY, UserDX, UserDY, MorphBall
        if self.life==0:  # 死亡：RETURN
            if self.screenin(zn, ux, uy):
                return RET_SCREENIN
        elif self.life<0:  # 消滅：RETURN
            self.life += 1
            self.ptn += 1
            if self.life==0:
                if pyxel.rndi(0,2):
                    return RET_NONE
                else:
                    return RET_DROPENERGY
        elif self.stan:  # ダメージ
            self.stan -= 1
        else:  # 生存
            self.ptn += 1
            if self.cont==DOWN:
                left1, right1, left2, right2 = cornertilemap(self.x+self.dx, self.y, self.w, self.h)
                _, _, bottom1, bottom2 = cornertilemap(self.x, self.y+4, self.w, self.h)  # 直下
                if not bottom1 in pict.TM_NOMOVE and not bottom2 in pict.TM_NOMOVE:  # 下接触なし
                    self.x, self.y = self.x//4*4, self.y//4*4+4
                    self.dx, self.dy, self.cont = 0, 2, RIGHT if self.dx<0 else LEFT
                elif (self.dx<0 and (left1 in pict.TM_NOMOVE or left2 in pict.TM_NOMOVE)) or \
                        (self.dx>0 and (right1 in pict.TM_NOMOVE or right2 in pict.TM_NOMOVE)):  # 障害物あり
                    self.dx, self.dy, self.cont = 0, -2, LEFT if self.dx<0 else RIGHT
                else:
                    self.x += self.dx
            elif self.cont==UP:
                left1, right1, left2, right2 = cornertilemap(self.x+self.dx, self.y, self.w, self.h)
                top1, top2, _, _ = cornertilemap(self.x, self.y-4, self.w, self.h)  # 直上
                if not top1 in pict.TM_NOMOVE and not top2 in pict.TM_NOMOVE:  # 上接触なし
                    self.x, self.y = self.x//4*4, self.y//4*4-4
                    self.dx, self.dy, self.cont = 0, -2, RIGHT if self.dx<0 else LEFT
                elif (self.dx<0 and (left1 in pict.TM_NOMOVE or left2 in pict.TM_NOMOVE)) or \
                        (self.dx>0 and (right1 in pict.TM_NOMOVE or right2 in pict.TM_NOMOVE)):  # 障害物あり
                    self.dx, self.dy, self.cont = 0, 2, LEFT if self.dx<0 else RIGHT
                else:
                    self.x += self.dx
            elif self.cont==RIGHT:
                top1, top2, bottom1, bottom2 = cornertilemap(self.x, self.y+self.dy, self.w, self.h)
                _, right1, _, right2 = cornertilemap(self.x+4, self.y, self.w, self.h)  # 直右
                if not right1 in pict.TM_NOMOVE and not right2 in pict.TM_NOMOVE:  # 右接触なし
                    self.x, self.y = self.x//4*4+4, self.y//4*4
                    self.dx, self.dy, self.cont = 2, 0, DOWN if self.dy<0 else UP
                elif (self.dy<0 and (top1 in pict.TM_NOMOVE or top2 in pict.TM_NOMOVE)) or \
                        (self.dy>0 and (bottom1 in pict.TM_NOMOVE or bottom2 in pict.TM_NOMOVE)):  # 障害物あり
                    self.dx, self.dy, self.cont = -2, 0, UP if self.dy<0 else DOWN
                else:
                    self.y += self.dy
            elif self.cont==LEFT:
                top1, top2, bottom1, bottom2 = cornertilemap(self.x, self.y+self.dy, self.w, self.h)
                left1, _, left2, _ = cornertilemap(self.x-4, self.y, self.w, self.h)  # 直左
                if not left1 in pict.TM_NOMOVE and not left2 in pict.TM_NOMOVE:  # 左接触なし
                    self.x, self.y = self.x//4*4-4, self.y//4*4
                    self.dx, self.dy, self.cont = -2, 0, DOWN if self.dy<0 else UP
                elif (self.dy<0 and (top1 in pict.TM_NOMOVE or top2 in pict.TM_NOMOVE)) or \
                        (self.dy>0 and (bottom1 in pict.TM_NOMOVE or bottom2 in pict.TM_NOMOVE)):  # 障害物あり
                    self.dx, self.dy, self.cont = 2, 0, UP if self.dy<0 else DOWN
                else:
                    self.y += self.dy
            if self.screenout(zn, ux, uy):
                return RET_SCREENOUT
            ret = user_hit(ux,uy, self.x,self.y,self.w//2*4,self.h*4, self.x+self.w//2*4,self.y,self.w//2*4,self.h*4, mb)
            if ret in (RET_ATKLEFT, RET_ATKRIGHT):
                return ret
        return RET_NONE
    def draw(self, zn, ux, uy):
        if self.life<0:
            if self.ptn%3==0:
                sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
                pict.burst(sx-4, sy-4)
        elif self.life>0 and not self.stan//2%2:
            sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
            pict.zoomer(sx, sy, self.cont, self.ptn//4)

class Skree(BaseEnemy):
    def reset(self):
        self.x, self.y = self.init_x, self.init_y 
        self.ptn, self.stan, self.dive = 0, 0, 0
        self.life = 9
    def setdxdy(self, ux, uy):
        pass
    def __init__(self, x, y, w, h):
        self.init_x, self.init_y, self.w, self.h = x, y, w, h
        self.atk_pt = 40
        self.reset()
        self.life = 0
    def update(self, zn, ux, uy, udx, udy, mb):  # Zone, UserX, UserY, UserDX, UserDY, MorphBall
        if self.life==0:  # 死亡：RETURN
            if self.screenin(zn, ux, uy):
                return RET_SCREENIN
        elif self.life<0:  # 消滅
            self.life += 1
            self.ptn += 1
            if self.life==0:
                if pyxel.rndi(0,1):
                    return RET_NONE
                else:
                    return RET_DROPENERGY
        elif self.stan:  # ダメージ
            self.stan -= 1
        else:  # 生存
            self.ptn += 1
            if self.dive==1:  # 降下
                dx = 3 if self.x<ux else -3 if self.x>ux else 0
                tl, tr, bl, br = cornertilemap(self.x+dx, self.y, self.w, self.h)
                if (dx>0 and not tr in pict.TM_NOMOVE and not br in pict.TM_NOMOVE) or (dx<0 and not tl in pict.TM_NOMOVE and not bl in pict.TM_NOMOVE):
                    self.x += dx
                dy = 10
                _, _, bl, br = cornertilemap(self.x, self.y+dy, self.w, self.h)
                if not bl in pict.TM_NOMOVE and not br in pict.TM_NOMOVE:
                    self.y += dy
                else:
                    self.dive = 2  # 接地
            if self.dive>=2:
                self.dive += 1
                if self.dive>50:
                    self.life = 0
                    return RET_EXPLOTION
            if self.screenout(zn, ux, uy):
                return RET_SCREENOUT
            if self.dive==0 and self.x-2*8*4<=ux<self.x+2*8*4:
                self.dive = 1 
            ret = user_hit(ux,uy, self.x,self.y,self.w//2*4,self.h*4, self.x+self.w//2*4,self.y,self.w//2*4,self.h*4, mb)
            if ret in (RET_ATKLEFT, RET_ATKRIGHT):
                return ret
        return RET_NONE
    def draw(self, zn, ux, uy):  # Zone, UserX, UserY
        if self.life<0:
            if self.ptn%3==0:
                sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
                pict.burst(sx-4, sy-2)
        elif self.life>0 and not self.stan//2%2:
            sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
            pict.skree(sx, sy, self.ptn//2 if self.dive else self.ptn//6)

class Explotion:
    def setscreen(self, zn, ux, uy):  # 画面内敵セット
        pass
    def damage(self, bx, by, bw, bh, dmg):  # BeamX,BeamY,BeamW,BeamH,Damage：RETURN
        return RET_NONE
    def __init__(self, x, y):
        self.x1,self.y1, self.x2,self.y2, self.x3,self.y3, self.x4,self.y4 = x-4*4,y+4*4, x+8*4, y+4*4, x-4*4,y-4*4, x+8*4,y-4*4
        self.atk_pt = 40
        self.cnt = 10
    def update(self, zn, ux, uy, udx, udy, mb):  # Zone, UserX, UserY, UserDX, UserDY, MorphBall
        self.cnt -= 1
        if self.cnt==0:
            return RET_DEL
        self.x1 -= 12
        self.x2 += 12
        self.x3 -= 4
        self.y3 -= 10
        self.x4 += 4
        self.y4 -= 10
        ret = user_hit(ux,uy, self.x1,self.y1,2*4,4*4, self.x1+2*4,self.y1,2*4,4*4, mb)
        if ret in (RET_ATKLEFT, RET_ATKRIGHT):
            return ret
        ret = user_hit(ux,uy, self.x2,self.y2,2*4,4*4, self.x2+2*4,self.y2,2*4,4*4, mb)
        if ret in (RET_ATKLEFT, RET_ATKRIGHT):
            return ret
        ret = user_hit(ux,uy, self.x3,self.y3,2*4,4*4, self.x3+2*4,self.y3,2*4,4*4, mb)
        if ret in (RET_ATKLEFT, RET_ATKRIGHT):
            return ret
        ret = user_hit(ux,uy, self.x4,self.y4,2*4,4*4, self.x4+2*4,self.y4,2*4,4*4, mb)
        if ret in (RET_ATKLEFT, RET_ATKRIGHT):
            return ret
        return RET_NONE
    def draw(self, zn, ux, uy):  # Zone, UserX, UserY
        sx, sy = xy2scrn(self.x1, self.y1, zn, ux, uy)
        pict.explotion(sx, sy)
        sx, sy = xy2scrn(self.x2, self.y2, zn, ux, uy)
        pict.explotion(sx, sy)
        sx, sy = xy2scrn(self.x3, self.y3, zn, ux, uy)
        pict.explotion(sx, sy)
        sx, sy = xy2scrn(self.x4, self.y4, zn, ux, uy)
        pict.explotion(sx, sy)

class Reo(BaseEnemy):
    def reset(self):
        self.x, self.y = self.init_x, self.init_y 
        self.dx, self.dy, self.ptn, self.stan, self.dive = 0, 0, 0, 0, False
        self.life = 9
    def setdxdy(self, ux, uy):
        pass
    def __init__(self, x, y, w, h):
        self.init_x, self.init_y, self.w, self.h = x, y, w, h
        self.atk_pt = 40
        self.reset()
        self.life = 0
    def update(self, zn, ux, uy, udx, udy, mb):  # Zone, UserX, UserY, UserDX, UserDY, MorphBall
        if self.life==0:  # 死亡
            if self.screenin(zn, ux, uy):
                return RET_SCREENIN
        elif self.life<0:  # 消滅
            self.life += 1
            self.ptn += 1
            if self.life==0:
                if pyxel.rndi(0,1):
                    return RET_NONE
                else:
                    return RET_DROPENERGY
        elif self.stan:  # ダメージ
            self.stan -= 1
        else:  # 生存
            self.ptn += 1
            if not self.dive and self.x-3*8*4<=ux<self.x+3*8*4:  # 近づくと降下
                self.dive = True
                self.dy = pyxel.rndi(22, 26)
                self.dx = pyxel.rndi(3, 4) if self.x<ux else pyxel.rndi(-4, -3)
            elif self.dive:
                if self.dx:
                    ul, ur, bl, br = cornertilemap(self.x+self.dx, self.y, self.w, self.h)
                    if (self.dx>0 and not ur in pict.TM_NOMOVE and not br in pict.TM_NOMOVE) or (self.dx<0 and not ul in pict.TM_NOMOVE and not bl in pict.TM_NOMOVE):
                        self.x += self.dx
                self.dy -= 1
                if self.dy:
                    if self.dy<-11:
                        self.dy = -11
                    ul, ur, bl, br = cornertilemap(self.x, self.y+self.dy, self.w, self.h)
                    if self.dy>0:  # 降下
                        if not bl in pict.TM_NOMOVE and not br in pict.TM_NOMOVE:  # 下障害物なし
                            self.y += self.dy
                        else:
                            self.dy = 0
                    else:  # 上昇
                        if not ul in pict.TM_NOMOVE and not ur in pict.TM_NOMOVE:  # 上障害物なし
                            self.y += self.dy
                        else:
                            self.dive = False  # 天井
            if self.screenout(zn, ux, uy):
                return RET_SCREENOUT
            ret = user_hit(ux,uy, self.x,self.y,self.w//2*4,self.h*4, self.x+self.w//2*4,self.y,self.w//2*4,self.h*4, mb)
            if ret in (RET_ATKLEFT, RET_ATKRIGHT):
                return ret
        return RET_NONE
    def draw(self, zn, ux, uy):  # Zone, UserX, UserY
        if self.life<0:
            if self.ptn%3==0:
                sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
                pict.burst(sx-2, sy-3)
        elif self.life>0 and not self.stan//2%2:
            sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
            pict.reo(sx, sy, self.ptn//2 if self.dive else self.ptn//6)

class Ripper(BaseEnemy):
    def reset(self):
        self.x, self.y = self.init_x, self.init_y 
        self.atk_pt = 40
        self.ptn, self.stan = 0, 0
        self.life = 500
    def setdxdy(self, ux, uy):
        self.dx = -2 if ux<self.x else 2
    def __init__(self, x, y, w, h):
        self.init_x, self.init_y, self.w, self.h = x, y, w, h
        self.reset()
        self.life = 0
    def update(self, zn, ux, uy, udx, udy, mb):  # Zone, UserX, UserY, UserDX, UserDY, MorphBall
        if self.life==0:  # 死亡
            if self.screenin(zn, ux, uy):
                return RET_SCREENIN
        elif self.life<0:  # 消滅
            self.life += 1
            self.ptn += 1
            if self.life==0:
                if pyxel.rndi(0,2):
                    return RET_NONE
                else:
                    return RET_DROPENERGY
        elif self.stan:  # ダメージ
            self.stan -= 1
        else:  # 生存
            ul, ur, bl, br = cornertilemap(self.x+self.dx, self.y, self.w, self.h)
            if (self.dx>0 and not ur in pict.TM_NOMOVE and not br in pict.TM_NOMOVE) or (self.dx<0 and not ul in pict.TM_NOMOVE and not bl in pict.TM_NOMOVE):
               self.x += self.dx
            else:
                self.dx *= -1
            if self.screenout(zn, ux, uy):
                return RET_SCREENOUT
            ret = user_hit(ux,uy, self.x,self.y,self.w//2*4,self.h*4, self.x+self.w//2*4,self.y,self.w//2*4,self.h*4, mb)
            if ret in (RET_ATKLEFT, RET_ATKRIGHT):
                return ret
        return RET_NONE
    def draw(self, zn, ux, uy):  # Zone, UserX, UserY
        if self.life<0:
            if self.ptn%3==0:
                sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
                pict.burst(sx-4, sy-6)
        elif self.life>0 and not self.stan//2%2:
            sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
            pict.ripper(sx, sy, self.dx)

class Waver(BaseEnemy):
    def reset(self):
        self.x, self.y = self.init_x, self.init_y 
        self.dx, self.dy, self.maxdy, self.ptn, self.stan = 0, 0, 0, 0, 0
        self.life = 9
    def setdxdy(self, ux, uy):
        self.dx = -4 if ux<self.x else 4
        self.dy = 0
        self.maxdy = pyxel.rndi(-9,-7) if uy<self.y else pyxel.rndi(7,9)
    def __init__(self, x, y, w, h):
        self.init_x, self.init_y, self.w, self.h = x, y, w, h
        self.atk_pt = 40
        self.reset()
        self.life = 0
    def update(self, zn, ux, uy, udx, udy, mb):  # Zone, UserX, UserY, UserDX, UserDY, MorphBall
        if self.life==0:  # 死亡
            if self.screenin(zn, ux, uy):
                return RET_SCREENIN
        elif self.life<0:  # 消滅
            self.life += 1
            self.ptn += 1
            if self.life==0:
                if pyxel.rndi(0,2):
                    return RET_NONE
                else:
                    return RET_DROPENERGY
        elif self.stan:  # ダメージ
            self.stan -= 1
        else:  # 生存
            self.ptn += 1
            if self.maxdy<0:
                self.dy -= 1
                if self.dy<self.maxdy:
                    self.maxdy = pyxel.rndi(7,9)
            else:
                self.dy += 1
                if self.dy>self.maxdy:
                    self.maxdy = pyxel.rndi(-9,-7)
            ul, ur, bl, br = cornertilemap(self.x, self.y+self.dy, self.w, self.h)
            if (self.dy>0 and not bl in pict.TM_NOMOVE and not br in pict.TM_NOMOVE) or (self.dy<0 and not ul in pict.TM_NOMOVE and not ur in pict.TM_NOMOVE):
                self.y += self.dy
            ul, ur, bl, br = cornertilemap(self.x+self.dx, self.y, self.w, self.h)
            if (self.dx>0 and not ur in pict.TM_NOMOVE and not br in pict.TM_NOMOVE) or (self.dx<0 and not ul in pict.TM_NOMOVE and not bl in pict.TM_NOMOVE):
                self.x += self.dx
            else:
                self.dx *= -1
            if self.screenout(zn, ux, uy):
                return RET_SCREENOUT
            ret = user_hit(ux,uy, self.x,self.y,self.w//2*4,self.h*4, self.x+self.w//2*4,self.y,self.w//2*4,self.h*4, mb)
            if ret in (RET_ATKLEFT, RET_ATKRIGHT):
                return ret
        return RET_NONE
    def draw(self, zn, ux, uy):  # Zone, UserX, UserY
        if self.life<0:
            if self.ptn%3==0:
                sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
                pict.burst(sx-4, sy-4)
        elif self.life>0 and not self.stan//2%2:
            sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
            p = self.ptn//4%16
            pict.waver(sx, sy, self.dx, 1 if p in (0,1) else 2 if p==2 else 0)

class Zeb(BaseEnemy):
    def reset(self):
        self.x, self.y = self.init_x, self.init_y 
        self.dx, self.dy, self.ptn, self.stan, self.appr_cnt = 0, 0, 0, 0, 30
        self.life = 3
    def setscreen(self, zn, ux, uy):  # 画面内敵セット
        pass
    def __init__(self, x, y, w, h):
        self.init_x, self.init_y, self.w, self.h = x, y, w, h
        self.atk_pt = 40
        self.reset()
        self.life = 0
    def update(self, zn, ux, uy, udx, udy, mb):  # Zone, UserX, UserY, UserDX, UserDY, MorphBall
        if self.life==0:  # 死亡
            if self.init_x-4*8*4<=ux<self.init_x+4*8*4:  # 4ブロック以内ユーザ近づくと羽ばたく
                self.appr_cnt -= 1
                if self.appr_cnt==0:
                    self.reset()
                    self.dy = -8
                    self.dx = 8 if self.x<ux else -8
        elif self.life<0:  # 消滅
            self.life += 1
            self.ptn += 1
            if self.life==0:
                if pyxel.rndi(0,4):
                    return RET_NONE
                else:
                    return RET_DROPENERGY
        elif self.stan:  # ダメージ
            self.stan -= 1
        else:  # 生存
            self.ptn += 1
            if self.dy:  # dy<0
                self.y += self.dy
                if self.y<uy+5*4:
                    self.dy = 0
                    self.wait_cnt = 10
            elif self.dx:
                self.wait_cnt -= 1
                if self.wait_cnt<0:
                    self.x += self.dx
            if self.screenout(zn, ux, uy):
                return RET_SCREENOUT
            ret = user_hit(ux,uy, self.x,self.y,self.w//2*4,self.h*4, self.x+self.w//2*4,self.y,self.w//2*4,self.h*4, mb)
            if ret in (RET_ATKLEFT, RET_ATKRIGHT):
                return ret
        return RET_NONE
    def draw(self, zn, ux, uy):  # Zone, UserX, UserY
        if self.life<0:
            if self.ptn%3==0:
                sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
                pict.burst(sx-4, sy-2)
        elif self.life>0 and not self.stan//2%2:
            sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
            pict.zeb(sx, sy, self.dx, self.ptn//2)

class Mellow(BaseEnemy):
    def reset(self):
        self.x, self.y = self.init_x, self.init_y 
        self.dx, self.dy, self.maxdy, self.ptn, self.stan, self.dive = 0, 0, 0, 0, 0, False
        self.life = 6
    def setdxdy(self, ux, uy):
        pass
    def __init__(self, x, y, w, h):
        self.init_x, self.init_y, self.w, self.h = x, y, w, h
        self.atk_pt = 40
        self.reset()
        self.life = 0
    def update(self, zn, ux, uy, udx, udy, mb):  # Zone, UserX, UserY, UserDX, UserDY, MorphBall
        if self.life==0:  # 死亡
            if self.screenin(zn, ux, uy):
                return RET_SCREENIN
        elif self.life<0:  # 消滅
            self.life += 1
            self.ptn += 1
            if self.life==0:
                if pyxel.rndi(0,2):
                    return RET_NONE
                else:
                    return RET_DROPENERGY
        elif self.stan:  # ダメージ
            self.stan -= 1
        else:  # 生存
            self.ptn += 1
            if not self.dive:  # 上空
                if self.x-3*8*4<=ux<self.x+3*8*4:  # 近づくと降下
                    self.dive = True
                    self.dx = pyxel.rndi(3, 4) if self.x<ux else pyxel.rndi(-4, -3)
                    self.dy = pyxel.rndi(18, 22)
                else:  # ランダムウォーク
                    self.dx = pyxel.rndi(-8, 8)
                    self.dy = pyxel.rndi(-4, 4)
            else:  # 降下
                self.dy -= 1
            if self.dx:
                ul, ur, bl, br = cornertilemap(self.x+self.dx, self.y, self.w, self.h)
                if (self.dx>0 and not ur in pict.TM_NOMOVE and not br in pict.TM_NOMOVE) or (self.dx<0 and not ul in pict.TM_NOMOVE and not bl in pict.TM_NOMOVE):
                    self.x += self.dx
            if self.dy:
                if self.dy<-11:
                    self.dy = -11
                ul, ur, bl, br = cornertilemap(self.x, self.y+self.dy, self.w, self.h)
                if self.dy>0:  # 降下
                    if not bl in pict.TM_NOMOVE and not br in pict.TM_NOMOVE:  # 下障害物なし
                        self.y += self.dy
                    elif self.dive:
                        self.dy = 0
                else:  # 上昇
                    if not ul in pict.TM_NOMOVE and not ur in pict.TM_NOMOVE:  # 上障害物なし
                        if self.dive and self.y<self.init_y:  # 元の高さ
                            self.dive = False
                        else:
                            self.y += self.dy
                    else:  # 上障害物あり
                        if self.dive:
                            self.dive = False
            if self.screenout(zn, ux, uy):
                return RET_SCREENOUT
            ret = user_hit(ux,uy, self.x,self.y,self.w//2*4,self.h*4, self.x+self.w//2*4,self.y,self.w//2*4,self.h*4, mb)
            if ret in (RET_ATKLEFT, RET_ATKRIGHT):
                return ret
        return RET_NONE
    def draw(self, zn, ux, uy):  # Zone, UserX, UserY
        if self.life<0:
            if self.ptn%3==0:
                sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
                pict.burst(sx-4, sy-6)
        elif self.life>0 and not self.stan//2%2:
            sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
            pict.mellow(sx, sy, self.ptn//2)

class Cannon(BaseEnemy):
    def setscreen(self, zn, ux, uy):  # 画面内敵セット
        pass
    def reset(self):
        self.x, self.y = self.init_x, self.init_y 
        self.stan, self.life = 0, 6
        self.x += self.dx*6
        self.y += self.dy*6
    def setdxdy(self, ux, uy):
        pass
    def __init__(self, x, y, w, h, dirc):
        self.init_x, self.init_y, self.w, self.h, self.dirc = x, y, w, h, dirc
        self.atk_pt = 60
        self.cnt = pyxel.rndi(0,319)
        if dirc==0:  # 左下
            self.dx, self.dy, self.seq = -4, 4, (0,1,0,7,6,5,6,7)
        elif dirc==1:  # 下
            self.dx, self.dy, self.seq = 0, 6, (1,2,3,2,1,0,7,0)
        else:  # dirc==2: 右下
            self.dx, self.dy, self.seq = 4, 4, (2,1,2,3,4,5,4,3)  # (2,3,4,5,4,3,2,1)
        self.reset()
        self.life = 0
    def update(self, zn, ux, uy, udx, udy, mb):  # Zone, UserX, UserY, UserDX, UserDY, MorphBall
        self.cnt += pyxel.rndi(1,2)
        if self.life==0:  # 死亡
            if (self.init_x-8*8*4<=ux<self.init_x+8*8*4 and self.init_y-8*8*4<=uy<self.init_y+8*8*4) and self.cnt//40%8==0:  # 8ブロック以下発射
                self.reset()
                return RET_SCREENIN
        elif self.life<0:  # 消滅
            self.life += 1
            if self.life==0:
                return RET_NONE
        elif self.stan:  # ダメージ
            self.stan -= 1
        else:  # 生存
            self.x += self.dx
            self.y += self.dy
            tl, tr, bl, br = cornertilemap(self.x, self.y, self.w, self.h)
            if tl in pict.TM_NOMOVE or tr in pict.TM_NOMOVE or bl in pict.TM_NOMOVE or br in pict.TM_NOMOVE:  # 障害物あり
                self.life = -10
            if self.screenout(zn, ux, uy):
                return RET_SCREENOUT
            ret = user_hit(ux,uy, self.x,self.y,self.w//2*4,self.h*4, self.x+self.w//2*4,self.y,self.w//2*4,self.h*4, mb)
            if ret in (RET_ATKLEFT, RET_ATKRIGHT):
                return ret
        return RET_NONE
    def draw(self, zn, ux, uy):  # Zone, UserX, UserY
        sx, sy = xy2scrn(self.init_x, self.init_y, zn, ux, uy)
        pict.cannon(sx, sy, self.seq[self.cnt//40%8])
        if self.life<0:
            sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
            pict.cannon_burst(sx, sy, 1 if -7<self.life<-3 else 0)
        elif self.life>0 and not self.stan//2%2:
            sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
            pict.cannon_missile(sx, sy, self.dirc)

class Rinka(BaseEnemy):
    def setscreen(self, zn, ux, uy):  # 画面内敵セット
        pass
    def reset(self):
        self.x, self.y = self.init_x, self.init_y 
        self.dx, self.dy, self.cnt, self.stan = 0, 0, 0, 0
        self.life = 6  # 一定距離で出現
    def setdxdy(self, ux, uy):
        self.dx, self.dy = dir16(ux-self.x, uy-self.y, 1)
    def __init__(self, x, y, w, h):
        self.init_x, self.init_y, self.w, self.h = x, y, w, h
        self.atk_pt = 60
        self.reset()
        self.life = 0
    def update(self, zn, ux, uy, udx, udy, mb):  # Zone, UserX, UserY, UserDX, UserDY, MorphBall
        if self.life==0:  # 死亡
            if (self.init_x-8*8*4<=ux<self.init_x+8*8*4 and self.init_y-8*8*4<=uy<self.init_y+8*8*4) and \
                    not (self.init_x-4*8*4<=ux<self.init_x+4*8*4 and self.init_y-4*8*4<=uy<self.init_y+4*8*4):  # 4ブロック以上8ブロック以下
                self.reset()
                self.setdxdy(ux, uy)
                return RET_SCREENIN
        elif self.life<0:  # 消滅
            self.life += 1
            self.cnt += 1
            if self.life==0:
                if pyxel.rndi(0,2):
                    return RET_NONE
                else:
                    return RET_DROPENERGY
        elif self.stan:  # ダメージ
            self.stan -= 1
        else:  # 生存
            self.cnt += 1
            if self.cnt>=10:  # 出現から移動
                self.x += self.dx
                self.y += self.dy
                if self.screenout(zn, ux, uy):
                    return RET_SCREENOUT
                ret = user_hit(ux,uy, self.x,self.y,self.w//2*4,self.h*4, self.x+self.w//2*4,self.y,self.w//2*4,self.h*4, mb)
                if ret in (RET_ATKLEFT, RET_ATKRIGHT):
                    return ret
        return RET_NONE
    def draw(self, zn, ux, uy):  # Zone, UserX, UserY
        if self.life<0:
            if self.cnt%3==0:
                sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
                pict.burst(sx-5, sy-5)
        elif self.life>0 and not self.stan//2%2:
            sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
            pict.rinka(sx, sy, 0 if self.cnt<5 else 1 if self.cnt<10 else 2)

class Metroid(BaseEnemy):
    def reset(self):
        self.x, self.y = self.init_x, self.init_y 
        self.dx, self.dy, self.ptn, self.stan = 0, 0, 0, 0
        self.life = 20
    def setdxdy(self, ux, uy):
        pass
    def __init__(self, x, y, w, h):
        self.init_x, self.init_y, self.w, self.h = x, y, w, h
        self.atk_pt = 4
        self.reset()
        self.life = 0
    def update(self, zn, ux, uy, udx, udy, mb):  # Zone, UserX, UserY, UserDX, UserDY, MorphBall
        if self.life==0:  # 死亡
            if self.screenin(zn, ux, uy):
                return RET_SCREENIN
        elif self.life<0:  # 消滅
            self.life += 1
            self.ptn += 1
            if self.life==0:
                if pyxel.rndi(0,1):
                    return RET_NONE
                else:
                    return RET_DROPENERGY
        elif self.stan:  # ダメージ
            self.stan -= 1
        else:  # 生存
            self.ptn += 1
            my = 8*4 if mb else 0
            if ux-12*8*4<self.x<ux+12*8*4 and uy-12*8*4<self.y<uy+12*8*4:  # 12ブロックより近づくと襲撃
                self.dx += pyxel.rndi(1,2) if self.dx<5 and self.x<ux-2*4 else pyxel.rndi(-2,-1) if self.dx>-5 and self.x>ux-2*4 else 0
                self.dy += pyxel.rndi(1,2) if self.dy<5 and self.y<uy-4*4+my else pyxel.rndi(-2,-1) if self.dy>-5 and self.y>uy-4*4+my else 0
            else:  # 離れると停止
                self.dx = 0
                self.dy = 0
            if self.dx:
                left1, right1, left2, right2 = cornertilemap(self.x+self.dx, self.y, self.w, self.h)
                if (self.dx>0 and not right1 in pict.TM_NOMOVE and not right2 in pict.TM_NOMOVE) or (self.dx<0 and not left1 in pict.TM_NOMOVE and not left2 in pict.TM_NOMOVE):
                    self.x += self.dx
            if self.dy:
                top1, top2, bottom1, bottom2 = cornertilemap(self.x, self.y+self.dy, self.w, self.h)
                if (self.dy>0 and not bottom1 in pict.TM_NOMOVE and not bottom2 in pict.TM_NOMOVE) or (self.dy<0 and not top1 in pict.TM_NOMOVE and not top2 in pict.TM_NOMOVE):
                    self.y += self.dy
            if self.screenout(zn, ux, uy):
                return RET_SCREENOUT
            ret = user_hit(ux,uy, self.x,self.y,self.w//2*4,self.h*4, self.x+self.w//2*4,self.y,self.w//2*4,self.h*4, mb)
            if ret in (RET_ATKLEFT, RET_ATKRIGHT):
                return RET_ATTACK
        return RET_NONE
    def draw(self, zn, ux, uy):  # Zone, UserX, UserY
        if self.life<0:
            if self.ptn%3==0:
                sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
                pict.burst(sx-2, sy-2)
        elif self.life>0 and not self.stan//2%2:
            sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
            pict.metroid(sx, sy, self.ptn//8)

class Zebetite(BaseEnemy):
    def setscreen(self, zn, ux, uy):  # 画面内敵セット
        pass
    def screenin(self, zn, ux, uy):  # スクリーンイン：RETURN
        return RET_NONE
    def screenout(self, zn, ux, uy):  # スクリーンアウト：RETURN
        return RET_NONE
    def __init__(self, x, y, w, h):
        self.init_x, self.init_y, self.x, self.y, self.w, self.h = x, y, x, y, w, h
        self.atk_pt = 40
        self.cnt, self.stan, self.life = 0, 0, 100
    def update(self, zn, ux, uy, udx, udy, mb):  # Zone, UserX, UserY, UserDX, UserDY, MorphBall
        if self.life<0:  # 消滅
            self.life += 1
            self.cnt += 1
            if self.life==0:
                return RET_NONE
        elif self.stan:  # ダメージ
            self.stan -= 1
        elif self.life>0:  # 生存
            ret = user_hit(ux,uy, self.x,self.y,self.w//2*4,self.h*4, self.x+self.w//2*4,self.y,self.w//2*4,self.h*4, mb)
            if ret in (RET_ATKLEFT, RET_ATKRIGHT):
                return ret
        return RET_NONE
    def draw(self, zn, ux, uy):  # Zone, UserX, UserY
        if self.life<0 and self.cnt%3==0:
            sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
            pict.burst(sx-4, sy)
        elif self.life>0 and not self.stan//2%2:
            sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
            pict.zebetite(sx, sy, (self.life-1)//20)

class Glass(BaseEnemy):
    def setscreen(self, zn, ux, uy):  # 画面内敵セット
        pass
    def screenin(self, zn, ux, uy):  # スクリーンイン：RETURN
        return RET_NONE
    def screenout(self, zn, ux, uy):  # スクリーンアウト：RETURN
        return RET_NONE
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.atk_pt = 40
        self.cnt, self.stan, self.life = 0, 0, 100
    def update(self, zn, ux, uy, udx, udy, mb):  # Zone, UserX, UserY, UserDX, UserDY, MorphBall
        if self.life<0:  # 消滅
            self.life += 1
            self.cnt += 1
            if self.life==0:
                return RET_GLASSBREAK
        elif self.stan:  # ダメージ
            self.stan -= 1
        elif self.life>0:  # 生存
            ret = user_hit(ux,uy, self.x,self.y,self.w//2*4,self.h*4, self.x+self.w//2*4,self.y,self.w//2*4,self.h*4, mb)
            if ret in (RET_ATKLEFT, RET_ATKRIGHT):
                return RET_ATKLEFT
        return RET_NONE
    def draw(self, zn, ux, uy):  # Zone, UserX, UserY
        if self.life<0 and self.cnt%3==0:
            sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
            pict.burst(sx-4, sy)
        elif self.life>0 and not self.stan//2%2:
            sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
            pict.glass(sx, sy)

class Ridley(BaseEnemy):
    def reset(self):
        self.x, self.y = self.init_x, self.init_y 
        self.dx, self.dy, self.ndx, self.cnt, self.stan = 1, 0, 100, 0, 0
        self.jump_cnt, self.fire_cnt = 40, 20
        self.left = False
        self.life = 250
    def setdxdy(self, ux, uy):
        pass
    def __init__(self, x, y, w, h):
        self.init_x, self.init_y, self.w, self.h = x, y+4*4, w, h
        self.atk_pt = 80
        self.reset()
        self.life = 0
    def update(self, zn, ux, uy, udx, udy, mb):  # Zone, UserX, UserY, UserDX, UserDY, MorphBall
        if self.life<0:  # 消滅
            self.life += 1
            self.cnt += 1
            pyxel.pal() if self.life==0 or self.cnt%3 else pyxel.pal(0, 7)
            if self.life==0:
                return RET_RIDLEYBEAT
        elif self.life>0:  # 生存
            self.cnt += 1
            if self.stan:  # ダメージ
                self.stan -= 1
            if self.jump_cnt:
                self.jump_cnt -= 1
                if self.jump_cnt==0:
                    self.dy = pyxel.rndi(-12,-10)
            else:  # ジャンプ中
                self.dy += 1
                self.y += self.dy
                if self.y > self.init_y:
                    self.y = self.init_y
                    self.jump_cnt = pyxel.rndi(20,40)
            self.left = ux<self.x
            ret = user_hit(ux,uy, self.x,self.y,self.w//2*4,self.h*4, self.x+self.w//2*4,self.y,self.w//2*4,self.h*4, mb)
            if ret in (RET_ATKLEFT, RET_ATKRIGHT):
                return ret
            self.fire_cnt -= 1
            if self.fire_cnt==0:
                self.fire_cnt = pyxel.rndi(10,50)
                return RET_FIRE
        return RET_NONE
    def draw(self, zn, ux, uy):  # Zone, UserX, UserY
        if self.life<0 and self.cnt%2==0:
            sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
            pict.burst(sx-2, sy)
        elif self.life>0 and not self.stan//2%2:
            sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
            pict.ridley(sx, sy, self.left, self.cnt//8%2 if self.jump_cnt else self.cnt//4%2+2)

class Fire(BaseEnemy):
    def setscreen(self, zn, ux, uy):  # 画面内敵セット
        pass
    def __init__(self, x, y, w, h, left):
        self.x, self.y, self.w, self.h = x if left else x+4*4, y+6*4, w, h
        self.atk_pt = 60
        self.dx = -3 if left else 3
        self.dy = pyxel.rndi(-10, -14)
        self.cnt, self.life = 0, 6
    def update(self, zn, ux, uy, udx, udy, mb):  # Zone, UserX, UserY, UserDX, UserDY, MorphBall
        if self.life<0:  # 消滅
            self.life += 1
            self.cnt += 1
            if self.life==0:
                return RET_DEL
        elif self.life>0:  # 生存
            self.cnt += 1
            self.dy += 1
            tl, tr, bl, br = cornertilemap(self.x, self.y+self.dy, self.w, self.h)
            if tl in pict.TM_NOMOVE or tr in pict.TM_NOMOVE or bl in pict.TM_NOMOVE or br in pict.TM_NOMOVE:  # 障害物あり
                self.dy = -self.dy*3//4
            else:
                self.y += self.dy
            tl, tr, bl, br = cornertilemap(self.x+self.dx, self.y, self.w, self.h)
            if tl in pict.TM_NOMOVE or tr in pict.TM_NOMOVE or bl in pict.TM_NOMOVE or br in pict.TM_NOMOVE:  # 障害物あり
                return RET_DEL
            else:
                self.x += self.dx
            if self.screenout(zn, ux, uy):
                return RET_DEL
            ret = user_hit(ux,uy, self.x,self.y,self.w//2*4,self.h*4, self.x+self.w//2*4,self.y,self.w//2*4,self.h*4, mb)
            if ret in (RET_ATKLEFT, RET_ATKRIGHT):
                return ret
        return RET_NONE
    def draw(self, zn, ux, uy):  # Zone, UserX, UserY
        if (self.life<0 and self.cnt%2==0) or self.life>0:
            sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
            pict.fire(sx, sy, self.cnt//2)

class Kraid(BaseEnemy):
    def reset(self):
        self.x, self.y = self.init_x, self.init_y 
        self.dx, self.dy, self.ndx, self.cnt, self.stan = 1, 0, 100, 0, 0
        self.needle_cnt, self.plate_cnt = 40,20
        self.left = False
        self.life = 300
    def setdxdy(self, ux, uy):
        pass
    def __init__(self, x, y, w, h):
        self.init_x, self.init_y, self.w, self.h = x, y, w, h
        self.atk_pt = 80
        self.reset()
        self.life = 0
    def update(self, zn, ux, uy, udx, udy, mb):  # Zone, UserX, UserY, UserDX, UserDY, MorphBall
        if self.life<0:  # 消滅
            self.life += 1
            self.cnt += 1
            pyxel.pal() if self.life==0 or self.cnt%3 else pyxel.pal(0, 7)
            if self.life==0:
                return RET_KRAIDBEAT
        elif self.life>0:  # 生存
            if self.stan:  # ダメージ
                self.stan -= 1
            self.cnt += 1
            self.left = ux-4*4<self.x
            if self.dx:
                left1, right1, left2, right2 = cornertilemap(self.x+self.dx, self.y, self.w, self.h)
                if (self.dx>0 and not right1 in pict.TM_NOMOVE and not right2 in pict.TM_NOMOVE) or (self.dx<0 and not left1 in pict.TM_NOMOVE and not left2 in pict.TM_NOMOVE):
                    self.x += self.dx
                else:
                    self.dx = -self.dx
                self.ndx -= 1
                if self.ndx<=0:
                    self.dx = -self.dx
                    self.ndx = pyxel.rndi(100,200)
            ret = user_hit(ux,uy, self.x,self.y,self.w//2*4,self.h*4, self.x+self.w//2*4,self.y,self.w//2*4,self.h*4, mb)
            if ret in (RET_ATKLEFT, RET_ATKRIGHT):
                return ret
            self.needle_cnt -= 1
            if self.needle_cnt==12:
                return RET_NEEDLE_UP
            elif self.needle_cnt==6:
                return RET_NEEDLE_MID
            elif self.needle_cnt==0:
                self.needle_cnt = pyxel.rndi(100,150)
                return RET_NEEDLE_LOW
            self.plate_cnt -= 1
            if self.plate_cnt==0:
                self.plate_cnt = pyxel.rndi(10,80)
                return RET_PLATE
        return RET_NONE
    def draw(self, zn, ux, uy):  # Zone, UserX, UserY
        if self.life<0 and self.cnt%2==0:
            sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
            pict.burst(sx-2, sy)
        elif self.life>0 and not self.stan//2%2:
            sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
            pict.kraid(sx, sy, self.left, self.cnt//8)

class Needle(BaseEnemy):
    def setscreen(self, zn, ux, uy):  # 画面内敵セット
        pass
    def __init__(self, x, y, w, h, left, row):
        self.x = x if left else x+10*4
        self.y = y if row==RET_NEEDLE_UP else y+16 if row==RET_NEEDLE_MID else y+32
        self.w, self.h = w, h
        self.atk_pt = 60
        self.dx = -6 if left else 6
        self.dy, self.cnt, self.life = 0, 0, 6
    def update(self, zn, ux, uy, udx, udy, mb):  # Zone, UserX, UserY, UserDX, UserDY, MorphBall
        if self.life<0:  # 消滅
            self.life += 1
            self.cnt += 1
            if self.life==0:
                return RET_DEL
        elif self.life>0:  # 生存
            self.x += self.dx
            tl, tr, bl, br = cornertilemap(self.x, self.y, self.w, self.h)
            if tl in pict.TM_NOMOVE or tr in pict.TM_NOMOVE or bl in pict.TM_NOMOVE or br in pict.TM_NOMOVE:  # 障害物あり
                return RET_DEL
            if self.screenout(zn, ux, uy):
                return RET_DEL  # RET_SCREENOUT
            ret = user_hit(ux,uy, self.x,self.y,self.w//2*4,self.h*4, self.x+self.w//2*4,self.y,self.w//2*4,self.h*4, mb)
            if ret in (RET_ATKLEFT, RET_ATKRIGHT):
                return ret
        return RET_NONE
    def draw(self, zn, ux, uy):  # Zone, UserX, UserY
        if (self.life<0 and self.cnt%2==0) or self.life>0:
            sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
            pict.needle(sx, sy)

class Plate(BaseEnemy):
    def setscreen(self, zn, ux, uy):  # 画面内敵セット
        pass
    def __init__(self, x, y, w, h, left):
        self.x, self.y, self.w, self.h = x+10*4 if left else x, y, w, h
        self.atk_pt = 60
        self.dx = -4 if left else 4
        self.dy = pyxel.rndi(-18, -12)
        self.cnt, self.life = 0, 6
    def update(self, zn, ux, uy, udx, udy, mb):  # Zone, UserX, UserY, UserDX, UserDY, MorphBall
        if self.life<0:  # 消滅
            self.life += 1
            self.cnt += 1
            if self.life==0:
                return RET_DEL
        elif self.life>0:  # 生存
            self.cnt += 1
            self.x += self.dx
            self.dy += 1
            self.y += self.dy
            tl, tr, bl, br = cornertilemap(self.x, self.y, self.w, self.h)
            if tl in pict.TM_NOMOVE or tr in pict.TM_NOMOVE or bl in pict.TM_NOMOVE or br in pict.TM_NOMOVE:  # 障害物あり
                return RET_DEL
            if self.screenout(zn, ux, uy):
                return RET_DEL  # RET_SCREENOUT
            ret = user_hit(ux,uy, self.x,self.y,self.w//2*4,self.h*4, self.x+self.w//2*4,self.y,self.w//2*4,self.h*4, mb)
            if ret in (RET_ATKLEFT, RET_ATKRIGHT):
                return ret
        return RET_NONE
    def draw(self, zn, ux, uy):  # Zone, UserX, UserY
        if (self.life<0 and self.cnt%2==0) or self.life>0:
            sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
            pict.plate(sx, sy, self.cnt//2)

class MotherBrain:
    def setscreen(self, zn, ux, uy):  # 画面内敵セット
        pass
    def damage(self, bx, by, bw, bh, dmg):  # BeamX,BeamY,BeamW,BeamH,Damage：RETURN
        if self.life>0 and hit(bx,by,bw,bh, self.x//4,self.y//4,self.w,self.h):
            self.life -= dmg
            if self.life<=0:
                self.life = -40
            else:
                self.stan = 20
            return RET_HIT
        return RET_NONE
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.atk_pt = 80
        self.cnt, self.stan = 0, 0
        self.life = 400
    def update(self, zn, ux, uy, udx, udy, mb):  # Zone, UserX, UserY, UserDX, UserDY, MorphBall
        if self.life<0:  # 消滅
            self.life += 1
            self.cnt += 1
            if self.life==0 or self.cnt%3:
                pyxel.pal()
            else:
                pyxel.pal(0, 7)
            if self.life==0:
                return RET_BRAINBREAK
        elif self.stan:  # ダメージ
            self.stan -= 1
        elif self.life>0:  # 生存
            ret = user_hit(ux,uy, self.x,self.y,self.w//2*4,self.h*4, self.x+self.w//2*4,self.y,self.w//2*4,self.h*4, mb)
            if ret in (RET_ATKLEFT, RET_ATKRIGHT):
                return RET_ATKLEFT
        return RET_NONE
    def draw(self, zn, ux, uy):  # Zone, UserX, UserY
        if self.life<0 and self.cnt%2==0:
            sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
            pict.burst(sx+pyxel.rndi(-8,16), sy+pyxel.rndi(0,16))
            if self.life==-1:
                pyxel.pal(0, 7)
            else:
                pyxel.pal(0, 7)
        elif self.life>0:
            sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
            if self.stan//2%2==0:
                pict.motherbrain(sx, sy, 0)
            else:
                pict.motherbrain(sx, sy, 1)

END_LOOP = 900
class App:
    def set_enemy_pos(self):  # 敵の位置を記録：1回だけ
        self.enemy_pos = []
        for x in range(256):
            for y in range(256):
                tm = pyxel.tilemaps[TM].pget(x, y)
                if tm in (pict.TM_ZOOMER, pict.TM_RIPPER, pict.TM_WAVER, pict.TM_ZEB, pict.TM_MELLOW, pict.TM_RINKA, 
                        pict.TM_CANNON0, pict.TM_CANNON1, pict.TM_CANNON2):  # Zoomer,Ripper,Waver,Zeb,Mellow,Rinka,Cannon：1*1
                    self.enemy_pos.append((x*8, y*8, tm))
                    pyxel.tilemaps[TM].pset(x, y, pict.TM_SPACE)
                elif tm in (pict.TM_SKREE, pict.TM_GLASS, pict.TM_ZEBETITE):  # Skree,glass,zebetite：1*2
                    self.enemy_pos.append((x*8, y*8, tm))
                    pyxel.tilemaps[TM].pset(x, y, pict.TM_SPACE)
                    pyxel.tilemaps[TM].pset(x, y+1, pict.TM_SPACE)
                elif tm in (pict.TM_REO, pict.TM_METROID, pict.TM_KRAID):  # Reo,Metroid,Kraid：2*2
                    self.enemy_pos.append((x*8, y*8, tm))
                    pyxel.tilemaps[TM].pset(x, y, pict.TM_SPACE)
                    pyxel.tilemaps[TM].pset(x+1, y, pict.TM_SPACE)
                    pyxel.tilemaps[TM].pset(x, y+1, pict.TM_SPACE)
                    pyxel.tilemaps[TM].pset(x+1, y+1, pict.TM_SPACE)
                elif tm==pict.TM_RIDLEY:  # Ridley：2*3
                    self.enemy_pos.append((x*8, y*8, tm))
                    pyxel.tilemaps[TM].pset(x, y, pict.TM_SPACE)
                    pyxel.tilemaps[TM].pset(x+1, y, pict.TM_SPACE)
                    pyxel.tilemaps[TM].pset(x, y+1, pict.TM_SPACE)
                    pyxel.tilemaps[TM].pset(x+1, y+1, pict.TM_SPACE)
                    pyxel.tilemaps[TM].pset(x, y+2, pict.TM_SPACE)
                    pyxel.tilemaps[TM].pset(x+1, y+2, pict.TM_SPACE)
                elif tm==pict.TM_MOTHERBRAIN:  # MotherBrain：3*4
                    self.enemy_pos.append((x*8, y*8, tm))
                    for u in range(3):
                        for v in range(4):
                            pyxel.tilemaps[TM].pset(x+u, y+v, pict.TM_SPACE)

    def set_zone_enemy(self):  # 現ゾーンの敵をセット
        self.enemy.clear()
        for x, y, tm in self.enemy_pos:
            if ZN[self.zone][0]<=x<ZN[self.zone][2] and ZN[self.zone][1]<=y<ZN[self.zone][3]:
                if tm==pict.TM_ZOOMER:
                    self.enemy.append(Zoomer(x*4,y*4, 8,8))
                elif tm==pict.TM_SKREE:
                    self.enemy.append(Skree(x*4,y*4, 8,12))
                elif tm==pict.TM_REO:
                    self.enemy.append(Reo((x+2)*4,y*4, 12,10))
                elif tm==pict.TM_RIPPER:
                    self.enemy.append(Ripper(x*4,y*4, 8,4))
                elif tm==pict.TM_WAVER:
                    self.enemy.append(Waver(x*4,y*4, 8,8))
                elif tm==pict.TM_ZEB:
                    self.enemy.append(Zeb((x+4)*4,(y+8)*4, 8,8))
                elif tm==pict.TM_MELLOW:
                    self.enemy.append(Mellow(x*4,y*4, 8,4))
                elif tm==pict.TM_CANNON0:
                    self.enemy.append(Cannon((x+10)*4,(y-6)*4, 4,4, 0))
                elif tm==pict.TM_CANNON1:
                    self.enemy.append(Cannon((x+2)*4,(y-6)*4, 4,4, 1))
                elif tm==pict.TM_CANNON2:
                    self.enemy.append(Cannon((x-6)*4,(y-6)*4, 4,4, 2))
                elif tm==pict.TM_RINKA:
                    self.enemy.append(Rinka((x+1)*4,(y+1)*4, 5,5))
                elif tm==pict.TM_METROID:
                    self.enemy.append(Metroid(x*4,y*4, 12,12))
                elif tm==pict.TM_ZEBETITE:
                    self.enemy.append(Zebetite(x*4,y*4, 8,16))
                elif tm==pict.TM_GLASS:
                    self.enemy.append(Glass(x*4,y*4, 8,16))
                elif tm==pict.TM_RIDLEY:
                    self.enemy.append(Ridley(x*4,y*4, 8,20))
                elif tm==pict.TM_KRAID:
                    self.enemy.append(Kraid(x*4,y*4, 12,16))
                elif tm==pict.TM_MOTHERBRAIN:
                    self.enemy.append(MotherBrain(x*4,y*4, 24,32))

    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title='Mini Metroid', capture_sec=60)
        pyxel.load('assets/MiniMetroid.pyxres')
        pyxel.mouse(True)
        self.set_enemy_pos()
        self.enemy = []
        self.dropitem = []
        self.zone = ZN_START
        self.gx, self.gy = ZN[self.zone][4], ZN[self.zone][5]
        self.set_zone_enemy()
        self.iv_energy, self.iv_missile, self.iv_ball, self.iv_bomb, self.iv_long, self.iv_varia = 0, 0, 0, 0, 0, 0
        self.iv_ice, self.iv_high, self.iv_screw, self.iv_ridley, self.iv_kraid = 0, 0, 0, 0, 0
        self.energy, self.maxenergy = 999, 999
        if DEBUG_MODE:
            self.iv_energy, self.iv_missile, self.iv_ball, self.iv_bomb, self.iv_long, self.iv_varia = 2, 4, 1, 1, 1, 1
            self.iv_ice, self.iv_high, self.iv_screw, self.iv_ridley, self.iv_kraid = 0, 1, 0, 1, 1
            self.energy, self.maxenergy = 2999, 2999
        self.cnt = 0
        self.dirc = LEFT
        self.dx, self.dy = 0, 0
        self.landing, self.pushjumpbtn, self.spinjump = False, BTN_ON, 0
        self.morphball = 0
        self.beam, self.beamcnt = [], 0
        self.bomb, self.bombcnt = [], 0
        self.pushbeambtn = True
        self.aimup = False
        self.opening, self.gameover, self.ending = 1, 0, 0
        self.ix, self.iy, self.found = 0, 0, 0
        self.scrolling, self.scrl_dirc, self.scrl_stage, self.scrl_newx, self.scrl_newy = 0,NO_DIR,0,0,0
        self.elev = 0
        self.bridging = False
        self.breakable = []
        self.door = []
        self.dmgcnt = 0
        pyxel.run(self.update, self.draw)

    def jumpbtn(self):
        return pyxel.btn(pyxel.KEY_CTRL) or pyxel.btn(pyxel.KEY_Z) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_Y)
    def beambtn(self):
        return pyxel.btn(pyxel.KEY_SHIFT) or pyxel.btn(pyxel.KEY_X) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_B) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_X)
    def leftbtn(self):
        return pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT)
    def rightbtn(self):
        return pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT)
    def upbtn(self):
        return pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP)
    def downbtn(self):
        return pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN)

    def hitgate(self, x, y):
        ret = SCRL_MAP.get(((x//4+3)//8, (y//4+11)//8), None)
        if ret!=None and self.landing:
            self.scrolling = 32
            self.scrl_dirc = ret[0]
            self.scrl_stage = ret[1]
            self.scrl_newx = x+4*4*8 if self.scrl_dirc==RIGHT else x-4*4*8
            self.scrl_newy = y

    def hititem(self, x, y):
        if pgettilemap(x//4+3, y//4+11)==pict.TM_BALL:
            self.ix, self.iy = x//4+3, y//4+11
            self.iv_ball = 1
            self.found = 2
        elif pgettilemap(x//4+3, y//4+11)==pict.TM_LONG:
            self.ix, self.iy = x//4+3, y//4+11
            self.iv_long = 1
            self.found = 2
        elif pgettilemap(x//4+3, y//4+11)==pict.TM_BOMB:
            self.ix, self.iy = x//4+3, y//4+11
            self.iv_bomb = 1
            self.found = 2
        elif pgettilemap(x//4+3, y//4+11)==pict.TM_ENERGY:
            self.ix, self.iy = x//4+3, y//4+11
            self.iv_energy += 1
            self.found = 2
            self.maxenergy += 1000
            if self.maxenergy>6999:
                self.maxenergy = 6999
            self.energy += 1000
            if self.energy>self.maxenergy:
                self.energy = self.maxenergy
        elif pgettilemap(x//4+3, y//4+11)==pict.TM_MISSILE:
            self.ix, self.iy = x//4+3, y//4+11
            self.iv_missile += 1
            self.found = 2
        elif pgettilemap(x//4+3, y//4+11)==pict.TM_VARIA:
            self.ix, self.iy = x//4+3, y//4+11
            self.iv_varia += 1
            self.found = 2
        elif pgettilemap(x//4+3, y//4+11)==pict.TM_ICE:
            self.ix, self.iy = x//4+3, y//4+11
            self.iv_ice += 1
            self.found = 2
        elif pgettilemap(x//4+3, y//4+11)==pict.TM_HIGH:
            self.ix, self.iy = x//4+3, y//4+11
            self.iv_high += 1
            self.found = 2

    def inswamp(self, x, y):  # Poison Swamp
        if pgettilemap(x//4+3, y//4+11) in pict.TM_SWAMP:
            self.energy -= 1 if self.iv_varia else 2
            if self.energy<0:
                self.energy = 0
                self.gameover = 1

    def onelevator(self, x, y, dx, dy, ball):
        if self.elev>0 or dx or dy or ball:
            return
        ret = ELEV_POS.get((x//4, y//4), None)
        if ret==None:
            self.elev = 0
        elif self.elev==0:
            self.elev = 128+20
            self.elev_dirc = ret[0]
            self.elev_zone = ret[1]
            self.elev_x = ret[2]*4
            self.elev_y = ret[3]*4

    def screen_enemy(self):  # draw all enemy in screen
        for i in reversed(range(len(self.enemy))):  # Zoomer,Skree,Reo,Ripper,Waver,Zeb,Mellow,Rinka,Metroid,Kraid,Ridley
            self.enemy[i].setscreen(self.zone, self.gx, self.gy)

    def update(self):
        if self.opening:  # オープニング：RETURN
            self.opening += 1
            if self.opening==2:
                pyxel.playm(2)  # Opening
                pass
            elif pyxel.play_pos(0)==None:
                self.opening = 0
                self.screen_enemy()  # draw all enemy in screen
            return
        if self.gameover:  # ゲームオーバー：RETURN
            pyxel.stop()
            self.gameover += 1
            if self.gameover>100 and (self.jumpbtn() or self.beambtn()):
                self.gameover = 0
                self.energy = self.maxenergy
                self.zone = ZN_START
                self.set_zone_enemy()
                self.gx, self.gy = ZN[self.zone][4], ZN[self.zone][5]
                self.dx, self.dy = 0, 0
                self.dmgcnt = 0
                self.opening = 1
            return
        if self.ending:  # エンディング：RETURN
            self.ending += 1
            if self.ending>END_LOOP+80 and (self.jumpbtn() or self.beambtn()):
                self.ending = END_LOOP
                if pyxel.play_pos(0)==None:
                    pyxel.playm(1)  # Ending
            return
        if self.found:  # アイテム入手：RETURN
            if self.found!=1:
                self.found = 1
                pyxel.playm(0)  # Item Found
            if pyxel.play_pos(0)==None:
                self.found = 0
                psettilemap(self.ix, self.iy, pict.TM_SPACE)
            return
        if self.scrolling:  #　ゾーン移動（ゲート）：RETURN
            self.scrolling -= 1
            if self.scrolling==0:
                self.gx = self.scrl_newx
                self.gy = self.scrl_newy
                self.zone = self.scrl_stage
                self.set_zone_enemy()
                self.screen_enemy()  # draw all enemy in screen
                if self.zone in ZN_NOBGM:  # BGM
                    pyxel.stop()
            return
        if self.elev>0:  #　ゾーン移動（エレベーター）：RETURN
            pyxel.stop()
            self.elev -= 1
            if self.elev==127+20:
                self.gx = self.elev_x
            elif self.elev==63:
                self.gy = self.elev_y
                self.zone = self.elev_zone
                self.set_zone_enemy()
                if self.zone==ZN_ENDING:
                    self.ending = 1
                    self.elev = 0
                    pyxel.playm(1)  # Ending
            elif self.elev==0:
                self.elev = -1
                self.screen_enemy()  # draw all enemy in screen
            return
        if self.bridging:  # 橋渡し：RETURN
            for i in range(len(BRIDGE_POS)):
                bx, by = BRIDGE_POS[i][0], BRIDGE_POS[i][1] 
                self.breakable.append(Breakable(bx*8, by*8, pict.TM_BRIDGE[1][0], pict.TM_BRIDGE[1][1]))
                self.breakable[-1].tm_breakable = pict.TM_BRIDGE[0]
                self.breakable[-1].cnt = 10+i*6
            self.bridging = False
            return
        if pyxel.play_pos(0)==None and not self.zone in ZN_NOBGM:
            pyxel.playm(3)  # Brinstar

        for i in reversed(range(len(self.dropitem))):  # EnergyBall,Missile
            ret = self.dropitem[i].update(self.zone, self.gx, self.gy, self.dx, self.dy, self.morphball)
            if ret==RET_HIT:
                self.energy += 50
                if self.energy>self.maxenergy:
                    self.energy = self.maxenergy
                del self.dropitem[i]
            elif ret==RET_DEL:
                del self.dropitem[i]

        for i in reversed(range(len(self.enemy))):  # Zoomer,Skree,Reo,Ripper,Waver,Zeb,Mellow,Rinka,Metroid,Kraid,Ridley
            ret = self.enemy[i].update(self.zone, self.gx, self.gy, self.dx, self.dy, self.morphball)
            if ret==RET_EXPLOTION:
                self.enemy.append(Explotion(self.enemy[i].x, self.enemy[i].y))
            elif ret==RET_FIRE:
                self.enemy.append(Fire(self.enemy[i].x,self.enemy[i].y,2,2,self.enemy[i].left))
            elif ret in (RET_NEEDLE_UP, RET_NEEDLE_MID, RET_NEEDLE_LOW):
                self.enemy.append(Needle(self.enemy[i].x,self.enemy[i].y,2,2,self.enemy[i].left,ret))
            elif ret==RET_PLATE:
                self.enemy.append(Plate(self.enemy[i].x,self.enemy[i].y,2,2,self.enemy[i].left))
            elif ret in (RET_ATKLEFT, RET_ATKRIGHT) and self.dmgcnt==0:
                self.dmgcnt = 22 if ret==RET_ATKLEFT else -22
                self.dy = -6
                self.landing = False
                self.energy -= self.enemy[i].atk_pt//2 if self.iv_varia else self.enemy[i].atk_pt
                if self.energy<0:
                    self.energy = 0
                    self.gameover = 1
            elif ret==RET_ATTACK and self.dmgcnt==0:  # メトロイドの攻撃
                self.landing = False
                self.energy -= self.enemy[i].atk_pt//2 if self.iv_varia else self.enemy[i].atk_pt
                if self.energy<0:
                    self.energy = 0
                    self.gameover = 1
            elif ret==RET_RIDLEYBEAT:
                pyxel.playm(0)  # Item Found
                if self.iv_ridley==0:
                    self.iv_ridley = 1
                del self.enemy[i]
            elif ret==RET_KRAIDBEAT:
                pyxel.playm(0)  # Item Found
                if self.iv_kraid==0:
                    self.iv_kraid = 1
                del self.enemy[i]
            elif ret==RET_GLASSBREAK:
                for j in reversed(range(len(self.enemy_pos))):
                    if self.enemy_pos[j][2]==pict.TM_GLASS:
                        del self.enemy_pos[j]
            elif ret==RET_BRAINBREAK:
                for j in reversed(range(len(self.enemy_pos))):
                    if self.enemy_pos[j][2]==pict.TM_MOTHERBRAIN:
                        del self.enemy_pos[j]
                for p in pict.TM_ALLGLASS:
                    pyxel.tilemaps[TM].pset(p[0], p[1], pict.TM_SPACE)
            elif ret==RET_DROPENERGY:
                self.dropitem.append(EnergyBall(self.enemy[i].x+2*4, self.enemy[i].y+2*4, 4, 4))
            elif ret==RET_DEL:
                del self.enemy[i]

        if self.dmgcnt<0:
            self.dmgcnt += 1
            if self.dmgcnt<-9:
                self.dx = -6
        elif self.dmgcnt>0:
            self.dmgcnt -= 1
            if self.dmgcnt>9:
                self.dx = 6

        for i in reversed(range(len(self.breakable))):  # 壊れるブロック
            if self.breakable[i].update()==RET_DEL:
                del self.breakable[i]
        for i in reversed(range(len(self.door))):  # ドア
            if self.door[i].update()==RET_DEL:
                del self.door[i]

        self.cnt += 1
        if self.spinjump:
            self.spinjump += 1
        if self.morphball:
            self.morphball += 1
        if self.beamcnt:
            self.beamcnt -= 1
        if self.bombcnt:
            self.bombcnt -= 1

        if self.beambtn():  # ビーム／ボムボタン
            if not self.pushbeambtn and not self.morphball and len(self.beam)<3:  # ビーム
                self.beamcnt = 8
                self.spinjump = 0
                self.beam.append(Beam(self.gx, self.gy, self.dirc, self.aimup, self.iv_long, 3 if self.iv_missile>5 else self.iv_missile//2))
            elif not self.pushbeambtn and self.morphball and len(self.bomb)<3 and self.iv_bomb:  # ボム
                self.bombcnt = 8
                self.bomb.append(Bomb(self.gx, self.gy))
            self.pushbeambtn = True
        else:
            self.pushbeambtn = False

        for i in reversed(range(len(self.beam))):  # ビーム
            ret = self.beam[i].update()
            bx, by = (self.beam[i].x+4)//4, (self.beam[i].y+4)//4
            for j in reversed(range(len(self.enemy))):  # Zoomer,Skree,Reo,Ripper,Waver,Zeb,Mellow,Rinka,Metroid,Kraid,Ridley
                if self.enemy[j].damage(bx,by, 2,2, 3+self.iv_missile)==RET_HIT:
                    ret = RET_DEL
            if ret==RET_HIT:
                tm_broken = pict.TM_BREAKABLE.get(pgettilemap(bx, by), None)  # 壊れるブロック
                if tm_broken!=None:
                    self.breakable.append(Breakable(bx, by, tm_broken[0], tm_broken[1]))
                poscol = pict.TM_DOOR_CLOSE.get(pgettilemap(bx, by), None)  # ドア
                if poscol!=None and poscol[0]<=self.iv_missile//2:
                    self.door.append(Door(bx//8-poscol[1], by//8-poscol[2], poscol[0]))
                if self.iv_ridley==1 and pgettilemap(bx, by)==pict.TM_RIDLEY_UP:
                    pict.ridley_appr(bx//8, by//8, TM)
                    self.iv_ridley = 2
                    if self.iv_kraid==2:
                        self.bridging = True
                elif self.iv_ridley==1 and pgettilemap(bx, by)==pict.TM_RIDLEY_LOW:
                    pict.ridley_appr(bx//8, by//8-1, TM)
                    self.iv_ridley = 2
                    if self.iv_kraid==2:
                        self.bridging = True
                elif self.iv_kraid==1 and pgettilemap(bx, by)==pict.TM_KRAID_UP:
                    pict.kraid_appr(bx//8, by//8, TM)
                    self.iv_kraid = 2
                    if self.iv_ridley==2:
                        self.bridging = True
                elif self.iv_kraid==1 and pgettilemap(bx, by)==pict.TM_KRAID_LOW:
                    pict.kraid_appr(bx//8, by//8-1, TM)
                    self.iv_kraid = 2
                    if self.iv_ridley==2:
                        self.bridging = True
            elif ret==RET_DEL:
                del self.beam[i]

        for i in reversed(range(len(self.bomb))):  # 爆弾
            ret = self.bomb[i].update()
            if ret==RET_BURST:
                if self.bomb[i].hit(self.gx+4, self.gy+36, 24, 24):
                    self.pushjumpbtn = BTN_FORCE
                    self.landing = False
                    self.dy = -11
                bx, by = (self.bomb[i].x+8)//4, (self.bomb[i].y+8)//4
                tm_broken = pict.TM_BREAKABLE.get(pgettilemap(bx, by), None)
                if tm_broken!=None:
                    self.breakable.append(Breakable(bx, by, tm_broken[0], tm_broken[1]))
                tm_broken = pict.TM_BREAKABLE.get(pgettilemap(bx+8, by), None)
                if tm_broken!=None:
                    self.breakable.append(Breakable(bx+8, by, tm_broken[0], tm_broken[1]))
                tm_broken = pict.TM_BREAKABLE.get(pgettilemap(bx-8, by), None)
                if tm_broken!=None:
                    self.breakable.append(Breakable(bx-8, by, tm_broken[0], tm_broken[1]))
                tm_broken = pict.TM_BREAKABLE.get(pgettilemap(bx, by+8), None)
                if tm_broken!=None:
                    self.breakable.append(Breakable(bx, by+8, tm_broken[0], tm_broken[1]))
                tm_broken = pict.TM_BREAKABLE.get(pgettilemap(bx, by-8), None)
                if tm_broken!=None:
                    self.breakable.append(Breakable(bx, by-8, tm_broken[0], tm_broken[1]))
                for j in reversed(range(len(self.enemy))):  # Zoomer,Skree,Reo,Waver,Zeb,Mellow,Rinka,Metroid,Kraid,Ridley
                    self.enemy[j].damage(bx-6,by-6, 16,16, 6)
            elif ret==RET_DEL:
                del self.bomb[i]

        if self.jumpbtn():  # ジャンプボタン
            if self.landing and self.morphball>3:  # モーフボール戻り
                morph1 = pgettilemap(self.gx//4+1, self.gy//4+1)
                morph2 = pgettilemap(self.gx//4+6, self.gy//4+1)
                if morph1 in pict.TM_NOMOVE or morph2 in pict.TM_NOMOVE:
                    pass
                else:
                    self.morphball = -4
            elif not self.morphball and ((self.pushjumpbtn==BTN_OFF and self.landing) or self.pushjumpbtn==BTN_FORCE):  # モーフボール戻りジャンプを可能
                self.pushjumpbtn = BTN_ON  # モーフボール戻りジャンプを可能
                self.landing = False
                if not self.aimup and self.dx:  # スピンジャンプ
                    self.spinjump = 1
                self.dy = -21 if self.iv_high else -18  # ジャンプ初速度:-18 ハイジャンプ:-21
            if self.pushjumpbtn==BTN_OFF:
                self.pushjumpbtn = BTN_ON
        else:
            if self.pushjumpbtn==BTN_ON:
                self.pushjumpbtn = BTN_OFF

        self.dy += 1
        if self.dy<0:  # ジャンプ
            if self.morphball>3:
                up1 = pgettilemap(self.gx//4+1, (self.gy+self.dy)//4+10)
                up2 = pgettilemap(self.gx//4+6, (self.gy+self.dy)//4+10)
            else:
                up1 = pgettilemap(self.gx//4+1, (self.gy+self.dy)//4+2)
                up2 = pgettilemap(self.gx//4+6, (self.gy+self.dy)//4+2)
            if up1 in pict.TM_NOMOVE or up2 in pict.TM_NOMOVE:  # 天井
                self.dy = 0
            elif self.pushjumpbtn==BTN_OFF and self.dmgcnt==0:  # 上昇中でジャンプ押していない => 落下早める
                self.dy += 6
        if self.dy>0:  # 落下
            if self.dy>9:  # 落下速度上限
                self.dy = 9
            down1 = pgettilemap(self.gx//4+1, (self.gy+self.dy+3)//4+15)
            down2 = pgettilemap(self.gx//4+6, (self.gy+self.dy+3)//4+15)
            self.landing = False
            if down1 in pict.TM_NOMOVE or down2 in pict.TM_NOMOVE:  # 着地
                self.gy = (self.gy+self.dy)//32*32
                self.dy = 0
                self.landing = True
                self.spinjump = 0
                if self.pushjumpbtn==BTN_FORCE:
                    self.pushjumpbtn=BTN_ON
        self.gy += self.dy

        if self.leftbtn():  # 左ボタン
            self.dirc = LEFT
            self.dx -= 1
            if self.dx<-6:
                self.dx = -6
        elif self.rightbtn():  # 右ボタン
            self.dirc = RIGHT
            self.dx += 1
            if self.dx>6:
                self.dx = 6
        else:
            if self.dx>0:
                self.dx -= 1
            elif self.dx<0:
                self.dx += 1

        if self.iv_ball and self.landing and not self.morphball and self.downbtn():  # 下ボタン～モーフボール
            self.morphball = 1

        if self.upbtn():  # 上ボタン
            if self.morphball>3:  # モーフボール戻り
                morph1 = pgettilemap(self.gx//4+1, self.gy//4+1)
                morph2 = pgettilemap(self.gx//4+6, self.gy//4+1)
                if morph1 in pict.TM_NOMOVE or morph2 in pict.TM_NOMOVE:
                    pass
                else:
                    self.morphball = -4
            self.aimup = True
        else:
            self.aimup = False

        if self.dx<0:  # 左移動
            if self.morphball>3:
                left1 = pgettilemap((self.gx+self.dx)//4+1, self.gy//4+10)
                left2 = pgettilemap((self.gx+self.dx)//4+1, self.gy//4+15)
                left3 = (0, 0)
            else:
                left1 = pgettilemap((self.gx+self.dx)//4+1, self.gy//4+2)
                left2 = pgettilemap((self.gx+self.dx)//4+1, self.gy//4+8)
                if self.landing:
                    left3 = pgettilemap((self.gx+self.dx)//4+1, self.gy//4+15)
                else:
                    left3 = pgettilemap((self.gx+self.dx)//4+1, self.gy//4+12)
            if left1 in pict.TM_NOMOVE or left2 in pict.TM_NOMOVE or left3 in pict.TM_NOMOVE:  # 左障害物
                self.dx = 0
        elif self.dx>0:  # 右移動
            if self.morphball>3:
                right1 = pgettilemap((self.gx+self.dx)//4+6, self.gy//4+10)
                right2 = pgettilemap((self.gx+self.dx)//4+6, self.gy//4+15)
                right3 = (0, 0)
            else:
                right1 = pgettilemap((self.gx+self.dx)//4+6, self.gy//4+2)
                right2 = pgettilemap((self.gx+self.dx)//4+6, self.gy//4+8)
                if self.landing:
                    right3 = pgettilemap((self.gx+self.dx)//4+6, self.gy//4+15)
                else:
                    right3 = pgettilemap((self.gx+self.dx)//4+6, self.gy//4+12)
            if right1 in pict.TM_NOMOVE or right2 in pict.TM_NOMOVE or right3 in pict.TM_NOMOVE:  # 右障害物
                self.dx = 0
        self.gx += self.dx
        if self.gx<ZN[self.zone][0]*4:  # ゲート越え防止
            self.gx = ZN[self.zone][0]*4
        elif self.gx>(ZN[self.zone][2]-7)*4:
            self.gx = (ZN[self.zone][2]-7)*4

        self.hititem(self.gx, self.gy)
        self.hitgate(self.gx, self.gy)
        self.onelevator(self.gx, self.gy, self.dx, self.dy, self.morphball)
        self.inswamp(self.gx, self.gy)

    def draw_chara(self, x, y, n, dirc, aimup):
        sx, sy = SCRN_X+x, SCRN_Y+y
        if n==1:  # Idle
            pict.user_idle(sx, sy, dirc==LEFT, aimup)
        elif n==2:  # Walk1
            pict.user_walk1(sx, sy, dirc==LEFT, aimup, self.beamcnt)
        elif n==3:  # Walk2
            pict.user_walk2(sx, sy, dirc==LEFT, aimup, self.beamcnt)
        elif n==4:  # Walk3
            pict.user_walk3(sx, sy, dirc==LEFT, aimup, self.beamcnt)
        elif n==5:  # Jump
            pict.user_jump(sx, sy, dirc==LEFT, aimup, self.beamcnt)
        elif n==6:  # SpinJump
            if self.spinjump in (1, 2, 3):
                pict.user_jump(sx, sy, dirc==LEFT)  # Jump
            elif self.spinjump//2%4==2:
                pict.user_spinjump1(sx, sy, dirc==LEFT)  # SpinJump1
            elif self.spinjump//2%4==3:
                pict.user_spinjump2(sx, sy, dirc==LEFT)  # SpinJump2
            elif self.spinjump//2%4==0:
                pict.user_spinjump3(sx, sy, dirc==LEFT)  # SpinJump3
            else:
                pict.user_spinjump4(sx, sy, dirc==LEFT)  # SpinJump4
        elif n==7:  # モーフボール
            if self.morphball in (1, -2, -1):
                pict.user_walk1(sx, sy, dirc==LEFT)  # Walk1
            elif self.morphball in (2, 3, -4, -3):
                pict.user_morphing(sx, sy, dirc==LEFT)  # Morphin
            elif self.morphball//2%4==2:
                pict.user_morphball1(sx, sy, dirc==LEFT)  # MorphBall1
            elif self.morphball//2%4==3:
                pict.user_morphball2(sx, sy, dirc==LEFT)  # MorphBall2
            elif self.morphball//2%4==0:
                pict.user_morphball3(sx, sy, dirc==LEFT)  # MorphBall3
            else:
                pict.user_morphball4(sx, sy, dirc==LEFT)  # MorphBall4

    def draw_invt(self):
        x, y = 1, 1
        if self.iv_energy:
            pict.invt_energy(x, y)  # Inventory EnergyTank
            pyxel.text(x+9, y+4, f'{self.iv_energy}', 13)
            pyxel.text(x+8, y+3, f'{self.iv_energy}', 7)
            x += 12
        if self.iv_missile:
            pict.invt_missile(x, y, self.iv_missile)  # Inventory Missile
            pyxel.text(x+9, y+4, f'{self.iv_missile}', 13)
            pyxel.text(x+8, y+3, f'{self.iv_missile}', 7)
            x += 12
        if self.iv_long:
            pict.invt_long(x, y)  # Inventory LongBeam
            x += 9
        if self.iv_ice:
            pict.invt_ice(x, y)  # Inventory IceBeam
            x += 9
        if self.iv_ball:
            pict.invt_ball(x, y)  # Inventory MorphBall
            x += 9
        if self.iv_bomb:
            pict.invt_bomb(x, y)  # Inventory Bomb
            x += 9
        if self.iv_high:
            pict.invt_high(x, y)  # Inventory HighJump
            x += 9
        if self.iv_varia:
            pict.invt_varia(x, y)  # Inventory Varia
            x += 9
        if self.iv_ridley:
            pict.invt_ridley(x, y)  # Inventory Ridley
            x += 9
        if self.iv_kraid:
            pict.invt_kraid(x, y)  # Inventory Ridley
            x += 9

    def draw_map(self, zn, ux, uy, cnt=0):  # Zone, UserX, UserY, ScrollCount<32
        pyxel.bltm(SCRN_X, SCRN_Y, TM, ZN[zn][0]+4*cnt if ux//4<ZN[zn][0]+CNTR_X else ZN[zn][2]-SCRN_W+4*cnt if ux//4>ZN[zn][2]-(SCRN_W-CNTR_X) else ux//4-CNTR_X+4*cnt, 
                ZN[zn][1] if uy//4<ZN[zn][1]+CNTR_Y else ZN[zn][3]-SCRN_H if uy//4>ZN[zn][3]-(SCRN_H-CNTR_Y) else uy//4-CNTR_Y, SCRN_W, SCRN_H, 1)

    def draw_user(self, zn, ux, uy, pose, dirc, aimup):
        sx, sy = xy2scrn(ux, uy, zn, ux, uy)
        if pose==0:  # Facing
            pict.user_faceing(sx, sy)

    def draw_death(self, zn, ux, uy, cnt):
        sx, sy = xy2scrn(ux, uy, zn, ux, uy)
        pict.user_death(sx, sy, cnt)

    def draw_elevator(self, zn, ux, uy):
        sx, sy = xy2scrn(ux-4*4, uy+16*4, zn, ux, uy)
        pict.elevator(sx, sy)

    def draw_energy(self):
        sx = SCRN_X+30
        maxen = self.maxenergy
        en = self.energy
        while maxen>1000:
            maxen -= 1000
            if en>1000:
                en -= 1000
                pict.energy100(sx, SCRN_Y+10, True)
            else:
                pict.energy100(sx, SCRN_Y+10, False)
            sx -= 5        
        pyxel.text(SCRN_X+11, SCRN_Y+16, 'EN-', 5)
        pyxel.text(SCRN_X+10, SCRN_Y+15, 'EN-', 12)
        pyxel.text(SCRN_X+23, SCRN_Y+16, f'{en//10}', 13)
        pyxel.text(SCRN_X+22, SCRN_Y+15, f'{en//10}', 7)

    def draw(self):
        pyxel.cls(0)
        if self.gameover:  # ：RETURN
            if self.gameover<=100:
                self.draw_map(self.zone, self.gx, self.gy)
                self.draw_invt()
                self.draw_energy()
                if self.gameover<30:
                    self.draw_death(self.zone, self.gx, self.gy, self.gameover)
            else:
                pyxel.text(SCRN_X+8*6, SCRN_Y+8*7, 'GAME  OVER', 7)
            return

        if self.ending:  # ：RETURN
            x, y = 8*7+4, 10*8+2
            pyxel.bltm(SCRN_X, SCRN_Y, TM, 0, 0, SCRN_W, SCRN_H, 1)
            if self.ending<90: # ユーザー表示
                pict.user_ending1(x, y)
            elif self.ending<END_LOOP:
                pyxel.text(12, 10, '           GREAT !!', 11)
                pyxel.text(12, 24, ' YOU FULFILED YOUR MISSION.', 11)
                pyxel.text(12, 32, ' IT WILL REVIVE PEACE IN', 11)
                pyxel.text(12, 40, 'SPACE.', 11)
                pyxel.text(12, 48, ' BUT, IT MAY BE INVADED BY', 11)
                pyxel.text(12, 56, 'THE OTHER METROID.', 11)
                pyxel.text(12, 64, ' PRAY FOR A TRUE PEACE IN', 11)
                pyxel.text(12, 72, 'SPACE!', 11)
                if self.ending<240+260:  # ユーザー表示
                    pict.user_ending1(x, y)
                elif self.ending<270+260:
                    if self.ending//4%2:  # ユーザー点滅
                        pict.user_ending1(x, y)
                elif self.ending<300+260:
                    if self.ending//2%2:  # ユーザー点滅
                        pict.user_ending1(x, y)
                elif self.ending<330+260:
                    if self.ending//2%2:  # ユーザー点滅
                        pict.user_ending2(x, y)
                elif self.ending<360+260:
                    if self.ending//4%2:  # ユーザー点滅
                        pict.user_ending2(x, y)
                else:  # ユーザー表示
                    pict.user_ending2(x, y)
            else:
                pict.the_end(5*8+4, 5*8)
                if self.ending<END_LOOP+80:
                    pict.user_ending3(x, y, self.ending//4%2)
                else:
                    pict.user_ending2(x, y)
            return

        if self.scrolling:  # ：RETURN
            self.draw_map(self.zone, self.gx, self.gy, 32-self.scrolling if self.scrl_dirc==RIGHT else self.scrolling-32)
            return
        if self.elev>0:  # ：RETURN
            if self.elev>127:
                if self.elev//4%2:  # ユーザー点滅
                    self.draw_user(self.zone, self.gx, self.gy, 0, self.dirc, self.aimup)
                    self.draw_elevator(self.zone, self.gx, self.gy)
            elif self.elev>63:  # 現ゾーン
                ddy = 128-self.elev if self.elev_dirc==DOWN else self.elev-128
                self.draw_user(self.zone, self.gx, self.gy+ddy*4, 0, self.dirc, self.aimup)
                self.draw_elevator(self.zone, self.gx, self.gy+ddy*4)
            else:  # 新ゾーン
                ddy = -self.elev  if self.elev_dirc==DOWN else self.elev
                self.draw_user(self.zone, self.gx, self.gy+ddy*4, 0, self.dirc, self.aimup)
                self.draw_elevator(self.zone, self.gx, self.gy+ddy*4)
            self.draw_map(self.zone, self.gx, self.gy)
            return
        if self.opening:  # ユーザー登場：RETURN
            self.draw_map(self.zone, self.gx, self.gy)
            self.draw_invt()
            self.draw_energy()
            if self.opening<60:
                if self.opening%2:  # ユーザー点滅
                    self.draw_user(self.zone, self.gx, self.gy, 0, self.dirc, self.aimup)
            elif self.opening<120:
                if self.opening%3:  # ユーザー点滅
                    self.draw_user(self.zone, self.gx, self.gy, 0, self.dirc, self.aimup)
            elif self.opening<180:
                if self.opening%5:  # ユーザー点滅
                    self.draw_user(self.zone, self.gx, self.gy, 0, self.dirc, self.aimup)
            else:
                    self.draw_user(self.zone, self.gx, self.gy, 0, self.dirc, self.aimup)
            return

        if self.dmgcnt//2%2==0:
            if self.morphball:
                sx, sy = xy2scrn(self.gx, self.gy, self.zone, self.gx, self.gy)
                self.draw_chara(sx, sy, 7, self.dirc, self.aimup)
            elif self.spinjump:
                sx, sy = xy2scrn(self.gx, self.gy, self.zone, self.gx, self.gy)
                self.draw_chara(sx, sy, 6, self.dirc, self.aimup)
            elif not self.landing:  # ジャンプ
                sx, sy = xy2scrn(self.gx, self.gy, self.zone, self.gx, self.gy)
                self.draw_chara(sx, sy, 5, self.dirc, self.aimup)
            elif self.dx==0:
                sx, sy = xy2scrn(self.gx, self.gy, self.zone, self.gx, self.gy)
                self.draw_chara(sx, sy, 1, self.dirc, self.aimup)
            else:
                sx, sy = xy2scrn(self.gx, self.gy, self.zone, self.gx, self.gy)
                self.draw_chara(sx, sy, self.cnt//2%3+2, self.dirc, self.aimup)

        for i in reversed(range(len(self.beam))):  # ビーム
            self.beam[i].draw(self.zone, self.gx, self.gy)
        for i in reversed(range(len(self.bomb))):  # 爆弾
            self.bomb[i].draw(self.zone, self.gx, self.gy)
        for i in reversed(range(len(self.dropitem))):  # ドロップアイテム：EnergyBall,Missile
            self.dropitem[i].draw(self.zone, self.gx, self.gy)
        for i in reversed(range(len(self.enemy))):  # 敵：Zoomer,Skree,Reo,Ripper,Waver,Zeb,Mellow
            self.enemy[i].draw(self.zone, self.gx, self.gy)

        self.draw_map(self.zone, self.gx, self.gy)
        self.draw_invt()
        self.draw_energy()

class Beam:
    def __init__(self, x, y, dirc, aimup, long, strg):
        self.dirc, self.strg = dirc, strg
        self.beamspd = 10  # 速度
        if aimup:
            if dirc==LEFT:  # UPLEFT
                self.x, self.y = x+8, y-16
                self.dirc = UP
            else:  # UPRIGHT
                self.x, self.y = x+16, y-16
                self.dirc = UP
        else:
            if dirc==LEFT:
                self.x, self.y = x-12, y+16
            else:  # RIGHT
                self.x, self.y = x+36, y+16
        self.atk_x, self.atk_y, self.atk_w, self.atk_h, self.atk_dir, self.atk_dmg, self.hitted = 0, 0, 0, 0, NO_DIR, 1, False  # 接触範囲
        self.disscnt = 48 if long else 16  # 消えるまでの時間
    def hit(self, x, y, w, h):
        if self.atk_x-w<x<self.atk_x+self.atk_w and self.atk_y-h<y<self.atk_y+self.atk_h:
            self.hitted = True
            return True
        return False
    def update(self):
        self.disscnt -= 1
        if self.disscnt==0:
            return RET_DEL
        elif self.disscnt>=3:
            if self.dirc==LEFT:
                self.x -= self.beamspd
            elif self.dirc==RIGHT:
                self.x += self.beamspd
            elif self.dirc==UP:
                self.y -= self.beamspd
            elif self.dirc==DOWN:
                self.y += self.beamspd
            if pgettilemap((self.x+4)//4,(self.y+4)//4) in pict.TM_NOMOVE:
                self.disscnt = 3
                return RET_HIT
        return RET_NONE
    def draw(self, zn, ux, uy):
        sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
        if self.disscnt:
            pict.beam(sx, sy, self.strg)  # Beam

class Bomb:
    def __init__(self, x, y):
        self.x, self.y = x+8, y+48
        self.atk_x, self.atk_y, self.atk_w, self.atk_h = self.x-24, self.y-24, 64, 32  # 接触範囲 
        self.burstcnt = 32  # 爆発までの時間
    def hit(self, x, y, w, h):
        return self.atk_x-w<x<self.atk_x+self.atk_w and self.atk_y-h<y<self.atk_y+self.atk_h
    def update(self):
        self.burstcnt -= 1
        if self.burstcnt==6:
            return  RET_BURST
        elif self.burstcnt==0:
            return RET_DEL
        return RET_NONE
    def draw(self, zn, ux, uy):
        sx, sy = xy2scrn(self.x, self.y, zn, ux, uy)
        if self.burstcnt>=8:
            pict.bomb(sx, sy, self.burstcnt//3%2)
        elif self.burstcnt==7:
            pict.bomb_burst(sx, sy, 0)
        elif self.burstcnt==6:
            pict.bomb_burst(sx, sy, 1)
        elif self.burstcnt in (1,3,5):
            pict.burst(sx-6, sy-6)

App()
