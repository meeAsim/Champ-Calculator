from tkinter import *

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def mode(a,b):
    return a % b

def lcm(a,b):
    L = a if a>b else b
    while L <= a*b:
        if L%a == 0 and L%b == 0:
            return L
        L+=1

def hcf(a,b):
    H = a if a<b else b
    while H >= 1:
        if a%H == 0 and b%H == 0:
            return H
        H-=1

def extraxt_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l

def calculate():
    text = txtinput.get()
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extraxt_from_text(text)
                r = operations[word.upper()](l[0] , l[1])
                list.delete(0,END)
                list.insert(END,r)
            except:
                list.delete(0,END)
                list.insert(END,'Invalid input')
            finally:
                break
        elif word.upper() not in operations.keys():
            list.delete(0,END)
            list.insert(END,'Application does not find any the solution')

operations = {'ADD':add , 'ADDITION':add , 'SUM':add , 'PLUS':add , '+':add ,
                'SUB':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub, '-':add ,
                 'LCM':lcm , 'HCF':hcf , 'PRODUCT':multiply , 'MULTIPLICATION':multiply, '*':multiply, 'X':multiply ,
                 'MULTIPLY':multiply , 'DIVISION':divide , 'DIV':divide ,'DIVIDE':divide, 'MOD':mode , '/':divide ,
                  'REMANDER':mode , 'MODULUS':mode}

win = Tk()
win.geometry('500x300')
win.title('CHAMP CALCULATOR')
win.configure(bg='tomato')

lvl1 = Label(win , text='Champ Calculator',width=20 , padx=3, font=('Poppins', 18, ) ,bg='tomato'  )
lvl1.place(x=120,y=10)
lvl2 = Label(win , text='Write your question ' , padx=3)
lvl2.place(x=180,y=60)

txtinput = StringVar()
infld = Entry(win , width=60 , textvariable = txtinput)
infld.place(x=80,y=100)
infld.insert(0,'example:  add 297 and 249')


btn = Button(win , text='Calculate' ,command=calculate)
btn.place(x=210,y=140)

list = Listbox(win,width=50,height=3,)
list.place(x=80,y=180)

win.mainloop()
