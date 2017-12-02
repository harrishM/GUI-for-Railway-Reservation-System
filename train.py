from tkinter import *

import train_backend


def add_command():
    train_backend.inserttrain(trainid_text.get(),trainname_text.get(),carriages1_text.get(),cap1_text.get(),price1_text.get(),carriages2_text.get(),cap2_text.get(),price2_text.get(),carriages3_text.get(),cap3_text.get(),price3_text.get())
    train_backend.insertroute(trainid_text.get(),stationidsource_text.get(),stationnamesource_text.get(),arrsource_text.get(),stationid1_text.get(),stationname1_text.get(),arr1_text.get(),dept1_text.get(),stationid2_text.get(),stationname2_text.get(),arr2_text.get(),dept2_text.get(),stationid3_text.get(),stationname3_text.get(),arr3_text.get(),dept3_text.get(),stationiddest_text.get(),stationnamedest_text.get(),arrdest_text.get())
    train_backend.insertstation(stationidsource_text.get(),stationnamesource_text.get(),stationid1_text.get(),stationname1_text.get(),stationid2_text.get(),stationname2_text.get(),stationid3_text.get(),stationname3_text.get(),stationiddest_text.get(),stationnamedest_text.get())

def delete_command():
    train_backend.deletetrain(trainid_text.get())
    train_backend.deleteroute(trainid_text.get())


window=Tk()



window.wm_title("RAILWAY RESERVATION")
window.geometry("1400x350")



l0=Label(window,text="ARAKSHAN", font="Times",fg="Brown")
l0.grid(row=1,column=6,columnspan=1)
l1=Label(window,text="TrainID",font="helvetica 12")
l1.grid(row=2,column=0)
trainid_text=StringVar()
e1=Entry(window,textvariable=trainid_text)
e1.grid(row=2,column=1)

l2=Label(window,text="TrainName",font="helvetica 13")
l2.grid(row=2,column=3)
trainname_text=StringVar()
e2=Entry(window,textvariable=trainname_text)
e2.grid(row=2,column=4)

l3=Label(window,text="Source",font="helvetica 14")
l3.grid(row=6,column=0)
l4=Label(window,text="StationID",font="helvetica 13")
l4.grid(row=7,column=0)
stationidsource_text=StringVar()
e4=Entry(window,textvariable=stationidsource_text)
e4.grid(row=7,column=1)
l5=Label(window,text="Station Name",font="helvetica 13")
l5.grid(row=8,column=0)
stationnamesource_text=StringVar()
e5=Entry(window,textvariable=stationnamesource_text)
e5.grid(row=8,column=1)
l6=Label(window,text="Time",font="helvetica 13")
l6.grid(row=9,column=0)
l7=Label(window,text="Dep.",font="helvetica 13")
l7.grid(row=10,column=0)
arrsource_text=StringVar()
e7=Entry(window,textvariable=arrsource_text)
e7.grid(row=10,column=1)





l8=Label(window,text="Stop 1",font="helvetica 14")
l8.grid(row=6,column=2,columnspan=4)
l9=Label(window,text="StationID",font="helvetica 13")
l9.grid(row=7,column=2)
stationid1_text=StringVar()
e9=Entry(window,textvariable=stationid1_text)
e9.grid(row=7,column=3)
l10=Label(window,text="Station Name",font="helvetica 13")
l10.grid(row=8,column=2)
stationname1_text=StringVar()
e10=Entry(window,textvariable=stationname1_text)
e10.grid(row=8,column=3)
l11=Label(window,text="Time",font="helvetica 13")
l11.grid(row=9,column=2)
l12=Label(window,text="Arr.",font="helvetica 13")
l12.grid(row=10,column=2)
arr1_text=StringVar()
e12=Entry(window,textvariable=arr1_text)
e12.grid(row=10,column=3)
l13=Label(window,text="Dep.",font="helvetica 13")
l13.grid(row=11,column=2)
dept1_text=StringVar()
e13=Entry(window,textvariable=dept1_text)
e13.grid(row=11,column=3)









l14=Label(window,text="Stop 2",font="helvetica 14")
l14.grid(row=6,column=6,columnspan=4)
l15=Label(window,text="StationID",font="helvetica 13")
l15.grid(row=7,column=6)
stationid2_text=StringVar()
e15=Entry(window,textvariable=stationid2_text)
e15.grid(row=7,column=7)
l16=Label(window,text="Station Name",font="helvetica 13")
l16.grid(row=8,column=6)
stationname2_text=StringVar()
e16=Entry(window,textvariable=stationname2_text)
e16.grid(row=8,column=7)
l17=Label(window,text="Time",font="helvetica 13")
l17.grid(row=9,column=6)
l18=Label(window,text="Arr.",font="helvetica 13")
l18.grid(row=10,column=6)
arr2_text=StringVar()
e18=Entry(window,textvariable=arr2_text)
e18.grid(row=10,column=7)
l19=Label(window,text="Dep.",font="helvetica 13")
l19.grid(row=11,column=6)
dept2_text=StringVar()
e19=Entry(window,textvariable=dept2_text)
e19.grid(row=11,column=7)


