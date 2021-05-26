import sqlite3
from tkinter import * 



root = Tk()
root.geometry("600x600")
root.title("Login Page")




def save():

  conn = sqlite3.connect("login_details.db")
  c = conn.cursor()

  record_id = select_value.get()

  # here first_name etc  are  the cloumn names we gave in the table
  c.execute(""" UPDATE login_details SET
        first_name = :first,
        last_name = :last,
        date_of_birth = :DOB,
        gender = :gender,
        contact_number = :contact,
        email = email,
        country = :country
        
        WHERE oid = :oid """, {"first" : f_name_update.get(),
                                "last" : l_name_update.get(),
                                "DOB" : DOB_update.get(),
                                "gender" : gender_update.get(),
                                "contact" : contact_num_update.get(),
                                "email" : email_update.get(),
                                "country" : country_update.get(),
                                "oid" : record_id
                                } ) 


  conn.commit()

  conn.close()

  editor.destroy()






def update_record():

  global editor

  editor = Tk()
  editor.geometry("600x600")
  editor.title("Update Page")
  


  conn = sqlite3.connect("login_details.db")
  c = conn.cursor()


  record_id = select_value.get()
  c.execute("SELECT *, oid FROM login_details WHERE  oid = " + record_id) 

  records_1 = c.fetchall()
  print(record_id)   # creates as a list
  

  print_records_1 = ""
  for record in records_1 :
    print_records_1 += f"{record[0]} {record[1]}\t{record[7]} \n "   # here 7 column resembles the oid number
  
  
  conn.commit()

  conn.close()
    
  #create global variables for text boxes names
  global f_name_update
  global l_name_update
  global DOB_update
  global gender_update
  global contact_num_update
  global email_update
  global country_update
  
  f_name_update = Entry(editor, width = 30 )
  f_name_update .grid(row = 0, column= 1, padx = 20, pady = 10)

  l_name_update  = Entry(editor, width = 30 )
  l_name_update .grid(row = 1, column= 1, padx = 20, pady = 10)

  DOB_update  = Entry(editor, width = 30 )
  DOB_update .grid(row = 2, column= 1, padx = 20, pady = 10)

  gender_update = Entry(editor, width = 30 )
  gender_update.grid(row = 3, column= 1, padx = 20, pady = 10)

  contact_num_update = Entry(editor, width = 30 )
  contact_num_update.grid(row = 4, column= 1, padx = 20, pady = 10)

  email_update = Entry(editor, width = 30 )
  email_update.grid(row = 5, column= 1, padx = 20, pady = 10)

  country_update = Entry(editor, width = 30 )
  country_update.grid(row = 6, column= 1, padx = 20, pady = 10)

  # labels
  f_name_label_update = Label(editor, text = "First Name" ,width = 30 )
  f_name_label_update.grid(row = 0, column= 0, padx = 20, pady = 10)

  l_name_label_update = Label(editor,text = "Last Name", width = 30 )
  l_name_label_update.grid(row = 1, column= 0, padx = 20, pady = 10)

  DOB_label_update = Label(editor, text = "Date of Birth", width = 30 )
  DOB_label_update.grid(row = 2, column= 0, padx = 20, pady = 10)

  gender_label_update = Label(editor,text = "Gender",  width = 30 )
  gender_label_update.grid(row = 3, column= 0, padx = 20, pady = 10)

  contact_num_label_update = Label(editor, text = "Contact Number", width = 30 )
  contact_num_label_update.grid(row = 4, column= 0, padx = 20, pady = 10)

  email_label_update = Label(editor, text = "Email", width = 30 )
  email_label_update.grid(row = 5, column= 0, padx = 20, pady = 10)

  country_label_update = Label(editor,text = "Country",  width = 30 )
  country_label_update.grid(row = 6, column= 0, padx = 20, pady = 10)
  

  for record in records_1 :
    # inserting values in entrys
    f_name_update.insert(0, record[0])
    l_name_update.insert(0, record[1])
    DOB_update.insert(0, record[2])
    gender_update.insert(0, record[3])
    contact_num_update.insert(0, record[4])
    email_update.insert(0, record[5])
    country_update.insert(0, record[6])


  # buttons
  save_btn = Button(editor, text = "Save Changes ", command=save )
  save_btn.grid(row = 7, column = 0, columnspan=2,padx = 10, pady = 10, ipadx=100 )











