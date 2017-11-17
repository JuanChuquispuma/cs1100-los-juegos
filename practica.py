try:
    from tkinter import *
    from tkinter import messagebox
except ImportError:
    from Tkinter import *
import random
import os
root = Tk()
root.geometry("600x520+230+180")
root.title('Piedra Papel Tijeras Lagarto Spock')
frame1 = Frame(root)
frame1.grid(row = 0, column = 0)
canvas = Canvas(root,width=500, height=520, bg='white')
canvas.grid(row = 0, column = 1)
rb_var = IntVar()
rb_mode_var = IntVar()
rb_var.set(" ")
player_ganadas = 0
comp_ganadas = 0
ties = 0
b_Rixner = False
FILL_CIRCLES = "#FFF8DC"
C_GUESS = '#FF69B4'
PLAYER_GUESS = '#87CEFA'
TIE_COLOR = '#FFD700'
CIRCLE_FONT = "Verdana 10"
F_HEL_12 = "Arial 12"
LAB_WIDTH = 14
FUDGE = 3
imagen2=PhotoImage(file="Free-Converter.com-r-80562244.pgm")
lglimagen2=Label(root,height=100,width=100,image=imagen2).place(x=320,y=200)
def contar_hist():
    messagebox.showinfo("Este es el reto de Sheldon Cooper"
                        ,message="Esta es una variacion del famoso juego Piedra, papel y tijera, creador por el famoso personaje Sheldon Cooper, tu objetivo es ganarle en su propio juego: Piedra, papel, tijera, Lagarto y Spock. El codigo de donde nos guiamos esta en el sitio web: http://www.pythondiario.com/2013/11/piedra-papel-o-tijera-juego-en-python.html .")
contar_hist()
def rb_pushed():
    pick = rb_var.get()
    canvas.itemconfig(Piedra, fill=FILL_CIRCLES)
    canvas.itemconfig(Papel, fill=FILL_CIRCLES)
    canvas.itemconfig(Tijera, fill=FILL_CIRCLES)
    canvas.itemconfig(lagarto, fill=FILL_CIRCLES)
    canvas.itemconfig(Spock, fill=FILL_CIRCLES)
    if pick == 0:
        canvas.itemconfig(Piedra, fill=PLAYER_GUESS)
    elif pick == 1:
        canvas.itemconfig(Spock, fill=PLAYER_GUESS)
    elif pick == 2:
        canvas.itemconfig(Papel, fill=PLAYER_GUESS)
    elif pick == 3:
        canvas.itemconfig(lagarto, fill=PLAYER_GUESS)
    elif pick == 4:
        canvas.itemconfig(Tijera, fill=PLAYER_GUESS)
    canvas.itemconfig(t_player_wins, state = 'hidden')
    canvas.itemconfig(t_comp_wins, state = 'hidden')
    canvas.itemconfig(t_tie, state = 'hidden')
    canvas.itemconfig(t_rix_wins, state = 'hidden')

def reset_scores():
    global player_ganadas, comp_ganadas, empate
    player_ganadas = 0
    comp_ganadas = 0
    empate = 0
    update_scores()
def update_scores():
    global player_wins, comp_wins, empate
    t_disp.delete(0.0, END)
    t_disp.insert(END, '\n')
    t_disp.insert(END, " Tu   = \t" + str(player_ganadas))
    t_disp.insert(END, '\n')
    if b_Rixner:
         t_disp.insert(END, " Scott = \t" + str(comp_ganadas))
    else:
        t_disp.insert(END, " Sheldon Cooper  = \t" + str(comp_ganadas))
    t_disp.insert(END, '\n')
    t_disp.insert(END, " Empates  = \t" + str(ties))
    t_disp.insert(END, '\n')
def play_game():
    global player_ganadas, comp_ganadas, ties
    player_pick = rb_var.get()
    comp_number = random.randrange(0,5)
    if b_Rixner and (player_ganadas + comp_ganadas + ties) % FUDGE == 0:
        if player_pick == 4:
            comp_number = 1
        else:
            comp_number = player_pick + 1
    if comp_number == 0:
        canvas.itemconfig(Piedra, fill=C_GUESS)
    elif comp_number == 1:
        canvas.itemconfig(Spock, fill=C_GUESS)
    elif comp_number == 2:
        canvas.itemconfig(Papel, fill=C_GUESS)
    elif comp_number == 3:
        canvas.itemconfig(lagarto, fill=C_GUESS)
    elif comp_number == 4:
        canvas.itemconfig(Tijera, fill=C_GUESS)
    diff = (comp_number - player_pick) % 5
    if diff == 0:
        ties = ties + 1
        canvas.itemconfig(t_tie, state = 'normal')
        if comp_number == 0:
            canvas.itemconfig(Piedra, fill=TIE_COLOR)
        elif comp_number == 1:
            canvas.itemconfig(Spock, fill=TIE_COLOR)
        elif comp_number == 2:
            canvas.itemconfig(Papel, fill=TIE_COLOR)
        elif comp_number == 3:
            canvas.itemconfig(lagarto, fill=TIE_COLOR)
        elif comp_number == 4:
            canvas.itemconfig(Tijera, fill=TIE_COLOR)
    elif diff == 3 or diff == 4:
            canvas.itemconfig(t_player_wins, state = 'normal')
            player_ganadas = player_ganadas + 1
    else:
        comp_ganadas = comp_ganadas + 1
        os.system('\a')
        if b_Rixner:
            canvas.itemconfig(t_rix_wins, state = 'normal')
        else:
            canvas.itemconfig(t_comp_wins, state = 'normal')
    update_scores()
    if ((comp_ganadas+ player_ganadas + ties) >= 4):
        canvas.itemconfig(t_rules1, state = 'hidden')
        canvas.itemconfig(t_rules2, state = 'hidden')

