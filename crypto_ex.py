import requests
from tkinter import *
from os import getcwd
win = Tk()
win['bg'] = "white"
win.geometry("605x350")
win.resizable(FALSE,True)

def api_reponse():
    global currency_output
    global crypto_output
    url = f"https://rest.coinapi.io/v1/assets?filter_asset_id={enrty_box.get()}"

    header = {
            'X-CoinAPI-Key' : '2F28A236-6A37-4B46-B665-CBC2A259811D'
     }
    res_crypto = requests.get(url,headers=header)
    crypto_output = res_crypto.json()

    res_currency = requests.get("https://raters.ir/exchange/api/currency/usd")
    currency_output = res_currency.json()['data']['prices']

def coin():

    price = []
    count = 0

    api_reponse()

    for j in currency_output:
        dollar = j['live']
        dollar_price = int(''.join(dollar.split(',')))


    for i in crypto_output:
        price.append(f"({count})  coin name :  {i['name']}  price coin usd:  {i['price_usd']:.3f}   price exchange IRR:   {i['price_usd'] * dollar_price:,.0f} IRR\n-----------------------------------------------------------------------\n")
        lbl.config(text = "".join(price))
        count += 1



img = PhotoImage(file = getcwd() + "/scr" + "/bg3.png")
Label(win,image = img, bg = "white").place(x = -5, y= -15)


Label(win, text = "get your coin price",font = "dyuthi 15 bold", bg = "#522a9d",fg = "white").place(x = 210 , y = 12)

enrty_box = Entry(win,font = "Tahoma 10 bold",bg = "white", fg = "black")
enrty_box.place(x = 160 , y = 100, height=35)

btn = Button(win,text = "exchange_price",fg ='black',activebackground="indianRed3",relief= RAISED,activeforeground="white", font = "Tahoma 10 bold", bg = "white",command=coin)
btn.place(x = 20 ,y = 100)

lbl = Label(win, text = " ",font = "Tahoma 9 bold", fg = "tomato",bg = "white")
lbl.place(x = 20 , y = 220)

#print(os.getcwd())

win.mainloop()