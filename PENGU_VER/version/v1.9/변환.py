f = open("log.txt", "r", encoding="utf-8")
data = f.read()
f.close()
f = open("log.txt", 'w')
f.write(data)
f.close()