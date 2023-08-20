num = None
ma = None
mi = None
total = 0
counter = 0
while True:
    num = input ("Enter a number: ")
    if num == "done":
        break
    try:
        num = float(num)
    except:
        print("Invalid input")
        continue
    total = total + num
    counter = counter + 1
    if mi is None:
        mi = num
    if ma is None:
        ma = num
    if num < mi:
        mi = num
    elif num > ma:
        ma = num
print(ma,mi,counter)
