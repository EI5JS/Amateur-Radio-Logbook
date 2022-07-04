

  ###############################################################################################################################
  #                                                                                                                             #
  #                                                                                                                             #
  #                                        EI5JS Logbook v1.0 , PYTHON 3.6, SQLite, tkinter                                     #
  #                                                          MARCH 2018                                                         #
  #                                                                                                                             #
  #                                                                                                                             #
  ###############################################################################################################################


##      About this program.
##
##      This Amateur Radio logging software is designed to be minimal focusing on ease of use. It uses a tkinter GUI to write
##      log entries to an SQLite database. The user has only three buttons, 'Save' to save the contact to the
##      logbook, 'Clear' to empty any or all of the text fields without saving, and 'Logbook' that opens the
##      log in DBViewer for exploring and maintaining the entries. 'Tab' allows movement forward through the
##      fields and buttons. Shift-Tab reverses the direction of Tab. The return key acts on any focused button.
##      Any action returns the user to the 'Callsign' field for the next entry. Windows X and Ctl-X closes the window.
##      Requirement is for Python3 and DBViewer to be installed on the PC. The database is auto-created on first startup.
##
##       John Clavin EI5JS, March/April 2018
##       Updated October 2019 for Arch Openbox Desktop to v2.0
##	     Further modified after move to Ubuntu 22.04LTS





#------------------------IMPORT MODULES AND INITIALISE VARIABLES---------------------------------------

from tkinter import *
import sqlite3
import time
import datetime
import os
import subprocess

#-----------------------------DEFINE FUNCTIONS FOR BUTTONS--------------------------------------------



