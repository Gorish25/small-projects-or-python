from tkinter import *
import speedtest


def speedcheck():
    sp = speedtest.Speedtest() # created a variable for speed
    sp.get_servers() # getting the servers
    down = str(round(sp.download()/(10**6),3))+ ' Mbps' #
    up = str(round(sp.upload()/(10**6),3))+" Mbps"
    lab_down.config(text=down)
    lab_upload.config(text=up)




sp=Tk()

# look of window
sp.title("Internel Speed Test")
sp.geometry('500x500')
sp.config(bg="black")


# specifying label for Internet Speed Test
lab_title=Label(sp,text="Internet Speed Test", font=("Time New Roman",20,"bold"),bg="black",fg="green")
lab_title.place(x=110,y=40,height=30,width=280)


# specifying label for download speed
lab_d=Label(sp,text="Download Speed", font=("Time New Roman",20,"bold"),bg="black",fg="green")
lab_d.place(x=110,y=100,height=30,width=280)


# actual speed
lab_down=Label(sp,text="00", font=("Time New Roman",20,"bold"),bg="black",fg="green")
lab_down.place(x=110,y=170,height=30,width=280)


# label for upload speed
lab_up=Label(sp,text="Upload Speed", font=("Time New Roman",20,"bold"),bg="black",fg="green")
lab_up.place(x=110,y=250,height=30,width=280)


# actual speed
lab_upload=Label(sp,text="00", font=("Time New Roman",20,"bold"),bg="black",fg="green")
lab_upload.place(x=110,y=300,height=30,width=280)


# button for speed testing purpose
button=Button(sp,text="Calculate", font=("Time New Roman",20,"bold"),fg="green",bg="pink",relief=RAISED,command=speedcheck) # relief for 3d effect
button.place(x=110,y=350,height=30,width=280)



sp.mainloop()