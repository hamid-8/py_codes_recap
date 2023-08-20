num = None
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
print(total,counter,total / counter)
