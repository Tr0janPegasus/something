# I can look at this and confidently say 
# I have absolutely NO IDEA what's happening
# This just straight up doesn't work

import pygame as pig
import time

pig.init()
WINDOW = pig.display.set_mode((450,700))
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
Text = 'Text'
run = True

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
        img = pig.font.SysFont('timesnewroman', 2*K).render('  ' + self.text,True, BLACK)
        WINDOW.blit(img, (self.x, self.y - 5))

    def click(self):
        pig.draw.rect(WINDOW, BLACK, (self.x, self.y, 3*K, 2*K))
        img = pig.font.SysFont('timesnewroman', 2*K).render('  ' + self.text,True, WHITE)
        WINDOW.blit(img, (self.x, self.y))


btn_1 = Button(D + K, D + 0.45*Y+ K, '1') #First row
btn_2 = Button(D + 5*K, btn_1.y, '2')
btn_3 = Button(D + 9*K, btn_1.y, '3')
btn_min = Button(D + 13*K, btn_1.y, '-')

btn_4 = Button(D + K, btn_1.y + 3*K, '4') #Second row
btn_5 = Button(D + 5*K, btn_4.y, '5')
btn_6 = Button(D + 9*K, btn_4.y, '6')
btn_mult = Button(D + 13*K, btn_4.y, '*')

btn_7 = Button(D + K, btn_4.y + 3*K, '7') #Third row
btn_8 = Button(D + 5*K, btn_7.y, '8')
btn_9 = Button(D + 9*K, btn_7.y, '9')
btn_div = Button(D + 13*K, btn_7.y, '/')

btn_back = Button(D + K, btn_7.y + 3*K,'<=') #Fourth row
btn_0 = Button(D + 5*K, btn_back.y, '0')
btn_add = Button(D + 9*K, btn_back.y, '+')
btn_eq = Button(D + 13*K, btn_back.y, '=')

A = '0'
B = '0'



