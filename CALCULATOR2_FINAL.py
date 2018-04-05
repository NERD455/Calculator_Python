import tkinter
import math

sin = math.sin
cos = math.cos
tan = math.tan
ln = math.log2
log = math.log10
e = math.exp
sqrt = math.sqrt
root = tkinter.Tk()


class Butt(tkinter.Button):
    def __init__(self, mas, height, width, tx, fnt, bd, bg, fg, row, colmn):
        tkinter.Button.__init__(self, master=mas, font=fnt, height=height, text=tx, width=width, bd=bd, fg=fg, bg=bg)
        self.grid(row=row, column=colmn)
        

frame = tkinter.Frame(root)

text = tkinter.Entry(frame, font='Ariel 16 bold', justify='right', bg='light blue', bd=8, fg='black',
                     width=11, insertwidth=3)

frame1 = tkinter.Frame(root)
frame2 = tkinter.Frame(root)

frame_next=tkinter.Frame(root)

def equal(event):
    event.w = text.get()
    event.a = eval(event.w)
    text.delete(0, len(event.w))
    text.insert(0, event.a)


def delete():
    w = text.get()
    text.delete(len(w)-1, len(w))


def button_ext():
    try:
        frame_next.pack_info()
        frame_next.pack_forget()
        frame1.pack()
        b_next['text'] = 'SCIENTIFIC'

    except tkinter.TclError:
        frame1.pack_forget()
        frame_next.pack()
        b_next['text'] = 'NORMAL'


b7 = Butt(frame1, 1, 2, '7', 'Ariel 16 bold', 4, 'black', 'white', 1, 0)
b8 = Butt(frame1, 1, 2, '8', 'Ariel 16 bold', 4, 'black', 'white', 1, 1)
b9 = Butt(frame1, 1, 2, '9', 'Ariel 16 bold', 4, 'black', 'white', 1, 2)
b4 = Butt(frame1, 1, 2, '4', 'Ariel 16 bold', 4, 'black', 'white', 2, 0)
b5 = Butt(frame1, 1, 2, '5', 'Ariel 16 bold', 4, 'black', 'white', 2, 1)
b6 = Butt(frame1, 1, 2, '6', 'Ariel 16 bold', 4, 'black', 'white', 2, 2)
b1 = Butt(frame1, 1, 2, '1', 'Ariel 16 bold', 4, 'black', 'white', 3, 0)
b2 = Butt(frame1, 1, 2, '2', 'Ariel 16 bold', 4, 'black', 'white', 3, 1)
b3 = Butt(frame1, 1, 2, '3', 'Ariel 16 bold', 4, 'black', 'white', 3, 2)
b_dot = Butt(frame1, 1, 2, '.', 'Ariel 16 bold', 4, 'black', 'white', 4, 0)
b_0 = Butt(frame1, 1, 2, '0', 'Ariel 16 bold', 4, 'black', 'white', 4, 1)
b_eu = Butt(frame1, 1, 2, '=', 'Ariel 16 bold', 4, 'light pink', 'black', 4, 2)


b_add = Butt(frame1, 1, 2, '+', 'Ariel 16 bold', 4, 'orange', 'black', 1, 3)
b_sub = Butt(frame1, 1, 2, '-', 'Ariel 16 bold', 4, 'orange', 'black', 2, 3)
b_mul = Butt(frame1, 1, 2, '*', 'Ariel 16 bold', 4, 'orange', 'black', 3, 3)
b_div = Butt(frame1, 1, 2, '/', 'Ariel 16 bold', 4, 'orange', 'black', 4, 3)


b_de = tkinter.Button(frame, text='DEL', font='Ariel 16 bold', bd=8, fg='black', bg='light pink', height=1,
                      width=2, command=delete)


b_next = tkinter.Button(frame2, text='SCIENTIFIC', font='Ariel 13 bold', bd=6, bg='light green', fg='black', height=1, width=18,
                        command=button_ext)

