#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_____, ___
   '+ .;.    
    , ;.    
     . :,  
     ;'.    
      ..    
     .;.    
      .;  
       :  
       ,   
       

┌─[Vaile]─[]
└──╼ VainlyStrain
"""

import os, re
import time
import random
from time import sleep
from datetime import datetime
from random import uniform as rflt

from core import variables as vars
from core.Core.colors import *


def loadstyle():
    os.system('clear')
    red_bold = R
    cursive = color.END + "\033[3m"
    reset = cursive
    loading = "Loading console.."
    swappy = "Loading console.."
    display = """





____, __{}
   + ;    
   .:,    
     ’    
    .     {}‹›{}  {}V A I L E{}  {}‹›{}
    + ;   {}{}{}
    ;.    
     ;
     ;
     ’   
    """.format(color.END, R, color.END, RB, color.END, R, C, cursive, swappy, color.END)
    #loading = "——·‹› Vaile ‹›·——"
    action = 0
    while action < 2:
        for i, char in enumerate(loading):
            if i == 0:
                swappy = "%s%s%s%s" % (red_bold, char.swapcase(), reset, loading[1:])
                #print("%s%s%s%s" % (red_bold, char.swapcase(), reset, loading[1:]))
            elif i == 1:
                old_loading = loading[0].swapcase()
                swappy = "%s%s%s%s%s" % (old_loading, red_bold, char.swapcase(), reset, loading[2:])
                #print("%s%s%s%s%s" % (old_loading, red_bold, char.swapcase(), reset, loading[2:]))
            elif i == i:
                old_loading = loading[-0:i]
                swappy = "%s%s%s%s%s" % (old_loading, red_bold, char.swapcase(), reset, loading[i + 1:])
                #print("%s%s%s%s%s" % (old_loading, red_bold, char.swapcase(), reset, loading[i + 1:]))
            display = """





