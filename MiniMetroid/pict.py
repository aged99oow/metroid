#
# MiniMetroid
# pict.py 2024/1/6
#
import pyxel
TM_SPACE = (0,0)  # TileMap Space
TM_NOMOVE = (  # TileMap Obstacle
    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7, 0),(8, 0),(9,0),(10,0),(11,0),(12,0),       (14,0),(15,0),                       (19,0),        (21,0),        (23,0),(24,0),(25, 0),(26, 0),(27,0),(28,0),
    (1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7, 1),       (9,1),                            (14,1),(15,1),(16, 1),        (18, 1),(19,1),(20,1),(21,1),(22, 1),(23,1),               (26, 1),
    (1,2),(2,2),(3,2),(4,2),      (6,2),(7, 2),       (9,2),(10,2),       (12,2),              (15,2),                        (19,2),       (21,2),        (23,2),(24,2),(25, 2),(26, 2),(27,2),(28,2),
    (1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(7, 3),                           (12,3),(13,3),(14,3),(15,3),(16, 3),(17, 3),(18, 3),(19,3),       (21,3),                              (26, 3),
    (1,4),(2,4),      (4,4),(5,4),(6,4),(7, 4),(8, 4),      (10,4),(11,4),              (14,4),       (16, 4),(17, 4),(18, 4),(19,4), 
    (1,5),(2,5),      (4,5),(5,5),(6,5),                    (10,5),(11,5),
    (1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7, 6),(8, 6),(9,6),(10,6),(11,6),(12,6),(13,6),(14,6),(15,6),(16, 6),(17, 6),(18, 6),(19,6),(20,6),                             (25, 6),(26, 6),
    (1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7, 7),(8, 7),(9,7),                                                          (18, 7),                      (22, 7),(23,7),      (25, 7),
                                                                                                              (17, 8),                      (21, 8),(22, 8),             (25, 8),(26, 8),
                                                                                                      (16, 9),(17, 9),                      (21, 9),(22, 9),             (25, 9),(26, 9),
                                                                                                      (16,10),(17,10),(18,10),              (21,10),(22,10),             (25,10),(26,10),
    (0,11),                                                                                                   (17,11),                      (21,11),(22,11),             (25,11),(26,11),
                                                                                                      (16,12),(17,12),                      (21,12),(22,12),             (25,12),(26,12),
                                                                                                      (16,13),(17,13),(18,13),              (21,13),(22,13),             (25,13),(26,13),
    (12,20),(16,20),
    (12,21),
    (12,23),(16,23),
)
TM_BREAKABLE = {
    (23,0):((24,0),(25,0)),
    (23,1):((24,0),(25,0)),
    (26,0):((27,0),(28,0)),
    (26,1):((27,0),(28,0)),
    (23,2):((24,2),(25,2)),
    (26,2):((27,2),(28,2)),
    (26,3):((27,2),(28,2)),
}
TM_BRIDGE = ((26,1),((27,0),(28,0)))
TM_DOOR_CLOSE = {
    (21, 8):(0,0,0),  # Blue,dx,dy
    (21, 9):(0,0,1),
    (21,10):(0,0,2),
    (22, 8):(0,3,0),
    (22, 9):(0,3,1),
    (22,10):(0,3,2),
    (21,11):(1,0,0),  # Red,dx,dy
    (21,12):(1,0,1),
    (21,13):(1,0,2),
    (22,11):(1,3,0),
    (22,12):(1,3,1),
    (22,13):(1,3,2),
    (25, 8):(2,0,0),  # Yellow,dx,dy
    (25, 9):(2,0,1),
    (25,10):(2,0,2),
    (26, 8):(2,3,0),
    (26, 9):(2,3,1),
    (26,10):(2,3,2),
    (25,11):(3,0,0),  # Purple,dx,dy
    (25,12):(3,0,1),
    (25,13):(3,0,2),
    (26,11):(3,3,0),
    (26,12):(3,3,1),
    (26,13):(3,3,2),
}
TM_DOOR_AJAR = (
    ((20, 8),(20, 9),(20,10),(23, 8),(23, 9),(23,10)),  # Blue
    ((20,11),(20,12),(20,13),(23,11),(23,12),(23,13)),  # Red
    ((24, 8),(24, 9),(24,10),(27, 8),(27, 9),(27,10)),  # Yellow
    ((24,11),(24,12),(24,13),(27,11),(27,12),(27,13)),  # Purple
)