###############################################################################
bb7 = Butt(frame_next, 1, 2, 'sin', 'Ariel 16 bold', 4, 'grey', 'white', 1, 0)
bb8 = Butt(frame_next, 1, 2, 'cos', 'Ariel 16 bold', 4, 'grey', 'white', 1, 1)
bb9 = Butt(frame_next, 1, 2, ')', 'Ariel 16 bold', 4, 'grey', 'white', 1, 2)
bb4 = Butt(frame_next, 1, 2, 'pi', 'Ariel 16 bold', 4, 'grey', 'white', 2, 0)
bb5 = Butt(frame_next, 1, 2, 'tan', 'Ariel 16 bold', 4, 'grey', 'white', 2, 1)
bb6 = Butt(frame_next, 1, 2, '(', 'Ariel 16 bold', 4, 'grey', 'white', 2, 2)
bb1 = Butt(frame_next, 1, 2, 'e', 'Ariel 16 bold', 4, 'grey', 'white', 3, 0)
bb2 = Butt(frame_next, 1, 2, 'log', 'Ariel 16 bold', 4, 'grey', 'white', 3, 1)
bb3 = Butt(frame_next, 1, 2, '%', 'Ariel 16 bold', 4, 'grey', 'white', 3, 2)
bb_dot = Butt(frame_next, 1, 2, 'ln', 'Ariel 16 bold', 4, 'grey', 'white', 4, 0)
bb_0 = Butt(frame_next, 1, 2, 'sqrt', 'Ariel 16 bold', 4, 'grey', 'white', 4, 1)

bb_eu = Butt(frame_next, 1, 2, '=', 'Ariel 16 bold', 4, 'light pink', 'black', 4, 2)


bb_add = Butt(frame_next, 1, 2, '+', 'Ariel 16 bold', 4, 'orange', 'black', 1, 3)
bb_sub = Butt(frame_next, 1, 2, '-', 'Ariel 16 bold', 4, 'orange', 'black', 2, 3)
bb_mul = Butt(frame_next, 1, 2, '*', 'Ariel 16 bold', 4, 'orange', 'black', 3, 3)
bb_div = Butt(frame_next, 1, 2, '/', 'Ariel 16 bold', 4, 'orange', 'black', 4, 3)


###############################################################################################################


class Numbers:
    def __init__(self, num, button, name):
        def name(event):
            text.insert(len(text.get()), num)

        button.bind('<Button-1>', name)


b_eu.bind('<Button-1>', equal)

Numbers(9, b9, 'c_b9')
Numbers(8, b8, 'c_b8')
Numbers(7, b7, 'c_b7')
Numbers(6, b6, 'c_b6')
Numbers(5, b5, 'c_b5')
Numbers(4, b4, 'c_b4')
Numbers(3, b3, 'c_b3')
Numbers(2, b2, 'c_b2')
Numbers(1, b1, 'c_b1')
Numbers(0, b_0, 'c_b0')

Numbers('.', b_dot, 'c_b_dot')
Numbers('+', b_add, 'c_b_add')
Numbers('-', b_sub, 'c_b_sub')
Numbers('*', b_mul, 'c_b_mul')
Numbers('/', b_div, 'c_b_div')

Numbers('+', bb_add, 'c_b_add')
Numbers('-', bb_sub, 'c_b_sub')
Numbers('*', bb_mul, 'c_b_mul')
Numbers('/', bb_div, 'c_b_div')

Numbers(')', bb9, 'c_bb9')
Numbers('cos(', bb8, 'c_bb8')
Numbers('sin(', bb7, 'c_bb7')
Numbers('(', bb6, 'c_bb6')
Numbers('tan(', bb5, 'c_bb5')
Numbers(3.14, bb4, 'c_bb4')
Numbers('%', bb3, 'c_bb3')
Numbers('log(', bb2, 'c_bb2')
Numbers('e(', bb1, 'c_bb1')
Numbers('sqrt(', bb_0, 'c_bb0')
Numbers('ln(', bb_dot, 'c_bb_dot')

##################################################################################################################
bb_eu.bind('<Button-1>',equal)

b_next.pack(expand='yes')

b_de.pack(side="right")
text.pack(side='left')

frame2.pack(side='bottom')
frame.pack(side='top')
frame1.pack(side='right')
root.mainloop()

#ajai