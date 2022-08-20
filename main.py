# Python练习小程序计算器V0.1
import tkinter.messagebox as msgbox
from tkinter import *

# 创建计算器类
class MY_GUI():
    def __init__(self, init_window, trigger):
        self.init_window = init_window
        self.trigger = trigger

    # 设置窗口
    def set_init_window(self):
        self.init_window.title("计算器V0.1")
        self.init_window.geometry("570x400")
        # self.init_window.attributes("-alpha", 0.9)
        # 生成组件，tkinter控件默认不能传参，因为要统一调用，所以要用lambda
        self.text = Text(self.init_window, width=40, height=4, relief=RAISED, font=("Helvetica", 24))
        self.btn_ac = Button(self.init_window, text='AC', height=2, command=lambda: self.ac_function())
        self.btn_del = Button(self.init_window, text='DEL', height=2, command=lambda: self.del_function())
        self.btn_per = Button(self.init_window, text='%', height=2, command=lambda: self.show_input('%'))
        self.btn_ad = Button(self.init_window, text='+', height=2, command=lambda: self.show_input('+'))
        self.btn_7 = Button(self.init_window, text='7', height=2, command=lambda: self.show_input('7'))
        self.btn_8 = Button(self.init_window, text='8', height=2, command=lambda: self.show_input('8'))
        self.btn_9 = Button(self.init_window, text='9', height=2, command=lambda: self.show_input('9'))
        self.btn_minus = Button(self.init_window, text='-', height=2, command=lambda: self.show_input('-'))
        self.btn_4 = Button(self.init_window, text='4', height=2, command=lambda: self.show_input('4'))
        self.btn_5 = Button(self.init_window, text='5', height=2, command=lambda: self.show_input('5'))
        self.btn_6 = Button(self.init_window, text='6', height=2, command=lambda: self.show_input('6'))
        self.btn_plus = Button(self.init_window, text='x', height=2, command=lambda: self.show_input('*'))
        self.btn_1 = Button(self.init_window, text='1', height=2, command=lambda: self.show_input('1'))
        self.btn_2 = Button(self.init_window, text='2', height=2, command=lambda: self.show_input('2'))
        self.btn_3 = Button(self.init_window, text='3', height=2, command=lambda: self.show_input('3'))
        self.btn_div = Button(self.init_window, text='/', height=2, command=lambda: self.show_input('/'))
        self.btn_dot = Button(self.init_window, text='.', height=2, command=lambda: self.show_input('.'))
        self.btn_0 = Button(self.init_window, text='0', height=2, command=lambda: self.show_input('0'))
        self.btn_eq = Button(self.init_window, text='=', height=2, command=lambda: self.eval_remake())


        # 排列组件
        self.text.grid(column=0, row=0, columnspan=4, sticky=(E,W))
        self.btn_ac.grid(column=0, row=1, sticky=(E,W))
        self.btn_del.grid(column=1, row=1, sticky=(E,W))
        self.btn_per.grid(column=2, row=1, sticky=(E,W))
        self.btn_ad.grid(column=3, row=1, sticky=(E,W))
        self.btn_7.grid(column=0, row=2, sticky=(E, W))
        self.btn_8.grid(column=1, row=2, sticky=(E, W))
        self.btn_9.grid(column=2, row=2, sticky=(E, W))
        self.btn_minus.grid(column=3, row=2, sticky=(E, W))
        self.btn_4.grid(column=0, row=3, sticky=(E, W))
        self.btn_5.grid(column=1, row=3, sticky=(E, W))
        self.btn_6.grid(column=2, row=3, sticky=(E, W))
        self.btn_plus.grid(column=3, row=3, sticky=(E, W))
        self.btn_1.grid(column=0, row=4, sticky=(E, W))
        self.btn_2.grid(column=1, row=4, sticky=(E, W))
        self.btn_3.grid(column=2, row=4, sticky=(E, W))
        self.btn_div.grid(column=3, row=4, sticky=(E, W))
        self.btn_dot.grid(column=0, row=5, sticky=(E, W))
        self.btn_0.grid(column=1, row=5, sticky=(E, W))
        self.btn_eq.grid(column=2, row=5, columnspan=2, sticky=(E, W))

    # 按钮显示到text区域
    def show_input(self, input_content):
        if self.trigger:
            self.trigger = False
            self.text.delete('1.0', END)
            self.text.insert(END, input_content)

        else:
            self.text.insert(END, input_content)

    # 等号显示
    def equals(self):
        self.show_input('=')
        text_content = self.text.get("1.0", END)
        print(text_content)

    # AC按钮事件
    def ac_function(self):
        self.text.delete('1.0', END)

    # The "-2c" part means "minus two characters".
    # Minus one character moves the index before
    # the invisible trailing newline, and moving
    # one more character moves the index before the last character.
    def del_function(self):
        self.text.delete('end-2c')

    # 等号事件
    def eval_remake(self):
        equation = self.text.get('1.0', END)
        try:
            result = eval(equation)
            self.text.delete('1.0', END)
            self.text.insert('1.0', result)
            self.trigger = True
            return result
        except ZeroDivisionError:
            msgbox.showerror('提示', '除数不能为0')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    init_window = Tk()
    my_calculator = MY_GUI(init_window, False)
    my_calculator.set_init_window()
    init_window.mainloop()
