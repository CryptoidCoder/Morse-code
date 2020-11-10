import winsound
import time
# import modules
debug_mode = 'off'

if debug_mode == 'on': 
    pitch = 900
    soundvisual = 0
else: 
    pitch = int(input('What is the pitch you want all the Morse code to be in? {between 300 and 1000}: '))
    soundvisual = int(input('Sound will always play, do you want visuals aswell? 1 if yes 0 if no: '))
    if soundvisual == 1:
        visualtype = int(input('Do you want the visuals to be as words(dot & dash) or as characters (* & -). 1 if words 0 if characters: '))
        if visualtype == 1:
            def visualdot():
                print ('dot')

            def visualdash():
                print('dash')

        elif visualtype == 0:
            def visualdot():
                print(' *')

            def visualdash():  
                print(' -')

def dotsound():
    winsound.Beep(pitch,100)
    time.sleep(0.7)

def dashsound():
    winsound.Beep(pitch,1000)
    time.sleep(0.7)
    
def dot():
    dotsound()
    if soundvisual == 1:
        visualdot()

def dash():
    dashsound()
    if soundvisual == 1:
        visualdash()
# determine definitions to make it easier
print(' ')
print('Definitions of sound complete')

if debug_mode == 'on':
    print(' ')
    print('Sound test skipped')

else:
    dot()
    dash()
    print(' ')
    print('Sound test complete')


def a():
    dot()
    dash()

def b():
    dash()
    dot()
    dot()
    dash()

def c():
    dash()
    dot()
    dash()
    dot()

def d():
    dash()
    dot()
    dash()

def e():
    dot()

def f():
    dot()
    dot()
    dash()
    dot()

def g():
    dash()
    dash()
    dot()

def h():
    dot()
    dot()
    dot()
    dot()

def i():
    dot()
    dot()

def j():
    dot()
    dash()
    dash()
    dash()
    
def k():
    dash()
    dot()
    dash()

def l():
    dot()
    dash()
    dot()
    dot()

def m():
    dash()
    dash()

def n():
    dash()
    dot()

def o():
    dash()
    dash()
    dash()

def p():
    dot()
    dash()
    dash()
    dot()

def q():
    dash()
    dash()
    dot()
    dash()

def r():
    dot()
    dash()
    dot()

def s():
    dot()
    dot()
    dot()

def t():
    dash()

def u():
    dot()
    dot()
    dash()

def v():
    dot()
    dot()
    dot()
    dash()

def w():
    dot()
    dash()
    dash()

def x():
    dash()
    dot()
    dot()
    dash()

def y():
    dash()
    dot()
    dash()
    dash()

def z():
    dash()
    dash()
    dot()
    dot()

def num1():
    dot()
    dash()
    dash()
    dash()
    dash()

def num2():
    dot()
    dot()
    dash()
    dash()
    dash()

def num3():
    dot()
    dot()
    dot()
    dash()
    dash()

def num4():
    dot()
    dot()
    dot()
    dot()
    dash()

def num5():
    dot()
    dot()
    dot()
    dot()
    dot()

def num6():
    dash()
    dot()
    dot()
    dot()
    dot()

def num7():
    dash()
    dash()
    dot()
    dot()
    dot()

def num8():
    dash()
    dash()
    dash()
    dot()
    dot()

def num9():
    dash()
    dash()
    dash()
    dash()
    dot()

def num0():
    dash()
    dash()
    dash()
    dash()
    dash()

    
# defining the numers 1-9-0 and the letters a-z
# if you want to add punctuation then add it here using the same technique

print(' ')
print('Definitions of letters done')


import keyboard

while True:
    print(keyboard.read_key())
    if keyboard.read_key() == "a":
        a()
    elif keyboard.read_key() == 'b':
        b()
    elif keyboard.read_key() == 'c':
        c()
    elif keyboard.read_key() == 'd':
        d()
    elif keyboard.read_key() == 'e':
        e()
    elif keyboard.read_key() == 'f':
        f()
    elif keyboard.read_key() == 'g':
        g()
    elif keyboard.read_key() == 'h':
        h()
    elif keyboard.read_key() == 'i':
        i()
    elif keyboard.read_key() == 'k':
        k()
    elif keyboard.read_key() == 'l':
        l()
    elif keyboard.read_key() == 'm':
        m()
    elif keyboard.read_key() == 'n':
        n()
    elif keyboard.read_key() == 'o':
        o()
    elif keyboard.read_key() == 'p':
        p()
    elif keyboard.read_key() == 'q':
        q()
    elif keyboard.read_key() == 'r':
        r()
    elif keyboard.read_key() == 's':
        s()
    elif keyboard.read_key() == 't':
        t()
    elif keyboard.read_key() == 'u':
        u()
    elif keyboard.read_key() == 'v':
        v()
    elif keyboard.read_key() == 'w':
        w()
    elif keyboard.read_key() == 'x':
        x()
    elif keyboard.read_key() == 'y':
        y()
    elif keyboard.read_key() == 'z':
        z()
    elif keyboard.read_key() == '1':
        num1()
    elif keyboard.read_key() == '2':
        num2()
    elif keyboard.read_key() == '3':
        num3()
    elif keyboard.read_key() == '4':
        num4()
    elif keyboard.read_key() == '5':
        num5()
    elif keyboard.read_key() == '6':
        num6()
    elif keyboard.read_key() == '7':
        num7()
    elif keyboard.read_key() == '8':
        num8()
    elif keyboard.read_key() == '9':
        num9()
    elif keyboard.read_key() == '0':
        num0()
