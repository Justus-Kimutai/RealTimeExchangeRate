import tkinter as tk
from tkinter import ttk


api_data = {'Realtime Currency Exchange Rate': {
    '1. From_Currency Code': 'USD', 
    '2. From_Currency Name': 'United States Dollar', 
    '3. To_Currency Code': 'KES',
    '4. To_Currency Name': 'Kenyan Shilling', 
    '5. Exchange Rate': '129.48000000', 
    '6. Last Refreshed': '2024-04-09 06:13:41', 
    '7. Time Zone': 'UTC', 
    '8. Bid Price': '129.47500000', 
    '9. Ask Price': '129.48200000'}}

def fetch_Api(api_data):
    country_1 = api_data['Realtime Currency Exchange Rate']['2. From_Currency Name']
    country_2 = api_data['Realtime Currency Exchange Rate']['4. To_Currency Name']

    results_section['text'] = f'{country_1 }  to {country_2}'


window = tk.Tk()
window.title('Exchange Rates')
window.geometry('400x400+1400+50')

frame = tk.Frame(window,background='#FF8A00')
my_label = ttk.Label(frame, text='Real Time Exchange Rates',font='Carldi 20 bold',background='#FF8A00')

country_section = tk.Frame(frame)
country_section.columnconfigure((0,1),weight=1,uniform='a')
country_section.rowconfigure((0,1),weight=1,uniform='a')


# country_one_var = tk.StringVar(value='Country One')
# country_two_var = tk.StringVar(value='Country two')
country_one = ttk.Label(country_section,text='Country One',background='#FF8A00',font='Cardi 12 bold')
country_two = ttk.Label(country_section,text='Country Two',background='#FF8A00',font='Cardi 12 bold')

country_one_entry = tk.Entry(country_section,background='#FF8A00',font='Cardi 12 bold')
country_two_entry = tk.Entry(country_section,background='#FF8A00',font='Cardi 12 bold')

call_to_action = tk.Frame(frame,background='#FF8A00')

# fetch_Api = tk.StringVar()
submit_btn = tk.Button(call_to_action,text='Send',background='#00C6FF',font='Cardi 12',command=lambda:fetch_Api(api_data))

results_section = ttk.Label(call_to_action, text='Country one to country two',background='#FF8A00',font='Cardi 15 bold')
exchange_rate_amount = ttk.Label(call_to_action,text='129.48098',background='#FF8A00',font='Cardi 15 bold')

country_one.grid(row=0,column=0,sticky='nwes',ipady=10)
country_two.grid(row=1,column=0,sticky='nwes',ipady=10)
country_one_entry.grid(row=0,column=1,sticky='nwes')
country_two_entry.grid(row=1,column=1,sticky='nwes')


my_label.pack(pady=15)
country_section.pack()
call_to_action.pack()
submit_btn.pack(expand=True,pady=10)
results_section.pack(pady=5)
exchange_rate_amount.pack(pady=5)
frame.pack(expand=True,fill='both')

window.mainloop()



