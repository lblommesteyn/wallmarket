from tkinter import *
from grocery_client import GroceryClient

client = GroceryClient()
result = client.get_url('beef')

def scankey(event):
    val = event.widget.get()
    print(val)

    if val == '':
        update(())
    else:
        result = client.get_url(val)
        list = (f'{product.name} ${round(product.price, 2)}' for product in result.products)

        update(list)


def update(data):
    listbox.delete(0, 'end')

    # put new data
    for item in data:
        listbox.insert('end', item)


list = ()

ws = Tk()

entry = Entry(ws, width=30)
entry.pack()
entry.bind('<KeyRelease>', scankey)

listbox = Listbox(ws, width=60, height=20)
listbox.pack()
update(list)

ws.mainloop()
