from tkinter import *
import math,random,os
from tkinter import messagebox


class Bill_app:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1350x700+0+0')
        self.root.title('Billing Software')
        bg_color = "#074463"
        title = Label(self.root, text="Billing Software", bd=12, relief=GROOVE, bg=bg_color, fg='white',
                      font=("times new roman", 30, "bold"), pady=2).pack(fill=X)
        #-----------Variables--------------
        #---------Cosmetics---------
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.lotion=IntVar()
        # ---------Groceries---------
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()
        # ---------Cold Drinks---------
        self.pepsi = IntVar()
        self.fanta = IntVar()
        self.limca = IntVar()
        self.sting = IntVar()
        self.apple_sidra = IntVar()
        self.seven_up = IntVar()
        # ---------Total Prices and Tax Variables---------
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        #------Customer------
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.c_bill_no=StringVar()
        x=random.randint(1000,9999)
        self.c_bill_no.set(str(x))
        self.search_bill=StringVar()


        # ----------Customer Details Frame ------------
        F1 = LabelFrame(self.root,bd=10,relief=GROOVE, text="Customer Details", font=("times new roman", 15, "bold"), fg='gold',
                        bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name", font=("times new roman", 18, 'bold'), bg=bg_color, fg='white').grid(
            row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1,width=15, font="arial 15",bd=7,textvariable=self.c_name,relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Phone No", font=("times new roman", 18, 'bold'), bg=bg_color, fg='white').grid(
            row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, font="arial 15",textvariable=self.c_phone, bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number", font=("times new roman", 18, 'bold'), bg=bg_color, fg='white').grid(
            row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, font="arial 15", bd=7,textvariable=self.search_bill, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F1,text='Search',command=self.find_bill,width =10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=10)

        #--------Cosmetics Frame---------
        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmetics", font=("times new roman", 15, "bold"),
                        fg='gold',
                        bg=bg_color)
        F2.place(x=5, y=180, width=325,height=380)

        bath_lbl=Label(F2,text ='Bath Soap',font=('times new roman',15,'bold'),bg=bg_color,fg='lightgreen').grid(row=0,column=0,padx=10,pady=10,sticky='w')
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=('times new roman',15,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        face_cream_lbl = Label(F2, text='Face Cream', font=('times new roman', 15, 'bold'), bg=bg_color, fg='lightgreen').grid(
            row=1, column=0, padx=10, pady=10, sticky='w')
        face_cream_txt = Entry(F2, width=10,textvariable=self.face_cream, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=1, column=1,
                                                                                                       padx=10, pady=10)

        face_w_lbl = Label(F2, text='Face Wash', font=('times new roman', 15, 'bold'), bg=bg_color, fg='lightgreen').grid(
            row=2, column=0, padx=10, pady=10, sticky='w')
        face_w_txt = Entry(F2, width=10,textvariable=self.face_wash, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=2, column=1,
                                                                                                       padx=10, pady=10)

        hair_s_lbl = Label(F2, text='Hair Spray', font=('times new roman', 15, 'bold'), bg=bg_color, fg='lightgreen').grid(
            row=3, column=0, padx=10, pady=10, sticky='w')
        hair_s_txt = Entry(F2, width=10,textvariable=self.spray, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=3, column=1,
                                                                                                       padx=10, pady=10)
        hair_g_lbl = Label(F2, text='Hair Gel', font=('times new roman', 15, 'bold'), bg=bg_color, fg='lightgreen').grid(
            row=4, column=0, padx=10, pady=10, sticky='w')
        hair_g_txt = Entry(F2, width=10,textvariable=self.gell, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=4, column=1,
                                                                                                       padx=10, pady=10)
        body_l_lbl = Label(F2, text='Body Lotion', font=('times new roman', 15, 'bold'), bg=bg_color, fg='lightgreen').grid(
            row=5, column=0, padx=10, pady=10, sticky='w')
        body_l_txt = Entry(F2, width=10,textvariable=self.lotion, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=5, column=1,
                                                                                                       padx=10, pady=10)

        # --------Grocery Frame---------
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocery", font=("times new roman", 15, "bold"),
                        fg='gold',
                        bg=bg_color)
        F3.place(x=340, y=180, width=325, height=380)

        g1_lbl = Label(F3, text='Rice', font=('times new roman', 15, 'bold'), bg=bg_color, fg='lightgreen').grid(
            row=0, column=0, padx=10, pady=10, sticky='w')
        g1_txt = Entry(F3, width=10,textvariable=self.rice, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                       padx=10, pady=10)

        g2_lbl = Label(F3, text='Food Oil', font=('times new roman', 15, 'bold'), bg=bg_color,
                               fg='lightgreen').grid(
            row=1, column=0, padx=10, pady=10, sticky='w')
        g2_txt = Entry(F3, width=10,textvariable=self.food_oil, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=1,
                                                                                                             column=1,
                                                                                                             padx=10,
                                                                                                             pady=10)

        g3_lbl = Label(F3, text='Daal', font=('times new roman', 15, 'bold'), bg=bg_color,
                           fg='lightgreen').grid(
            row=2, column=0, padx=10, pady=10, sticky='w')
        g3_txt = Entry(F3, width=10,textvariable=self.daal, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=2,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)

        g4_lbl = Label(F3, text='Wheat', font=('times new roman', 15, 'bold'), bg=bg_color,
                           fg='lightgreen').grid(
            row=3, column=0, padx=10, pady=10, sticky='w')
        g4_txt = Entry(F3, width=10,textvariable=self.wheat, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=3,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)
        g5_lbl = Label(F3, text='Sugar', font=('times new roman', 15, 'bold'), bg=bg_color,
                           fg='lightgreen').grid(
            row=4, column=0, padx=10, pady=10, sticky='w')
        g5_txt = Entry(F3, width=10,textvariable=self.sugar, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=4,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)
        g6_lbl = Label(F3, text='Tea', font=('times new roman', 15, 'bold'), bg=bg_color,
                           fg='lightgreen').grid(
            row=5, column=0, padx=10, pady=10, sticky='w')
        g6_txt = Entry(F3, width=10,textvariable=self.tea, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=5,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)
        # --------Cold Drink Frame---------
        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cold Drinks", font=("times new roman", 15, "bold"),
                        fg='gold',
                        bg=bg_color)
        F4.place(x=670, y=180, width=325, height=380)

        cd1_lbl = Label(F4, text='Pepsi', font=('times new roman', 15, 'bold'), bg=bg_color, fg='lightgreen').grid(
            row=0, column=0, padx=10, pady=10, sticky='w')
        cd1_txt = Entry(F4, width=10,textvariable=self.pepsi, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                       padx=10, pady=10)

        cd2_lbl = Label(F4, text='Fanta', font=('times new roman', 15, 'bold'), bg=bg_color,
                               fg='lightgreen').grid(
            row=1, column=0, padx=10, pady=10, sticky='w')
        cd2_txt = Entry(F4, width=10,textvariable=self.fanta, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=1,
                                                                                                             column=1,
                                                                                                             padx=10,
                                                                                                             pady=10)

        cd3_lbl = Label(F4, text='Limca', font=('times new roman', 15, 'bold'), bg=bg_color,
                           fg='lightgreen').grid(
            row=2, column=0, padx=10, pady=10, sticky='w')
        cd3_txt = Entry(F4, width=10,textvariable=self.limca, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=2,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)

        cd4_lbl = Label(F4, text='Sting', font=('times new roman', 15, 'bold'), bg=bg_color,
                           fg='lightgreen').grid(
            row=3, column=0, padx=10, pady=10, sticky='w')
        cd4_txt = Entry(F4, width=10,textvariable=self.sting, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=3,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)
        cd5_lbl = Label(F4, text='Apple Sidra', font=('times new roman', 15, 'bold'), bg=bg_color,
                           fg='lightgreen').grid(
            row=4, column=0, padx=10, pady=10, sticky='w')
        cd5_txt = Entry(F4, width=10,textvariable=self.apple_sidra, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=4,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)
        cd6_lbl = Label(F4, text='7UP', font=('times new roman', 15, 'bold'), bg=bg_color,
                           fg='lightgreen').grid(
            row=5, column=0, padx=10, pady=10, sticky='w')
        cd6_txt = Entry(F4, width=10,textvariable=self.seven_up, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=5,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)
        #-------Bill Area----------
        F5 = LabelFrame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=350, height=380)

        bill_title = Label(F5,text='Bill Area',font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand =1)

        #------Button Frame-------
        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"),
                        fg='gold',
                        bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_lbl=Label(F6,text='Total Cosmetics Price',font=('times new roman',14,'bold'),bg=bg_color,fg="white").grid(row=0,column=0,padx=20,pady=1,sticky='w')
        m1_txt=Entry(F6,width=18,font="arial 10 bold",textvariable=self.cosmetic_price,bd=8,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl = Label(F6, text='Total Groceries Price', font=('times new roman', 14, 'bold'), bg=bg_color,
                       fg="white").grid(row=1, column=0, padx=20, pady=1, sticky='w')
        m2_txt = Entry(F6, width=18, font="arial 10 bold",textvariable=self.grocery_price, bd=8, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(F6, text='Total Cold Drinks Price', font=('times new roman', 14, 'bold'), bg=bg_color,
                       fg="white").grid(row=2, column=0, padx=20, pady=1, sticky='w')
        m3_txt = Entry(F6, width=18, font="arial 10 bold", bd=8,textvariable=self.cold_drink_price, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        c1_lbl = Label(F6, text='Cosmetics Tax', font=('times new roman', 14, 'bold'), bg=bg_color,
                       fg="white").grid(row=0, column=2, padx=20, pady=1, sticky='w')
        c1_txt = Entry(F6, width=18, font="arial 10 bold", bd=8,textvariable=self.cosmetic_tax, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        c2_lbl = Label(F6, text='Groceries Tax', font=('times new roman', 14, 'bold'), bg=bg_color,
                       fg="white").grid(row=1, column=2, padx=20, pady=1, sticky='w')
        c2_txt = Entry(F6, width=18, font="arial 10 bold", bd=8,textvariable=self.grocery_tax, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        c3_lbl = Label(F6, text='Cold Drinks Tax', font=('times new roman', 14, 'bold'), bg=bg_color,
                       fg="white").grid(row=2, column=2, padx=20, pady=1, sticky='w')
        c3_txt = Entry(F6, width=18, font="arial 10 bold",textvariable=self.cold_drink_tax, bd=8, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        btn_frame =Frame(F6,bd=7,relief=GROOVE)
        btn_frame.place(x=750,width=585,height=105)

        total_btn = Button(btn_frame,command=self.total,text='Total',bg='cadetblue',fg='white',pady=15,width=10,bd=2,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        gbill_btn = Button(btn_frame, text='Generate Bill',command=self.bill_area, bg='cadetblue', fg='white', pady=15, width=10, bd=2,
                           font="arial 15 bold").grid(row=0, column=1, padx=5, pady=5)
        clear_btn = Button(btn_frame, text='Clear', bg='cadetblue', fg='white', pady=15, width=10, bd=2,
                           font="arial 15 bold").grid(row=0, column=2, padx=5, pady=5)
        exit_btn = Button(btn_frame, text='Exit', bg='cadetblue', fg='white', pady=15, width=10, bd=2,
                           font="arial 15 bold").grid(row=0, column=3, padx=5, pady=5)
        self.wellcome_bill()

    def total(self):
        self.c_s_p= self.soap.get() * 40
        self.c_fc_p= self.face_cream.get() * 120
        self.c_fw_p= self.face_wash.get() * 250
        self.c_spray_p= self.spray.get() * 240
        self.c_g_p= self.gell.get() * 140
        self.c_l_p= self.lotion.get() * 140

        self.total_cosmetic_price = float(
                 self.c_s_p+
                 self.c_fc_p+
                 self.c_fw_p+
                 self.c_spray_p+
                 self.c_g_p+
                 self.c_l_p
        )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price * 0.02),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))

        self.g_r_p = self.rice.get() * 150
        self.g_fo_p = self.food_oil.get() * 140
        self.g_d_p = self.daal.get() * 150
        self.g_w_p = self.wheat.get() * 140
        self.g_s_p = self.sugar.get() * 240
        self.g_t_p = self.tea.get() * 170

        self.total_grocries_price = float(
             self.g_r_p+
             self.g_fo_p+
             self.g_d_p+
             self.g_w_p+
             self.g_s_p+
             self.g_t_p
        )
        self.grocery_price.set("Rs. "+str(self.total_grocries_price))
        self.g_tax=round((self.total_grocries_price*0.02),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))

        self.cd_p_p =  self.pepsi.get() * 50
        self.cd_f_p =  self.fanta.get() * 50
        self.cd_l_p =  self.limca.get() * 30
        self.cd_s_p =  self.sting.get() * 50
        self.cd_as_p = self.apple_sidra.get() * 50
        self.cd_sup_p = self.seven_up.get() * 50

        self.total_cold_drink_price = float(
             self.cd_p_p+
             self.cd_f_p+
             self.cd_l_p+
             self.cd_s_p+
             self.cd_as_p+
             self.cd_sup_p
        )
        self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
        self.cd_tax=round((self.total_cold_drink_price * 0.01),2)
        self.cold_drink_tax.set("Rs. "+str(self.cd_tax))

        self.total_bill=float(self.total_cosmetic_price+
                              self.total_grocries_price+
                              self.total_cold_drink_price+
                              self.c_tax+
                              self.g_tax+
                              self.cd_tax
                              )

    def  wellcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END, "\tWelcome to Our Mart\n")
        self.txtarea.insert(END, f"\nBill Number: {self.c_bill_no.get()} ")
        self.txtarea.insert(END, f"\nCustomer Name: {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number: {self.c_phone.get()}")
        self.txtarea.insert(END, "\n======================================")
        self.txtarea.insert(END, "\nProducts\t\tQTY\t\tPrice ")
        self.txtarea.insert(END, "\n======================================")


    def bill_area(self):
        if self.c_name.get()== "" or  self.c_phone.get()=="":
            messagebox.showerror("Error","Customer Details not found")
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No Product Selected")
        else:
            self.wellcome_bill()
            # -----------Cosmetics-------------------
            if self.soap.get() != 0:
                self.txtarea.insert(END, f"\nBath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get() != 0:
                self.txtarea.insert(END, f"\nFace Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get() != 0:
                self.txtarea.insert(END, f"\nFace Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.spray.get() != 0:
                self.txtarea.insert(END, f"\nHair Spray\t\t{self.spray.get()}\t\t{self.c_spray_p}")
            if self.gell.get() != 0:
                self.txtarea.insert(END, f"\nHair Gell\t\t{self.gell.get()}\t\t{self.c_g_p}")
            if self.lotion.get() != 0:
                self.txtarea.insert(END, f"\nBody Lotion\t\t{self.lotion.get()}\t\t{self.c_l_p}")
            # -----------Grocries-------------------------
            if self.rice.get() != 0:
                self.txtarea.insert(END, f"\nRice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.food_oil.get() != 0:
                self.txtarea.insert(END, f"\nFood Oil\t\t{self.food_oil.get()}\t\t{self.g_fo_p}")
            if self.daal.get() != 0:
                self.txtarea.insert(END, f"\nDaal\t\t{self.daal.get()}\t\t{self.g_d_p}")
            if self.wheat.get() != 0:
                self.txtarea.insert(END, f"\nWheat\t\t{self.spray.get()}\t\t{self.g_w_p}")
            if self.sugar.get() != 0:
                self.txtarea.insert(END, f"\nSugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.tea.get() != 0:
                self.txtarea.insert(END, f"\nTea\t\t{self.tea.get()}\t\t{self.g_t_p}")
            # ---------Cold Drink----------------------
            if self.pepsi.get() != 0:
                self.txtarea.insert(END, f"\nPepsi\t\t{self.pepsi.get()}\t\t{self.cd_p_p}")
            if self.fanta.get() != 0:
                self.txtarea.insert(END, f"\nFanta\t\t{self.fanta.get()}\t\t{self.cd_f_p}")
            if self.limca.get() != 0:
                self.txtarea.insert(END, f"\nLimca\t\t{self.limca.get()}\t\t{self.cd_l_p}")
            if self.sting.get() != 0:
                self.txtarea.insert(END, f"\nSting\t\t{self.sting.get()}\t\t{self.cd_s_p}")
            if self.apple_sidra.get() != 0:
                self.txtarea.insert(END, f"\nApple Sidra\t\t{self.apple_sidra.get()}\t\t{self.cd_as_p}")
            if self.seven_up.get() != 0:
                self.txtarea.insert(END, f"\n7UP\t\t{self.seven_up.get()}\t\t{self.cd_sup_p}")
            self.txtarea.insert(END, "\n--------------------------------------")
            if self.cosmetic_tax.get() != 'Rs. 0.0':
                self.txtarea.insert(END, f"\nCosmetics Tax\t\t\t    {self.cosmetic_tax.get()} ")
            if self.grocery_tax.get() != 'Rs. 0.0':
                self.txtarea.insert(END, f"\nGroceries Tax\t\t\t    {self.grocery_tax.get()} ")
            if self.cold_drink_tax.get() != 'Rs. 0.0':
                self.txtarea.insert(END, f"\nCold Drink Tax\t\t\t    {self.cold_drink_tax.get()} ")
            self.txtarea.insert(END, f"\nTotal Bill: \t\t\t    Rs:{self.total_bill} ")
            self.txtarea.insert(END, "\n--------------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0',END)
            f1 = open("Bills\ " + str(self.c_bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo('Saved',f'Bill No. {self.c_bill_no.get()} Saved Successfully')
        else:
            return

    def find_bill(self):
        present='no'
        for i in os.listdir("D:\Python\Billing Application\Bills"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"D:\Python\Billing Application\Bills {i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present='yes'
        if present=='no':
            messagebox.showerror('Error','Invalid Bill Number')
            


root = Tk()
obj = Bill_app(root)
root.mainloop()
