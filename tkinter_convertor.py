from tkinter import *
from tkinter.font import *
from tkinter import messagebox
#from convertor import *

window = Tk()
my_font = Font(family='sas',size=16)
pad_x=5
pad_y=5


def calculate() :
    f_listbox_from = listfrom.get(ACTIVE)
    f_listbox_to = listto.get(ACTIVE)

    x=float (entry_from.get())

    #con=convertor(f_listbox_from,f_listbox_to,x)

    if f_listbox_from=='Centemeter' :
        if f_listbox_to=='Centemeter':
            result=x
        elif f_listbox_to=='Meter' :
            result = x/100
        elif f_listbox_to=='Kilometer' :
            result=(x/100)/1000
        elif f_listbox_to=='Milimeter' :
            result=(x/100)*1000
        elif f_listbox_to=='Desimeter' :
            result=(x/100)*10



    elif f_listbox_from=='Meter' :
        if f_listbox_to=='Centemeter' :
            result=x*100
        elif f_listbox_to=='Meter':
            result=x
        elif f_listbox_to=='Kilometer' :
            result=x*1000
        elif f_listbox_to=='Milimeter' :
            result=x/1000
        elif f_listbox_to=='Desimeter' :
            result=x/10



    elif f_listbox_from=='Kilometer' :
        if f_listbox_to=='Centemeter':
            result=x*100000
        elif f_listbox_to=='Meter' :
            result = x/1000
        elif f_listbox_to=='Kilometer' :
            result=x
        elif f_listbox_to=='Milimeter' :
            result=x*1000000
        elif f_listbox_to=='Desimeter' :
            result=x*10000        



    elif f_listbox_from=='Milimeter' :
        if f_listbox_to=='Centemeter':
            result=x*10
        elif f_listbox_to=='Meter' :
            result = x/1000
        elif f_listbox_to=='Kilometer' :
            result=x/1000000
        elif f_listbox_to=='Milimeter' :
            result=x
        elif f_listbox_to=='Desimeter' :
            result=x/100


    elif f_listbox_from=='Desimeter' :
        if f_listbox_to=='Centemeter':
            result=x*10
        elif f_listbox_to=='Meter' :
            result = x/10
        elif f_listbox_to=='Kilometer' :
            result=x/10000
        elif f_listbox_to=='Milimeter' :
            result=x*100
        elif f_listbox_to=='Desimeter' :
            result=x

            
    #messagebox.showinfo(title='The result is :',message=result)
    entry_to.delete(0,END)
    entry_to.insert (END,result)

label_from =Label(window,text=' From ',font=my_font , bg='gray')
label_to = Label(window,text=' To ',font=my_font , bg='gray')
label_from.grid(row=0,column=0 ,sticky=W,padx=pad_x,pady=pad_y)
label_to.grid(row=0,column=1,sticky=W,padx=pad_x,pady=pad_y)

entry_from=Entry(window,font=my_font,fg='blue' , bg='gray')
entry_to = Entry(window,font=my_font,fg='blue', bg='gray')
entry_from.grid(row=2 , column=0 ,padx=pad_x,pady=pad_y)
entry_to.grid(row=2,column=1)

listfrom=Listbox(window,font=my_font,exportselection=False , bg='green')
listto=Listbox(window,font=my_font,exportselection=False,bg= 'green')
listfrom.grid(row=3,column=0,padx=pad_x,pady=pad_y)
listto.grid(row=3,column=1,padx=pad_x,pady=pad_y)

listfrom.insert(END,'Centemeter')
listfrom.insert(END,'Meter')
listfrom.insert(END,'Kilometer')
listfrom.insert(END,'Milimeter')
listfrom.insert(END,'Desimeter')

listto.insert(END,'Centemeter')
listto.insert(END,'Meter')
listto.insert(END,'Kilometer')
listto.insert(END,'Milimeter')
listto.insert(END,'Desimeter')



Button_=Button(window ,font=my_font, text='RESULT' , bg='black' , fg='white' , command=calculate)
Button_.grid(row=4,column=0 , columnspan=2 , sticky=E+W ,padx=pad_x,pady=pad_y)


window.mainloop()