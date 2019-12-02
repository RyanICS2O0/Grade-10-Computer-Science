
i = 1
while i == 1:
  pin = str(input("Please enter a six digit pin. "))
  if len(pin) != 6:
    print ("Try again")
  else:
    i = 2


import time
startTime = time.time()

guess = [000000]
i = 1
while i < 10:
  guess = i * 111111
  i += 1
  if guess == int(pin):
    print ("Your pin has been cracked, it is %s" % pin)
    print ("Your pin was easy to crack")
    endTime = time.time()
    print ("Elapsed time is: ", (endTime - startTime))
    quit()

numlist = "1234567890"
n = 0
i = 0
while n < 4:
  guess = numlist[i] + numlist[i + 1] + numlist[i + 2] + numlist[i + 3] + numlist[i + 4] + numlist[i + 5]
  n += 1
  if guess == int(pin):
      print ("Your pin has been cracked, it is %s" % pin)
      print ("Your pin was easy to crack")
      endTime = time.time()
      print ("Elapsed time is: ", (endTime - startTime))
      quit()


guess = 0
while guess != str(pin):
  guess += 1
  if guess == int(pin):
    print ("Your pin has been cracked, it is %s" % pin)
    print ("Your pin was hard to crack")
    endTime = time.time()
    print ("Elapsed time is: ", (endTime - startTime))
    quit()

