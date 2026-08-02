import tkinter as tk  # Tkinter supposedly suitable for beginners and small desktop apps
from tkinter import messagebox
import produceSheets as ps
import tkinter.font as tkFont
from tkinter import PhotoImage 
import os

farmerImage = os.path.join(os.path.dirname(__file__), 'farmer3.png')

# creating the main window
root = tk.Tk()
root.title("Veggie Counter")
root.geometry("800x300")

image = PhotoImage(file=farmerImage)
image_label = tk.Label(root, image=image)
image_label.pack()
image_label.place(x=500,y=80)


def add_produce():
    veggie_name = task_veggie_entry.get().strip()
    try:
        quantity = float(task_quantity_entry.get())
        price = float(task_price_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Quantity and price must be numbers.")
        return

    if not veggie_name:
        messagebox.showerror("Missing vegetable", "Please enter a vegetable name.")
        return

    ps.new_produce(veggie_name, quantity, price)
    messagebox.showinfo("Added", f"{veggie_name} was added.") #throws error like message to confirm it was added
    task_veggie_entry.delete(0, tk.END) #empties the fields
    task_quantity_entry.delete(0, tk.END)
    task_price_entry.delete(0, tk.END)

def calculated_savings():
    veggie_name = task_veggieSaved_entry.get().strip()
    if not veggie_name:
        messagebox.showerror("Missing vegetable","Please enter a vegetable name to calculate savings")
        return
    messagebox.showinfo("Savings",f"Total saved from {veggie_name.title()}: {ps.calculate_total_spending(veggie_name)}")
    task_veggieSaved_entry.delete(0,tk.END)

def gather_veggies():
    veggie_name = task_veggieGathered_entry.get().strip()
    if not veggie_name:
        messagebox.showerror("Missing vegetable","Please enter a vegetable name to find out how much has been gathered")
        return
    messagebox.showinfo("Gathered",f"You've gathered {ps.calculate_total_gathered(veggie_name)}kg {veggie_name}")
    task_veggieGathered_entry.delete(0,tk.END)



#LEFT SIDE -------------------ADD VEGETABLE------------------------------------------------------------
title_font = tkFont.Font(size=12, weight="bold")
task_header = tk.Label(root, text="ADD VEGETABLE",font=title_font)
task_header.place(x=10,y=10)

task_veggie = tk.Label(root, text="Enter a vegetable:")
task_veggie.pack(pady=10)  # adds spacing around the label
task_veggie.place(x=10, y=30)  # positions the label at the top left corner
task_veggie_entry = tk.Entry(root, width=30)
task_veggie_entry.pack(pady=10)  # adds spacing around the field
task_veggie_entry.place(x=10, y=50)

task_price = tk.Label(root, text="Enter the price per unit:")
task_price.pack(pady=10)  # adds spacing around the label
task_price.place(x=10, y=80)  # positions the label below the vegetable label
task_price_entry = tk.Entry(root, width=30)
task_price_entry.pack()  # adds spacing around the field
task_price_entry.place(x=10, y=100)  # positions the field below the price label

task_quantity = tk.Label(root, text="Enter the quantity:")
task_quantity.pack(pady=10)  # adds spacing around the label
task_quantity.place(x=10, y=130)  # positions the label below the price label
task_quantity_entry = tk.Entry(root, width=30)
task_quantity_entry.pack()  # adds spacing around the field
task_quantity_entry.place(x=10, y=150)  # positions the field below the quantity label

task_button = tk.Button(root, text="Add Vegetable", command=add_produce)
task_button.pack(pady=10)
task_button.place(x=10,y=180)
#---------------------------------------------------------------------------------------------------------


#MIDDLE ------------------DISPLAY TOTAL POSSIBLE SPENDING-------------------------------------------------

task_headerTwo = tk.Label(root, text="Calculate total saved",font=title_font)
task_headerTwo.place(x=250,y=10)

task_veggieSaved = tk.Label(root, text="Enter a vegetable")
task_veggieSaved.place(x=250,y=30)
task_veggieSaved_entry = tk.Entry(root, width=30)
task_veggieSaved_entry.place(x=250,y=50)

task_veggieSaved_button = tk.Button(root,text="Calculate",command=calculated_savings)
task_veggieSaved_button.place(x=250,y=70)


#-------------------------------------------------------------------------------------------------------------

#RIGHT SIDE ----------------------------DISPLAY THE AMOUNT OF PRODUCE MADE -----------------------------------

task_headerThree = tk.Label(root, text = "Gathered produce", font=title_font)
task_headerThree.place(x=500,y=10)
task_veggieGathered = tk.Label(root, text="Enter a vegetable")
task_veggieGathered.place(x=500,y=30)
task_veggieGathered_entry = tk.Entry(root, width=30)
task_veggieGathered_entry.place(x=500,y=50)

task_veggieGathered_button = tk.Button(root,text="Gather",command=gather_veggies)
task_veggieGathered_button.place(x=500,y=70)

#--------------------------------------------------------------------------------------------------




#start the program
root.mainloop()