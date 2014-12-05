from Tkinter import *
import ttk
import mypackage.StockClass as SC
import pandas as pd
import datetime

class MultiStocksWindow:
	def __init__(self, master):
		self.master = master
		self.frame = ttk.Frame(self.master,padding="4 4 200 200")
		self.frame.grid(column=0, row=0, sticky=(N, W, E, S))
		self.frame.columnconfigure(0, weight=1)
		self.frame.rowconfigure(0, weight=1)

		stock_one_name = StringVar()
		stock_two_name = StringVar()
		stock_three_name = StringVar()
		stock_four_name = StringVar()
		start_date = StringVar()
		end_date = StringVar()

		stock_one_name_entry = ttk.Entry(self.frame, width=7, textvariable=stock_one_name)
		stock_one_name_entry.grid(column=2, row=1, sticky=(W, E))

		stock_two_name_entry = ttk.Entry(self.frame, width=7, textvariable=stock_two_name)
		stock_two_name_entry.grid(column=2, row=2, sticky=(W, E))

		stock_three_name_entry = ttk.Entry(self.frame, width=7, textvariable=stock_three_name)
		stock_three_name_entry.grid(column=2, row=3, sticky=(W, E))

		stock_four_name_entry = ttk.Entry(self.frame, width=7, textvariable=stock_four_name)
		stock_four_name_entry.grid(column=2, row=4, sticky=(W, E))

		start_date_entry = ttk.Entry(self.frame, width=7, textvariable=start_date)
		start_date_entry.grid(column=4, row=1, sticky=(W, E))

		end_date_entry = ttk.Entry(self.frame, width=7, textvariable=end_date)
		end_date_entry.grid(column=4, row=2, sticky=(W, E))

		ttk.Label(self.frame, text="please enter the first stock name").grid(column=1, row=1, sticky=W)
		ttk.Label(self.frame, text="please enter the second stock name").grid(column=1, row=2, sticky=W)
		ttk.Label(self.frame, text="please enter the third stock name").grid(column=1, row=3, sticky=W)
		ttk.Label(self.frame, text="please enter the fourth stock name").grid(column=1, row=4, sticky=W)

		ttk.Label(self.frame, text="please enter the start date").grid(column=3, row=1, sticky=W)
		ttk.Label(self.frame, text="please enter the start date").grid(column=3, row=2, sticky=W)

		ttk.Button(self.frame, text="Plot", command=lambda: self.plot\
			([stock_one_name.get(), stock_two_name.get(), stock_three_name.get(), stock_four_name.get()], \
				start_date.get(), end_date.get())).grid(column=4, row=4, sticky=W)


		for child in self.frame.winfo_children(): 
			child.grid_configure(padx=20, pady=20)

		stock_one_name_entry.focus()


	def plot(self, stock_list, start_date, end_date):
		#stock = SC.Stock(stock_list, start_date, end_date)
		#stock.plot_closeprice()
		print stock_list
		print start_date
      

