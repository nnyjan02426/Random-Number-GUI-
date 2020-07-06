import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk()
window.title('抽籤')
window.geometry('250x250+450+200')
window.configure(background='white')

start_frame = tk.Frame(window)
start_frame.pack(side=tk.TOP)
tk.Label(start_frame, text='起始數字').pack(side=tk.LEFT)
start_num = tk.Entry(start_frame)
start_num.pack(side=tk.LEFT)

end_frame = tk.Frame(window)
end_frame.pack(side=tk.TOP)
tk.Label(end_frame, text='結束數字').pack(side=tk.LEFT)
end_num = tk.Entry(end_frame)
end_num.pack(side=tk.LEFT)
tk.Label(window).pack()

rand_output = tk.Label(window, font=('Times', 50))
rand_output.pack()


def if_input_err(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)

        if num1 == num2:
            tk.messagebox.showerror('ERROR', '請輸入相異的數字')
            return True
        if num1 > num2:
            tk.messagebox.showerror('ERROR', '起始數字 需比 結束數字 大')
            return True

    except ValueError:
        tk.messagebox.showerror('ERROR', '請輸入正整數')
        return True

    return False


class Commands:
    def __init__(self):
        self.repeat_bool = False
        self.repeat_lst = []

    def repeat(self):
        if variable1.get() == 1:
            self.repeat_bool = True
        else:
            self.repeat_bool = False

    def clear_hist(self):
        self.repeat_lst = []
        rand_output.configure(text=' ')

    def main(self):
        go = True
        num1 = start_num.get()
        num2 = end_num.get()
        if not if_input_err(num1, num2):
            num1 = int(num1)
            num2 = int(num2)
            if len(self.repeat_lst) == len(range(num1, num2 + 1)):
                if tk.messagebox.askyesno(' ', '所有數字已輪過一遍，是否重輪一遍？'):
                    rand_output.configure(text=' ')
                    self.repeat_lst = []
                    go = False
                else:
                    go = False
                    window.destroy()
            else:
                rand_num = random.randint(num1, num2)

            if go:
                if not self.repeat_bool:
                    while rand_num in self.repeat_lst:
                        rand_num = random.randint(num1, num2)
                    else:
                        rand_output.configure(text=str(rand_num))
                        self.repeat_lst.append(rand_num)
                else:
                    rand_output.configure(text=str(rand_num))


tk.Label(window).pack()
command = Commands()

rand_button = ttk.Button(window, text='RUN', command=command.main)
rand_button.pack()

check_frame = tk.Frame(window)
check_frame.pack(side=tk.BOTTOM)
variable1 = tk.IntVar()
repeat_check = tk.Checkbutton(check_frame, text='重複', variable=variable1, onvalue=1, offvalue=0, command=command.repeat)
repeat_check.pack(side=tk.LEFT)
clear_hist_check = ttk.Button(check_frame, text='清除歷史', command=command.clear_hist)
clear_hist_check.pack(side=tk.LEFT)

window.mainloop()
