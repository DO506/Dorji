from Tkinter import *
from Tkinter import Tk

def Register_info():
	name_info = name.get()
	gender_info = gender.get()
	DOB_info = DOB.get()
	address_info = address.get()
	number_info = number.get()
	email_info = email.get()

	file = open("Database.txt", "a")
	file.write("name:" +name_info+ "\n")
	file.write("Gender:" +gender_info+ "\n")
	file.write("DOB:" +address_info+ "\n")
	file.write("address:" +number_info+ "\n")
	file.write("number:" +email_info+ "\n\n\n")
	file.close()

	name_entry.delete(0,END)
	gender_entry.delete(0,END)
	DOB_entry.delete(0,END)
	address_entry.delete(0,END)
	number_entry.delete(0,END)
	email_entry.delete(0,END)

	Label(screen1,text= "Your details are registered. thank you" ,font = ("calibri",12)).pack()

def Insert():
	global screen1
	screen1 = Toplevel(screen)
	screen1.title("Register Form")
	screen1.geometry("700x650")

	global name, gender, DOB, address, number, email
	global name_entry, gender_entry, DOB_entry,address_entry, number_entry , email_entry
	name=StringVar()
	gender = StringVar()
	DOB = StringVar()
	address = StringVar()
	number = StringVar()
	email = StringVar()

	Label(screen1,text= "Fill in your details", font = ("calibri", 14, "bold")).pack()
	Label(screen1, text = " ").pack()

	Label(screen1, text = "Name:", font = ("calibri", 12, "bold")).pack()
	name_entry = Entry(screen1,textvariable = name)
	name_entry.pack()

	Label(screen1, text = "Gender: ", font = ("calibri", 12, "bold")).pack()
	gender_entry = Entry(screen1,textvariable = gender)
	gender_entry.pack()

	Label(screen1, text = "DOB : ", font = ("calibri", 12, "bold")).pack()
	DOB_entry = Entry(screen1,textvariable = DOB)
	DOB_entry.pack()

	Label(screen1, text = "Address :" , font = ("calibri", 12, "bold")).pack()
	address_entry = Entry(screen1,textvariable = address)
	address_entry.pack()

	Label(screen1, text = "Number : " , font = ("calibri", 12, "bold")).pack()
	number_entry = Entry(screen1,textvariable = number)
	number_entry.pack()

	Label(screen1, text = "Email no. : " , font = ("calibri", 12, "bold")).pack()
	email_entry = Entry(screen1,textvariable = email)
	email_entry.pack()


	Label(screen1,text = " ").pack()
	Button(screen1, text = "Enter", width = 10, height = 1, command = Register_info).pack()
	

def Display():
    global screen2
    screen2 = Toplevel()
    screen2.title("Display")
    screen2.geometry("700x650")

    Label(screen2, text="Details of your Friends", font=("times new roman", 15, "bold")).pack()
    Label(screen2, text=" ").pack()

    Label(screen2, text="Total Number of Friends: ", font=("times new roman", 12, "bold")).pack()
    with open("Database.txt",'r') as f:
        contents = f.read()
        count = contents.count("Name")
    Label(screen2, text=count).pack()
    Label(screen2, text=" ").pack()

    #=============graph=======================================
    Label(screen2, text="Graph: ", font=("times new roman", 12, "bold")).pack()
    import matplotlib.pyplot as p
    with open("Database.txt", 'r') as f:
        x = f.read()
        count_male = x.count("Male")
        count_female = x.count("Female")
    gender = ["Male","Female"]
    values = [count_male,count_female]
    p.title("Number of male and female pie graph")
    p.pie(values, labels=gender,autopct='%1.1f%%')
    Label(screen2, text="Number of Male: ", font=("times new roman", 12, "bold")).pack()
    Label(screen2, text=count_male).pack()
    Label(screen2, text="Number of Female: ", font=("times new roman", 12, "bold")).pack()
    Label(screen2, text=count_female).pack()
    Label(screen2, text=p.show()).pack()
    


def Search():
	global screen3
	screen3 = Toplevel(screen)
	screen3.title("Search")
	screen3.geometry("700x650")
	global search_var,search_entry
	search_var = StringVar()
	
	Label(screen3, text="Search your friends detail: ",font=("calibri", 12,"bold")).pack()
	Label(screen3, text=" ").pack()
	Label(screen3, text="Enter name: ",font=("calibri", 12,"bold")).pack()
	search_entry = Entry(screen3,textvariable = search_var)
	search_entry.pack()

	Label(screen3,text=" ").pack()
	Button(screen3, text = "Search", width = 10, height = 1, command = search).pack()
def search():
	search_entry= search_var.get()
	f = open("Database.txt",'r')
	fr = f.read()

	if search_entry in fr:
		a = "Search match"
		Label(screen3, text = a).pack()
	else:
		b = "Search result not found"
		Label(screen3, text = b).pack()	
	
def Delete():
	global screen4
	screen4 = Toplevel()
	screen4.title("Delete")
	screen4.geometry("700x650")
	global delete,delete_entry
	delete = StringVar()

	Label(screen4, text = "Remove friends", font = ("calibri", 12, "bold")).pack()
	Label(screen4,text = " ").pack()
	
	Label(screen4, text = "Enter name to remove *", font = ("calibri", 12, "bold")).pack()
	delete_entry = Entry(screen4,textvariable=delete)
	delete_entry.pack()
	Label(screen4,text = " ").pack()
	Button(screen4,text = "Delete", bg = "red" ,height= "1", width= "10", command = delete).pack()
def delete():
	delete_info = delete.get()
	with open("Database.txt", "r")	as f:
		lines = f.readlines()
	with open("Database.txt","w") as f:
		for line in lines:
			if line.strip("")+Delete_info:
				f.write(line)
	f.close()

	Label(screen4, text="Successful!",font=("calibri",12)).pack()

	
def main_screen():
	global screen
	screen = Toplevel()
	screen.geometry("700x650")
	screen.title("Nge charo")
	screen.config(bg="blue")
	Label(text = "nge charo", bg = "green" ,height= "2", width= "25",font = ("calibri",12)).pack()
	Label(text = " ").pack()
	Button(text = "Insert", bg = "red" ,height= "2", width= "25", command = Insert).pack()
	Label(text = " ").pack()
	Button(text = "Dispaly", bg = "red" ,height= "2", width= "25", command = Display).pack()
	Label(text = " ").pack()
	Button(text = "Search", bg = "red" ,height= "2", width= "25", command = Search).pack()
	Label(text = " ").pack()
	Button(text = "Delete", bg = "red" ,height= "2", width= "25", command = Delete).pack()
	Label(text = " ").pack()
	screen.mainloop()
main_screen()
