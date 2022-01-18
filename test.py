import pyshorteners

url=input("Enter url:")

con_url = pyshorteners.Shortener().tinyurl.short(url)

print(con_url)