____, __{}
   + ;    
   .:,    
     ’    
    .     {}‹›{}  {}V A I L E{}  {}‹›{}
    + ;   {}{}{}
    ;.    
     ;
     ;
     ’   
            """.format(color.END, R, color.END, RB, color.END, R, C, cursive, swappy, color.END)
            print(display)
            time.sleep(0.1)
            os.system('clear')
        action += 1



vaile = '''{}                      |
                      :   
                      |   
                      .   
                      .   
                      .   
____, __             .|   
   + ;               .|   
   .{}:,                       
     ’                      
    .              /      
    + ;           :,      
    ;.           /,       
   {}  ;          /;' ;    
     ;         /;{}|{}  : ^  
     ’      /  . ;..  °   
          '/; '           
         ./ '.        
          '.  ’
         {}   '.
              \\
              .\\.    
                \\.               
                 .,.      
                   .'.    
                  ''.;:     
                    .|.   
                     | .  
                     .    
'''.format(color.END, color.BOLD, color.END, color.CURSIVE, color.END, color.BOLD)

vaile = '''{}                      |
                      :   
                      |   
                      .   
                      .   
                      .   
____, __             .|   
   + ;               .|   
   .{}:,                       
     ’                      
    .              /      
    + ;           :,      
    ;.           /,       
   {}  ;          /;' ;    
     ;         /;{}|{}  : ^  
     ’      / {}:{}  ;.’  °   
          '/; \\           
         ./ '. \\      {}|{}
          '.  ’·    __\\,_
         {}   '.      {}\\{}`{};{}{} 
              \\      {}\\ {}
              .\\.     {}V{}   
                \\.               
                 .,.      
                   .'.    
                  ''.;:     
                    .|.   
                     | .  
                     .    
'''.format(color.END, color.BOLD, color.END, color.CURSIVE, color.END, color.CURSIVE, color.END, color.CURSIVE, color.END, color.BOLD, color.END, color.BOLD, color.CURSIVE, color.END, color.BOLD, color.END, color.BOLD, color.END, color.BOLD)

sp00k70b3r = """
      ___
     /   \\
    / O O \\       _ __         
   |   O   |     /// / _   _   _ _ __ 
 , |       | ,  / ` /,'o| /o| /o|\\V / 
  \\/(     )\\/  /_n_/ |_,7/_,'/_,' )/  
   | )   ( |            //  //   //    
   |(     )|      ___
   ||   | |'    ,' _/ _   _   _   /7  /7  _   /7  __ _ 
   `|   | |    _\\ `. /o|,'o|,'o| //_7/_7,'o| /o\\,'o///7
    |   | |   /___,'/_,'|_,'|_,'//\\\\//  |_,'/_,'|_(//  
    |   /-'        //        
    |_.'    
""" 

christmas = """\033[1m
               ,--.
              (:.. )
           ,--.`--'
          (:.. )'""`.
           `--/`.__,'
             f f                      .-.   .-..----..----. .----..-.  .-. 
            ,'.`.                     |  `.'  || {_  | {}  }| {}  }\\ \\/ / 
        _,-'  :  `-._                 | |\\ /| || {__ | .-. \\| .-. \\ }  {  
        `-._ .:. _,-'                 `-' ` `-'`----'`-' `-'`-' `-' `--' 
            ) :.(          .---. .-. .-..----. .-. .----..---. .-.   .-.  .--.   .----.
        _,-' .:  `-._     /  ___}| {_} || {}  }| |{ {__ {_   _}|  `.'  | / {} \\ { {__  
       '-._  .:.  _,-`    \\     }| { } || .-. \\| |.-._} } | |  | |\\ /| |/  /\\  \\.-._} }
           )  :  (         `---' `-' `-'`-' `-'`-'`----'  `-'  `-' ` `-'`-'  `-'`----' 
       _,-'..::.  `-._
       `-._  .:   _,-'
           `. : ,'
         _,-' : `-._
         `-. .:. ,-'
            \\ . /
             `v' 

"""

currentMonth = datetime.now().month
currentDay = datetime.now().day

def f00l():
    return

def banner():
    os.system("clear")
    if currentMonth == 10:
        print(sp00k70b3r)
    elif currentDay == 1 and currentMonth == 4:
        f00l()
    elif currentDay in [24,25,26] and currentMonth == 12:
        print(christmas)
    else:
        print(vaile)

def randomsg():
    with open("files/ms.lst","r") as msg_list:
        return random.choice(msg_list.readlines()).strip()

def bannerbelownew():
    #print("   Vaile {}{}{}".format(color.END, RB, vars.e_version) + C)
    print("   {}Vaile{}{}{}{}{}{}{}{}{}{}".format(color.END, color.END, color.TR6, color.END, RB, vars.e_version.split("#")[0],C,color.TR3,G,vars.e_version.split("#")[1],color.TR2) + C)
    print("  {}{}{}".format(RC, randomsg(), color.END))


def info():
  print('''{}  {}                                                    {}  {}
 !  attack    Attack specified target(s)              M
 :  clear     Clear terminal.                         :
 V  creds     Handle target credentials.              
 :  fetch     Check for and install updates.          :
 :  find      Search a module.                        :
    help      Show help message.                      :
    info      Show description of current module.     M
 :  intro     Display Intro.                          :
 :  leave     Leave module.                           M
    list      List all modules of a category.         :
 :  load      Load module.                            :
 :  netinfo   Show network information.               :
 :  opts      Show options of current module.         M
    phpsploit Load the phpsploit framework.           :
              (needs to be downloaded externally)
 :  processes Set number of processes in parallelis.  :
    q         Terminate Vaile session.                :
 :  sessions  Interact with cached sessions.          :
 :  set       Set option value of module.             M
 :  tor       Pipe Attacks through the Tor Network.   :
    vicadd    Add Target to list.                     :
    vicdel    Delete Target from list.                :
    viclist   List all targets.                       :

  {}Avail. Cmds{}
    {}M{} needs loaded modvle
    {}V [! potentially]{} need loaded target(s)
'''.format(color.UNDERLINE, color.END, color.UNDERLINE, color.END, color.UNDERLINE, color.END, color.BOLD, color.END, color.BOLD, color.END,))


def disclaimer():
    print("""
DISCLAIMER
----------

Vaile Attack was provided as an open-source, royalty-free penetration testing toolkit. It has capable modules in various phases which can unveil potential dangerous flaws in various web-applications which can further be exploited maliciously. Therefore the author as well as the contrbutors assume no liability for misuseof this toolkit. Usage of Vaile Attack for testing or exploiting websites without prior mutual consent can be considered as an illegal activity. It is the final user's responsibility to obey all applicable local, state and federal laws.  
            """)

def title(mod):
    return " ".join(mod[i].upper() for i in range(0, len(mod)))

def posintpas(mod):
    print("""
   ,_       
 ,'  `\\,_   
 |_,-'_)    
 /##c '\\  (   {}O S I N T   P A S S I V E{}
' |'  -{{.  )
  /\\__-' \\[]        {}{}{}
 /`-_`\\     
 '     \\    
""".format(color.END, C, RC, title(mod), C))

def posint(mod):
    print("""
   ,_       
 ,'  `\\,_   
 |_,-'_)    
 /##c '\\  (   {}O S I N T{}
' |'  -{{.  )
  /\\__-' \\[]        {}{}{}
 /`-_`\\     
 '     \\    
""".format(color.END, C, RC, title(mod), C))

def posintact(mod):
    print("""
   ,_       
 ,'  `\\,_   
 |_,-'_)    
 /##c '\\  (   {}O S I N T   A C T I V E{}
' |'  -{{.  )
  /\\__-' \\[]        {}{}{}
 /`-_`\\     
 '     \\    
""".format(color.END, C, RC, title(mod), C))

def psploit(mod):
    print("""
      ,--.!,
   __/   -*-    {}S P L O I T{}
 ,d08b.  '|`
 0088MM     {}{}{}
 `9MMP'  
""".format(color.END, C, RC, title(mod), C))

def pvln(mod):
    print("""
   (
   '\\
  '  )       {}V L N Y S I S{}
##-------->     
  .  )       {}{}{}
   ./
   (
""".format(color.END, C, RC, title(mod), C))

def pscan(mod):
    print("""
       /\\
      /  \\
     /    \\   {}S C A N N I N G   &{}
    /      \\
   /        \\   {}E N U M E R A T I O N{}
  /          \\
 / /\\/\\  /\\/\\ \\   {}{}{}
/ /    \\/    \\ \\
\\/            \\/
""".format(color.END, C, color.END, C, RC, title(mod), C))

def pbrute(mod):
    print("""
 .--.
/.-. '----------.   {}B R U T E F O R C E{}
\\'-' .--"--""-"-'       {}{}{}
 '--'
""".format(color.END, C, RC, title(mod), C))

def pleak(mod):
    print("""
   ,_       
 ,'  `\\,_   
 |_,-'_)    
 /##c '\\  (   {}I N F D I S C{}
' |'  -{{.  )
  /\\__-' \\[]        {}{}{}
 /`-_`\\     
 '     \\ 
""".format(color.END, C, RC, title(mod), C))

def cprint(text1, text2):
    print(RC + text1 + color.END + RB + text2 + color.END)


def progressbar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + "{}༛{}".format(RD, color.END) * (length - filledLength)
    #print('\r%s [%s] %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    print('\r%s ———·›%s»·——— %s%% %s' % (prefix, bar, C+percent+color.END, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def summary(module, msg):
    display = """





{}____, __
   + ;    
   .:,    
     ’    
    .     {}‹›{}  {}{}{}  {}‹›{}
    + ;   {}{}{}
    ;.    
     ;
     ;
     ’   
    """.format(color.END, R, color.END, RB, title(module), color.END, R, C, color.CURSIVE, msg, color.END)
    print(display)

def loadstyle2():
    for i in range(0, 31):
        rnd = rflt(0.08, 0.15)
        time.sleep(rnd) #0.055
        #base = "Vaile {}".format(vars.r_version)
        base = "vailyn"
        if i%4 == 0:
            splitted = re.findall(".", base)
            for j in range(0, len(splitted)):
                #if j%4 == 0:
                if j == i%len(splitted):
                    splitted[j] = splitted[j].swapcase()
            disp = "".join(c for c in splitted)
            #progressbar(i, 30, fill="{}༛{}".format(color.END, color.END), length=20, suffix=" {} \\".format(disp))
            progressbar(i, 30, fill="{}༛{}".format(color.END, color.END), length=20, suffix="\\", prefix=disp+" ୰")
        elif i%4 == 1:
            splitted = re.findall(".", base)
            for j in range(0, len(splitted)):
                #if j%4 == 1:
                if j == i%len(splitted):
                    splitted[j] = splitted[j].swapcase()
            disp = "".join(c for c in splitted)
            #progressbar(i, 30, fill="{}༛{}".format(color.END, color.END), length=20, suffix=" {} |".format(disp))
            progressbar(i, 30, fill="{}༛{}".format(color.END, color.END), length=20, suffix="|", prefix=disp+" ୰")
        elif i%4 == 2:
            splitted = re.findall(".", base)
            for j in range(0, len(splitted)):
                #if j%4 == 2:
                if j == i%len(splitted):
                    splitted[j] = splitted[j].swapcase()
            disp = "".join(c for c in splitted)
            #progressbar(i, 30, fill="{}༛{}".format(color.END, color.END), length=20, suffix=" {} /".format(disp))
            progressbar(i, 30, fill="{}༛{}".format(color.END, color.END), length=20, suffix="/", prefix=disp+" ୰")
        else:
            splitted = re.findall(".", base)
            for j in range(0, len(splitted)):
                #if j%4 == 3:
                if j == i%len(splitted):
                    splitted[j] = splitted[j].swapcase()
            disp = "".join(c for c in splitted)
            #progressbar(i, 30, fill="{}༛{}".format(color.END, color.END), length=20, suffix=" {} -".format(disp))
            progressbar(i, 30, fill="{}༛{}".format(color.END, color.END), length=20, suffix="-", prefix=disp+" ୰")
    time.sleep(0.75)
    os.system("clear")
    """୰ง༒༛ለ៖៱៴▯ヾ"""