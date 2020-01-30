import winsound
# import modules

pitch = int(input('What is the pitch you want all the Morse code to be in? {between 300 and 1000}'))

def dot():
    winsound.Beep(pitch,100)

def dash():
    winsound.Beep(pitch,2000)

def word_end():
    print('/')

def a():
    dot()
    dash()

#a = dot(), dash()
#b = dash(), dot(), dot(), dot()
#c = dash(), dot(), dash(), dot()
#d = dash(), dot(), dot()
#e = dot()
#f = dot(), dot(), dash(), dot()
#g = dash(), dash(), dot()
#h = dot(), dot(), dot(), dot()
#i = dot(), dot()
#j = dot(), dash(), dash(), dash()
#k = dash(), dot(), dash()
#l = dot(), dash(), dot(), dot()
#m = dash(), dash()
#n = dash(), dot()
#o = dash(), dash(), dash()
#p = dot(), dash(), dash(), dot()
#q = dash(), dash(), dot(), dash()
#r = dot(), dash(), dot()
#s = dot(), dot(), dot()
#t = dash()
#u = dot(), dot(), dash()
#v = dot(), dot(), dot(), dash()
#w = dot(), dash(), dash()
#x = dash(), dot(), dot(), dash()
#y = dash(), dot(), dash(), dash()
#z = dash(), dash(), dot(), dot()
#num1 = dot(), dash(), dash(), dash(), dash()
#num2 = dot(), dot(), dash(), dash(), dash()
#num3 = dot(), dot(), dot(), dash(), dash()
#num4 = dot(), dot(), dot(), dot(), dash()
#num5 = dot(), dot(), dot(), dot(), dot()
#num6 = dash(), dot(), dot(), dot(), dot()
#num7 = dash(), dash(), dot(), dot(), dot()
#num8 = dash(), dash(), dash(), dot(), dot()
#num9 = dash(), dash(), dash(), dash(), dot()
#num0 = dash(), dash(), dash(), dash(), dash()

# determine definitions to make it easier
print('definitions complete')


a()
print ('executed a')
input('program finished, press any key to continue...')

