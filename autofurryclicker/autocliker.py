import keyboard
import time
mode = 1
paused = True
import mouse
print("keybind pause shift+s selection de mode shift+m")
click_conte_sesion = 0 

def load_click_conte():
    global click_conte
    with open(r"C:\Users\alexa\Documents\phyton\autofurryclicker\click_conte.txt","r") as f:
        content = f.read().strip()
        if content.isdigit():
            click_conte = int(content)

def save_click_conte():
    with open(r"C:\Users\alexa\Documents\phyton\autofurryclicker\click_conte.txt","w") as f:
        f.write(str(click_conte))

def toggle_pause():
    global paused
    paused = not paused
    global click_conte
    global click_conte_sesion
    if paused:
        print("Pause activée. Pressez Shift+S pour reprendre.")
        print("nombre totalede click","(",click_conte,")""nombre click sesion","(",click_conte_sesion,")")
    else:
        print("Reprise du script.")
    time.sleep(2)

def mod_selection():
    global mode 
    mod_selection = True
    print("mode selection press - ou + pour changer de mode et s pour quiter la selecton")
    while mod_selection:
        if keyboard.is_pressed("="):
            if mode < 5 :
                mode += 1 
            else:
                mode = 1
            time.sleep(0.2)
            print("mode:",mode)
            
        if keyboard.is_pressed("-"):
            if mode > 1 :
                mode -= 1 
            else:
                mode = 5
            time.sleep(0.2)
            print("mode:",mode)
        if keyboard.is_pressed("s"):
            #mod_selection = False
            print("mode actif:",mode)
            break

def autoclic_1():
    mouse.click()
    time.sleep(0.01)

def autoclic_2():
    mouse.click()
    time.sleep(0.05)

def autoclic_3():
    mouse.click()
    time.sleep(0.1)

def autoclic_4():
    mouse.click()
    time.sleep(0.2)

keyboard.add_hotkey('Shift+s',toggle_pause,time.sleep(0.02))
keyboard.add_hotkey('Shift+m',mod_selection)

load_click_conte()

while(True):
    if not paused :
        click_conte += 1 
        click_conte_sesion += 1 

        if mode == 1 :
            autoclic_1()
        if mode == 2:
            autoclic_2()
        if mode == 3:
            autoclic_3()
        if mode == 4:
            autoclic_4()

    if click_conte % 100 == 0:
        save_click_conte()