Piedra = canvas.create_oval(200, 100, 300, 200, width=2, fill= FILL_CIRCLES)
Tijera = canvas.create_oval(75, 180, 175, 280, width=2, fill=FILL_CIRCLES)
Spock = canvas.create_oval(325, 180, 425, 280, width=2, fill=FILL_CIRCLES)
lagarto = canvas.create_oval(125, 300, 225, 400, width=2, fill=FILL_CIRCLES)
Papel = canvas.create_oval(275, 300, 375, 400, width=2, fill=FILL_CIRCLES)
t_Piedra = canvas.create_text(250, 150, text = "Piedra", font = CIRCLE_FONT)
t_Tijera = canvas.create_text(125, 230, text = "Tijera", font = CIRCLE_FONT)
t_Spock = canvas.create_text(378, 230, text = "Spock", font = CIRCLE_FONT)
t_lagarto = canvas.create_text(175, 350, text = "lagarto", font = CIRCLE_FONT)
t_Papel = canvas.create_text(328, 350, text = "Pepel", font = CIRCLE_FONT)
t_rules1 = canvas.create_text(20,40, justify = 'left', anchor = 'w', font = "Helvetica 9",
text = "Reglas: \n\nPiedra aplasta a lagarto o tijera\ntijera corta al papel y decapita al lagarto\nSpock rompe a la tijera o explota piedra")
t_rules2 = canvas.create_text(260,450, justify = 'left', font = "Helvetica 9",
text = "Reglas (con't): \n\n lagarto envenena Spock o come Papel\nPapel envuelve piedra o ahoga Spock")
t_comp_wins = canvas.create_text(250,250, text = "¡Computadora gana!",
   fill = "magenta", font = F_HEL_12 )
canvas.itemconfig(t_comp_wins, state = 'hidden')
t_player_wins = canvas.create_text(250,250, text = "¡Ganaste!",
   fill = "blue", font = F_HEL_12 )
canvas.itemconfig(t_player_wins, state = 'hidden')
t_tie = canvas.create_text(250,250, text = "¡Empate!",
   state = 'hidden', font = F_HEL_12 )
canvas.itemconfig(t_tie, state = 'hidden')
t_rix_wins = canvas.create_text(250,250, text = "Computadora Gana!",
   fill = "magenta", font = F_HEL_12 )
canvas.itemconfig(t_rix_wins, state = 'hidden')
L_sel = Label(frame1, text="Elige una", width = 12)
L_sel.grid(column = 0, row = 0, pady = 2)
rb_Piedra = Radiobutton(frame1, text="Piedra",variable = rb_var, value=0,
command = rb_pushed, width = LAB_WIDTH, pady = 2,anchor = W)
rb_Piedra.grid(row = 2, column = 0)
rb_Papel = Radiobutton(frame1, text ="Papel",variable = rb_var, value=2,
command = rb_pushed, width = LAB_WIDTH, pady = 2, anchor = W)
rb_Papel.grid(row = 4, column = 0)
rb_Tijera = Radiobutton(frame1, text = "Tijera",variable = rb_var, value=4,
command = rb_pushed, width = LAB_WIDTH,pady = 2, anchor = W)
rb_Tijera.grid(row = 5, column = 0)
rb_lagarto = Radiobutton(frame1, text = "lagarto",variable = rb_var, value=3,
command = rb_pushed, width = LAB_WIDTH,pady = 2, anchor = W)
rb_lagarto.grid(row = 6, column = 0)
rb_Spock = Radiobutton(frame1, text = "Spock",variable = rb_var, value=1,
command = rb_pushed, width = LAB_WIDTH, pady = 2,anchor = W)
rb_Spock.grid(row = 7, column = 0)
Lblank = Label(frame1, text="", width = 12)  # blank label for spacing ...
Lblank.grid(column = 0, row = 8, pady = 2)
b_play = Button(frame1, text='Presione para jugar', command=play_game, width = LAB_WIDTH,
pady = 2, background = "white")
b_play.grid(row = 9, column = 0)
Lblank2 = Label(frame1, text="", width = LAB_WIDTH)
Lblank2.grid(column = 0, row = 10, pady = 2)
L_score = Label(frame1, text="Scores", width = LAB_WIDTH)
L_score.grid(column = 0, row = 11, pady = 2)
t_disp = Text(frame1, width = LAB_WIDTH, height = 5)
t_disp.grid(row = 13, column = 0)
Lblank_text = Label(frame1, text="", width = LAB_WIDTH)
Lblank_text.grid(column = 0, row = 15, pady = 2)
Lblank_mode = Label(frame1, text="", width = 12)
Lblank_mode.grid(column = 0, row = 17, pady = 2)
L_sel_mode = Label(frame1, text="Selecciona modo", width = 12)
L_sel_mode.grid(column = 0, row = 18, pady = 2)

def quit_this():
    root.quit()
    root.destroy()
rb_Quit = Radiobutton(frame1, text = "QUIT", variable = rb_mode_var, value=3,
    command = quit_this, width = LAB_WIDTH, pady = 6, indicatoron=0)
rb_Quit[ "fg" ] = "DarkRed"
rb_Quit[ "bg" ] = "Bisque"
rb_Quit.grid(row = 25, column = 0)

mainloop()