l20=Label(window,text="Stop 3",font="helvetica 14")
l20.grid(row=6,column=11,columnspan=4)
l21=Label(window,text="StationID",font="helvetica 13")
l21.grid(row=7,column=11)
stationid3_text=StringVar()
e21=Entry(window,textvariable=stationid3_text)
e21.grid(row=7,column=12)
l22=Label(window,text="Station Name",font="helvetica 13")
l22.grid(row=8,column=11)
stationname3_text=StringVar()
e22=Entry(window,textvariable=stationname3_text)
e22.grid(row=8,column=12)
l23=Label(window,text="Time",font="helvetica 13")
l23.grid(row=9,column=11)
l24=Label(window,text="Arr.",font="helvetica 13")
l24.grid(row=10,column=11)
arr3_text=StringVar()
e24=Entry(window,textvariable=arr3_text)
e24.grid(row=10,column=12)
l25=Label(window,text="Dep.",font="helvetica 13")
l25.grid(row=11,column=11)
dept3_text=StringVar()
e25=Entry(window,textvariable=dept3_text)
e25.grid(row=11,column=12)




l26=Label(window,text="Destination",font="helvetica 14")
l26.grid(row=6,column=15)
l27=Label(window,text="StationID",font="helvetica 13")
l27.grid(row=7,column=15)
stationiddest_text=StringVar()
e27=Entry(window,textvariable=stationiddest_text)
e27.grid(row=7,column=16)
l28=Label(window,text="Station Name",font="helvetica 13")
l28.grid(row=8,column=15)
stationnamedest_text=StringVar()
e28=Entry(window,textvariable=stationnamedest_text)
e28.grid(row=8,column=16)
l29=Label(window,text="Time",font="helvetica 13")
l29.grid(row=9,column=15)
l30=Label(window,text="Arr.",font="helvetica 13")
l30.grid(row=10,column=15)
arrdest_text=StringVar()
e30=Entry(window,textvariable=arrdest_text)
e30.grid(row=10,column=16)





l31=Label(window,text="Class 1",font="helvetica 14")
l31.grid(row=13,column=0)
l32=Label(window,text="No. of carriages",font="helvetica 13")
l32.grid(row=14,column=0)
carriages1_text=StringVar()
e32=Entry(window,textvariable=carriages1_text)
e32.grid(row=14,column=1)
l33=Label(window,text="Capacity",font="helvetica 13")
l33.grid(row=15,column=0)
cap1_text=StringVar()
e33=Entry(window,textvariable=cap1_text)
e33.grid(row=15,column=1)

l34=Label(window,text="Price",font="helvetica 13")
l34.grid(row=16,column=0)
price1_text=StringVar()
e34=Entry(window,textvariable=price1_text)
e34.grid(row=16,column=1)





l35=Label(window,text="Class 2",font="helvetica 14")
l35.grid(row=13,column=6)
l36=Label(window,text="No. of carriages",font="helvetica 13")
l36.grid(row=14,column=6)
carriages2_text=StringVar()
e36=Entry(window,textvariable=carriages2_text)
e36.grid(row=14,column=7)
l37=Label(window,text="Capacity",font="helvetica 13")
l37.grid(row=15,column=6)
cap2_text=StringVar()
e37=Entry(window,textvariable=cap2_text)
e37.grid(row=15,column=7)

l38=Label(window,text="Price",font="helvetica 13")
l38.grid(row=16,column=6)
price2_text=StringVar()
e38=Entry(window,textvariable=price2_text)
e38.grid(row=16,column=7)






l39=Label(window,text="Class 3",font="helvetica 14")
l39.grid(row=13,column=15)
l40=Label(window,text="No. of carriages",font="helvetica 13")
l40.grid(row=14,column=15)
carriages3_text=StringVar()
e40=Entry(window,textvariable=carriages3_text)
e40.grid(row=14,column=16)
l41=Label(window,text="Capacity",font="helvetica 13")
l41.grid(row=15,column=15)
cap3_text=StringVar()
e41=Entry(window,textvariable=cap3_text)
e41.grid(row=15,column=16)

l42=Label(window,text="Price",font="helvetica 13")
l42.grid(row=16,column=15)
price3_text=StringVar()
e42=Entry(window,textvariable=price3_text)
e42.grid(row=16,column=16)

b1=Button(window,text="       Add ",command=add_command,relief=FLAT,font="helvetica 13 bold")
b1.grid(row=17,column=16)

b2=Button(window,text="Remove    ",command=delete_command,relief=FLAT,font="helvetica 13 bold")
b2.grid(row=17,column=17)




window.mainloop()
