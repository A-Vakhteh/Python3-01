from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("900x500+230+100")
root.resizable(0,0)
root.config(background='#E55311')
root.title('Vakhteh-1')
#================================Func=====================================================
def Insert():
    name = ent_name.get()
    family = ent_family.get()
    city = ent_city.get()
    tell = int(ent_tell.get())
    lst_s.insert(END,f'{name},{family},{city},{tell}')
def delet():
    index = lst_s.curselection() 
    result = messagebox.askquestion('Delete','Are you sure you want to delete?')
    if(result=='yes'):
        lst_s.delete(index)
def clear():
    ent_name.delete(0,END)
    ent_city.delete(0,END)
    ent_family.delete(0,END)
    ent_tell.delete(0,END)
    ent_name.focus_set()
def Fetch():
   index = lst_s.curselection()
   data = lst_s.get(index)
   item =data.split(',')
   ent_name.insert(0,item[0])
   ent_city.insert(0,item[2])
   ent_family.insert(0,item[1])
   ent_tell.insert(0,item[3])
def exit():
   i=messagebox.askquestion('Exit','Are you sure want to leave?')
   if(i=='yes'):
        root.destroy()
  

    





#===============================lable=====================================================
lbl1 = Label(root, text='Name : ',font='Montserrat 18 bold',background='#E55311',foreground='black')
lbl1.place(x=50,y=30)

lbl2 = Label(root, text='Family: ',font='Montserrat 18 bold',background='#E55311',foreground='black')
lbl2.place(x=50,y=60)

lbl3 = Label(root, text='City : ',font='Montserrat 18 bold',background='#E55311',foreground='black')
lbl3.place(x=500,y=60)

lbl3 = Label(root, text='Tell : ',font='Montserrat 18 bold',background='#E55311',foreground='black')
lbl3.place(x=500,y=30)
#=============================Ent==========================================================
ent_name = Entry(root,font='Montserrat ',background='black',foreground='#E55311',width=20)
ent_name.place(x=150,y=40)

ent_family = Entry(root,font='Montserrat ',background='black',foreground='#E55311',width=20)
ent_family.place(x=150,y=70)

ent_tell = Entry(root,font='Montserrat ',background='black',foreground='#E55311',width=20)
ent_tell.place(x=570,y=40)

ent_city = Entry(root,font='Montserrat ',background='black',foreground='#E55311',width=20)
ent_city.place(x=570,y=70)

#==============================btn====================================================

btn_insert= Button(root, text='Insert',background='black',font= 'arial 15 bold',foreground='#E55311',width=10,command=Insert)
btn_insert.place(x=664,y=144)

btn_delete= Button(root, text='Delete',background='black',font= 'arial 15 bold',foreground='#E55311',width=10,command=delet)
btn_delete.place(x=664,y=200)

btn_clear= Button(root, text='Clear',background='black',font= 'arial 15 bold',foreground='#E55311',width=10,command=clear)
btn_clear.place(x=664,y=256)

btn_fetch= Button(root, text='Fetch',background='black',font= 'arial 15 bold',foreground='#E55311',width=10,command=Fetch)
btn_fetch.place(x=664,y=312)

btn_exit= Button(root, text='Exit',background='black',font= 'arial 15 bold',foreground='#E55311',width=10,command=exit)
btn_exit.place(x=664,y=368)
#=================================lst===================================
lst_s = Listbox(root , width= 80 , height=16 , background='black',font= 'arial 10 bold',foreground='#E55311')
lst_s.place(x=58,y=144)


root.mainloop()