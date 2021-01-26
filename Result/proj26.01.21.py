from pynput import keyboard
import time
start=0
end=0

s=0
e=0
def on_press(key):
    
    global start
    start=time.time()
    try:
        print('кнопка {0} была нажата'.format(key))
        global e
        
        
        e=time.time()
        
        ela=e-s
        
        print('Время между нажатиями:',ela)
        
        
        
    except AttributeError:
        print('особая кнопка {0} была нажата'.format(key))
    
def on_release(key):
    
    print('{0} отпущена'.format(key))
    global end
    global start
    end=time.time()
    elapsed=end-start
    print('время нажатия кнопки',elapsed)
    global s
    s=time.time()
    
    
    
    if key == keyboard.Key.esc:
        
        
        return False

with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    s=time.time()
    
    listener.join()
    


