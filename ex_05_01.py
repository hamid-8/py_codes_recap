num = None
total = 0
counter = 0
while num != "done":
    num = input ("Enter a number: ")
    try:
        num = float(num)
    except:
        if num == "done":
            break
        print("Invalid input")
        continue
    total = total + num
    counter = counter + 1
ave = total / counter
print(total,counter,ave)
