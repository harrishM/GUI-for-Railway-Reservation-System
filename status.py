from tkinter import *

import train_backend


def Status():
    list1.delete(0,END)
    list2.delete(0,END)
    list3.delete(0,END)
    list4.delete(0,END)
    list5.delete(0,END)
    list6.delete(0,END)
    list7.delete(0,END)
    list8.delete(0,END)
    list9.delete(0,END)
    list10.delete(0,END)
    list11.delete(0,END)
    list12.delete(0,END)
    list13.delete(0,END)
    list14.delete(0,END)
    list15.delete(0,END)
    list16.delete(0,END)
    list17.delete(0,END)
    list18.delete(0,END)
    list19.delete(0,END)
    list20.delete(0,END)
    list21.delete(0,END)
    list22.delete(0,END)
    list23.delete(0,END)
    list24.delete(0,END)
    list25.delete(0,END)
    list26.delete(0,END)
    list27.delete(0,END)
    list28.delete(0,END)
    for item in train_backend.searchtrainname(trainid_text.get()):
        list1.insert(END,item)
    for item in train_backend.searchclass1carriages(trainid_text.get()):
        list2.insert(END,item)
    for item in train_backend.searchclass1cap(trainid_text.get()):
        list3.insert(END,item)
    for item in train_backend.searchclass1price(trainid_text.get()):
        list4.insert(END,item)


    for item in train_backend.searchclass2carriages(trainid_text.get()):
        list5.insert(END,item)
    for item in train_backend.searchclass2cap(trainid_text.get()):
        list6.insert(END,item)
    for item in train_backend.searchclass2price(trainid_text.get()):
        list7.insert(END,item)


    for item in train_backend.searchclass3carriages(trainid_text.get()):
        list8.insert(END,item)
    for item in train_backend.searchclass3cap(trainid_text.get()):
        list9.insert(END,item)
    for item in train_backend.searchclass3price(trainid_text.get()):
        list10.insert(END,item)
    for item in train_backend.searchssourceid(trainid_text.get()):
        list11.insert(END,item)
    for item in train_backend.searchsourcename(trainid_text.get()):
        list12.insert(END,item)
    for item in train_backend.searchsourcedep(trainid_text.get()):
        list13.insert(END,item)

    for item in train_backend.searchstop1id(trainid_text.get()):
        list14.insert(END,item)
    for item in train_backend.searchstop1name(trainid_text.get()):
        list15.insert(END,item)
    for item in train_backend.searchstop1arr(trainid_text.get()):
        list16.insert(END,item)
    for item in train_backend.searchstop1dep(trainid_text.get()):
        list17.insert(END,item)

    for item in train_backend.searchstop2id(trainid_text.get()):
        list18.insert(END,item)
    for item in train_backend.searchstop2name(trainid_text.get()):
        list19.insert(END,item)
    for item in train_backend.searchstop2arr(trainid_text.get()):
        list20.insert(END,item)
    for item in train_backend.searchstop2dep(trainid_text.get()):
        list21.insert(END,item)


    for item in train_backend.searchstop3id(trainid_text.get()):
        list22.insert(END,item)
    for item in train_backend.searchstop3name(trainid_text.get()):
        list23.insert(END,item)
    for item in train_backend.searchstop3arr(trainid_text.get()):
        list24.insert(END,item)
    for item in train_backend.searchstop3dep(trainid_text.get()):
        list25.insert(END,item)


    for item in train_backend.searchstopdestid(trainid_text.get()):
        list26.insert(END,item)
    for item in train_backend.searchstopdestname(trainid_text.get()):
        list27.insert(END,item)
    for item in train_backend.searchstopdestarr(trainid_text.get()):
        list28.insert(END,item)











window=Tk()



window.wm_title("RAILWAY RESERVATION")
window.geometry("1400x350")



l0=Label(window,text="ARAKSHAN", font="Times",fg="Brown")
l0.grid(row=1,column=6,columnspan=1)
l1=Label(window,text="TrainID",font="helvetica 12 bold",foreground="red")
l1.grid(row=2,column=0)
trainid_text=StringVar()

e1=Entry(window,textvariable=trainid_text)
e1.grid(row=2,column=1)

l2=Label(window,text="TrainName",font="helvetica 13")
l2.grid(row=2,column=3)
list1=Listbox(window,height=1,width=20)
list1.grid(row=2,column=4)


l3=Label(window,text="Source",font="helvetica 14")
l3.grid(row=6,column=0)
l4=Label(window,text="StationID",font="helvetica 13")
l4.grid(row=7,column=0)
list11=Listbox(window,height=1,width=20)
list11.grid(row=7,column=1)
l5=Label(window,text="Station Name",font="helvetica 13")
l5.grid(row=8,column=0)
list12=Listbox(window,height=1,width=20)
list12.grid(row=8,column=1)
l6=Label(window,text="Time",font="helvetica 13")
l6.grid(row=9,column=0)
l7=Label(window,text="Dep.",font="helvetica 13")
l7.grid(row=10,column=0)
list13=Listbox(window,height=1,width=20)
list13.grid(row=10,column=1)





