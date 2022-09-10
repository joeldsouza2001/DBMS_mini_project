from tkinter import *
from tkinter.ttk import Notebook
from main import Tabs
from tkinter import ttk



root=Tk()
root.geometry('1300x750')
root.title('LEARN2DRIVE')

main_frame = Frame(root,padx=5,pady=5)

title_frame=Frame(main_frame,padx=5,pady=5)
Label(title_frame,text='DRIVING SCHOOL MANAGEMENT SYSTEM',font=('ms sans serif',20)).pack()
title_frame.grid(row=0,column=0,padx=10,pady=15)


tabControl=Notebook(main_frame,width=1230)

ob1 = Tabs(tabControl,'CUSTOMER DETAILS','customer',['Customer ID','Name','Age','Gender','Phone','Aadhar number','Address'],
           ['cust_id','c_name','c_age','c_gender','c_phone','c_aadhar','c_address'],
           ['Customer ID','Customer Name','Customer Phone','Course ID'],
           ['cust_id','c_name','c_phone','course_id'])
tb1=ob1.funcc()

ob2 = Tabs(tabControl,'EMPLOYEE DETAILS','employee',['Employee ID','Name','Age','Gender','Designation','Salary','Date of Join','Aadhar number','Phone'],
           ['emp_id','e_name','e_age','e_gender','dsgn','salary','join_date','e_aadhar','e_phone'],
           ['Employee ID','Employee Name'],
           ['emp_id','e_name'])
tb2=ob2.funcc()

ob3 = Tabs(tabControl,'CLASS DETAILS','class',['Class ID','Date','Towards Course ID','RC number of vehicle'],
           ['class_id','date','towards_course','reg_no_vehicle'],
           ['Class ID','Date','Course ID'],
           ['class_id','date','towards_course'])
tb3=ob3.funcc()

ob4 = Tabs(tabControl,'COURSE DETAILS','course',['Course ID','Classes Enrolled','Classes Done','Classes remaining','Start Date','Time of the Day','Total Amount for Enrolled Classes','Amount Received','Amount Remaining','Type of Vehicle','Trainer ID','Towards Customer ID'],
           ['course_id','total_class_enrolled','total_class_done','total_class_remaining','start_date','time','total_amt','amt_received','amt_remaining','vehicle_type','trainer_id','towards_customer'],
           ['Course ID','Customer ID','Customer Name','Trainer ID'],
           ['course_id','cust_id','c_name','trainer_id'])
tb4=ob4.funcc()

ob5 = Tabs(tabControl,'VEHICLE DETAILS','vehicle',['RC Number','Name','Insurance Expiry Date','Emission Expiry Date','Last Service Date','Type of Vehicle'],
           ['reg_no','v_name','insurance_expiry','emission_expiry','last_service_date','type'],
           ['RC number','Type'],
           ['reg_no','type'])
tb5=ob5.funcc()

ob6 = Tabs(tabControl,'PAYMENT DETAILS','payment',['Payment ID','Amount','Date','Mode','Towards Course','Collected By'],
           ['payment_id','amount','payment_date','mode','amt_towards_course','collected_by'],
           ['Payment ID','Date','Course ID'],
           ['payment_id','date','course_id'])
tb6=ob6.funcc()


tabControl.add(tb1,text='CUSTOMER DETAILS')
tabControl.add(tb2,text='EMPLOYEE DETAILS')
tabControl.add(tb5,text='VEHICLE DETAILS')
tabControl.add(tb4,text='COURSE DETAILS')
tabControl.add(tb3,text='CLASS DETAILS')
tabControl.add(tb6,text='PAYMENT DETAILS')
tabControl.grid(row=1,column=0)
main_frame.pack()
root.mainloop()
        


