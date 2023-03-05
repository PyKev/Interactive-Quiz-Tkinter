import tkinter
from tkinter import Tk, Label, Button, messagebox,font as tkFont
from PIL import ImageTk, Image


def abriVentana():
    window1.withdraw()
    window2 = tkinter.Toplevel()
    window2.geometry('610x490+400+150')
    window2.configure(background='sky blue')

    questionnumberiter = iter(range(2, 6))
    questions = ['Escribir aqui la pregunta ......', '  Escribir aqui la pregunta ......',
                 '  Escribir aqui la pregunta ......', '  Escribir aqui la pregunta ......']
    questionsiter = iter(questions)
    questions_images = ["Images\\imagen.png", "Images\\imagen.png", "Images\\imagen.png",
                        "Images\\imagen.png"]
    questions_images_iter = iter(questions_images)
    answer1 = ['Op 1 Pgta 2', 'Op 1 Pgta 3', 'Op 1 Pgta 4', 'Op 1 Pgta 5']
    answer1_iter = iter(answer1)
    answer2 = ['Op 2 Pgta 2', 'Op 2 Pgta 3', 'Op 2 Pgta 4', 'Op 2 Pgta 5']
    answer2_iter = iter(answer2)
    answer3 = ['Op 3 Pgta 2', 'Op 3 Pgta 3', 'Op 3 Pgta 4', 'Op 3 Pgta 5']
    answer3_iter = iter(answer3)

    def nextquestion():
        global nextquestionumber
        global nextquestiondescription
        global nextquestionimage
        global nextanswer1
        global nextanswer2
        global nextanswer3

        nextquestionumber = next(questionnumberiter)
        nextquestiondescription = next(questionsiter)
        nextquestionimage = next(questions_images_iter)
        nextanswer1 = next(answer1_iter)
        nextanswer2 = next(answer2_iter)
        nextanswer3 = next(answer3_iter)

    def botonnext():
        if int(label_titulo.cget('text')[9]) == 5:
            window2.destroy()
            window1.destroy()
        else:
            nextquestion()
            label_titulo.config(text='Pregunta '+str(nextquestionumber)+':'+nextquestiondescription)
            imagennueva = ImageTk.PhotoImage(Image.open(nextquestionimage).resize((180, 200)))
            label_pregunta.config(image= imagennueva)
            label_pregunta.imagennueva = imagennueva
            button_answer1.config(text=nextanswer1)
            button_answer2.config(text=nextanswer2)
            button_answer3.config(text=nextanswer3)
            if nextquestionumber == 5:
                button_next.config(text='Fin')
            disablebutton()

    def enabledbutton():
        button_next["state"] = 'normal'

    def disablebutton():
        button_next["state"] = 'disabled'

    def validacion(boton):
        pregunta = int(label_titulo.cget('text')[9:10])

        for p in range(1,6):
            if pregunta ==p:
                if boton ==2:
                    messagebox.showinfo(message=f"Opción {str(boton)} correcta", title="Mensaje bien")
                    enabledbutton()
                else:
                    messagebox.showerror(message=f"Opción {str(boton)} incorrecta", title="Mensaje mal")
                break

    #Labels
    label_titulo = Label(window2,text='Pregunta '+str(1)+':'+'Escribir aqui la pregunta ......',font=("Helvetica 20 bold"))
    label_titulo.grid(row=1, column=1, padx=10,pady=10)
    label_titulo.config(bg="sky blue")

    imagen1 = ImageTk.PhotoImage(Image.open("Images\\imagen.png").resize((180, 200)))
    label_pregunta = Label(window2,image=imagen)
    label_pregunta.grid(row=2, column=1, padx=90, pady=10)

    #Button Primera respuesta
    helv14 = tkFont.Font(family='Helvetica', size=14, weight='bold')
    button_answer1 = Button(window2, text="Op 1 Pgta 1",height=1, width=20, bg='grey', fg='white',command= lambda: validacion(1))
    button_answer1.grid(row=3, column=1, padx=0, pady=5)
    button_answer1['font'] = helv14
    #Button Segunda respuesta
    button_answer2 = Button(window2, text="Op 2 Pgta 1", height=1, width=20, bg='grey', fg='white',command= lambda: validacion(2))
    button_answer2.grid(row=4, column=1, padx=0, pady=5)
    button_answer2['font'] = helv14
    #Button Tercera respuesta
    button_answer3 = Button(window2, text="Op 3 Pgta 1", height=1, width=20, bg='grey', fg='white',command= lambda: validacion(3))
    button_answer3.grid(row=5, column=1, padx=0, pady=5)
    button_answer3['font'] = helv14
    #Button Next
    button_next = Button(window2, text="Siguiente", height=1, width=10, bg='blanched almond', fg='black',command=botonnext)
    button_next.grid(row=6, column=1, padx=0, pady=8)
    button_next['font'] = helv14
    button_next["state"] = 'disabled'
    window2.mainloop()

def mensajeBienvenida():
    messagebox.showinfo(message="Selecciona la respuesta correcta", title="mensaje")

window1 = Tk()
window1.title("Cuestionario")
window1.geometry('600x400+400+150')
window1.configure(background='sky blue')

#Label
label_welcome = Label(window1, text = 'BIENVENIDO AL CUESTIONARIO',font=("Helvetica 20 bold"))
label_welcome.grid(row=1, column=3,padx=45,pady=20)
label_welcome.config(bg="sky blue")
imagen = ImageTk.PhotoImage(Image.open("Images\\imagen.png").resize((180, 200)))
label_welcome2 = Label(image=imagen)
label_welcome2.grid(row=2, column=3, padx=50,pady=20)

#Button new window
button_neww = Button(window1, text="Empecemos!",command=lambda:[mensajeBienvenida(), abriVentana()],height= 1, width=15,bg='grey', fg='white')
helv36 = tkFont.Font(family='Helvetica', size=14, weight='bold')
button_neww.grid(row=3, column=3, padx=50,pady=25)
button_neww['font'] = helv36
window1.mainloop()

