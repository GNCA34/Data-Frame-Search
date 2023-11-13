from tkinter import *
import tkinter.ttk as ttk
import csv
root = Tk()
root.title("Veri goruntuleme")
width = 900
height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("Product", "Issue", "Company","State","ZIP code","Complaint ID"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('Product', text="Product", anchor=W)
tree.heading('Issue', text="Issue", anchor=W)
tree.heading('Company', text="Company", anchor=W)
tree.heading('State', text="State", anchor=W)
tree.heading('ZIP code', text="ZIP code", anchor=W)
tree.heading('Complaint ID', text="Complaint ID", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=200)
tree.column('#2', stretch=NO, minwidth=0, width=200)
tree.column('#4', stretch=NO, minwidth=0, width=200)
tree.column('#5', stretch=NO, minwidth=0, width=200)
tree.column('#6', stretch=NO, minwidth=0, width=200)

tree.pack()

with open('son.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        Product = row['Product']
        Issue = row['Issue']
        Company = row['Company']
        State = row['State']
        ZIP_code = row['ZIP code']
        ComplaintID = row['Complaint ID']
        tree.insert("", 0, values=(Product, Issue, Company,State,ZIP_code,ComplaintID))

if __name__ == '__main__':
    root.mainloop()
