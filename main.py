import curses
from curses import wrapper
import time 

def main(stdscr):
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_RED)
    curses.init_pair(2,curses.COLOR_MAGENTA,curses.COLOR_GREEN)
    BLUE_RED = curses.color_pair(1)
    MAGENTA_GREEN = curses.color_pair(2)
    word = '''  .__                                             
|  |   _______  __ ____    ___.__. ____  __ __  
|  |  /  _ \  \/ // __ \  <   |  |/  _ \|  |  \ 
|  |_(  <_> )   /\  ___/   \___  (  <_> )  |  / 
|____/\____/ \_/  \___  >  / ____|\____/|____/  
                      \/   \/                    '''
    for i in range(0,60):
        
        stdscr.clear()
        color = BLUE_RED
        stdscr.addstr(i,0,word,color )

        if i%2 == 0:
            color = MAGENTA_GREEN
            stdscr.addstr(i,0,word,color )
        stdscr.refresh()
        time.sleep(0.2)

    stdscr.getch()

wrapper(main)    