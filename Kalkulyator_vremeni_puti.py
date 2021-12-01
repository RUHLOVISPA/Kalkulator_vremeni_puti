'''
Создать программу, которая рассчитает примерное время прибытия для заданного расстояния и скорости. Программа должна вести учет действий пользователя в текстовый файл.
Ввод: 10 км, 5 км/ч
Вывод: 2 часа
'''

def withdrawal():
    time = str(float(ent_distance.get()) / float(ent_speed.get()))
    withdrawal = "При скорости " + ent_speed.get() + " км/ч, расстояние в " + ent_distance.get() + " км будет пройдено за " + time + " часов."
    lbl_two = Label(window, text=withdrawal)
    lbl_two.pack()
    try:
        fail = open('История Калькулятора времени пути.txt', 'w')
        try:
            fail.write("\n" + now.strftime("%d.%m.%Y %H:%M") + " : " + withdrawal)
        except Exception as e:
            print(e)
        finally:
            fail.close()
    except Exception as ex:
        print(ex)

def isfloat():
    try:
        float(ent_distance.get())
        float(ent_speed.get())
        withdrawal()
        return True
    except ValueError:
        messagebox.showinfo('Fatal ERROR', 'Число?')
        return False

def check():
    entry = {"расстояние ": ent_distance.get(), "скорость ": ent_speed.get()}
    sequence = []
    for ent in entry:
        if entry[ent] == "":
            sequence.append("\n" + ent)
    if sequence != []:
        sequence = ''.join(sequence)
        messagebox.showinfo('Fatal ERROR', "Вы забыли: " + sequence)
    else:
        isfloat()

from tkinter import *
from tkinter import messagebox
from datetime import *

now = datetime.now()
current_time = now.strftime("%d-%m-%Y %H:%M")

window = Tk()
window.title("Калькулятор времени пути")

lbl_datetime1 = Label(window, text="Текущая дата и время:")
lbl_datetime1.pack()
lbl_datetime2 = Label(window, text=now.strftime("%d-%m-%Y %H:%M"))
lbl_datetime2.pack()

frm_entry = Frame()

lbl_distance = Label(master=frm_entry, text="Расстояние (км):")
lbl_distance.grid(row=0, column=0)
ent_distance = Entry(master=frm_entry)
ent_distance.grid(row=0, column=1)
lbl_speed = Label(master=frm_entry, text="Скорость (км/ч):")
lbl_speed.grid(row=1, column=0)
ent_speed = Entry(master=frm_entry)
ent_speed.grid(row=1, column=1,)
btn_done = Button(master=frm_entry, text="Готово", command=check)
btn_done.grid(row=2, column=0, columnspan=2)

frm_entry.pack()

window.mainloop()