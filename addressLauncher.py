import webbrowser, pyperclip

address = pyperclip.paste()  #copy the adress

webbrowser.open('https://www.google.com/maps/place/' + address) # address is pasted by function paste from pyperclip module