l8=Label(window,text="Stop 1",font="helvetica 14")
l8.grid(row=6,column=2,columnspan=4)
l9=Label(window,text="StationID",font="helvetica 13")
l9.grid(row=7,column=2)
list14=Listbox(window,height=1,width=20)
list14.grid(row=7,column=3)
l10=Label(window,text="Station Name",font="helvetica 13")
l10.grid(row=8,column=2)
list15=Listbox(window,height=1,width=20)
list15.grid(row=8,column=3)
l11=Label(window,text="Time",font="helvetica 13")
l11.grid(row=9,column=2)
l12=Label(window,text="Arr.",font="helvetica 13")
l12.grid(row=10,column=2)
list16=Listbox(window,height=1,width=20)
list16.grid(row=10,column=3)
l13=Label(window,text="Dep.",font="helvetica 13")
l13.grid(row=11,column=2)
list17=Listbox(window,height=1,width=20)
list17.grid(row=11,column=3)









l14=Label(window,text="Stop 2",font="helvetica 14")
l14.grid(row=6,column=6,columnspan=4)
l15=Label(window,text="StationID",font="helvetica 13")
l15.grid(row=7,column=6)
list18=Listbox(window,height=1,width=20)
list18.grid(row=7,column=7)
l16=Label(window,text="Station Name",font="helvetica 13")
l16.grid(row=8,column=6)
list19=Listbox(window,height=1,width=20)
list19.grid(row=8,column=7)
l17=Label(window,text="Time",font="helvetica 13")
l17.grid(row=9,column=6)
l18=Label(window,text="Arr.",font="helvetica 13")
l18.grid(row=10,column=6)
list20=Listbox(window,height=1,width=20)
list20.grid(row=10,column=7)
l19=Label(window,text="Dep.",font="helvetica 13")
l19.grid(row=11,column=6)
list21=Listbox(window,height=1,width=20)
list21.grid(row=11,column=7)


l20=Label(window,text="Stop 3",font="helvetica 14")
l20.grid(row=6,column=11,columnspan=4)
l21=Label(window,text="StationID",font="helvetica 13")
l21.grid(row=7,column=11)
list22=Listbox(window,height=1,width=20)
list22.grid(row=7,column=12)
l22=Label(window,text="Station Name",font="helvetica 13")
l22.grid(row=8,column=11)
list23=Listbox(window,height=1,width=20)
list23.grid(row=8,column=12)
l23=Label(window,text="Time",font="helvetica 13")
l23.grid(row=9,column=11)
l24=Label(window,text="Arr.",font="helvetica 13")
l24.grid(row=10,column=11)
list24=Listbox(window,height=1,width=20)
list24.grid(row=10,column=12)
l25=Label(window,text="Dep.",font="helvetica 13")
l25.grid(row=11,column=11)
list25=Listbox(window,height=1,width=20)
list25.grid(row=11,column=12)




l26=Label(window,text="Destination",font="helvetica 14")
l26.grid(row=6,column=15)
l27=Label(window,text="StationID",font="helvetica 13")
l27.grid(row=7,column=15)
list26=Listbox(window,height=1,width=20)
list26.grid(row=7,column=16)
l28=Label(window,text="Station Name",font="helvetica 13")
l28.grid(row=8,column=15)
list27=Listbox(window,height=1,width=20)
list27.grid(row=8,column=16)
l29=Label(window,text="Time",font="helvetica 13")
l29.grid(row=9,column=15)
l30=Label(window,text="Arr.",font="helvetica 13")
l30.grid(row=10,column=15)
list28=Listbox(window,height=1,width=20)
list28.grid(row=10,column=16)





l31=Label(window,text="Class 1",font="helvetica 14")
l31.grid(row=13,column=0)
l32=Label(window,text="No. of carriages",font="helvetica 13")
l32.grid(row=14,column=0)
list2=Listbox(window,height=1,width=20)
list2.grid(row=14,column=1)
l33=Label(window,text="Capacity",font="helvetica 13")
l33.grid(row=15,column=0)
cap1_text=StringVar()
list3=Listbox(window,height=1,width=20)
list3.grid(row=15,column=1)

l34=Label(window,text="Price",font="helvetica 13")
l34.grid(row=16,column=0)
price1_text=StringVar()
list4=Listbox(window,height=1,width=20)
list4.grid(row=16,column=1)





l35=Label(window,text="Class 2",font="helvetica 14")
l35.grid(row=13,column=6)
l36=Label(window,text="No. of carriages",font="helvetica 13")
l36.grid(row=14,column=6)
list5=Listbox(window,height=1,width=20)
list5.grid(row=14,column=7)
l37=Label(window,text="Capacity",font="helvetica 13")
l37.grid(row=15,column=6)
list6=Listbox(window,height=1,width=20)
list6.grid(row=15,column=7)

l38=Label(window,text="Price",font="helvetica 13")
l38.grid(row=16,column=6)
list7=Listbox(window,height=1,width=20)
list7.grid(row=16,column=7)






l39=Label(window,text="Class 3",font="helvetica 14")
l39.grid(row=13,column=15)
l40=Label(window,text="No. of carriages",font="helvetica 13")
l40.grid(row=14,column=15)
list8=Listbox(window,height=1,width=20)
list8.grid(row=14,column=16)
l41=Label(window,text="Capacity",font="helvetica 13")
l41.grid(row=15,column=15)
list9=Listbox(window,height=1,width=20)
list9.grid(row=15,column=16)

l42=Label(window,text="Price",font="helvetica 13")
l42.grid(row=16,column=15)
list10=Listbox(window,height=1,width=20)
list10.grid(row=16,column=16)




b1=Button(window,text="Status",command=Status,relief=FLAT,font="helvetica 13 bold",foreground="red2")
b1.grid(row=17,column=16)






window.mainloop()
