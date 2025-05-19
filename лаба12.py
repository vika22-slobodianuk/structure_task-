from tkinter import *
from tkinter import messagebox
def inf():
    s = edit4.get()
    if s == "111M":
        messagebox.showinfo("Про спеціальність", f"{s}\nСпеціальність 111 Математика\nОсвітня програма Комп'ютерна математика")
    elif s == "СОМ":
        messagebox.showinfo("Про спеціальність", f"{s}\nСпеціальність 014 Середня освіта\nОсвітня програма Середня освіта. Математика, інформатика")
    else:
        messagebox.showinfo("Про спеціальність", f"{s}\nТакої спеціальності на факультеті немає")
def show():
    global photo
    photo = PhotoImage(file="lb12.gif")
    label5.configure(image=photo, text="")
root = Tk()
root.title("Анкета")
root.geometry("400x600")
root.configure(bg='azure')
font_label = ("Arial", 10, "bold")

#Прізвище
Label(root, text='Прізвище:', bg='azure', font=font_label).grid(row=0, column=0, padx=10, pady=5, sticky='w')
edit1 = Entry(root, width=30)
edit1.grid(row=0, column=1, padx=10, pady=5)
#Ім'я
Label(root, text="Ім'я:", bg='azure', font=font_label).grid(row=1, column=0, padx=10, pady=5, sticky='w')
edit2 = Entry(root, width=30)
edit2.grid(row=1, column=1, padx=10, pady=5)
#По-батькові
Label(root, text='По-батькові:', bg='azure', font=font_label).grid(row=2, column=0, padx=10, pady=5, sticky='w')
edit3 = Entry(root, width=30)
edit3.grid(row=2, column=1, padx=10, pady=5)
#Стать
Label(root, text='Стать:', bg='azure', font=font_label).grid(row=3, column=0, padx=10, pady=5, sticky='w')
checkbutton1 = Checkbutton(root, text="ч", bg='azure')
checkbutton1.grid(row=3, column=1, sticky='w')
checkbutton2 = Checkbutton(root, text="ж", bg='azure')
checkbutton2.grid(row=3, column=1, padx=40, sticky='w')
#Курс
Label(root, text="Виберіть курс:", bg='azure', font=font_label).grid(row=4, column=0, padx=10, pady=5, sticky='w')
result1 = IntVar()
result1.set(1)
for i in range(1, 5):
    Radiobutton(root, text=str(i), variable=result1, value=i, bg='azure').grid(row=4+i, column=1, sticky='w', padx=10)
#Спеціальність
Label(root, text="Спеціальність:", bg='azure', font=font_label).grid(row=9, column=0, padx=10, pady=5, sticky='w')
edit4 = Entry(root, width=30)
edit4.grid(row=9, column=1, padx=10, pady=5)
#Кнопки
Button(root, text="Про спеціальність", width=20, command=inf).grid(row=10, column=0, columnspan=2, pady=10)
Button(root, text="Фото", width=20, command=show).grid(row=11, column=0, columnspan=2, pady=5)
# Місце для зображення
label5 = Label(root, text="(Тут з’явиться фото)", bg='azure')
label5.grid(row=12, column=0, columnspan=2, pady=10)

root.mainloop()