def user_faceing(x, y):  # User Facing
    pyxel.blt(x, y, 0, 4, 144, 8, 16, 1)
def user_idle(x, y, left, aimup):  # User Idle
    if aimup:
        pyxel.blt(x-2, y-3, 0, 18, 181, -12 if left else 12, 19, 1)
    else:
        pyxel.blt(x-2, y, 0, 18, 144, -12 if left else 12, 16, 1)
def user_walk1(x, y, left, aimup=False, shoot=False):  # User Walk1
    if aimup:
        pyxel.blt(x+1, y-3, 0, 37, 181, -6 if left else 6, 19, 1)  # AimUpWalk1
    elif shoot:
        pyxel.blt(x-2, y+1, 0, 34, 161, -12 if left else 12, 15, 1)  # ShootWalk1
    else:
        pyxel.blt(x, y, 0, 36, 144, -8 if left else 8, 16, 1)  # Walk1
def user_walk2(x, y, left, aimup, shoot):  # User Walk2
    if aimup:
        pyxel.blt(x-1, y-3, 0, 51, 181, -10 if left else 10, 19, 1)  # AimUpWalk2
    elif shoot:
        pyxel.blt(x-2, y+1, 0, 50, 161, -12 if left else 12, 15, 1)  # ShootWalk2
    else:
        pyxel.blt(x-1, y, 0, 51, 144, -10 if left else 10, 16, 1)  # Walk2
def user_walk3(x, y, left, aimup, shoot):  # User Walk3
    if aimup:
        pyxel.blt(x-2, y-3, 0, 66, 181, -12 if left else 12, 19, 1)  # AimUpWalk3
    elif shoot:
        pyxel.blt(x-3, y+1, 0, 65, 161, -14 if left else 14, 15, 1)  # ShootWalk3
    else:
        pyxel.blt(x-3, y, 0, 65, 144, -14 if left else 14, 16, 1)  # Walk3
def user_jump(x, y, left, aimup=False, shoot=False):  # User Jump
    if aimup:
        pyxel.blt(x-2, y-3, 0, 82, 181, -12 if left else 12, 16, 1)  # AimUpJump
    elif shoot:
        pyxel.blt(x-2, y+1, 0, 82, 161, -12 if left else 12, 12, 1)  # ShootJump
    else:
        pyxel.blt(x-2, y, 0, 82, 144, -12 if left else 12, 13, 1)  # Jump
def user_spinjump1(x, y, left):
    pyxel.blt(x, y-1, 0, 100, 144, -8 if left else 8, 12, 1)  # SpinJump1
def user_spinjump2(x, y, left):
    pyxel.blt(x, y, 0, 116, 144, -10 if left else 10, 8, 1)  # SpinJump2
def user_spinjump3(x, y, left):
    pyxel.blt(x, y-1, 0, 132, 144, -8 if left else 8, 11, 1)  # SpinJump3
def user_spinjump4(x, y, left):
    pyxel.blt(x-1, y, 0, 147, 144, -10 if left else 10, 9, 1)  # SpinJump4
def user_morphing(x, y, left):
    pyxel.blt(x, y, 0, 160, 144, -8 if left else 8, 16, 1)  # Morphing
def user_morphball1(x, y, left):
    pyxel.blt(x, y+8, 0, 168, 152, -8 if left else 8, 8, 1)  # MorphBall1
def user_morphball2(x, y, left):
    pyxel.blt(x, y+8, 0, 176, 152, -8 if left else 8, 8, 1)  # MorphBall2
def user_morphball3(x, y, left):
    pyxel.blt(x, y+8, 0, 184, 152, -8 if left else 8, 8, 1)  # MorphBall3
