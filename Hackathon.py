from tkinter import *
import xlrd
from tkinter import ttk
import tkinter.font as tkFont
import re
from pathlib import Path

def raise_frame(frame):
    frame.tkraise()

file_location=r"nutrition data.xls"
workbook=xlrd.open_workbook(file_location)
sheet=workbook.sheet_by_index(0)
lista=[]
d={}
for i in range(1,sheet.nrows):
	lista.append(sheet.cell_value(i,0))
	l=[]
	l.append(sheet.cell_value(i,1))
	l.append(sheet.cell_value(i,3))
	l.append(sheet.cell_value(i,4)) 	
	d[sheet.cell_value(i,0)]=l

file_location1=r"recommendations.xls"
workbook1=xlrd.open_workbook(file_location1)
sheet1=workbook1.sheet_by_index(0)
lista1=[]
d1={}
for i in range(1,sheet1.nrows):
	lista1.append(sheet1.cell_value(i,0))
	l=[]
	l.append(sheet1.cell_value(i,1))
	#l.append(sheet1.cell_value(i,3))
	#l.append(sheet1.cell_value(i,4)) 	
	d1[sheet1.cell_value(i,0)]=l

#lista = ['a', 'actions', 'additional', 'also', 'an', 'and', 'angle', 'are', 'as', 'be', 'bind', 'bracket', 'brackets', 'button', 'can', 'cases', 'configure', 'course', 'detail', 'enter', 'event', 'events', 'example', 'field', 'fields', 'for', 'give', 'important', 'in', 'information', 'is', 'it', 'just', 'key', 'keyboard', 'kind', 'leave', 'left', 'like', 'manager', 'many', 'match', 'modifier', 'most', 'of', 'or', 'others', 'out', 'part', 'simplify', 'space', 'specifier', 'specifies', 'string;', 'that', 'the', 'there', 'to', 'type', 'unless', 'use', 'used', 'user', 'various', 'ways', 'we', 'window', 'wish', 'you']


