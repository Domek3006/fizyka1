import pygame, sys
import random
import math

pygame.init()
czas = pygame.time.Clock()

H=500                                       # wysokość zbiornika
L=800                                       # szerokość zbiornika
screen = pygame.display.set_mode((L,H))     # -------------

class Atom():
    def __init__(self,Rect,x,y,s,kolor):
        self.Rect = Rect
        self.speed_x = x
        self.speed_y = y
        self.r = s/2
        self.col = kolor


def kolizja(j,atomy):                       #zwraca indeks pierwszego atomu z którym wykryje zdarzenie
    atom=atomy[j]
    for i in range(len(atomy)):
        atom2=atomy[i]
        # print(math.sqrt((atom.Rect.x - atom2.Rect.x) ** 2 + (atom.Rect.y - atom2.Rect.y) ** 2))
        if 56 < math.sqrt((atom.Rect.x - atom2.Rect.x)**2 + (atom.Rect.y-atom2.Rect.y)**2) < 2*atom.r + 4:      #zamiast 56 2xpromień a x powinien r/10
            return i
    return -1



atomy=[]                #lista atomów

s=60                    #średnica


# set 1 ukośne ten sam kierunek x
obiekt0 = pygame.Rect(200, 200, s, s)
atom0 = Atom(obiekt0,-3,-3,s,(100,100,250))
atomy.append(atom0)
obie1 = pygame.Rect(100, 100, s, s )
atom1 = Atom(obie1,3,3,s,(250,100,100))
atomy.append(atom1)

#set2 ukośne ten sam kierunek y
obiekt2 = pygame.Rect(650, 400, s, s )
atom2 = Atom(obiekt2,-3,-4,s,(255,255,255))
atomy.append(atom2)
obie3 = pygame.Rect(350, 300, s, s )
atom3 = Atom(obie3,3,-2,s,(0,0,0))
atomy.append(atom3)

# set3    prawo lewo
obiekt4 = pygame.Rect(70, 430, s, s)
atom4 = Atom(obiekt4,3,0,s,(50,150,100))
atomy.append(atom4)
obie5 = pygame.Rect(200, 430, s, s )
atom5 = Atom(obie5,-3,0,s,(250,250,100))
atomy.append(atom5)

# set4              góra dół
obiekt6 = pygame.Rect(80, 200, s, s )
atom6 = Atom(obiekt6,0,3,s,(250,100,250))
atomy.append(atom6)
obiekt7 = pygame.Rect(80, 360, s, s )
atom7 = Atom(obiekt7,0,-3,s,(100,250,250))
atomy.append(atom7)


def ruch():
    for atom in atomy:
        # print(atom.col,atom.Rect.x,atom.Rect.y)
        atom.Rect.x += atom.speed_x
        atom.Rect.y += atom.speed_y
        # print(atom.col, atom.Rect.x, atom.Rect.y)
    tablica = [0] * len(atomy)
    print(f"pozycja atomu {atom.col} {atom.Rect.x} i {atom.Rect.y}")

    for i in range(len(atomy)):
        atom=atomy[i]
        kol=kolizja(i,atomy)

        if atom.Rect.x <=0 or atom.Rect.x + 2*atom.r >= L:             #współrzędne wskazują na lewy górny róg kwadratu który wypełnia kulka
            print("pyk róg")
            atom.speed_x *= -1

        elif atom.Rect.y <=0 or atom.Rect.y + 2*atom.r >= H:
            print("pyk odbicie")
            atom.speed_y *= -1


        elif kol>=0 and tablica[kol]==0:
            atom1=atomy[kol]
            tablica[kol]=1
            tablica[i]=1
            #
            # atom.speed_y, atom1.speed_y = atom1.speed_y, atom.speed_y
            # atom.speed_x, atom1.speed_x = atom1.speed_x, atom.speed_x

            print(f"zderzenie atom {i} i {kol}","\nyspeed", atom.speed_y * atom1.speed_y, "\nxspeed",atom.speed_x * atom1.speed_x)

            if atom.speed_x * atom1.speed_x > 0 and atom.speed_y * atom1.speed_y < 0:              #atomy zderzają się góra dół, set2
                print("1")
                atom.speed_y, atom1.speed_y = atom1.speed_y, atom.speed_y
            elif atom.speed_x * atom1.speed_x > 0 and atom.speed_y * atom1.speed_y < 0:         #atomy zderzają się prawo lewo, set1
                print("2")
                atom.speed_x, atom1.speed_x = atom1.speed_x, atom.speed_x
            elif atom.speed_x * atom1.speed_x < 0 and atom.speed_y * atom1.speed_y <= 0:
                print("3")
                atom.speed_x, atom1.speed_x = atom1.speed_x, atom.speed_x
                atom.speed_y, atom1.speed_y = atom1.speed_y, atom.speed_y

            elif atom.speed_x * atom1.speed_x < 0 and atom.speed_y * atom1.speed_y > 0:
                print("4")
                atom.speed_y, atom1.speed_y = atom1.speed_y, atom.speed_y
                atom.speed_x, atom1.speed_x = atom1.speed_x, atom.speed_x


    # print("_____________________________",atom.Rect.colliderect(atom1.Rect))






        pygame.draw.ellipse(screen,atom.col,atom.Rect)




# Pętla programu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:       #wyście iksem z okienka konczy program
            pygame.quit()
            sys.exit()


    screen.fill((80,80,80))     #zmienia kolor tła okna
    ruch()
    pygame.display.flip()                   #wyświetla obiekty
    czas.tick(60)                           #spowalnia, max 60 klatek na sekundę

