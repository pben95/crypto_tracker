import json, urllib, threading
from Tkinter import *
master = Tk()
master.resizable(width=False, height=False)
images = [PhotoImage(file='bitcoin.png'),
          PhotoImage(file='ethereum.png'),
          PhotoImage(file='neo.png'),
          PhotoImage(file='bitcoin-cash.png'),
          PhotoImage(file='stellar.png'),
          PhotoImage(file='nano.png')]
coins = ['https://api.coinmarketcap.com/v1/ticker/bitcoin/',
    'https://api.coinmarketcap.com/v1/ticker/ethereum/',
    'https://api.coinmarketcap.com/v1/ticker/neo/',
    'https://api.coinmarketcap.com/v1/ticker/bitcoin-cash/',
    'https://api.coinmarketcap.com/v1/ticker/stellar/',
    'https://api.coinmarketcap.com/v1/ticker/raiblocks/']
def APIupdate():
    threading.Timer(306.0, APIupdate).start()
    print('update!')
    for j, i in enumerate(coins):
        with urllib.urlopen(i) as url:
            r = json.loads(url)
            info = ("$" + r[0]["price_usd"] + " | " + r[0]["price_btc"] + " BTC \n1H " + r[0][
                "percent_change_1h"] + " | 24H " + r[0]["percent_change_24h"])
        if j < 3:
            label = Label(master, text=info).grid(row=j, column=1)
            image = Label(master, image=images[j]).grid(row=j, column=0)
        elif j >= 3:
            label = Label(master, text=info).grid(row=j - 3, column=5)
            image = Label(master, image=images[j]).grid(row=j - 3, column=4)
APIupdate()
mainloop()