import tkinter as tk
from tkinter import *
from tkinter import ttk
import datetime
import sqlite3

#Creating the initial frame
LARGE_FONT = ("Verdana", 15)
class SimeonAuctions(tk.Tk):
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, *kwargs)
        container = tk.Frame(self)
        container.pack(side="left", fill="both", expand=1)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        #This is telling the program all of the classes that i want to be run when buttons are clicked
        for F in (MainMenu, CustomerReg, ItemRegistration, Orders, SearchStock, Stock):

            frame= F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky=NSEW)

        self.show_frame(MainMenu)

    def show_frame(self, cont):

        frame= self.frames[cont]
        frame.tkraise()
        
#Creating the main menu that allows the user to click a button and go to another page
class MainMenu(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Main Menu", font = LARGE_FONT)
        label.pack(side=TOP)

        #creating the buttons that allow me to travel to other pages
        button1 = tk.Button(self, text = "Customer registration",
                            command= lambda: controller.show_frame(CustomerReg), bg = "#00FF00")
        button1.config(height = 2, width = 20)
        button1.pack(side=TOP)

        lbBlank = Label(self, text = "", width = 30, font=("bold",10))
        lbBlank.pack()

        button2 = tk.Button(self, text = "Orders",
                            command= lambda: controller.show_frame(Orders), bg = "#00FF00")
        button2.config(height = 2, width = 20)
        button2.pack(side=TOP)
        

        lbBlank = Label(self, text = "", width = 30, font=("bold",10))
        lbBlank.pack()

        button3 = tk.Button(self, text = "Item Registration",
                            command= lambda: controller.show_frame(ItemRegistration), bg = "#00FF00")
        button3.config(height = 2, width = 20)
        button3.pack(side=TOP)

        lbBlank = Label(self, text = "", width = 30, font=("bold",10))
        lbBlank.pack()

        button4 = tk.Button(self, text = "Check our stock",
                            command= lambda: controller.show_frame(SearchStock), bg = "#00FF00")
        button4.config(height = 2, width = 20)
        button4.pack(side=TOP)

    
class CustomerReg(tk.Frame):
    

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Customer registration", font = LARGE_FONT)
        label.pack()


        FirstName = StringVar()
        LastName = StringVar()
        Address = StringVar()
        Email = StringVar()
        Number = StringVar()
        

        def database():
            firstname= FirstName.get()
            lastname = LastName.get()
            address = Address.get()
            email = Email.get()
            number = Number.get()
            
            conn = sqlite3.connect('Data2.db')
            with conn:
                cursor=conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS CustomersData(FirstName text, LastName text, Email text, Number text, Address text)')
            cursor.execute('INSERT INTO CustomersData(FirstName,LastName,Email,number,Address) VALUES(?,?,?,?,?)',(firstname,lastname,email,number, address))
            conn.commit()

        button1 = tk.Button(self, text = "Main Menu",
                        command= lambda: controller.show_frame(MainMenu))
        button1.pack()
            
        lb = Label(self, text = "Please insert your details", width = 30, font=("bold",12))
        lb.pack()

        lbFirstName = Label(self, text="First name", width = 30, font=('bold',10))
        lbFirstName.pack()

        txtFirstName = Entry(self, textvar=FirstName)
        txtFirstName.pack()

        lbLastName = Label(self, text="Last name", width = 30, font=('bold',10))
        lbLastName.pack()

        txtLastName = Entry(self, textvar=LastName)
        txtLastName.pack()

        lbEmail = Label(self, text = "Email", width = 30, font=("bold",10))
        lbEmail.pack()

        txtEmail = Entry(self, textvar=Email)
        txtEmail.pack()

        txtNumber = ""
        lbNumber = Label(self, text = "Phone number", width = 30, font=("bold",10))
        lbNumber.pack()

        txtNumber = Entry(self, textvar=Number)
        txtNumber.pack()

        lbAddress = Label(self, text="Address", width = 30, font=('bold',10))
        lbAddress.pack()

        txtAddress = Entry(self, textvar=Address)
        txtAddress.pack()


        lbBlank = Label(self, text = "", width = 30, font=("bold",10))
        lbBlank.pack()

        def DeleteForm():
            txtFirstName.delete('0', END)
            txtFirstName.insert(INSERT, txtFirstName.get())
            txtLastName.delete('0', END)
            txtLastName.insert(INSERT, txtLastName.get())
            txtEmail.delete('0', END)
            txtEmail.insert(INSERT, txtEmail.get())
            txtAddress.delete('0', END)
            txtAddress.insert(INSERT, txtAddress.get())
            txtNumber.delete('0', END)
            txtNumber.insert(INSERT, txtNumber.get())

        DeleteForm()
        
        Button(self, text = "Submit", width = 30,bg ='red', fg='white', command = database).pack()
        Button(self, text = "Clear form", width = 15,bg ='#FFFF00', fg='black', command = DeleteForm).pack()



class Orders(tk.Frame):
    

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Orders", font = LARGE_FONT)
        label.pack()

        button1 = tk.Button(self, text = "Main Menu",
                        command= lambda: controller.show_frame(MainMenu))
        button1.pack()

        #Order form
        

        #self = Tk()
        #self.geometry('400x400')
        #self.title("Registration form")

        ItemID = IntVar()
        CustomerID = IntVar()
        Price = IntVar()
        Registration = StringVar()


        def database():
            itemid= ItemID.get()
            customerid = CustomerID.get()
            price = Price.get()
            registration = Registration.get()
            conn = sqlite3.connect('Data2.db')
            with conn:
                cursor=conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS Orders (ItemID int, CustomerID int, Price int, Registration text)')
            cursor.execute('INSERT INTO Orders (ItemID,CustomerID,Price,Registration) VALUES(?,?,?,?)',(itemid,customerid,price,registration))
            conn.commit()
            

        lbItemID = Label(self, text="ItemID", width = 30, font=('bold',10))
        lbItemID.pack()

        txtItemID = Entry(self, textvar=ItemID)
        txtItemID.pack()

        lbCustomerID= Label(self, text="CustomerID", width = 30, font=('bold',10))
        lbCustomerID.pack()

        txtCustomerID = Entry(self, textvar=CustomerID)
        txtCustomerID.pack()

        lbPrice = Label(self, text="Price", width = 30, font=('bold',10))
        lbPrice.pack()

        txtPrice = Entry(self, textvar=Price)
        txtPrice.pack()

        lbRegistration = Label(self, text = "Registration", width = 30, font=("bold",10))
        lbRegistration.pack()

        txtRegistration = Entry(self, textvar=Registration)
        txtRegistration.pack()

        lbBlank = Label(self, text = "", width = 30, font=("bold",10))
        lbBlank.pack()

        def DeleteForm():
            txtPrice.delete('0', END)
            txtPrice.insert(INSERT, txtPrice.get())
            txtRegistration.delete('0', END)
            txtRegistration.insert(INSERT, txtRegistration.get())
            txtCustomerID.delete('0', END)
            txtCustomerID.insert(INSERT, txtCustomerID.get())
            txtItemID.delete('0', END)
            txtItemID.insert(INSERT, txtItemID.get())

        DeleteForm()

        Button(self, text = "Submit", width = 30,bg ='red', fg='white', command = database).pack()
        Button(self, text = "Clear form", width = 15,bg ='#FFFF00', fg='black', command = DeleteForm).pack()


class ItemRegistration(tk.Frame):
    

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Item registration", font = LARGE_FONT)
        label.pack()

        button1 = tk.Button(self, text = "Main Menu",
                        command= lambda: controller.show_frame(MainMenu))
        button1.pack()

        Colour = StringVar()
        TranSel = StringVar()
        ManuSel = StringVar()
        ModelSel = StringVar()
        CC = StringVar()
        Mileage = StringVar()
        DoorSel = StringVar()
        RegNum = StringVar()
        Year = StringVar()

        def database():
            colour= Colour.get()
            transel = TranSel.get()
            manusel = ManuSel.get()
            modelsel = ModelSel.get()
            cc = CC.get()
            mileage = Mileage.get()
            doorsel = DoorSel.get()
            regnum = RegNum.get()
            year = Year.get()

            conn = sqlite3.connect('Data2.db')
            with conn:
                cursor=conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS Stocklist4 (Colour text, Manusel text, ModelSel text, TranSel text, CC text,Mileage text, DoorSel text,RegNum text,Year text)')
            cursor.execute('INSERT INTO Stocklist4 (Colour,ManuSel,TranSel,ModelSel,CC,Mileage,DoorSel,RegNum,Year) VALUES(?,?,?,?,?,?,?,?)',(colour,manusel,modelsel,transel,cc,mileage,doorsel,regnum,year))
            conn.commit()
            
        lbColour = Label(self, text="Colour", width = 30, font=('bold',10))
        lbColour.pack()

        txtColour = Entry(self, textvar=Colour)
        txtColour.pack()

        lbTransmission = Label(self, text = "Transmission", width = 30, font=("bold",10))
        lbTransmission.pack()


        TranList = ["Automatic", "Manual"]
        droplist = OptionMenu(self, TranSel, *TranList)
        droplist.config(width = 15)
        TranSel.set('Select')
        droplist.pack()

        lbManufacturer  = Label(self, text = "Manufacturer", width = 30, font=("bold",10))
        lbManufacturer.pack()
        ManuList = ["Abarth", "Alfa Romeo", "Alpine", "Aston Martin", "Audi", "Austin", "Bentley", "BMW", "Chevrolet", "Citreon", "Corvette", "Dacia", "Daf", "Daihatsu", "Dodge", "DS", "Ferrari", "Fiat", "Ford", "Great Wall", "Honda", "Hyundai", "Infiniti", "Isuzu", "Jaguar", "Jeep", "Kia", "Lamborghini", "Land Rover", "LDV", "Lexus", "Lotus", "Maserati", "Mazda", "Mercedes", "MG", "MINI", "Mitsubishi", "Morris", "Nissan", "Peugeot", "Porsche", "Proton", "Renault", "Rover", "SAAB", "Seat", "Skoda", "Smart", "SsangYong", "Subaru", "TESLA", "Toyota", "TVR", "Vauxhall", "Volkswagen", "Volvo"]

        droplist = OptionMenu(self, ManuSel, *ManuList)
        droplist.config(width = 15)
        ManuSel.set('Select')
        droplist.pack()

        lbModel = Label(self, text = "Model", width = 30, font=("bold",10))
        lbModel.pack()
        ModelList = ["Focus","Fiesta","Citigo"]
        
        droplist = OptionMenu(self, ModelSel, *ModelList)
        droplist.config(width = 15)
        ModelSel.set('Select')
        droplist.pack()

        lbCC= Label(self, text="CC", width = 30, font=('bold',10))
        lbCC.pack()

        txtCC= Entry(self, textvar=CC)
        txtCC.pack()

        lbMileage= Label(self, text="Mileage", width = 30, font=('bold',10))
        lbMileage.pack()

        txtMileage= Entry(self, textvar=Mileage)
        txtMileage.pack()

        lbDoors  = Label(self, text = "Doors", width = 30, font=("bold",10))
        lbDoors.pack()
        DoorList = ["3", "5"]

        droplist = OptionMenu(self, DoorSel, *DoorList)
        droplist.config(width = 15)
        DoorSel.set('Select')
        droplist.pack()

        lbRegNum= Label(self, text="Reg number", width = 30, font=('bold',10))
        lbRegNum.pack()

        txtRegNum= Entry(self, textvar=RegNum)
        txtRegNum.pack()

        lbYear= Label(self, text="Year", width = 30, font=('bold',10))
        lbYear.pack()

        txtYear= Entry(self, textvar=Year)
        txtYear.pack()

        lbBlank= Label(self, text="", width = 30, font=('bold',10))
        lbBlank.pack()

        def DeleteForm():
            txtColour.delete('0', END)
            txtColour.insert(INSERT, txtColour.get())
            txtCC.delete('0', END)
            txtCC.insert(INSERT, txtCC.get())
            txtMileage.delete('0', END)
            txtMileage.insert(INSERT, txtMileage.get())
            txtRegNum.delete('0', END)
            txtRegNum.insert(INSERT, txtRegNum.get())
            txtYear.delete('0', END)
            txtYear.insert(INSERT, txtYear.get())
            TranSel.set("Select")
            DoorSel.set("Select")
            ManuSel.set("Select")
            ModelSel.set("Select")
        


        Button(self, text = "Submit", width = 30,bg ='red', fg='white', command=lambda:[database(),DeleteForm()]).pack()
        lbBlank = Label(self, text = "", width = 30, font=("bold",10))
        lbBlank.pack()

class Stock(tk.Frame):
    

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text = "Current stock", font = LARGE_FONT)
        label.pack()

        button1 = tk.Button(self, text = "Main Menu",
                        command= lambda: controller.show_frame(MainMenu))
        button1.pack()

        FilterSel = StringVar()
        def FilterStock():
            
            filtersel = FilterSel.get()
            lbFilters  = Label(self, text = "Filters", width = 30, font=("bold",10))
            
            FilterList = ["Manual", "Automatic","Year","Manufacturer","Model","Doors(5)","Doors(3)","Mileage","CC","Colour"]
            droplist = OptionMenu(self, FilterSel, *FilterList)
            droplist.config(width = 15)
            lbFilters.pack()
            droplist.pack()
            FilterSel.set('Select')
            
            print(filtersel)
            if filtersel == "Doors(3)":
                
                con = sqlite3.connect('Data2.db')
                cur = con.cursor()
                cur.execute('SELECT * from Stocklist4 WHERE DoorSel = "3" ')
                result2d = (cur.fetchall())  
                

                RecordNumQuery = "SELECT COUNT(*) FROM Stocklist4"
                cur.execute(RecordNumQuery)
                RecordNumTup = cur.fetchall()
                print(RecordNumTup)
                RecordNum = RecordNumTup[0][0]

                ListColour = Listbox(self)
                ListColour.pack(side = LEFT)
                ListManufacturer = Listbox(self)
                ListManufacturer.pack(side = LEFT)
                ListTrans = Listbox(self)
                ListTrans.pack(side = LEFT)
                ListCC = Listbox(self)
                ListCC.pack(side = LEFT)
                ListMiles = Listbox(self)
                ListMiles.pack(side = LEFT)
                ListDoors = Listbox(self)
                ListDoors.pack(side = LEFT)
                ListReg = Listbox(self)
                ListReg.pack(side = LEFT)
                ListYear = Listbox(self)
                ListYear.pack(side = LEFT)
                
                for i in range(0, RecordNum):
                    colorCar = result2d[i][0]
                    manufacturerCar = result2d[i][1]
                    transCar = result2d[i][2]
                    ccCar = result2d[i][3]
                    milageCar = result2d[i][4]
                    doorsCar = result2d[i][5]
                    print(doorsCar)
                    regCar = result2d[i][6]
                    yearCar = result2d[i][7]
                    ListColour.insert(0, colorCar), ListManufacturer.insert(0, manufacturerCar), ListTrans.insert(0, transCar), ListCC.insert(0, ccCar), ListMiles.insert(0, milageCar), ListDoors.insert(0, doorsCar), ListReg.insert(0, regCar), ListYear.insert(0, yearCar)
                    

            if filtersel == "Doors(5)":
                con = sqlite3.connect('Data2.db')
                cur = con.cursor()
                cur.execute('SELECT * from Stocklist4 WHERE DoorSel = "5" ')
                result2d = (cur.fetchall())  
                

                RecordNumQuery = "SELECT COUNT(*) FROM Stocklist4"
                cur.execute(RecordNumQuery)
                RecordNumTup = cur.fetchall()
                print(RecordNumTup)
                RecordNum = RecordNumTup[0][0]

                ListColour = Listbox(self)
                ListColour.pack(side = LEFT)
                ListManufacturer = Listbox(self)
                ListManufacturer.pack(side = LEFT)
                ListTrans = Listbox(self)
                ListTrans.pack(side = LEFT)
                ListCC = Listbox(self)
                ListCC.pack(side = LEFT)
                ListMiles = Listbox(self)
                ListMiles.pack(side = LEFT)
                ListDoors = Listbox(self)
                ListDoors.pack(side = LEFT)
                ListReg = Listbox(self)
                ListReg.pack(side = LEFT)
                ListYear = Listbox(self)
                ListYear.pack(side = LEFT)
                
                for i in range(0, RecordNum):
                    colorCar = result2d[i][0]
                    manufacturerCar = result2d[i][1]
                    transCar = result2d[i][2]
                    ccCar = result2d[i][3]
                    milageCar = result2d[i][4]
                    doorsCar = result2d[i][5]
                    print(doorsCar)
                    regCar = result2d[i][6]
                    yearCar = result2d[i][7]
                    ListColour.insert(0, colorCar), ListManufacturer.insert(0, manufacturerCar), ListTrans.insert(0, transCar), ListCC.insert(0, ccCar), ListMiles.insert(0, milageCar), ListDoors.insert(0, doorsCar), ListReg.insert(0, regCar), ListYear.insert(0, yearCar)
            
            if filtersel == "Manual":
                con = sqlite3.connect('Data2.db')
                cur = con.cursor()
                cur.execute('SELECT * from Stocklist4 WHERE TranSel = "Manual" ')
                result2d = (cur.fetchall())  
                

                RecordNumQuery = "SELECT COUNT(*) FROM Stocklist4"
                cur.execute(RecordNumQuery)
                RecordNumTup = cur.fetchall()
                print(RecordNumTup)
                RecordNum = RecordNumTup[0][0]

                ListColour = Listbox(self)
                ListColour.pack(side = LEFT)
                ListManufacturer = Listbox(self)
                ListManufacturer.pack(side = LEFT)
                ListTrans = Listbox(self)
                ListTrans.pack(side = LEFT)
                ListCC = Listbox(self)
                ListCC.pack(side = LEFT)
                ListMiles = Listbox(self)
                ListMiles.pack(side = LEFT)
                ListDoors = Listbox(self)
                ListDoors.pack(side = LEFT)
                ListReg = Listbox(self)
                ListReg.pack(side = LEFT)
                ListYear = Listbox(self)
                ListYear.pack(side = LEFT)
                
                for i in range(0, RecordNum):
                    colorCar = result2d[i][0]
                    manufacturerCar = result2d[i][1]
                    transCar = result2d[i][2]
                    ccCar = result2d[i][3]
                    milageCar = result2d[i][4]
                    doorsCar = result2d[i][5]
                    print(doorsCar)
                    regCar = result2d[i][6]
                    yearCar = result2d[i][7]
                    ListColour.insert(0, colorCar), ListManufacturer.insert(0, manufacturerCar), ListTrans.insert(0, transCar), ListCC.insert(0, ccCar), ListMiles.insert(0, milageCar), ListDoors.insert(0, doorsCar), ListReg.insert(0, regCar), ListYear.insert(0, yearCar)
            
            if filtersel == "Automatic":
                con = sqlite3.connect('Data2.db')
                cur = con.cursor()
                cur.execute('SELECT * from Stocklist4 WHERE TranSel = "Automatic" ')
                result2d = (cur.fetchall())  
                

                RecordNumQuery = "SELECT COUNT(*) FROM Stocklist4"
                cur.execute(RecordNumQuery)
                RecordNumTup = cur.fetchall()
                print(RecordNumTup)
                RecordNum = RecordNumTup[0][0]

                ListColour = Listbox(self)
                ListColour.pack(side = LEFT)
                ListManufacturer = Listbox(self)
                ListManufacturer.pack(side = LEFT)
                ListTrans = Listbox(self)
                ListTrans.pack(side = LEFT)
                ListCC = Listbox(self)
                ListCC.pack(side = LEFT)
                ListMiles = Listbox(self)
                ListMiles.pack(side = LEFT)
                ListDoors = Listbox(self)
                ListDoors.pack(side = LEFT)
                ListReg = Listbox(self)
                ListReg.pack(side = LEFT)
                ListYear = Listbox(self)
                ListYear.pack(side = LEFT)
                
                for i in range(0, RecordNum):
                    colorCar = result2d[i][0]
                    manufacturerCar = result2d[i][1]
                    transCar = result2d[i][2]
                    ccCar = result2d[i][3]
                    milageCar = result2d[i][4]
                    doorsCar = result2d[i][5]
                    print(doorsCar)
                    regCar = result2d[i][6]
                    yearCar = result2d[i][7]
                    ListColour.insert(0, colorCar), ListManufacturer.insert(0, manufacturerCar), ListTrans.insert(0, transCar), ListCC.insert(0, ccCar), ListMiles.insert(0, milageCar), ListDoors.insert(0, doorsCar), ListReg.insert(0, regCar), ListYear.insert(0, yearCar)
            
            if filtersel == "Year":
                con = sqlite3.connect('Data2.db')
                cur = con.cursor()
                cur.execute('SELECT * from Stocklist4 ORDER BY Year ASC ')
                result2d = (cur.fetchall())  
                

                RecordNumQuery = "SELECT COUNT(*) FROM Stocklist4"
                cur.execute(RecordNumQuery)
                RecordNumTup = cur.fetchall()
                print(RecordNumTup)
                RecordNum = RecordNumTup[0][0]

                ListColour = Listbox(self)
                ListColour.pack(side = LEFT)
                ListManufacturer = Listbox(self)
                ListManufacturer.pack(side = LEFT)
                ListTrans = Listbox(self)
                ListTrans.pack(side = LEFT)
                ListCC = Listbox(self)
                ListCC.pack(side = LEFT)
                ListMiles = Listbox(self)
                ListMiles.pack(side = LEFT)
                ListDoors = Listbox(self)
                ListDoors.pack(side = LEFT)
                ListReg = Listbox(self)
                ListReg.pack(side = LEFT)
                ListYear = Listbox(self)
                ListYear.pack(side = LEFT)
                
                for i in range(0, RecordNum):
                    colorCar = result2d[i][0]
                    manufacturerCar = result2d[i][1]
                    transCar = result2d[i][2]
                    ccCar = result2d[i][3]
                    milageCar = result2d[i][4]
                    doorsCar = result2d[i][5]
                    print(doorsCar)
                    regCar = result2d[i][6]
                    yearCar = result2d[i][7]
                    ListColour.insert(0, colorCar), ListManufacturer.insert(0, manufacturerCar), ListTrans.insert(0, transCar), ListCC.insert(0, ccCar), ListMiles.insert(0, milageCar), ListDoors.insert(0, doorsCar), ListReg.insert(0, regCar), ListYear.insert(0, yearCar)
            
            if filtersel == "Manufacturer":
                con = sqlite3.connect('Data2.db')
                cur = con.cursor()
                cur.execute('SELECT * from Stocklist4 WHERE Manufacturer = "" ')
                result2d = (cur.fetchall())  
                

                RecordNumQuery = "SELECT COUNT(*) FROM Stocklist4"
                cur.execute(RecordNumQuery)
                RecordNumTup = cur.fetchall()
                print(RecordNumTup)
                RecordNum = RecordNumTup[0][0]

                ListColour = Listbox(self)
                ListColour.pack(side = LEFT)
                ListManufacturer = Listbox(self)
                ListManufacturer.pack(side = LEFT)
                ListTrans = Listbox(self)
                ListTrans.pack(side = LEFT)
                ListCC = Listbox(self)
                ListCC.pack(side = LEFT)
                ListMiles = Listbox(self)
                ListMiles.pack(side = LEFT)
                ListDoors = Listbox(self)
                ListDoors.pack(side = LEFT)
                ListReg = Listbox(self)
                ListReg.pack(side = LEFT)
                ListYear = Listbox(self)
                ListYear.pack(side = LEFT)
                
                for i in range(0, RecordNum):
                    colorCar = result2d[i][0]
                    manufacturerCar = result2d[i][1]
                    transCar = result2d[i][2]
                    ccCar = result2d[i][3]
                    milageCar = result2d[i][4]
                    doorsCar = result2d[i][5]
                    print(doorsCar)
                    regCar = result2d[i][6]
                    yearCar = result2d[i][7]
                    ListColour.insert(0, colorCar), ListManufacturer.insert(0, manufacturerCar), ListTrans.insert(0, transCar), ListCC.insert(0, ccCar), ListMiles.insert(0, milageCar), ListDoors.insert(0, doorsCar), ListReg.insert(0, regCar), ListYear.insert(0, yearCar)
            

        def CurrentStock():
            con = sqlite3.connect('Data2.db')
            cur = con.cursor()
            cur.execute('SELECT * from Stocklist4')
            result2d = (cur.fetchall())  
            print(result2d)         
           
            
            #for i in range(0,len(result2d)):
                #exec('Label%d=Label(text="%s")\nLabel%d.pack()' % (i,result2d[i],i))
        
            RecordNumQuery = "SELECT COUNT(*) FROM Stocklist4"
            cur.execute(RecordNumQuery)
            RecordNumTup = cur.fetchall()
            print(RecordNumTup)
            RecordNum = RecordNumTup[0][0]

            
            ListColour = Listbox(self)
            ListColour.pack(side = LEFT)
            ListManufacturer = Listbox(self)
            ListManufacturer.pack(side = LEFT)
            ListTrans = Listbox(self)
            ListTrans.pack(side = LEFT)
            ListCC = Listbox(self)
            ListCC.pack(side = LEFT)
            ListMiles = Listbox(self)
            ListMiles.pack(side = LEFT)
            ListDoors = Listbox(self)
            ListDoors.pack(side = LEFT)
            ListReg = Listbox(self)
            ListReg.pack(side = LEFT)
            ListYear = Listbox(self)
            ListYear.pack(side = LEFT)
            
            for i in range(0, RecordNum):
                colorCar = result2d[i][0]
                manufacturerCar = result2d[i][1]
                transCar = result2d[i][2]
                ccCar = result2d[i][3]
                milageCar = result2d[i][4]
                doorsCar = result2d[i][5]
                print(doorsCar)
                regCar = result2d[i][6]
                yearCar = result2d[i][7]
                ListColour.insert(0, colorCar), ListManufacturer.insert(0, manufacturerCar), ListTrans.insert(0, transCar), ListCC.insert(0, ccCar), ListMiles.insert(0, milageCar), ListDoors.insert(0, doorsCar), ListReg.insert(0, regCar), ListYear.insert(0, yearCar)
                
        def deleteFrame():
            for widget in self.winfo_children():
                widget.destroy()
            label1 = tk.Label(self, text = "Current stock", font = LARGE_FONT)
            label1.pack()

            button2 = tk.Button(self, text = "Main Menu",
                    command= lambda: controller.show_frame(MainMenu))
            button2.pack()
            Button(self, text = "Refresh", width = 30,bg ='red', fg='white',  command= lambda:[deleteFrame(),FilterStock(), CurrentStock()]).pack()
        


        Button(self, text = "Refresh", width = 30,bg ='red', fg='white',  command= lambda:[deleteFrame(),CurrentStock(), FilterStock()]).pack()

    

class SearchStock(tk.Frame):
    

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Search Stock", font = LARGE_FONT)
        label.pack()

        button1 = tk.Button(self, text = "Main Menu",
                        command= lambda: controller.show_frame(MainMenu))
        button1.pack()
        
        label = tk.Label(self, text = "", font = LARGE_FONT)
        label.pack()

        button1 = tk.Button(self, text = "Current stock",
                        command= lambda: controller.show_frame(Stock))
        button1.pack()

app = SimeonAuctions()
app.mainloop()
