# -*-coding:utf-8 -*


"""
Game docstring
"""


# ##############################################################################
# Importation of modules

import os
import pygame
from pygame.locals import *


from classes.mac import Mac
from classes.map import Map
from classes.obj import Obj

# ##############################################################################
# Definition of fonctions and start variables


map = Map()
map.load_cart()

mac = Mac(map.maincart)

obj = Obj(map.maincart)

obj_1 = Obj(map.maincart)
obj_1.random_obj()

obj_2 = Obj(map.maincart)
obj_2.random_obj()


obj_3 = Obj(map.maincart)
obj_3.random_obj()






win = False
los = False

"""
obj1_x, obj1_y = obj.random_obj()
obj2_x, obj2_y = obj.random_obj()
while map.maincart[obj2_x][obj2_y] != map.maincart[obj1_x][obj1_y]:
    obj2_x, obj2_y = obj.random_obj()

obj3_x, obj3_y = obj.random_obj()
while map.maincart[obj3_x][obj3_y] != map.maincart[obj2_x][obj2_y]\
and map.maincart[obj3_x][obj3_y] != map.maincart[obj1_x][obj1_y] :
    obj2_x, obj2_y = obj.random_obj()
"""
def initpygame():

    check = pygame.init()
    if check[1] != 0:
        print("""

        Error while loading PyGame

        """)

    else:
        print("""

        PyGame's loading : OK

        """)


def display_map(mac,obj):

    
        
    window = pygame.display.set_mode((300, 330)) #Size of 15 blocs of 20px each

    floors = pygame.image.load("ressources/floor.jpg").convert()  
    walls = pygame.image.load("ressources/wall.jpg").convert()  
    macg = pygame.image.load("ressources/mac.png").convert_alpha() 
    grdn = pygame.image.load("ressources/grd.png").convert_alpha() 
    obj1 = pygame.image.load("ressources/ether.png").convert_alpha()
    obj2 = pygame.image.load("ressources/syringe.png").convert_alpha()
    obj3 = pygame.image.load("ressources/tube.png").convert_alpha()
    wini = pygame.image.load("ressources/wini.png").convert_alpha()
    losi = pygame.image.load("ressources/losi.png").convert_alpha()
    topb = pygame.image.load("ressources/topbar.png").convert()


    # Loading map from the class Map
    carte = map.load_cart()
    

    
    
    for l in range(15):
        for e in range(15):
            window.blit(walls, (e*20,l*20+30))
            
            if map.maincart[l][e] == "@" or map.maincart[l][e] == "M" :
               
                window.blit(floors, (e*20,l*20+30))
             
            elif map.maincart[l][e] == "G":
               
                window.blit(floors, (e*20,l*20+30))
                window.blit(grdn, (e*20,l*20+30))
                
    
    window.blit(macg, (mac.mac_x*20,mac.mac_y*20+30))
    window.blit(topb, (0,0))

    if obj_1.objpick == False :
        window.blit(obj1, (obj_1.obj_y*20,obj_1.obj_x*20+30))
    else:
        window.blit(obj1, (240,5))


    if obj_2.objpick == False :
        window.blit(obj2, (obj_2.obj_y*20,obj_2.obj_x*20+30))
    else:
        window.blit(obj2, (260,5))
     
    if obj_3.objpick == False :
        window.blit(obj3, (obj_3.obj_y*20,obj_3.obj_x*20+30))
    else:
        window.blit(obj3, (280,5))
    

    if win :
        window.blit(wini, (0,0))
    if los :
        window.blit(losi, (0,0))
        
        
        
def loop():

    #Infinite loop to let the window open
    continuer = 1
    


    while continuer:
        for event in pygame.event.get():  
            if event.type == QUIT:      
                continuer = 0       

    

    #loop to display the walls, floors, macgyver and the guardian
    #------------------------------------------------------------

            
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    mac.mac_down() 
                    pick_obj()
                    display_map(mac,obj)  
                    print(obj.objcounter)
                if event.key == K_UP:
                    mac.mac_up()  
                    pick_obj()
                    display_map(mac,obj)  
                    print(obj.objcounter)
                if event.key == K_LEFT:
                    mac.mac_left()
                    pick_obj()
                    display_map(mac,obj)  
                    print(obj.objcounter)
                if event.key == K_RIGHT:
                    mac.mac_right() 
                    pick_obj()
                    display_map(mac,obj)  
                    print(obj.objcounter)
            
            
        
        pygame.display.flip()       #Display refresh



def pick_obj():

    

    if map.maincart[mac.mac_y]\
    [mac.mac_x] == map.maincart\
    [obj_1.obj_y][obj_1.obj_x] :
        
        obj.objcounter += 1
        obj_1.objpick = True
        print("test")
        
    
    if map.maincart[mac.mac_y]\
    [mac.mac_x] == map.maincart\
    [obj_2.obj_y][obj_2.obj_x] :
        
        obj.objcounter += 1
        obj_2.objpick = True


    if map.maincart[mac.mac_y]\
    [mac.mac_x] == map.maincart\
    [obj_3.obj_y][obj_3.obj_x] :
        
        obj.objcounter += 1
        obj_3.objpick = True

        
def winlose():

    if mac.front_g == True and obj.objcounter == 3 :
        win = True
    elif mac.front_g == True and obj.objcounter < 3 :
        los = True



# ##############################################################################

initpygame()

display_map(mac,obj)

loop()    