def user_morphball4(x, y, left):
    pyxel.blt(x, y+8, 0, 192, 152, -8 if left else 8, 8, 1)  # MorphBall4
def user_ending1(x, y):  # User Ending Suit
    pyxel.blt(x, y, 0,  0, 224, 16, 24, 1)
def user_ending2(x, y):  # User Ending Bikini
    pyxel.blt(x, y, 0, 16, 224, 16, 24, 1)
def user_ending3(x, y, w):  # User Ending WaveHand
    pyxel.blt(x, y, 0, 32 if w else 48, 224, 16, 24, 1)
def user_death(x, y, n):  # death
    ulx, uly, urx, ury = 0, 160, 4, 160
    mlx, mly, mrx, mry = 0, 164, 4, 164
    dlx, dly, drx, dry = 0, 168, 4, 168
    pyxel.blt(x  -n//3, y   -n//2, 0, ulx, uly, 4, 4, 1)
    pyxel.blt(x+4+n//3, y   -n//2, 0, urx, ury, 4, 4, 1)
    pyxel.blt(x  -n//2, y+4 -n//3, 0, mlx, mly, 4, 4, 1)
    pyxel.blt(x+4+n//2, y+4 -n//3, 0, mrx, mry, 4, 4, 1)
    pyxel.blt(x  -n//2, y+8     , 0, dlx, dly, 4, 4, 1)
    pyxel.blt(x+4+n//2, y+8     , 0, drx, dry, 4, 4, 1)

def the_end(x, y):
    pyxel.blt(x, y, 0, 208, 112, 48, 16, 1)
def elevator(x, y):  # Elevator
    pyxel.blt(x, y, 0, 136, 16, 16, 4, 1)

TM_ENERGY = (2, 15)  # TileMap EnergyTank
def invt_energy(x, y):  # Inventory EnergyTank
    pyxel.blt(x, y, 0, 16, 120, 8, 8, 1)
TM_MISSILE = (15, 15)  # TileMap Missile
def invt_missile(x, y, ptn):  # Inventory Missile
    pyxel.blt(x, y, 0, 112 if ptn==1 else 120 if ptn==2 else 128 if ptn==3 else 136, 120, 8, 8, 1)
TM_BALL = (4, 15)  # TileMap MorphBall
def invt_ball(x, y):  # Inventory MorphBall
    pyxel.blt(x, y, 0, 32, 120, 8, 8, 1)
TM_BOMB = (7, 15)  # TileMap Bomb
def invt_bomb(x, y):  # Inventory Bomb
    pyxel.blt(x, y, 0, 56, 120, 8, 8, 1)
TM_LONG = (9, 15)  # TileMap LongBeam
def invt_long(x, y):  # Inventory LongBeam
    pyxel.blt(x, y, 0, 72, 120, 8, 8, 1)
TM_VARIA = (6, 15)  # Inventory Varia
def invt_varia(x, y):  # Inventory Varia
    pyxel.blt(x, y, 0, 48, 120, 8, 8, 1)
TM_ICE = (11, 15)  # Inventory IceBeam
def invt_ice(x, y):  # Inventory IceBeam
    pyxel.blt(x, y, 0, 11*8, 15*8, 8, 8, 1)
TM_HIGH = (5, 15)  # Inventory HighJump
def invt_high(x, y):  # Inventory HighJump
    pyxel.blt(x, y, 0, 5*8, 15*8, 8, 8, 1)
def invt_ridley(x, y):  # Inventory Ridley
    pyxel.blt(x, y, 0, 96, 120, 8, 8, 1)
def invt_kraid(x, y):  # Inventory Kraid
    pyxel.blt(x, y, 0, 104, 120, 8, 8, 1)

TM_SWAMP = ((0,8),(1,8),(0,9),(1,9),(0,10),(1,10))

def beam(x, y, ptn):  # Beam
    pyxel.blt(x, y, 0, 202 if ptn==1 else 200, 144 if ptn in (0,1) else 146, 2, 2, 1)
def bomb(x, y, ptn):  # Bomb
    pyxel.blt(x, y, 0, 216 if ptn%2 else 220, 144, 4, 4, 1)
def bomb_burst(x, y, ptn):  # BombBurst
    pyxel.blt(x-2, y-2, 0, 216 if ptn%2==0 else 224, 152, 8, 8, 1)
def burst(x, y):  # Burst
    pyxel.blt(x, y, 0, 232, 144, 16, 16, 1)

def energyball(x, y, ptn):  # Energy Ball
    pyxel.blt(x, y, 0, 0 if ptn%2 else 4, 120, 4, 4, 1)
def missile(x, y, ptn):  # Missile
    pyxel.blt(x, y, 0, 8 if ptn%2 else 12, 120, 4, 6, 1)

def energy100(x, y, full):
    pyxel.blt(x, y, 0, 4 if full else 0, 124, 4, 4, 1)

TM_ZOOMER = (0, 25)
TM_SKREE = (2, 25)
TM_REO = (6, 25)
TM_RIPPER = (12, 25)
TM_WAVER = (13, 25)
TM_ZEB = (15, 25)
TM_MELLOW = (17, 25)

NO_DIR, LEFT, RIGHT, UP, DOWN = 0,1,2,3,4
def zoomer(x, y, cont, ptn):
    if cont==DOWN:
        pyxel.blt(x, y, 0, 0, 200, 8 if ptn%2 else -8, 8, 1)
    elif cont==UP:
        pyxel.blt(x, y, 0, 0, 200, 8 if ptn%2 else -8, -8, 1)
    elif cont==RIGHT:
        pyxel.blt(x, y, 0, 8, 200, 8, 8 if ptn%2 else -8, 1)
    elif cont==LEFT:
        pyxel.blt(x, y, 0, 8, 200, -8, 8 if ptn%2 else -8, 1)

def skree(x, y, ptn):
    if ptn%3==0:
        pyxel.blt(x, y, 0, 16, 200, 8, 12, 1)
    elif ptn%3==1:
        pyxel.blt(x+2, y, 0, 26, 200, 4, 12, 1)
    else:
        pyxel.blt(x+2, y, 0, 26, 200, -4, 12, 1)

def explotion(x, y):
    pyxel.blt(x, y, 0, 16, 216, 4, 4, 1)

def reo(x, y, ptn):
    if ptn%2==0:
        pyxel.blt(x, y, 0, 50, 200, 12, 10, 1)
    else:
        pyxel.blt(x, y+2, 0, 50, 216, 12, 8, 1)

def ripper(x, y, dx):
    pyxel.blt(x, y, 0, 96, 200, 8 if dx>0 else -8, 4, 1)

def waver(x, y, dx, ptn):
    pyxel.blt(x, y, 0, 104, 200 if ptn%3==0 else 208 if ptn%3==1 else 216, 8 if dx<0 else -8, 8, 1)

def zeb(x, y, dx, ptn):
    pyxel.blt(x, y, 0, 120 if ptn%2==0 else 128, 200, 8 if dx<0 else -8, 8, 1)

def mellow(x, y, ptn):
    pyxel.blt(x, y, 0, 136, 200 if ptn%2==0 else 208, 8, 4, 1)

TM_METROID = (10, 28)
def metroid(x, y, ptn):
    pyxel.blt(x, y, 0, 80 if ptn%2==0 else 96, 224, 12, 12, 1)

TM_RINKA = (5, 27)
def rinka(x, y, ptn):
    pyxel.blt(x, y, 0, 24 if ptn==0 else 32 if ptn==1 else 40, 216, 5, 5, 1)

TM_CANNON0 = (22,30)
TM_CANNON1 = (23,30)
TM_CANNON2 = (24,30)
def cannon(x, y, ptn):
    if ptn==0:  # 左下
        ax,ay, u,v = -7,3, 176,240
    elif ptn==1:  # 下
        ax,ay, u,v = -2,4, 184,240
    elif ptn==2:  # 右下
        ax,ay, u,v = 3,3, 192,240
    elif ptn==3:  # 右
        ax,ay, u,v = 4,-2, 192,232
    elif ptn==4:  # 右上
        ax,ay, u,v = 3,-7, 192,224
    elif ptn==5:  # 上
        ax,ay, u,v = -2,-8, 184,224
    elif ptn==6:  # 左上
        ax,ay, u,v = -7,-7, 176,224
    else:  # ptn==7: 左
        ax,ay, u,v = -8, -2, 176,232
    pyxel.blt(x+ax, y+ay, 0, u, v, 8, 8, 1)

def cannon_missile(x, y, ptn):  # ptn：0～2
    pyxel.blt(x, y, 0, 200 if ptn==1 else 204, 224 if ptn in (0,2) else 228, -4 if ptn==2 else 4, 4, 1)
def cannon_burst(x, y, ptn):  # ptn：0～2
    if ptn==0:
        pyxel.blt(x, y, 0, 204, 228, 4, 4, 1)
    else:
        pyxel.blt(x-2, y-2, 0, 208, 224, 8, 8, 1)

TM_ZEBETITE = (20,20)
def zebetite(x, y, ptn):
    pyxel.blt(x, y  , 0, 160, 184 if ptn==0 else 176 if ptn==1 else 168 if ptn==2 else 160, 8, 8, 1)
    pyxel.blt(x, y+8, 0, 160, 184 if ptn==0 else 176 if ptn==1 else 168 if ptn==2 else 160, 8, 8, 1)

#TM_ALLGLASS = ((18,102),(18,103),(18,104),(18,105),(22,102),(22,105))
TM_ALLGLASS = ((18,70),(18,71),(18,72),(18,73),(22,70),(22,73))
TM_GLASS = (16,21)
def glass(x, y):
    pyxel.blt(x, y  , 0, 128, 168, 8, 8, 1)
    pyxel.blt(x, y+8, 0, 128, 168, 8, 8, 1)

# RIDLEY
TM_RIDLEY_UP = (19,2)
TM_RIDLEY_LOW = (19,3)
def ridley_appr(tx, ty, tm):
    pyxel.tilemaps[tm].pset(tx, ty, (19,0))
    pyxel.tilemaps[tm].pset(tx, ty+1, (19,1))
TM_RIDLEY = (18, 25)
def ridley(x, y, left, ptn):
    pyxel.blt(x if left else x-8, y, 0, 144 if ptn%4==0 else 160 if ptn%4==1 else 176 if ptn%4==2 else 192, 200, -16 if left else 16, 20 if ptn%4 in (0,1) else 24, 1)
def fire(x, y, ptn):
    pyxel.blt(x,y, 0, 208 if ptn%4 in (0,2) else 212, 200 if ptn%4 in (0,1) else 204, 4, 4, 1)

# KRAID
TM_KRAID_UP = (21,2)
TM_KRAID_LOW = (21,3)
def kraid_appr(tx, ty, tm):
    pyxel.tilemaps[tm].pset(tx,   ty,   (21,0))
    pyxel.tilemaps[tm].pset(tx+1, ty,   (22,0))
    pyxel.tilemaps[tm].pset(tx-1, ty+1, (20,1))
    pyxel.tilemaps[tm].pset(tx,   ty+1, (21,1))
    pyxel.tilemaps[tm].pset(tx+1, ty+1, (22,1))
TM_KRAID = (18, 28)
def kraid(x, y, left, ptn):
    pyxel.blt(x, y, 0, 144 if ptn%2==0 else 160, 224, -12 if left else 12, 16, 1)
def needle(x, y):
    pyxel.blt(x,y, 0, 144, 240, 2, 2, 1)
def plate(x, y, ptn):
    pyxel.blt(x,y, 0, 152 if ptn%4 in (0,2) else 156, 240 if ptn%4 in (0,1) else 244, 4, 4, 1)

TM_MOTHERBRAIN = (13,20)
def motherbrain(x, y, ptn):
    if ptn==0:
        pyxel.blt(x, y, 0, 104, 160, 24, 32, 1)
    else:
        pyxel.blt(x, y, 0, 136, 160, 24, 32, 1)

