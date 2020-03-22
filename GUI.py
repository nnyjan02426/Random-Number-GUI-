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
tk.Label(start_frame, text = '起始數字').pack(side=tk.LEFT)
start_num = tk.Entry(start_frame)
start_num.pack(side=tk.LEFT)

end_frame = tk.Frame(window)
end_frame.pack(side=tk.TOP)
tk.Label(end_frame, text = '結束數字').pack(side=tk.LEFT)
end_num = tk.Entry(end_frame)
end_num.pack(side=tk.LEFT)
tk.Label(window).pack()


rand_output = tk.Label(window, font=('Times',50))
rand_output.pack()

repeat_lst = []
lst_num = 1
clear_all = False

class commands():
    def __init__(self):
        self.repeat_bool = False

    def repeat(self):
        if variable1.get() == 1:
            self.repeat_bool = True
        else:
            self.repeat_bool = False

    def clear_hist(self):
        global repeat_lst
        repeat_lst = []
        rand_output.configure(text=' ')

    def rand_command(self):
        global repeat_lst
        num1 = start_num.get()
        num2 = end_num.get()
        try:
            num1_int = int(num1)
            num2_int = int(num2)
            if num1_int == num2_int:
                tk.messagebox.showerror('ERROR', '請輸入相異的數字')
            elif num1_int > num2_int:
                tk.messagebox.showerror('ERROR', '起始數字 需比 結束數字 大')
            else:
                if len(repeat_lst) == len(range(num1_int, num2_int+1)):
                    if tk.messagebox.askyesno(' ', '所有數字已輪過一遍，是否重輪一遍？') == True:
                        rand_output.configure(text=' ')
                        repeat_lst = []
                    else:
                        window.destroy()
                else:
                    rand_num = random.randint(num1_int, num2_int)
                    if self.repeat_bool == False:
                        while rand_num in repeat_lst:
                            rand_num = random.randint(num1_int, num2_int)
                        else:
                            rand_output.configure(text=str(rand_num))
                            self.lst_get = True
                            repeat_lst.append(rand_num)
                            self.lst_get = False
                    else:
                        rand_output.configure(text=str(rand_num))
        except ValueError:
            tk.messagebox.showerror('ERROR', '請輸入正整數')


tk.Label(window).pack()
comm = commands()

rand_button = ttk.Button(window, text='RUN', command=comm.rand_command)
rand_button.pack()

check_frame = tk.Frame(window)
check_frame.pack(side=tk.BOTTOM)
variable1 = tk.IntVar()
repeat_check = tk.Checkbutton(check_frame, text='重複', variable=variable1, onvalue=1, offvalue=0, command=comm.repeat)
repeat_check.pack(side=tk.LEFT)
clear_hist_check = ttk.Button(check_frame, text='清除歷史', command=comm.clear_hist)
clear_hist_check.pack(side=tk.LEFT)

window.mainloop()