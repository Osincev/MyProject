import tkinter as tk
from tkinter import ttk
#from tkinter import PhotoImage
import sys
from datetime import datetime as dt

# from process import CpuBar
# from widget_update import Configure_widgets
nScreenNum = 0

sLastMeltNum = str(3333)
sLastWheelNum = str(2222)
sLastWheelID = str(2222)

class Application(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.attributes('-alpha', 1)
        self.attributes('-topmost', True)
        # self.overrideredirect(True)
        # self.resizable(False, False)
        self.title('ARM Application')
        self.run_set_ui()

    def run_set_ui(self):   # Окно с постоянными элементами (Шаблон)
        '''
        if nScreenNum == 0:
            self.StartScreen()
        elif nScreenNum == 1:
            self.WorkScreen()
        else:
            self.WorkScreen()
        '''
        self.StartScreen()

    def StartScreen(self):
        bg = tk.PhotoImage(file = '111.gif')
        lbl = ttk.Label(self, image = bg)
        lbl.image = bg
        lbl.grid()
        bg2 = tk.PhotoImage(file = '333.gif')

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

        def b1(event):
            now = dt.now()
            self.title(f"{now:%d.%m.%Y %H:%M:%S}")
            #self.WorkScreen()
        lbl.bind('<Button-1>', b1)

        def b3(event):
            #self.WorkScreen()
            self.set_ui()
        lbl.bind('<Button-3>', b3)


    def WorkScreen(self):
        SetsBar = ttk.Frame(self)
        SetsBar.grid(row=1,column=0,sticky='NSWE')

        ttk.Button(SetsBar, text='Настройки 1').grid(row=0,column=0,sticky='NSWE')
        ttk.Button(SetsBar, text='Настройки 2').grid(row=0,column=1,sticky='NSWE')
        SetsBar.grid_columnconfigure((0,1),weight=1)
        SetsBar.grid_rowconfigure(0,weight=1)

        self.grid_rowconfigure(0,weight=10)
        self.grid_rowconfigure(1,weight=1)
        self.grid_columnconfigure(0,weight=1)

        #self.set_ui()

        #WorkFrame = ttk.Frame(self)
        #WorkFrame.grid(row=0,column=0,sticky='WE')

        # self.make_bar_cpu_usage()
        # self.configure_cpu_bar()

    def set_ui(self):
        WinFrame = ttk.Frame(self)
        WinFrame.grid(row=0,column=0,sticky='NSWE')
        WinFrame.grid_columnconfigure(0,weight=1)
        WinFrame.grid_rowconfigure(0,weight=1)

        WheelInfoFrame = ttk.Frame(WinFrame)
        WheelInfoFrame.grid(row=0, column=0,sticky='NWES')
        ttk.Label(WheelInfoFrame, text='Последнее записанное колесо', font='Arial 20', borderwidth=2).grid(row=0, column=0,columnspan=6,sticky='N')
        ttk.Label(WheelInfoFrame, text='Номер плавки:', font='20', borderwidth=2).grid(row=1, column=0,sticky='N')
        ttk.Label(WheelInfoFrame, text=f'{sLastMeltNum}', font='20',borderwidth=2).grid(row=1, column=1,sticky='N')
        ttk.Label(WheelInfoFrame, text='Номер колеса:', font='20',borderwidth=2).grid(row=1, column=2,sticky='N')
        ttk.Label(WheelInfoFrame, text=f'{sLastWheelNum}', font='20',borderwidth=2).grid(row=1, column=3,sticky='N')
        ttk.Label(WheelInfoFrame, text='ID колеса:', font='20',borderwidth=2).grid(row=1, column=4,sticky='N')
        ttk.Label(WheelInfoFrame, text=f'{sLastWheelID}', font='20',borderwidth=2).grid(row=1, column=5,sticky='N')
        ttk.Label(WheelInfoFrame, text=f'ЛОГ', font='Arial 10',borderwidth=2).grid(row=2, column=0,columnspan=6,sticky='S')

        WheelInfoFrame.grid_columnconfigure((0,1,2,3,4,5,6),weight=1)
        WheelInfoFrame.grid_rowconfigure((0,1),weight=1)

        LogFrame = ttk.Frame(WinFrame)
        LogFrame.grid(row=1,column=0,sticky='NWSE')
        ttk.Entry(LogFrame).grid(sticky='NSWE')
        #ttk.Button(LogFrame, text='Выход').grid(row=0,column=0,sticky='NSWE')
        LogFrame.grid_columnconfigure(0,weight=1)
        LogFrame.grid_rowconfigure(0,weight=1)

        ButtonFrame = ttk.Frame(WinFrame)
        ButtonFrame.grid(row=0, column=1,rowspan=2,sticky='NSWE')
        ttk.Button(ButtonFrame, text='Выход').grid(row=0,column=0,sticky='NSWE')
        ttk.Button(ButtonFrame, text='Перезапуск АРМ').grid(row=1,column=0,sticky='NSWE')
        ttk.Button(ButtonFrame, text='Подключиться по TCP').grid(row=2,column=0,sticky='NSWE')
        ttk.Button(ButtonFrame, text='Считать твердость по TCP').grid(row=3,column=0,sticky='NSWE')
        ttk.Button(ButtonFrame, text='Фиктивное измерение').grid(row=4,column=0,sticky='NSWE')
        ttk.Button(ButtonFrame, text='Очистить').grid(row=5,column=0,sticky='NSWE')
        ButtonFrame.grid_rowconfigure((0,1,2,3,4,5),weight=1)
        ButtonFrame.grid_columnconfigure(0,weight=1)


        # self.grid_columnconfigure(([x for x in range(5)]),weight=1)
        #self.grid_columnconfigure(0,weight=4)
        #self.grid_columnconfigure(1,weight=1)
        #self.grid_rowconfigure(0,weight=1)
        #self.grid_rowconfigure(1,weight=8)



    def app_exit(self):
        self.destroy()
        sys.exit()

if __name__ == '__main__':
    root = Application()
    root.mainloop()


'''
        self.combo_win = ttk.Combobox(self.bar2,
                                        values = ["hide", "don't hide", "min"],
                                        width=9, state = 'readonly')
        self.combo_win.pack(side=tk.LEFT)

        ttk.Button(self.bar2, text='move', command=self.configure_win)
                                                            .pack(side=tk.LEFT)
        ttk.Button(self.bar2, text='>>>').pack(side=tk.LEFT)

        self.bar = ttk.LabelFrame(self, text='Power')
        self.bar.pack(fill=tk.BOTH)

        self.bind_class('Tk', '<Enter>', self.enter_mouse)
        self.bind_class('Tk', '<Leave>', self.leave_mouse)
        self.combo_win.bind('<<ComboboxSelected>>', self.choise_combo)
'''
'''
    def run_set_ui(self):
        self.set_ui()
        self.make_bar_cpu_usage()
        self.configure_cpu_bar()

'''
'''
    def make_bar_cpu_usage(self):
        ttk.Label(self.bar, text = f'physical cores: {self.cpu.cpu_count},
                        logical cores: {self.cpu.cpu_count_logical}',
                        anchor=tk.CENTER).pack(fill=tk.X)

        self.list_label = []
        self.list_pbar = []

        for i in range(self.cpu.cpu_count_logical):
            self.list_label.append(ttk.Label(self.bar, anchor=tk.CENTER))
            self.list_pbar.append(ttk.Progressbar(self.bar, length=100))
        for i in range(self.cpu.cpu_count_logical):
            self.list_label[i].pack(fill=tk.X)
            self.list_pbar[i].pack(fill=tk.X)

        self.ram_lab = ttk.Label(self.bar, text='', anchor=tk.CENTER)
        self.ram_lab.pack(fill=tk.X)
        self.ram_bar = ttk.Progressbar(self.bar, length=100)
        self.ram_bar.pack(fill=tk.X)

    def make_minimal_win(self):
        self.bar_one = ttk.Progressbar(self, length=100)
        self.bar_one.pack(side=tk.LEFT)

        self.ram_bar = ttk.Progressbar(self, length=100)
        self.ram_bar.pack(side=tk.LEFT)

        ttk.Button(self, text='full', width=5,
                    command=self.make_full_win
                    ).pack(side=tk.RIGHT)

        ttk.Button(self, text='move', width=5,
                    command=self.configure_win
                    ).pack(side=tk.RIGHT)

        self.update()
        self.configure_minimal_win()


    def enter_mouse(self, event):
        if self.combo_win.current() == 0 or 1:
            self.geometry('')

    def leave_mouse(self, event):
        if self.combo_win.current() == 0:
            self.geometry(f'{self.winfo_width()}x1')

    def choise_combo(self, event):
        if self.combo_win.current() == 2:
            self.enter_mouse('')
            self.unbind_class('Tk', '<Enter>')
            self.unbind_class('Tk', '<Leave>')
            self.combo_win.unbind('<<ComboboxSelected>>')
            self.after_cancel(self.wheel)
            self.clear_win()
            self.update()
            self.make_minimal_win()


    def make_full_win(self):
        self.after_cancel(self.wheel)
        self.clear_win()
        self.update()
        self.run_set_ui()
        self.enter_mouse('')
        self.combo_win.current(1)

'''
