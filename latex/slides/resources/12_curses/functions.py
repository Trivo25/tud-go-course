curses.initscr()

curses.endwin()

curses.wrapper(func, ...)

window.addch(ch[, attr])
window.addch(y, x, ch[, attr])

window.addstr(str[, attr])
window.addstr(y, x, str[, attr])

window.delch([y, x])
window.deleteln()
window.erase()

curses.textpad.rectangle(win, uly, ulx, lry, lrx)

curses.textpad.Textbox(win)

Textbox().edit([validator])
Textbox().do_command(ch)
Textbox().gather()