# create submit function for database
def submit():
    conn = sqlite3.connect("login_details.db")
    c = conn.cursor()

    # insert  into table
    c.execute("INSERT INTO login_details VALUES (:f_name, :l_name, :dob, :gender, :contact, :email, :country)", 
             {
                 "f_name" : f_name.get(),
                 "l_name" : l_name.get(),
                 "dob"    : DOB.get(),
                 "gender" : gender.get(),
                 "contact": contact_num.get(),
                 "email"  : email.get(),
                 "country": country.get()
             })


    

    conn.commit()

    conn.close()

    # clearing entry widgets
    f_name.delete(0, END)
    l_name.delete(0, END)
    DOB.delete(0, END)
    gender.delete(0, END)
    contact_num.delete(0, END)
    email.delete(0, END)
    country.delete(0, END)
    


# create query function for getting records from  database
def query():
    conn = sqlite3.connect("login_details.db")
    c = conn.cursor()

    # c.execute("SELECT * FROM login_details WHERE last_name = :l_name ", {"l_name" : "durga"})
    # query the db
    c.execute("SELECT *, oid FROM login_details ") 
 
    records = c.fetchall()
    print(records)   # creates as a list
    print_records = ""
    for record in records :
      print_records += f"{record[0]} {record[1]}\t{record[7]} \n "   # here 7 column resembles the oid number
    
    # print(print_records)
    query_label = Label(root, text = print_records, )
    query_label.grid(row = 15, column=0, columnspan=2)

    
    
    conn.commit()

    conn.close()
    


# create a function to delete a record a/c oid
def delete_record():
  conn = sqlite3.connect("login_details.db")
  c = conn.cursor()

  # c.execute("SELECT * FROM login_details WHERE last_name = :l_name ", {"l_name" : "durga"})
  # query the db
  print(select_value.get())
  c.execute("DELETE from login_details where oid = " + select_value.get() )

  select_value.delete(0, END)
  conn.commit()

  conn.close()





f_name = Entry(root, width = 30 )
f_name.grid(row = 0, column= 1, padx = 20, pady = 10)

l_name = Entry(root, width = 30 )
l_name.grid(row = 1, column= 1, padx = 20, pady = 10)

DOB = Entry(root, width = 30 )
DOB.grid(row = 2, column= 1, padx = 20, pady = 10)

gender = Entry(root, width = 30 )
gender.grid(row = 3, column= 1, padx = 20, pady = 10)

contact_num = Entry(root, width = 30 )
contact_num.grid(row = 4, column= 1, padx = 20, pady = 10)

email = Entry(root, width = 30 )
email.grid(row = 5, column= 1, padx = 20, pady = 10)

country = Entry(root, width = 30 )
country.grid(row = 6, column= 1, padx = 20, pady = 10)

select_value = Entry(root, width = 30 )
select_value.grid(row = 9, column= 1, padx = 20, pady = 10)


# labels
f_name_label = Label(root, text = "First Name" ,width = 30 )
f_name_label.grid(row = 0, column= 0, padx = 20, pady = 10)

l_name_label = Label(root,text = "Last Name", width = 30 )
l_name_label.grid(row = 1, column= 0, padx = 20, pady = 10)

DOB_label = Label(root, text = "Date of Birth", width = 30 )
DOB_label.grid(row = 2, column= 0, padx = 20, pady = 10)

gender_label = Label(root,text = "Gender",  width = 30 )
gender_label.grid(row = 3, column= 0, padx = 20, pady = 10)

contact_num_label = Label(root, text = "Contact Number", width = 30 )
contact_num_label.grid(row = 4, column= 0, padx = 20, pady = 10)

email_label = Label(root, text = "Email", width = 30 )
email_label.grid(row = 5, column= 0, padx = 20, pady = 10)

country_label = Label(root,text = "Country",  width = 30 )
country_label.grid(row = 6, column= 0, padx = 20, pady = 10)

select_label = Label(root,text = "Select Record Id ",  width = 30 )
select_label.grid(row = 9, column= 0, padx = 20, pady = 10)


# buttons
submit_btn = Button(root, text = "Add record to DB", command=submit )
submit_btn.grid(row = 7, column = 0, columnspan=2,padx = 10, pady = 10, ipadx=100 )

query_btn = Button(root, text = "Show record ", command=query )
query_btn.grid(row = 8, column = 0, columnspan=2,padx = 10, pady = 10, ipadx=100 )


update_btn = Button(root, text = "Update record ", command=update_record )
update_btn.grid(row = 12, column = 0, columnspan=2,padx = 10, pady = 10, ipadx=100 )


delete_btn = Button(root, text = "Delete record ", command=delete_record)
delete_btn.grid(row = 10 , column = 0, columnspan=2,padx = 10, pady = 10, ipadx=100 )



root.mainloop()