class AutocompleteEntry(Entry):
    def __init__(self, lista, *args, **kwargs):
        
        Entry.__init__(self, *args, **kwargs)
        self.lista = lista        
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection)
        self.bind("<Up>", self.up)
        self.bind("<Down>", self.down)
        
        self.lb_up = False

    def changed(self, name, index, mode):  

        if self.var.get() == '':
        	self.lb.destroy()
        	self.lb_up = False
        else:
            words = self.comparison()
            if words:            
                if not self.lb_up:
                    self.lb = Listbox()
                    self.lb.bind("<Double-Button-1>", self.selection)
                    self.lb.bind("<Right>", self.selection)
                    self.lb.place(x=self.winfo_x(), y=self.winfo_y()+self.winfo_height())
                    self.lb_up = True
                
                self.lb.delete(0, END)
                for w in words:
                    self.lb.insert(END,w)
            else:
                if self.lb_up:
                    self.lb.destroy()
                    self.lb_up = False
        
    def selection(self, event):

        if self.lb_up:
            self.var.set(self.lb.get(ACTIVE))
            self.lb.destroy()
            self.lb_up = False
            self.icursor(END)

    def up(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != '0':                
                self.lb.selection_clear(first=index)
                index = str(int(index)-1)                
                self.lb.selection_set(first=index)
                self.lb.activate(index) 

    def down(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != END:                        
                self.lb.selection_clear(first=index)
                index = str(int(index)+1)        
                self.lb.selection_set(first=index)
                self.lb.activate(index) 

    def comparison(self):
        pattern = re.compile('.*' + self.var.get() + '.*')
        return [w for w in self.lista if re.match(pattern, w)]

#############################################################################################33

root = Tk()
root.configure(background='black')
root.title("Health App")
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
f1 = Frame(root,bg='#FFAFAF')
f2 = Frame(root,bg='#FFAFAF')
f3 = Frame(root,bg='#FFAFAF')
f4 = Frame(root, bg='#FFAFAF')
f5 = Frame(root, bg='#FFAFAF')



for frame in (f1, f2, f3, f4,f5):
    frame.grid(row=0, column=0, sticky='news')
text = PhotoImage(file=r'Health Text.png')
Label(f1,image=text,bg="#FFAFAF").pack(ipadx=0,ipady=20,expand=0,pady=1)
dwnd = PhotoImage(file=r'Rectangle 1.png')
Button(f1, image=dwnd, command=lambda:raise_frame(f2),bg="#FFAFAF",borderwidth=0).pack(ipadx=0,ipady=8,expand=0,pady=1)
dwnd1= PhotoImage(file=r'Rectangle 2.png')
Button(f1, image=dwnd1, command=lambda:raise_frame(f3),bg="#FFAFAF",borderwidth=0).pack(ipadx=0,ipady=8,expand=0,pady=1)
dwnd2=PhotoImage(file=r'Rectangle 3.png')
Button(f1, image=dwnd2, command=lambda:raise_frame(f4),bg="#FFAFAF",borderwidth=0).pack(ipadx=0,ipady=8,expand=0,pady=1)
dwnd3=PhotoImage(file=r'Rectangle 4.png')
Button(f1, image=dwnd3, command=lambda:raise_frame(f5),bg="#FFAFAF",borderwidth=0).pack(ipadx=0,ipady=8,expand=0,pady=1)
#Button(f1, text='FOOD INTAKE',font=tkFont.Font(family='Sans-serif', size=24), command=lambda:raise_frame(f2),bg='#FFFFFF',fg="#FFAFAF").pack(fill=BOTH,ipadx=0,ipady=15,expand=0,pady=10)
#Button(f1, text='BMI CHECK', command=lambda:raise_frame(f3),font=tkFont.Font(family='Sans-serif', size=24),bg='#FFFFFF',fg="#FFAFAF").pack(fill=BOTH,ipadx=0,ipady=15,expand=0,pady=10)
#Button(f1, text='REPORT ANALYZER', command=lambda:raise_frame(f4),font=tkFont.Font(family='Sans-serif', size=26), bg='#FFFFFF',fg="#FFAFAF").pack(fill=BOTH,ipadx=0,ipady=15,expand=0,pady=10)
#Button(f1, text='Recommendations', command=lambda:raise_frame(f5),font=tkFont.Font(family='Sans-serif', size=26), bg='#FFFFFF',fg="#FFAFAF").pack(fill=BOTH,ipadx=0,ipady=15,expand=0,pady=10)

############ f2
Label(f2, text = "How many servings did you eat today?",fg="#FFFFFF", bg="#FFAFAF",font=('Raleway',14, 'bold')).grid(row = 0, column = 0, padx = 60, pady = 10,sticky='e,w')
Label(f2, text = "(Maximum 2 at once)",fg="#FFFFFF", bg="#FFAFAF",font=('Raleway',14, 'bold')).grid(row = 1, column = 0, padx = 60, pady = 5,sticky='e,w')
Servings = Entry(f2, border=0, font=('Raleway',14, 'bold'), fg="#FFAFAF")
Servings.grid(row = 2, column = 0,sticky='e,w',padx=100,pady=10, ipady = 10)
Servings.insert(0, "")       
Button(f2, text = "Submit",command=lambda:serve(),bg='#FF8888',fg='white',activeforeground='#FF8888', font=('Raleway',14, 'bold'),border=0).grid(row=4,column=0,padx=50,pady=10)
Button(f2, text='Main Menu', command=lambda:raise_frame(f1),bg='white',fg='#FFAFAF',activeforeground='#FF8888', font=('Raleway',12, 'bold'),border=0).grid(row=5,column=0,padx=10)
Button(f3, text='Main Menu', command=lambda:raise_frame(f1),bg='white',fg='#FFAFAF',activeforeground='#FF8888', font=('Raleway',12, 'bold'),border=0).grid(row=5,column=3,pady=10, sticky="w")
Button(f4, text='Main Menu', command=lambda:raise_frame(f1),bg='white',fg='#FFAFAF',activeforeground='#FF8888', font=('Raleway',12, 'bold'),border=0).grid(row=13,column=0,padx=0,pady=10)
Button(f4, text = "Submit",command=lambda:norms(),bg='#FF8888',fg='white',activeforeground='#FF8888', font=('Raleway',14, 'bold'), border=0).grid(row=12,column=0,padx=0,pady=5)
Button(f5, text = "Submit",command=lambda:serve1(),bg='#FF8888',fg='white',activeforeground='#FF8888', font=('Raleway',14, 'bold'),border=0).grid(row=4,column=0,padx=0,pady=0)
Button(f5, text='Main Menu', command=lambda:raise_frame(f1),bg='white',fg='#FFAFAF',activeforeground='#FF8888', font=('Raleway',12, 'bold'),border=0).grid(row=4,column=0,padx=5,sticky='e')
def serve():

	serve = int(Servings.get())
	temp=1
	tserv=serve

	servelist=[]
	while serve>0:
		serve=serve-1
		Label(f2, text = "Food "+str(tserv-serve),font=tkFont.Font(family='Sans-serif',size=10), border = 0,fg="#FFFFFF", bg="#FFAFAF").grid(row = 5+temp, column = 0, pady = 10)
		Serving = AutocompleteEntry(lista, f2, border = 0, font=('Raleway',14, 'bold'), fg="#FFAFAF")
		Serving.grid(row = 6+temp, column = 0,padx=80, ipady = 10)
		Serving.insert(0, "")
		servelist.append(Serving)
		temp=temp+2
	Button(f2, text = "Enter",command=lambda:calcal(servelist,temp),bg='#FF8888',fg='white',activeforeground='#FF8888', font=('Raleway',14, 'bold'),border=0).grid(row=5+temp,column=0, pady = 10)	

def calcal(servelist,temp):

	kcal=0
	prot=0
	fat=0

	for i in servelist: 
		kcal=kcal+int(d[i.get()][0])

	for i in servelist: 
		prot=prot+int(d[i.get()][1])
		
	for i in servelist: 
		fat=fat+int(d[i.get()][2])		

	Label(f2, text = ("Kcal=",kcal, "Protein=",prot,'g',"Fats=",fat,'g'),fg="#FFFFFF", bg="#FFAFAF",font=('Raleway',12, 'bold')).grid(row = 6+temp, column = 0)

    #Commented Code
'''	Label(f2, text = ("Protein=",prot,'g'),fg="#FFFFFF", bg="#FFAFAF",font=('Raleway',12, 'bold')).grid(row = 7+temp, column = 0)
	Label(f2, text = ("Fats=",fat,'g'),fg="#FFFFFF", bg="#FFAFAF",font=('Raleway',12, 'bold')).grid(row = 8+temp, column = 0)'''


#Label(f2, text = "___________________________________________________________________________________",bg='#ff7580').grid(row = 5, column = 0)
############ f2

############ F3
Label(f3, text = "BMI Calculator",fg="#FFFFFF", bg="#FFAFAF",font=('Raleway',14, 'bold')).grid(row=0,columnspan = 6,padx=20,pady=10)

Label(f3, text = "Height (ft)",bg='#FFAFAF',font=("Raleway",10,'bold'), fg="white").grid(row = 1, column = 0,pady=10)
txtHeightFt = Entry(f3, border=0,font=("Inter",10,'bold'), width=8, fg="#FF8888")
txtHeightFt.grid(row = 1, column = 1, sticky="w", pady=5)
txtHeightFt.insert(0, "")

Label(f3, text = "  Height (in)",bg='#FFAFAF',font=("Raleway",10,'bold'), fg="white").grid(row = 1, column = 2,pady=10)
txtHeightIn = Entry(f3, width=8, border=0, fg="#FF8888",font=("Inter",10,'bold'))
txtHeightIn.grid(row = 1, column = 3, padx=10)
txtHeightIn.insert(0, "")

Label(f3, text = "Weight (kgs)",bg='#FFAFAF',font=("Raleway",10,'bold'), fg="white").grid(row = 2, column = 0,pady=10)
txtWeight = Entry(f3, border=0,font=("Inter",10,'bold'), width=8, fg="#FF8888")
txtWeight.grid(row = 2, column = 1, sticky="w")
txtWeight.insert(0, "")

Label(f3, text = "Your BMI:",bg='#FFAFAF',font=("Raleway",10,'bold'), fg="white").grid(row = 5, column = 0,padx=10,pady=10)
f3.lblBMI = Label(f3, bg = "#FFAFAF",relief = "groove", border=0,font=("Inter",10,'bold'), fg="white")
f3.lblBMI.grid(row = 5, column = 1, sticky = "we")
Label(f3,text="You are:",bg='#FFAFAF',font=("Raleway",10,'bold'), fg="white").grid(row = 2, column = 2,padx=10,pady=10)
f3.lblBMIStatus = Label(f3,bg='#FFFFFF',font=("Inter",10,'bold'), fg="#FF8888", border=0)
f3.lblBMIStatus.grid(row = 2, column = 3)

#Label(f3, text = "____________________________________________________________________________________",bg='#f73848').grid(row = 11, columnspan = 10)
Label(f3, text = " Suggestions:",bg='#FFAFAF', fg="white", font=('Raleway',12, 'bold')).grid(row = 15, columnspan = 6, sticky='w',padx=200,pady=10)
Label(f3, text = " Weight:",bg='#FFAFAF', fg="white",font=("Raleway",14,'bold')).grid(row = 17, columnspan = 1,sticky='w', pady=10, padx=20)
Label(f3, text = " Calories: ",bg='#FFAFAF', fg="white",font=("Raleway",14,'bold')).grid(row = 18, columnspan = 1,sticky='w', pady=10, padx=20)
Label(f3, text = " Protein: ",bg='#FFAFAF', fg="white",font=("Raleway",14,'bold')).grid(row = 19, columnspan = 1,sticky='w', pady=10, padx=20)
f3.SWeight=Label(f3,bg='#FFAFAF', fg='white',font=("Inter",11,'bold'))
f3.SWeight.grid(row = 17,column=1, columnspan = 3,sticky='w')
f3.SCalorie=Label(f3,bg='#FFAFAF', fg="white",font=("Inter",11,'bold'))
f3.SCalorie.grid(row = 18,column=1, columnspan = 3,sticky='w')
f3.SProtein=Label(f3,bg='#FFAFAF', fg="white",font=("Inter",11,'bold'))
f3.SProtein.grid(row = 19,column=1, columnspan = 3,sticky='w')

f3.btnCalc = Button(f3, text = "Calculate BMI",bg='#FF8888',fg='white',activeforeground='#FF8888',border=0,font=('Raleway',14, 'bold'),command=lambda:calcBMI())
f3.btnCalc.grid(row = 10, column = 1, sticky = "we", columnspan=2, pady=10)

def calcBMI():
    """calculate the BMI of a person using the formula"""
    #calculate BMI
    feet = int(txtHeightFt.get())
    inches = int(txtHeightIn.get())
    totalHeight = (12 * feet) + inches
    weight = float(txtWeight.get())
    #BMI needs to be a float, int * float is float
    bmi = weight * 703*2.20462 / (totalHeight * totalHeight)
    f3.lblBMI["text"] = "%.2f" % bmi


    #label for BMI status
    if bmi < 18.5:
    	f3.lblBMIStatus["text"] = "Underweight"
    	f3.SWeight["text"] = "Gain: 2 kg"
    	f3.SCalorie["text"] = "3000 Calories if MALE, 2500 if FEMALE"
    	f3.SProtein["text"] = str(int(weight*0.48)) + " grams per Kg"
    elif bmi < 24.9:
        f3.lblBMIStatus["text"] = "Normal"
        f3.SWeight["text"] = "Maintain"
        f3.SCalorie["text"] = "2500 Calories if MALE, 2000 if FEMALE"
        f3.SProtein["text"] = str(int(weight*0.38)) + " grams per Kg"
    elif bmi < 29.9:
        f3.lblBMIStatus["text"] = "Overweight"
        f3.SWeight["text"] = "Lose: 2 kg"
        f3.SCalorie["text"] = "2000 Calories if MALE, 1500 if FEMALE"
        f3.SProtein["text"] = str(int(weight*0.48)) + " grams per Kg"
    else:
        f3.lblBMIStatus["text"] = "Obese"
        f3.SWeight["text"] = "Lose: 4 kg"
        f3.SCalorie["text"] = "1600 Calories if MALE, 1200 if FEMALE"
        f3.SProtein["text"] = str(int(weight*0.48)) + " grams per Kg"
#f3.btnCalc["command"] = f3.calcBMI

############ F3

############ F4
Label(f4, text = "                  Triglycerides", bg='#FFAFAF',fg="#FFFFFF",font=("Arial",20, "bold")).grid(row = 0, column = 0, padx = 0, pady = 5,sticky="w")
Triglycerides = Entry(f4, border=0)
Triglycerides.grid(row = 2,sticky='e,w',column=0,padx=170,pady=8, ipady=5)
Triglycerides.insert(0, "")
Label(f4, text = "              Total Cholesterol", bg='#FFAFAF',fg="#FFFFFF",font=("Arial",20, "bold")).grid(row = 3, column = 0, padx = 0, pady = 5,sticky="w")
#Label(f4, text = "Total Cholesterol", bg='#add8e6',font=("Helvetica",16)).grid(row = 3,sticky='e,w',column=0,padx=0,pady=5)
Cholesterol = Entry(f4, border=0)
Cholesterol.grid(row = 5,sticky='e,w',column=0,padx=170,pady=8, ipady=5)
Cholesterol.insert(0, "")
Label(f4, text = "                  Haemoglobin", bg='#FFAFAF',fg="#FFFFFF",font=("Arial",20, "bold")).grid(row = 6, column = 0, padx = 0, pady = 5,sticky="w")
#Label(f4, text = "Hemoglobin", bg='#add8e6',font=("Helvetica",16)).grid(row = 5,sticky='e,w',column=0,padx=0,pady=5)
Hemoglobin = Entry(f4, border=0)
Hemoglobin.grid(row = 8,sticky='e,w',column=0,padx=170,pady=8, ipady=5)
Hemoglobin.insert(0, "")
#Label(f4, text = "            White blood cells (WBC)", bg='#add8e6',font=("Helvetica",16)).grid(row = 7,sticky='e,w',column=0,padx=0,pady=1)
#Label(f4, text = "\n_________________________________________________________________________________",bg='#e4717a').grid(row = 12,sticky='e,w',column=0,padx=1)
Label(f4, text = "          White blood cells (WBC) ", bg='#FFAFAF',fg="#FFFFFF",font=("Arial",20, "bold")).grid(row = 9, column = 0, padx = 0, pady = 5,sticky="w")
WBC = Entry(f4, border=0)
WBC.grid(row = 11,sticky='e,w',column=0,padx=170,pady=1, ipady=5)
WBC.insert(0, "")
#Button(f4, text = "Enter",command=lambda:norms(),bg='#add8e6').grid(row=8,column=8,padx=5,pady=0)

def norms():
    if int(Triglycerides.get()) < 50:
        Triglycerides.delete(0,END)
        Triglycerides.insert(0,'LOW')
  
    elif int(Triglycerides.get()) < 150:
        Triglycerides.delete(0,END)
        Triglycerides.insert(0,'NORMAL')
  
    elif int(Triglycerides.get()) > 150:
        Cholesterol.delete(0,END)
        Cholesterol.insert(0,'HIGH')

    if int(Cholesterol.get()) < 3:
        Cholesterol.delete(0,END)
        Cholesterol.insert(0,'LOW')
  
    elif int(Cholesterol.get()) < 5.5:
        Cholesterol.delete(0,END)
        Cholesterol.insert(0,'NORMAL')
  
    elif int(Cholesterol.get()) > 5.5:
        Cholesterol.delete(0,END)
        Cholesterol.insert(0,'HIGH')

    if int(Hemoglobin.get()) < 12:
        Hemoglobin.delete(0,END)
        Hemoglobin.insert(0,'LOW')
  
    elif int(Hemoglobin.get()) < 15:
        Hemoglobin.delete(0,END)
        Hemoglobin.insert(0,'NORMAL')
  
    elif int(Hemoglobin.get()) > 15:
        Hemoglobin.delete(0,END)
        Hemoglobin.insert(0,'HIGH')

    if int(WBC.get()) < 4:
        WBC.delete(0,END)
        WBC.insert(0,'LOW')
  
    elif int(WBC.get()) < 10:
        WBC.delete(0,END)
        WBC.insert(0,'NORMAL')
  
    elif int(WBC.get()) > 10:
        WBC.delete(0,END)
        WBC.insert(0,'HIGH')
############ F4

###########  F5
Label(f5, text = "Enter your age",fg="#FFFFFF", bg="#FFAFAF",font=('Raleway',14, 'bold')).grid(row = 0, column = 0, padx = 50, pady = 20,sticky='e,w')
Servings1 = Entry(f5, border=0, font=('Inter',14, 'bold'), fg="#FFAFAF")
Servings1.grid(row = 2, column = 0,sticky='e,w',padx=100,pady=10, ipady = 10)
Servings1.insert(0, "")
medicines={"cough":"vishal","cold":"Ujjwal"}

def serve1():
	serve1 = int(Servings1.get())
	serve1=1
	temp=1
	tserv=serve1

	servelist1=[]
	while serve1>0:
		serve1=serve1-1
		Label(f5, text = "Enter the problem ",font=('Raleway',14, 'bold'), border = 0,fg="#FFFFFF", bg="#FFAFAF").grid(row = 5+temp, column = 0, pady = 10)
		Serving1 = AutocompleteEntry(lista1,f5, border = 0, font=('Raleway',14, 'bold'), fg="#FFAFAF")
		Serving1.grid(row = 6+temp, column = 0,padx=80, ipady = 10)
		Serving1.insert(0, "")
		servelist1.append(Serving1)
		temp=temp+2
	Button(f5, text = "Enter",command=lambda:calcal1(servelist1,temp),bg='#FF8888',fg='white',activeforeground='#FF8888', font=('Raleway',14, 'bold'),border=0).grid(row=5+temp,column=0, pady = 10)	

def calcal1(servelist1,temp):
    ans=""
    for i in servelist1:
        ans=ans+(d1[i.get()][0])

    Label(f5, text = (ans),fg="#FFFFFF", bg="#FFAFAF",font=('Raleway',15, 'bold')).grid(row = 6+temp, column = 0)

raise_frame(f1)
root.maxsize(480,580)
icon = PhotoImage(file= r'favicon.png')
root.tk.call('wm','iconphoto',root._w,icon)
root.mainloop()
