import time 
try: #importation des fonction
    import keyboard
    import mouse
except ImportError: #instalation des fonction manquante 
    print("une erreur et survenu le module <keyboard> et/ou <mouse>  et manquant voules vous l'instaler ? oui (o) si non (n) ")
    choix = input().lower()

    if choix == "n":
        import sys
        print("telechargement annuler le programe va se fermer ")
        time.sleep(3)
        sys.exit()
    if choix == "o":
            import subprocess
            import sys
            try:
                subprocess.check_call([sys.executable, "-m","pip","install","keyboard"]) #code pour pip install automatique
            except Exception as err:
                print("une erreur et survenu le programe va s'arreter")
                time.sleep(3)
                exit()
            
            try:
                subprocess.check_call([sys.executable, "-m","pip","install","mouse"])
            except Exception as err:
                print("une erreur et survenu le programe va s'arreter")
                time.sleep(3)
                exit()
            print("tout et instaler")
            import keyboard
            import mouse 



mode = 1
paused = True
import mouse
print("keybind pause shift+s selection de mode shift+m")
click_conte_sesion = 0 
record = False

def load_click_conte():
    global click_conte
    try:
        with open(r"C:\Users\alexa\Documents\phyton\autofurryclicker v1.1\click_conte.txt","r") as f:
            content = f.read().strip()
            if content.isdigit():
                click_conte = int(content)
    except FileNotFoundError:
        click_conte = 0

def save_click_conte():
    global click_conte
    try:
        with open(r"C:\Users\alexa\Documents\phyton\autofurryclicker v1.1\click_conte.txt","w") as f:
            try:
                f.write(str(click_conte))
            except NameError :
                click_conte = 0
    except FileNotFoundError :
        import os 
        os.makedirs(r"C:\Users\alexa\Documents\phyton\autofurryclicker v1.1")



def toggle_pause():
    global paused
    paused = not paused
    global click_conte
    global click_conte_sesion
    save_click_conte()
    if paused:
        print(r"""----------------------
⠀⠀⠀⠀⠀⢠⣒⣤⠤⣀⣀
⠀⠀⠠⣒⢤⠋⠂⠈⡷⠒⠒⣗⠢⡀
⠀⢠⠋⠀⡇⠀⠀⣰⠁⠀⢀⡼⠠⣱
⠀⢈⠀⠀⣧⣀⣠⣏⢀⠴⠋⠉⠙⡟⡄
⠀⠘⣄⢠⠟⠉⠉⢻⡎⠀⠀⠀⣸⠇⢸
⠀⢀⠜⡏⠁⠀⠀⠀⣧⣀⣠⠾⠋⠀⡜
⠀⡜⠀⠁⠀⠀⠀⠀⠘⣷⠀⠀⡠⠊
⠀⠹⣁⡤⢾⡀⠀⠀⢠⠏⠀⡐⠁
⠀⠀⠃⢴⠀⠉⠒⠚⠃⠀⢠
⠀⢸⠀⠈⠁
""")
        print("Pawse activée. Pressez Shift+S pour reprendre.")
        print("----------------------\nnombre totale de click","(",click_conte,")""\nnombre click sesion","(",click_conte_sesion,")\n----------------------")
        # click_conte = nombre de click totale du script sur le pc : click_conte_sesion = nombre de clique de la sesion acuelle 
    else:
        print("Reprise du script.")
    time.sleep(2)

def mod_selection():
    global mode 
    global mode_4_delay
    global paused
    while True:
        mod_selection = True
        print("mode selection")
        print(" mode 1 = (0.01) sec \n mode 2 = (0.05) \n mode 3 = (0.1)sec \n mode 4 = delay personaliser \n mode 5 = en devlopment ")
        mode = input()
        try:
            mode = int(mode)
        except ValueError :
            mode = 0

        if mode == 4:
            print("selection du delay entrer le delay sous sait forme (*.**) ")
            while True :
                mode_4_delay = input().replace(",", ".")
                try:
                    mode_4_delay = float(mode_4_delay)
                    print(mode_4_delay, "\n" )
                    if not paused :
                        toggle_pause()
                    else:
                        print("""----------------------
⠀⠀⠀⠀⠀⢠⣒⣤⠤⣀⣀
⠀⠀⠠⣒⢤⠋⠂⠈⡷⠒⠒⣗⠢⡀
⠀⢠⠋⠀⡇⠀⠀⣰⠁⠀⢀⡼⠠⣱
⠀⢈⠀⠀⣧⣀⣠⣏⢀⠴⠋⠉⠙⡟⡄
⠀⠘⣄⢠⠟⠉⠉⢻⡎⠀⠀⠀⣸⠇⢸
⠀⢀⠜⡏⠁⠀⠀⠀⣧⣀⣠⠾⠋⠀⡜
⠀⡜⠀⠁⠀⠀⠀⠀⠘⣷⠀⠀⡠⠊
⠀⠹⣁⡤⢾⡀⠀⠀⢠⠏⠀⡐⠁
⠀⠀⠃⢴⠀⠉⠒⠚⠃⠀⢠
⠀⢸⠀⠈⠁

Pawse activée. Pressez Shift+S pour reprendre.
----------------------
nombre totale de click ( 2503 )
nombre click sesion ( 178 )
----------------------""")
                    return

                except ValueError:
                    print("delay non valide entrer un nouveau delay")
                    time.sleep(0.5)

        elif mode >= 1 and mode <= 5 :
                print("mode selectionner mode (",mode,")")
                if not paused :
                    toggle_pause()
                return
        else :
            print("mode invalide")
            time.sleep(0.5)




def record_action():
    global record
    print("enregistrement lancer press (esc)")
    record = []

    def callback(event):
        record.append(event)

    mouse.hook(callback)
    keyboard.wait("esc")
    mouse.unhook(callback)

    print("enregistrement arreter")
    toggle_pause()

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
    time.sleep(mode_4_delay)

def autoclic_5():
    print("debut du replay")
    mouse.play(record)

keyboard.add_hotkey('Shift+s',toggle_pause)
keyboard.add_hotkey('Shift+m',mod_selection)

load_click_conte()

while(True):
    if not paused :
        click_conte += 1 
        click_conte_sesion += 1 

        if mode == 1 :
            autoclic_1()
        elif mode == 2:
            autoclic_2()
        elif mode == 3:
            autoclic_3()
        elif mode == 4:
            autoclic_4()
        elif mode == 5:
            if record == True :
                autoclic_5()
            else:
                record_action()
                time.sleep(0.05)
    else:
        time.sleep(0.1)