while run:
    Num_a = float(A) if '.' in A else int(A)
    Num_b = float(B) if '.' in B else int(B)

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
                Text += btn_1.text
            elif pos[0] in range(int(btn_2.x), int(btn_2.x + 3*K)) and pos[1] in range(int(btn_2.y), int(btn_2.y + 2*K)):
                btn_2.click()
                Text += btn_2.text
            elif pos[0] in range(int(btn_3.x), int(btn_3.x + 3*K)) and pos[1] in range(int(btn_3.y), int(btn_3.y + 2*K)):
                btn_3.click()
                Text += btn_3.text
            elif pos[0] in range(int(btn_min.x), int(btn_min.x + 3*K)) and pos[1] in range(int(btn_min.y), int(btn_min.y + 2*K)):
                btn_min.click()
                if Num_a != 0:
                    B = '0'
                    B = Text[1:]
                    if B != '':
                        Num_b = int(B)
                        A = str(Num_a - Num_b)
                    else:
                        B = '0'
                    print('1')
                    print('text: '+Text,'A:'+ A,'B:'+ B, Num_a, Num_b)
                else:
                    A = Text
                    print('2')
                    print('text: '+Text,'A:'+ A,'B:'+ B, Num_a, Num_b)
                Text = btn_min.text

            #Second row
            elif pos[0] in range(int(btn_4.x), int(btn_4.x + 3*K)) and pos[1] in range(int(btn_4.y), int(btn_4.y + 2*K)):
                btn_4.click()
                Text += btn_4.text
            elif pos[0] in range(int(btn_5.x), int(btn_5.x + 3*K)) and pos[1] in range(int(btn_5.y), int(btn_5.y + 2*K)):
                btn_5.click()
                Text += btn_5.text
            elif pos[0] in range(int(btn_6.x), int(btn_6.x + 3*K)) and pos[1] in range(int(btn_6.y), int(btn_6.y + 2*K)):
                btn_6.click()
                Text += btn_6.text
            elif pos[0] in range(int(btn_mult.x), int(btn_mult.x + 3*K)) and pos[1] in range(int(btn_mult.y), int(btn_mult.y + 2*K)):
                btn_mult.click()
                if Num_a != 0:
                    B = Text[1:]
                    if B != '':
                        Num_b = int(B)
                        A = str(Num_a * Num_b)
                        print('3')
                        print('text: '+Text,'A:'+ A,'B:'+ B, Num_a, Num_b)
                    else:
                        B = '0'
                else:
                    A = Text
                    print('4')
                    print('text: '+Text,'A:'+ A,'B:'+ B, Num_a, Num_b)
                Text = btn_mult.text

            #Third row
            elif pos[0] in range(int(btn_7.x), int(btn_7.x + 3*K)) and pos[1] in range(int(btn_7.y), int(btn_7.y + 2*K)):
                btn_7.click()
                Text += btn_7.text
            elif pos[0] in range(int(btn_8.x), int(btn_8.x + 3*K)) and pos[1] in range(int(btn_8.y), int(btn_8.y + 2*K)):
                btn_8.click()
                Text += btn_8.text
            elif pos[0] in range(int(btn_9.x), int(btn_9.x + 3*K)) and pos[1] in range(int(btn_9.y), int(btn_9.y + 2*K)):
                btn_9.click()
                Text += btn_9.text
            elif pos[0] in range(int(btn_div.x), int(btn_div.x + 3*K)) and pos[1] in range(int(btn_div.y), int(btn_div.y + 2*K)):
                btn_div.click()
                if Num_a != 0:
                    B = '0'
                    B = Text[1:]
                    if B != '':
                        Num_b = int(B) if '.' not in B else float(B)
                        try:
                            Num_a = Num_a / Num_b
                            Text = str(Num_a)
                        except Exception:
                            Text = 'Dividing by 0'
                    else:
                        B = '0'
                    print('5')
                    print('text: '+Text,'A:'+ A,'B:'+ B, Num_a, Num_b)
                else:
                    A = Text
                    print('6')
                    print('text: '+Text,'A:'+ A,'B:'+ B, Num_a, Num_b)
                Text = btn_div.text

            #Fourth row
            elif pos[0] in range(int(btn_back.x), int(btn_back.x + 3*K)) and pos[1] in range(int(btn_back.y), int(btn_back.y + 2*K)):
                btn_back.click()
                if len(Text)>0:
                    Text = Text[:-1]
            elif pos[0] in range(int(btn_0.x), int(btn_0.x + 3*K)) and pos[1] in range(int(btn_0.y), int(btn_0.y + 2*K)):
                btn_0.click()
                Text += btn_0.text
            elif pos[0] in range(int(btn_add.x), int(btn_add.x + 3*K)) and pos[1] in range(int(btn_add.y), int(btn_add.y + 2*K)):
                btn_add.click()
                if Num_a != 0:
                    B = '0'
                    B = Text[1:]
                    if B != '':
                        Num_b = int(B)
                        A = str(Num_a + Num_b)
                    else:
                        B = '0'
                    print('7')
                    print('text: '+Text,'A:'+ A,'B:'+ B, Num_a, Num_b)
                else:
                    A = Text
                    print('8')
                    print('text: '+Text,'A:'+ A,'B:'+ B, Num_a, Num_b)
                Text = btn_add.text

            elif pos[0] in range(int(btn_eq.x), int(btn_eq.x + 3*K)) and pos[1] in range(int(btn_eq.y), int(btn_eq.y + 2*K)):
                btn_eq.click()
                if Num_a != 0:
                    B = '0'
                    B = Text[1:]
                    print(B)
                    if B != '':
                        Num_b = int(B) if '.' not in B else float(B)
                        if Text[0] == '+':
                            A = str(Num_a + Num_b)
                            Text = A
                        elif Text[0] == '-':
                            A = str(Num_a - Num_b)
                            Text = A
                        elif Text[0] == '*':
                            A = str(Num_a * Num_b)
                            Text = A
                        elif Text[0] == '/':
                            try:
                                Num_a = Num_a / Num_b
                                Text = str(Num_a)
                            except ZeroDivisionError:
                                Text = 'Division by 0'
                    else:
                        B = '0'
                    print('9')
                    print("text:"+Text,'A:'+A,'B:'+B,Num_a,Num_b)
                else:
                    A = Text
                    print('10')
                    print('text: '+Text,'A:'+ A,'B:'+ B, Num_a, Num_b)
    

        else:
            WINDOW.fill(WHITE)
            pig.draw.rect(WINDOW, BLACK, (D, D, X, Y), 4)
            pig.draw.rect(WINDOW, BLACK, (D + K, D + K, X - 2*K, 0.35*Y + K))
            img = pig.font.SysFont(None, 48).render(Text, True, WHITE)
            WINDOW.blit(img, (D + X - 2*K - K*len(Text), 0.35*Y - K))

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