### Create 'Save' button. Writes to database if 'Callsign' has input ###
def save_to_log(event=None):
    datenow = str(datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%Y'))
    timenow = str(datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M'))
    callsign=(callsig.get()).upper()
    freq=(fre.get())
    mode=(mod.get()).upper()
    power=(powe.get())
    rptrecv=(rptrec.get())
    rptsent=(rptsen.get())
    comment=(commen.get())


    conn = sqlite3.connect('/home/john/Dev/Projects/Logbook/logbookdata.db', check_same_thread=False, isolation_level=None)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Logbook (Date TEXT, UTC REAL, Callsign TEXT, Freq TEXT, Mode TEXT, Pwr TEXT, Rpt_rec TEXT, Rpt_Sent TEXT, Comments TEXT)''')
    if len(callsig.get()) >= 1:   ### Check for 'Callsign' input before writing to logbook ###
        c.execute("INSERT INTO Logbook(Date, UTC, Callsign, Freq, Mode, Pwr, Rpt_Rec, Rpt_Sent, Comments) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (datenow, timenow, callsign, freq, mode, power, rptrecv, rptsent, comment))

    clear_fields()
    entry_1.focus_set()
    conn.commit()
    conn.close()
    return


### Create 'Clear' button action###
def clear_fields(event=None):
    entry_1.delete(0, END)
    entry_2.delete(0, END)
    entry_3.delete(0, END)
    entry_4.delete(0, END)
    entry_5.delete(0, END)
    entry_6.delete(0, END)
    entry_7.delete(0, END)
    entry_1.focus_set()
    return



### Create 'Exit' Keybinding (Ctl-X)
def close(event=None):
    contact.destroy()


## Open logbook app
def launch_logbook(event=None):
    entry_1.focus_set()
    subprocess.run(['python3', '/home/john/Dev/Projects/Logbook/logbook.pyw'])


#-----------------CONSTRUCTION OF GRAPHICAL INTERFACE---------------------------------


contact = Tk()
contact.bind('<Control-x>', close)
contact.geometry("400x657+1190+240")
contact.configure(bg='#373737')
contact.resizable(width=False, height=False)
contact.attributes("-topmost", True)

variable=StringVar()
callsig=StringVar()
fre=StringVar()
mod=StringVar()
powe=StringVar()
rptrec=StringVar()
rptsen=StringVar()
locator=StringVar()
commen=StringVar()


contact.title("  EI5JS Logbook v2.0")

Frame1 = Frame(contact, bg="#373737")
Frame1.pack(side=TOP)
Frame2 = Frame(contact, bg="#373737")
Frame2.pack()
Frame3 = Frame(contact, bg="#373737")
Frame3.pack()
Frame4 = Frame(contact, bg="#373737")
Frame4.pack()
Frame5 = Frame(contact, bg="#373737")
Frame5.pack()
Frame6 = Frame(contact, bg="#373737")
Frame6.pack()
Frame7 = Frame(contact, bg="#373737")
Frame7.pack()
Frame8 = Frame(contact, bg="#373737")
Frame8.pack()
Frame9 = Frame(contact, bg="#373737")
Frame9.pack(side=BOTTOM)


lab=Label(Frame1, text="     EI5JS Logbook v2.0", font=("cantarell", 13), bg=("#373737"), fg=("white"))
lab.pack(pady=28)

label1=Label(Frame2, text="Callsign:",font=("cantarell", 12), width="10", height="3", bg="#373737", fg="#ffffff")
label1.pack(side=LEFT)
entry_1=Entry(Frame2, textvariable=callsig, bg="#d0d2da",font=("cantarell", 11), width="18", justify="center")
entry_1.pack(side=RIGHT)

label2=Label(Frame3, text="Freq:",font=("cantarell", 12), width="10", height="3", bg="#373737", fg="#ffffff")
label2.pack(side=LEFT)
entry_2=Entry(Frame3,textvariable=fre, bg="#d0d2da",font=("cantarell", 11), width="18", justify="center")
entry_2.pack(side=RIGHT)

label3=Label(Frame4, text="Mode:",font=("cantarell", 12), width="10", height="3", bg="#373737", fg="#ffffff")
label3.pack(side=LEFT)
entry_3=Entry(Frame4,textvariable=mod, bg="#d0d2da",font=("cantarell", 11), width="18", justify="center")
entry_3.pack(side=RIGHT)

label4=Label(Frame5, text="Pwr(W):",font=("cantarell", 12), width="10", height="3", bg="#373737", fg="#ffffff")
label4.pack(side=LEFT)
entry_4=Entry(Frame5, textvariable=powe, bg="#d0d2da",font=("cantarell", 11), width="18", justify="center")
entry_4.pack(side=RIGHT)

label5=Label(Frame6, text="Rpt in:",font=("cantarell", 12), width="10", height="3", bg="#373737", fg="#ffffff")
label5.pack(side=LEFT)
entry_5=Entry(Frame6,textvariable=rptrec, bg="#d0d2da",font=("cantarell", 11), width="18", justify="center")
entry_5.pack(side=RIGHT)

label6=Label(Frame7, text="Rpt out:",font=("cantarell", 12), width="10", height="3", bg="#373737", fg="#ffffff")
label6.pack(side=LEFT)
entry_6=Entry(Frame7,textvariable=rptsen, bg="#d0d2da",font=("cantarell", 11), width="18", justify="center")
entry_6.pack(side=RIGHT)

label7=Label(Frame8, text="Notes:",font=("cantarell", 12), width="10", height="3", bg="#373737", fg="#ffffff")
label7.pack(side=LEFT)
entry_7=Entry(Frame8,textvariable=commen, bg="#d0d2da",font=("cantarell", 11), width="18", justify="left")
entry_7.pack(side=RIGHT)


button1 = Button(Frame9,font=("cantarell", 12),text="Save", bg="#00cc00", fg="black", width=8, borderwidth=2, command=save_to_log)
button2 = Button(Frame9,font=("cantarell", 12),text="Clear", bg="#8888dd", fg="black", width=8, borderwidth=2, command=clear_fields)
button3 = Button(Frame9,font=("cantarell", 12),text="Logbook", bg="#fC9083", fg="black", width=8, borderwidth=2, command=launch_logbook)


button1.bind('<Return>', save_to_log)
button2.bind('<Return>', clear_fields)
button3.bind('<Return>', launch_logbook)

button1.pack(padx=7, pady=23, side=LEFT)
button2.pack(padx=7, pady=23, side=LEFT)
button3.pack(padx=7, pady=23, side=RIGHT)

entry_1.focus_set()


contact.mainloop()


#-------------------------------END----------------------------------
