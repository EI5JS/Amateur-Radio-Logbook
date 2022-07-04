
from tkinter import *
from tkinter import ttk
import sqlite3
import os
import subprocess


##  define main logbook window
def stationlogbook():

    def launch_DBviewer(event=None):
        subprocess.run(['sqlitebrowser', '/home/john/Dev/Projects/Logbook/logbookdata.db'])
        logbook.destroy()

    logbook=Tk()
    logbook.title("   EI5JS Logbook v2")
    logbook.configure(bg='#373737', border=40)
    logbook.geometry("1000x715+155+58")
    logbook.overrideredirect(False)
    logbook.resizable(width=False, height=False)

    lab=Label(logbook, text="      EI5JS  Station Logbook      ", font=("verdana", 14), bg=("#373737"), fg=("white"))
    lab.pack()
    lab=Label(logbook, text="", font=("verdana", 30), bg=("#373737"), fg=("white"))
    lab.pack() ## Extra label used for spacing

     ##  define treeview
    treeview=ttk.Treeview(logbook)
    treeview.config(height=22)

    treeview['show'] = 'headings'  ## This mutes the empty first column in treeview
    style=ttk.Style()
    style.configure("Treeview.Heading",background = "#aaaaff",foreground="#05056f", font=(None, 12))
    style.configure("Treeview", font=(None, 11), foreground="white", background="#3c3a3a")

    vsb = ttk.Scrollbar(logbook, orient="vertical", command=treeview.yview)
    vsb.place(x=910, y=180, height=270)
    treeview.configure(yscrollcommand=vsb.set)
    treeview.yview_moveto(1)




##  define columns
    treeview.config(columns = ('Date', 'UTC', 'Callsign', 'Freq', 'Mode', 'Pwr', 'Rpt_rec', 'Rpt_sent','Notes'))
    treeview.column('#1', width=118, anchor="center")
    treeview.heading('#1', text='Date')
    treeview.column('#2', width=70, anchor="center")
    treeview.heading('#2', text='UTC')
    treeview.column('#3', width=100, anchor="center")
    treeview.heading('#3', text='Callsign')
    treeview.column('#4', width=80, anchor="center")
    treeview.heading('#4', text='Freq')
    treeview.column('#5', width=65, anchor="center")
    treeview.heading('#5', text='Mode')
    treeview.column('#6', width=60, anchor="center")
    treeview.heading('#6', text='Pwr')
    treeview.column('#7', width=83, anchor="center")
    treeview.heading('#7', text='Rpt rec')
    treeview.column('#8', width=83, anchor="center")
    treeview.heading('#8', text='Rpt sent')
    treeview.column('#9', width=171, anchor="w")
    treeview.heading('#9', text='Notes')
    treeview.pack()


    conn = sqlite3.connect('/home/john/Dev/Projects/Logbook/logbookdata.db', check_same_thread=False, isolation_level=None)
    c = conn.cursor()


    lab=Label(logbook, text="", font=("verdana", 30), bg=("#373737"), fg=("white")) ## Blank line used for spacing
    lab.pack()


##  define buttons
    button1 = Button(logbook,font=("verdana", 11),text="Edit in DB Browser", bg="#fc9083", fg="black", width=20,borderwidth=2, command=launch_DBviewer)
    button1.pack(padx=140)



##  read from logbook database and place in treeview columns
    def read_from_logbook():
        c.execute("SELECT * FROM Logbook")
        data=c.fetchall()

        for column in data:
            treeview.insert("", END, values=(column[0],column[1], column[2],column[3],
            column[4],column[5], column[6],column[7], column[8]))




    read_from_logbook()
    conn.commit()
    conn.close()
    logbook.mainloop()

stationlogbook()
