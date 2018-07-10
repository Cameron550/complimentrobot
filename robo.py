import pygame
import random
import pyttsx3
import time

#display settings
displaywidth = 250
displayheight = 140
screen = pygame.display.set_mode((displaywidth,displayheight))
pygame.display.set_caption("Compliment bot")
white = (255,255,255)
#

pygame.init()

class interface:
    def __init__(self):
        self.roboimg = pygame.image.load("robot.png")
        self.meanrobot = 1
        

    def robot(self):
        #loads then displays the image based on which robot is selected
        if self.meanrobot == -1:        
            self.roboimg = pygame.image.load("insultrobot.png")

        
        elif self.meanrobot == 1:
            self.roboimg =  pygame.image.load("robot.png")
            
        screen.blit(self.roboimg, (1,0))
        #

    def update(self):
        pygame.display.update()

        
class speechrobot:
    def __init__(self):
        self.sentence = ""
        self.grp1list1 = ["hey,", "how are you doing,", "you're a great", "you are a ", "your a super"]
        self.grp2list2 = ["awesome", "real kind guy/girl", "great person",  "accomplished person", "talented indivisual"]

        self.brp1list1 = ["Hey super", "Hey", "How are you", "You're very", "Why do you have to be such a"]
        self.brp2list2 = ["ugly", "idiot", "hooligan", "trash bag", "mean person"]

        self.p1list1 = []
        self.p2list2 = []

            
    def generator(self):
        #selects random sentence from sentence parts
        if gui.meanrobot == 1:
            self.p1list1 = self.grp1list1
            self.p2list2 = self.grp2list2


        if gui.meanrobot == -1:
            self.p1list1 = self.brp1list1
            self.p2list2 = self.brp2list2

        self.randompart1 = random.randint(0,4)
        self.randompart2 = random.randint(0,4)

        self.part1 = self.p1list1[self.randompart1]
        self.part2 = self.p2list2[self.randompart2]
               
        self.sentence = self.part1 + self.part2
        #
        
    def speech1(self):
        #robot speaks the randomised sentence
        engine = pyttsx3.init()
        engine.say(self.sentence)
        engine.runAndWait()
        #

#class instances
gui = interface()
robottalk = speechrobot()
#    


def programloop():
    running = True

    while running:
        screen.fill(white)
        gui.robot()
        gui.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                
                print pos[1]
                #if player moves mouse to upper button then clicks, switch robots
                if pos[1] < 75:
                    if pygame.mouse.get_pressed()[:]:
                        gui.meanrobot = gui.meanrobot * -1         
                #
                
                elif pos[1] > 75:
                    if pygame.mouse.get_pressed()[:]:
                        robottalk.generator()
                        robottalk.speech1()
                        

                        
programloop()

pygame.quit()
quit()

    
