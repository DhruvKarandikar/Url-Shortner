import pyshorteners


'''Get API in progress for url shortners'''


url = input('Enter url: ')


print("Short url: ", pyshorteners.Shortener().tinyurl.short(url))

