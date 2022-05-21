from tkinter import *

first_number=second_number=operator=None

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')

def get_operator(op):
    global first_number,operator

    first_number = int(result_label['text'])
    operator = op
    result_label.config(text='')
    
def get_result():
    global first_number,second_number,operator

    second_number = int(result_label['text'])

    if operator == '+':
        result_label.config(text=str(first_number+second_number))
    elif operator == '-':
        result_label.config(text=str(first_number-second_number))
    elif operator == '*':
        result_label.config(text=str(first_number*second_number))
    else:
        if second_number == 0:
             result_label.config(text='Error')
        else: 
            result_label.config(text=str(round(first_number/second_number)))
            
win = Tk()
win.title("Calculator")
win.geometry('280x380')
win.resizable(0,0)  #your windows will be fixed sized if it assign(0,0)
win.configure(background="black") #background of the windows

result_label = Label(win,text='',bg='black',fg='white')
result_label.grid(row=0,column=0,columnspan=5,pady=(50,25),sticky='w') 
result_label.config(font=('verdana',30,'bold'))

button7 = Button(win,text='7',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(7))
button7.grid(row=1,column=0)
button7.config(font=('verdana',14))

button8 = Button(win,text='8',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(8))
button8.grid(row=1,column=1)
button8.config(font=('verdana',14))

button9 = Button(win,text='9',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(9))
button9.grid(row=1,column=2)
button9.config(font=('verdana',14))

button_add = Button(win,text='+',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_operator('+'))
button_add.grid(row=1,column=3)
button_add.config(font=('verdana',14))

button4 = Button(win,text='4',bg='#00a64a',fg='white',width=5,height=2,command=lambda :get_digit(4))
button4.grid(row=2,column=0)
button4.config(font=('verdana',14))

button5 = Button(win,text='5',bg='#00a64a',fg='white',width=5,height=2,command=lambda :get_digit(5))
button5.grid(row=2,column=1)
button5.config(font=('verdana',14))

button6 = Button(win,text='6',bg='#00a64a',fg='white',width=5,height=2,command=lambda :get_digit(6))
button6.grid(row=2,column=2)
button6.config(font=('verdana',14))

button_subtract = Button(win,text='-',bg='#00a64a',fg='white',width=5,height=2,command=lambda :get_operator('-'))
button_subtract.grid(row=2,column=3)
button_subtract.config(font=('verdana',14))

button1 = Button(win,text='1',bg='#00a64a',fg='white',width=5,height=2,command=lambda :get_digit(1))
button1.grid(row=3,column=0)
button1.config(font=('verdana',14))

button2 = Button(win,text='2',bg='#00a64a',fg='white',width=5,height=2,command=lambda :get_digit(2))
button2.grid(row=3,column=1)
button2.config(font=('verdana',14))

button3 = Button(win,text='3',bg='#00a64a',fg='white',width=5,height=2,command=lambda :get_digit(3))
button3.grid(row=3,column=2)
button3.config(font=('verdana',14))

button_multiply = Button(win,text='*',bg='#00a64a',fg='white',width=5,height=2,command=lambda :get_operator('*'))
button_multiply.grid(row=3,column=3)
button_multiply.config(font=('verdana',14))

button_clear = Button(win,text='C',bg='#00a64a',fg='white',width=5,height=2,command=lambda :clear())
button_clear.grid(row=4,column=0)
button_clear.config(font=('verdana',14))

button0 = Button(win,text='0',bg='#00a64a',fg='white',width=5,height=2,command=lambda :get_digit(0))
button0.grid(row=4,column=1)
button0.config(font=('verdana',14))

button_calculate = Button(win,text='=',bg='#00a64a',fg='white',width=5,height=2,command=get_result)
button_calculate.grid(row=4,column=2)
button_calculate.config(font=('verdana',14))

button_division = Button(win,text='/',bg='#00a64a',fg='white',width=5,height=2,command=lambda :get_operator('/'))
button_division.grid(row=4,column=3)
button_division.config(font=('verdana',14))





win.mainloop()
