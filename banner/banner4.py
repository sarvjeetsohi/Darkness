import os,sys,time,datetime,random,hashlib,re,threading

R = '\033[1;91m' # Red
N = '\033[1;97m' # White
G = '\033[1;92m' # Green
O = '\033[1;93m' # Orange
B = '\033[1;94m' # Blue
C = '\033[1;96m' # Orange
M = '\033[1;95m' # Orange
X = '\033[1;30m' # Grey
Y = '\033[48;5;0;38;5;94m'

def delay(z): 
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.002)

print ""
delay("\033[1;92m     ___                   ___                                                               ")
delay("\033[1;92m    (   )                 (   )                                                              ")
delay("\033[1;92m  .-.| |  .---.  ___ .-.   | |   ___   ___ .-.   .--.      .--.      .--.                    ")
delay("\033[1;92m /   \ | / .-, \(   )   \  | |  (   ) (   )   \ /    \   /  _  \   /  _  \                   ")
delay("\033[1;92m|  .-. |(__) ; | | ' .-. ; | |  ' /    |  .-. .|  .-. ; . .' `. ; . .' `. ;                  ")
delay("\033[1;92m| |  | |  .'`  | |  / (___)| |,' /     | |  | ||  | | | | '   | | | '   | |                  ")
delay("\033[1;92m| |  | | / .'| | | |       | .  '.     | |  | ||  |/  | _\_`.(___)_\_`.(___)                 ")
delay("\033[1;92m| |  | || /  | | | |       | | `. \    | |  | ||  ' _.'(   ). '. (   ). '.                   ")
delay("\033[1;92m| '  | |; |  ; | | |       | |   \ \   | |  | ||  .'.-. | |  `\ | | |  `\ |                  ")
delay("\033[1;92m' `-'  /' `-'  | | |       | |    \ .  | |  | |'  `-' / ; '._,' ' ; '._,' '                  ")
delay("\033[1;92m `.__,' `.__.'_.(___)     (___ ) (___)(___)(___)`.__.'   '.___.'   '.___.'                   ")
delay("\033[1;97m ___                                                                                         ")
delay("\033[1;97m(   )                                                                                        ")
delay("\033[1;97m | |_      .--.  ___ .-.   ___ .-. .-.  ___  ___  ___  ___                                   ")
delay("\033[1;97m(   __)   /    \(   )   \ (   )   '   \(   )(   )(   )(   )                                  ")
delay("\033[1;97m | |     |  .-. ;| ' .-. ; |  .-.  .-. ;| |  | |  | |  | |                                   ")
delay("\033[1;97m | | ___ |  | | ||  / (___)| |  | |  | || |  | |   \ `' /                                    ")
delay("\033[1;97m | |(   )|  |/  || |       | |  | |  | || |  | |   / ,. \                                    ")
delay("\033[1;97m | | | | |  ' _.'| |       | |  | |  | || |  | |  ' .  ; .                                   ")
delay("\033[1;97m | ' | | |  .'.-.| |       | |  | |  | || |  ; '  | |  | |                                   ")
delay("\033[1;97m ' `-' ; '  `-' /| |       | |  | |  | |' `-'  /  | |  | |                                   ")
delay("\033[1;97m  `.__.   `.__.'(___)     (___)(___)(___)'.__.'  (___)(___)                                  ")
print ""
delay("\033[1;91m                         ___             ___                                                 ")
delay("\033[1;91m                        (   )       .-. (   )                                                ")
delay("\033[1;91m  .--.  ___  ___   .-..  | |  .--. ( __) | |_                                                ")
delay("\033[1;91m /    \(   )(   ) /    \ | | /    \('^')(   __)                                              ")
delay("\033[1;91m|  .-. ;| |  | | ' .-,  ;| ||  .-. ;| |  | |                                                 ")
delay("\033[1;91m|  | | | \ `' /  | |  . || || |  | || |  | | ___                                             ")
delay("\033[1;91m|  |/  | / ,. \  | |  | || || |  | || |  | |(   )                                            ")
delay("\033[1;91m|  ' _.'' .  ; . | |  | || || |  | || |  | | | |                                             ")
delay("\033[1;91m|  .'.-.| |  | | | |  ' || || '  | || |  | ' | |                                             ")
delay("\033[1;91m'  `-' /| |  | | | `-'  '| |'  `-' /| |  ' `-' ;                                             ")
delay("\033[1;91m `.__.'(___)(___)| \__.'(___)`.__.'(___)  `.__.                                              ")
delay("\033[1;95m  .-.       \033[1;91m     | |   \033[1;95m                                                         ___          ")
delay("\033[1;95m /    \     \033[1;91m    (___)  \033[1;95m                                                        (   )         ")
delay("\033[1;95m | .`. ;  ___ .-.    .---.  ___ .-. .-.    .--.  ___  ___  ___  .--.  ___ .-.   | |   ___    ")
delay("\033[1;95m | |(___)(   )   \  / .-, \(   )   '   \  /    \(   )(   )(   )/    \(   )   \  | |  (   )   ")
delay("\033[1;95m | |_     | ' .-. ;(__) ; | |  .-.  .-. ;|  .-. ;| |  | |  | ||  .-. ;| ' .-. ; | |  ' /     ")
delay("\033[1;95m(   __)   |  / (___) .'`  | | |  | |  | ||  | | || |  | |  | || |  | ||  / (___)| |,' /      ")
delay("\033[1;95m | |      | |       / .'| | | |  | |  | ||  |/  || |  | |  | || |  | || |       | .  '.      ")
delay("\033[1;95m | |      | |      | /  | | | |  | |  | ||  ' _.'| |  | |  | || |  | || |       | | `. \     ")
delay("\033[1;95m | |      | |      ; |  ; | | |  | |  | ||  .'.-.| |  ; '  | || '  | || |       | |   \ \    ")
delay("\033[1;95m | |      | |      ' `-'  | | |  | |  | |'  `-' /' `-'   `-' ''  `-' /| |       | |    \ .   ")
delay("\033[1;95m(___)    (___)     `.__.'_.(___)(___)(___)`.__.'  '.__.'.__.'  `.__.'(___)     (___)  (___)  ")
print ""
time.sleep(1)
