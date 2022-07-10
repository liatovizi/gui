import sqlite3
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Nexi's word")
root.geometry("400x600")

'''conn = sqlite3.connect('address_book.db')
c = conn.cursor()

c.execute("""CREATE TABLE addresses(
    first_name text, 
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer)
""")

conn.commit()
conn.close()
'''

# Create function to delete a record
def delete():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute('DELETE from addresses WHERE oid=' + delete_box.get())


    conn.commit()
    conn.close()

def submit():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zip_code)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address':address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zip_code': zip_code.get()
              })

    conn.commit()
    conn.close()
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zip_code.delete(0, END)

def query():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM addresses")
    records= c.fetchall()
    #print(records)

    pr = " "
    for record in records:
        pr += str(record[0]) + " " + str(record[1]) + " " + "\t"
    query_label = Label(root, text=pr)
    query_label.grid(row=14, column=0, columnspan=2)

    conn.commit()
    conn.close()


#create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10,0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
zip_code = Entry(root, width=30)
zip_code.grid(row=5, column=1, padx=20)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)


#Create tex box labels
f_name_label= Label(root, text='First name')
f_name_label.grid(row=0, column=0, pady=(10,0))
l_name_label= Label(root, text='Last name')
l_name_label.grid(row=1, column=0)
address_label= Label(root, text='Address')
address_label.grid(row=2, column=0)
city_label= Label(root, text='City')
city_label.grid(row=3, column=0)
state_label= Label(root, text='State')
state_label.grid(row=4, column=0)
zip_code_label= Label(root, text='Zip Code')
zip_code_label.grid(row=5, column=0)
delete_box_label=Label(root, text='Select ID')
delete_box_label.grid(row=9, column=0, pady=5)

# Submit button
submit_button= Button(root, text='Add record to database', command= submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=110)

# Create a query button
query_button=Button(root, text='Show records', command=query)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

delete_button=Button(root, text='Delete record', command=delete)
delete_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=138)



mainloop()


