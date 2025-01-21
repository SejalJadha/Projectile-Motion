import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import backend
window = Tk()
window.title('Projectile Motion')
window.geometry('900x500')
image = Image.open("sakeclogo.jpg")
photo = ImageTk.PhotoImage(image.resize((100,100)))
graph = Image.open("output_start.png")
graph_img = ImageTk.PhotoImage(graph.resize((400,300)))

window.resizable()

def submit():
    print('User filled the form')
    v0=entry1.get()
    angle=entry3.get()
    g=entry4.get()
    [r,h,t] = backend.calculate(float(v0),float(angle),float(g))
    label_range.config(text= round(r,2))
    label_height.config(text= round(h,2))
    label_time.config(text= round(t,2))
    graph = Image.open("output.jpg")
    graph_img = ImageTk.PhotoImage(graph.resize((400,300)))
    Label_Result.configure(image=graph_img)
    Label_Result.image = graph_img
    
    print("Initial Velocity :", v0)
    print("Angle :",angle)
    print("Gravitational Force :",g)
    print(r,h,t)
    print("Image Saved as Output.jpg")
    

label = Label(window,text='PROJECTILE MOTION',font=('Serif',25),fg='red',padx=125,pady=10)
label.grid(row=1,column=1)


Label_logo = Label(image=photo) 
Label_logo.grid(row=1,column=3,pady=20,padx=137,rowspan=3)

Label_Result = Label(image=graph_img)
Label_Result.grid(row=3,column=1,rowspan=3)

label1 = Label(window,text='Initial Velocity Vo',font=('arial bold',11),fg='blue')
label1.place(x=600,y=150)

label3 = Label(window,text='Initial Angle',font=('arial bold',11),fg='blue')
label3.place(x=600,y=225)


label4 = Label(window,text='Gravitational acc. g',font=('arial bold',11),fg='blue')
label4.place(x=600,y=300)


label5 = Label(window,text='Range',font=('arial bold',11),fg='black')
label5.place(x=80,y=425)


label6 = Label(window,text='Flight Time',font=('arial bold',11),fg='black')
label6.place(x=325,y=425)


label7 = Label(window,text='Max Height',font=('arial bold',11),fg='black')
label7.place(x=585,y=425)


submit = Button(window,text='RESULT',font=('Serif',11),fg='black',bg='yellow',bd=5,activeforeground='White',
                activebackground='#1979a9',command=submit)
submit.place(x=695,y=360)

entry1= Entry(window,font=('Serif',11),fg='black',width=15)
entry1.place(x=730,y=150)


entry3= Entry(window,font=('Serif',11),fg='black',width=15)
entry3.place(x=730,y=225)

entry4= Entry(window,font=('Serif',11),fg='black',width=15)
entry4.place(x=730,y=300)

label_range = Label(window,text='-',font=('arial bold',11),fg='black')
label_range.place(x=135,y=425)

label_time = Label(window,text='-',font=('arial bold',11),fg='black')
label_time.place(x=410,y=425)

label_height = Label(window,text='-',font=('arial bold',11),fg='black')
label_height.place(x=673,y=425)


window.mainloop()
