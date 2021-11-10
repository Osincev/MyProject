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
        self.state('zoomed')
        self.title('ARM Application')
        self.StartScreen()
        self.PasswScreen()

    def PasswScreen(self):
        new_win = tk.Toplevel()
        new_win.title("111")
        new_win.geometry("200x200")
        ttk.Label(new_win, text='Номер колеса:', font='20',borderwidth=2).grid(row=1, column=2,sticky='N')

    def StartScreen(self):
        bg = tk.PhotoImage(file = '111.gif')
        lbl = ttk.Label(self, image = bg)
        lbl.image = bg
        lbl.grid()
        bg2 = tk.PhotoImage(file = '333.gif')

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

        def b1(event):
            #self.WorkScreen()
            lbl.destroy()
            self.WorkScreen()
        lbl.bind('<Button-1>', b1)

    def WorkScreen(self):
        # ----------------WinFrame----------------
        WinFrame = ttk.Frame(self)
        WinFrame.grid(row=0,column=0,sticky='NSWE')
        WinFrame.grid_columnconfigure(0,weight=1)
        WinFrame.grid_rowconfigure(0,weight=1)
        ## ----------------WinFrame - WheelInfoFrame----------------
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
        WheelInfoFrame.grid_columnconfigure((0,1,2,3,4,5,6),weight=1,minsize=30)
        WheelInfoFrame.grid_rowconfigure((0,1),weight=1,minsize=30)
        ## ----------------WinFrame - LogFrame----------------
        LogFrame = ttk.Frame(WinFrame)
        LogFrame.grid(row=1,column=0,sticky='NWSE')
        ### ----------------WinFrame - LogFrame - LogTree----------------
        ### ----------------WinFrame - LogFrame - LogScrlbar----------------
        style = ttk.Style()
        #style.theme_use("default")
        #style.configure("Treeview")
        style.map("Treeview",background=[('selected', 'lightgray')],foreground=[('selected', 'gray')])
        logTreeRows = (('sign','timestamp','text','status'),('Знак','Дата и время','Сообщение','Статус'),(80,100,800,100),(10,10,100,10))
        LogTree =  ttk.Treeview(LogFrame, columns=logTreeRows[0],show = 'headings',height=20, style="Treeview")
        LogScrlbar = ttk.Scrollbar(LogFrame, orient="vertical", command=LogTree.yview)
        LogTree.configure(yscrollcommand=LogScrlbar.set)

        for i in range(len(logTreeRows[0])):
            LogTree.column('#' + str(i), width=logTreeRows[2][i], stretch=1,minwidth=logTreeRows[3][i])
            LogTree.heading(i, text=logTreeRows[1][i])

        LogTree.grid(row=0,column=0,sticky='NSWE')
        LogScrlbar.grid(row=0,column=1,sticky='NWSE')
        #ttk.Entry(LogFrame).grid(sticky='NSWE')
        EventBtn = ttk.Button(LogFrame, text='Событие')
        EventBtn.grid(row=0,column=0)
        LogFrame.grid_columnconfigure(0,weight=1)
        LogFrame.grid_rowconfigure(0,weight=1)

        def AddEventToLog11(msgt):
            sgn = '*'
            now = str(f"{dt.now():%d.%m.%Y %H:%M:%S}")
            sts = 'odd' if dt.now().second%2 else 'even'#== 0) else 'odd'
            LogTree.tag_configure('almstyle', background="red")#, selectmode="browse")
            LogTree.tag_configure('wrnstyle', background="blue")
            if dt.now().second%2:
                LogTree.insert(parent='', index='end', values=(sgn, now, msgt, sts), tags=('almstyle',))
            else:
                LogTree.insert(parent='', index='end', values=(sgn, now, msgt, sts), tags=('wrnstyle',))

            #LogTree.tag_configure('evenrow', background="lightblue")#, selectmode="browse")
            #LogTree.tag_configure('almrow', background="green",foreground="red" )
            #LogTree.tag_bind('ttk', '<1>', itemClicked)

        def EventBtn_b1(event):
            #now = dt.now()
            msgt = 'qqqq'
            AddEventToLog11(msgt)
            ##self.title('111n')
        EventBtn.bind('<Button-1>', EventBtn_b1)

        ## ----------------WinFrame - ButtonFrame----------------
        ButtonFrame = ttk.Frame(WinFrame)
        ButtonFrame.grid(row=0, column=1,rowspan=2,sticky='NSWE')
        MngBtn1 = ttk.Button(ButtonFrame, text='Выход');        MngBtn1.grid(row=0,column=0,sticky='NSWE')
        MngBtn2 = ttk.Button(ButtonFrame, text='Перезапуск АРМ');        MngBtn2.grid(row=1,column=0,sticky='NSWE')
        MngBtn3 = ttk.Button(ButtonFrame, text='Подключиться по TCP');        MngBtn3.grid(row=2,column=0,sticky='NSWE')
        MngBtn4 = ttk.Button(ButtonFrame, text='Считать твердость по TCP');     MngBtn4.grid(row=3,column=0,sticky='NSWE')
        MngBtn5 = ttk.Button(ButtonFrame, text='Фиктивное измерение');      MngBtn5.grid(row=4,column=0,sticky='NSWE')
        MngBtn6 = ttk.Button(ButtonFrame, text='Очистить');     MngBtn6.grid(row=5,column=0,sticky='NSWE')
        ButtonFrame.grid_rowconfigure((0,1,2,3,4,5),weight=1)
        ButtonFrame.grid_columnconfigure(0,weight=1)
        def MngBtn1_b1(event):
            self.app_exit()
        MngBtn1.bind('<Button-1>', MngBtn1_b1)

        # ----------------SetsBar----------------
        SetsBar = ttk.Frame(self)
        SetsBar.grid(row=1,column=0,sticky='NSWE')
        SetsBtn1 = ttk.Button(SetsBar, text='Стартовый экран')
        SetsBtn1.grid(row=0,column=0,sticky='NSWE')
        SetsBtn2 = ttk.Button(SetsBar, text='Настройки')
        SetsBtn2.grid(row=0,column=1,sticky='NSWE')
        SetsBar.grid_columnconfigure((0,1),weight=1)
        SetsBar.grid_rowconfigure(0,weight=1)

        self.grid_rowconfigure(0,weight=50)
        self.grid_rowconfigure(1,weight=1)
        self.grid_columnconfigure(0,weight=1)

        def SetsBtn1_b1(event):
            WinFrame.destroy()
            self.StartScreen()

        SetsBtn1.bind('<Button-1>', SetsBtn1_b1)

        def SetsBtn2_b1(event):
            WinFrame.destroy()
            self.SetsScreen()

        SetsBtn2.bind('<Button-1>', SetsBtn2_b1)

    def SetsScreen(self):
        '''
        WinFrame = ttk.Frame(self)
        WinFrame.grid(row=0,column=0,sticky='NSWE')
        WinFrame.grid_columnconfigure(0,weight=1)
        WinFrame.grid_rowconfigure(0,weight=1)

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
        '''
        SetsBar = ttk.Frame(self)
        SetsBar.grid(row=1,column=0,sticky='NSWE')
        SetsBtn1 = ttk.Button(SetsBar, text='Стартовый экран')
        SetsBtn1.grid(row=0,column=0,sticky='NSWE')
        SetsBtn2 = ttk.Button(SetsBar, text='Рабочий экран')
        SetsBtn2.grid(row=0,column=1,sticky='NSWE')
        SetsBar.grid_columnconfigure((0,1),weight=1)
        SetsBar.grid_rowconfigure(0,weight=1)

        self.grid_rowconfigure(0,weight=50)
        self.grid_rowconfigure(1,weight=1)
        self.grid_columnconfigure(0,weight=1)
        # self.grid_columnconfigure(([x for x in range(5)]),weight=1)
        #self.grid_columnconfigure(0,weight=4)
        #self.grid_columnconfigure(1,weight=1)
        #self.grid_rowconfigure(0,weight=1)
        #self.grid_rowconfigure(1,weight=8)
        def b11(event):
            #WinFrame.destroy()
            self.StartScreen()

        SetsBtn1.bind('<Button-1>', b11)

        def b21(event):
            #WinFrame.destroy()
            self.WorkScreen()

        SetsBtn2.bind('<Button-1>', b21)





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
