import math
from tkinter import *


def calculatePayment():
    amt = float(amount.get())
    itrt = float(intRate.get())
    yrs = float(years.get())
    interest = itrt / 100
    interest = interest / 12
    payment = (amt * interest) / (1 - (math.pow(1 / (1 + interest), yrs * 12)))
    lblMonthly = Label(main, text='$ %.2f' % payment).grid(row=3, column=1,
                                                           padx=0, pady=10)
    totpayment = payment * 12 * yrs
    lblTotal = Label(main, text='$ %.2f' % totpayment).grid(row=4, column=1,
                                                            padx=0, pady=10)
    return


main = Tk()
main.title("How Much?")
main.geometry('300x300')

amount = StringVar()
intRate = StringVar()
years = StringVar()

lblAmount = Label(main, text='Amount of Purchase:').grid(row=0, column=0,
                                                         padx=0, pady=10)
entAmount = Entry(main, textvariable=amount).grid(row=0, column=1)

lblIntRate = Label(main, text='Interest Rate (like 7.5):').grid(row=1,
                                                                column=0,
                                                                padx=0,
                                                                pady=10)
entIntRate = Entry(main, textvariable=intRate).grid(row=1, column=1)

lblYears = Label(main, text='Years to Pay:').grid(row=2, column=0, padx=0,
                                                  pady=10)
entYears = Entry(main, textvariable=years).grid(row=2, column=1)

btn = Button(main, text='Calculate', command=calculatePayment).grid(row=5,
                                                                    column=1)

lblMonthly = Label(main, text='Monthly Payment:').grid(row=3, column=0, padx=0,
                                                       pady=10)
lblTotal = Label(main, text='Total Purchase Cost:').grid(row=4, column=0,
                                                         padx=0, pady=10)

main.mainloop()