import pygame as pig

pig.init()
WINDOW = pig.display.set_mode((450,700))
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#Random ratios and constants I made as per design
K = 20
X = 17*K
Y = 13/0.55*K
D = 50

class Button():
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw(self):
        pig.draw.rect(WINDOW, BLACK, (self.x, self.y, 3*K, 2*K), 2)
        img = pig.font.SysFont('timesnewroman', 2*K).render(self.text,True, BLACK)
        WINDOW.blit(img, (self.x, self.y - 3))

    def click(self):
        pig.draw.rect(WINDOW, BLACK, (self.x, self.y, 3*K, 2*K))
        img = pig.font.SysFont('timesnewroman', 2*K).render(self.text,True, WHITE)
        WINDOW.blit(img, (self.x, self.y))


btn_1 = Button(D + K, D + 0.45*Y+ K, '  1') #First row
btn_2 = Button(D + 5*K, btn_1.y, '  2')
btn_3 = Button(D + 9*K, btn_1.y, '  3')
btn_min = Button(D + 13*K, btn_1.y, '  -')

btn_4 = Button(D + K, btn_1.y + 3*K, '  4') #Second row
btn_5 = Button(D + 5*K, btn_4.y, '  5')
btn_6 = Button(D + 9*K, btn_4.y, '  6')
btn_mult = Button(D + 13*K, btn_4.y, '  x')

btn_7 = Button(D + K, btn_4.y + 3*K, '  7') #Third row
btn_8 = Button(D + 5*K, btn_7.y, '  8')
btn_9 = Button(D + 9*K, btn_7.y, '  9')
btn_div = Button(D + 13*K, btn_7.y, '  /')

btn_back = Button(D + K, btn_7.y + 3*K,' <=') #Fourth row
btn_0 = Button(D + 5*K, btn_back.y, '  0')
btn_add = Button(D + 9*K, btn_back.y, '  +')
btn_eq = Button(D + 13*K, btn_back.y, '  =')



run = True


while run:

    for event in pig.event.get():
        if event.type == pig.QUIT:
            run = False
        if event.type == pig.KEYDOWN:
            if event.key == pig.K_ESCAPE:
                run = False

        elif event.type == pig.MOUSEBUTTONDOWN:
            pos = event.pos

            #First row
            if pos[0] in range(int(btn_1.x), int(btn_1.x + 3*K)) and pos[1] in range(int(btn_1.y), int(btn_1.y + 2*K)):
                btn_1.click()
            elif pos[0] in range(int(btn_2.x), int(btn_2.x + 3*K)) and pos[1] in range(int(btn_2.y), int(btn_2.y + 2*K)):
                btn_2.click()
            elif pos[0] in range(int(btn_3.x), int(btn_3.x + 3*K)) and pos[1] in range(int(btn_3.y), int(btn_3.y + 2*K)):
                btn_3.click()
            elif pos[0] in range(int(btn_min.x), int(btn_min.x + 3*K)) and pos[1] in range(int(btn_min.y), int(btn_min.y + 2*K)):
                btn_min.click()

            #Second row
            elif pos[0] in range(int(btn_4.x), int(btn_4.x + 3*K)) and pos[1] in range(int(btn_4.y), int(btn_4.y + 2*K)):
                btn_4.click()
            elif pos[0] in range(int(btn_5.x), int(btn_5.x + 3*K)) and pos[1] in range(int(btn_5.y), int(btn_5.y + 2*K)):
                btn_5.click()
            elif pos[0] in range(int(btn_6.x), int(btn_6.x + 3*K)) and pos[1] in range(int(btn_6.y), int(btn_6.y + 2*K)):
                btn_6.click()
            elif pos[0] in range(int(btn_mult.x), int(btn_mult.x + 3*K)) and pos[1] in range(int(btn_mult.y), int(btn_mult.y + 2*K)):
                btn_mult.click()

            #Third row
            elif pos[0] in range(int(btn_7.x), int(btn_7.x + 3*K)) and pos[1] in range(int(btn_7.y), int(btn_7.y + 2*K)):
                btn_7.click()
            elif pos[0] in range(int(btn_8.x), int(btn_8.x + 3*K)) and pos[1] in range(int(btn_8.y), int(btn_8.y + 2*K)):
                btn_8.click()
            elif pos[0] in range(int(btn_9.x), int(btn_9.x + 3*K)) and pos[1] in range(int(btn_9.y), int(btn_9.y + 2*K)):
                btn_9.click()
            elif pos[0] in range(int(btn_div.x), int(btn_div.x + 3*K)) and pos[1] in range(int(btn_div.y), int(btn_div.y + 2*K)):
                btn_div.click()

            #Fourth row
            elif pos[0] in range(int(btn_back.x), int(btn_back.x + 3*K)) and pos[1] in range(int(btn_back.y), int(btn_back.y + 2*K)):
                btn_back.click()
            elif pos[0] in range(int(btn_0.x), int(btn_0.x + 3*K)) and pos[1] in range(int(btn_0.y), int(btn_0.y + 2*K)):
                btn_0.click()
            elif pos[0] in range(int(btn_add.x), int(btn_add.x + 3*K)) and pos[1] in range(int(btn_add.y), int(btn_add.y + 2*K)):
                btn_add.click()
            elif pos[0] in range(int(btn_eq.x), int(btn_eq.x + 3*K)) and pos[1] in range(int(btn_eq.y), int(btn_eq.y + 2*K)):
                btn_eq.click()


        else:
            WINDOW.fill(WHITE)
            pig.draw.rect(WINDOW, BLACK, (D, D, X, Y), 4)
            pig.draw.rect(WINDOW, BLACK, (D + K, D + K, X - 2*K, 0.35*Y + K))

            btn_1.draw() #First row
            btn_2.draw()
            btn_3.draw()
            btn_min.draw()

            btn_4.draw() #Second row
            btn_5.draw()
            btn_6.draw()
            btn_mult.draw()

            btn_7.draw() #Third row
            btn_8.draw()
            btn_9.draw()
            btn_div.draw()

            btn_back.draw() #Fourth row
            btn_0.draw()
            btn_add.draw()
            btn_eq.draw()


    pig.display.update()


pig.quit()