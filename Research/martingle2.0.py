import OCT
import nov
import dec
import masterlist
    
#variables
#Martingle_Arr=[1,1,1,1,3,3,3,8,8,8,20,20,50,125,783,783,2461]
#Martingle_Arr=[1,3,6,14,30,60,150,300,600,1200,2400,4800,8400,1]
#Martingle_Arr=[1,3,6,14,30,60,150,300,600,1200,1200,600,300,150,60]
#Martingle_Arr=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,144,233,377,610,987, 1597, 2584, 4181]
Martingle_Arr = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
row1 = 0
row2 = 0
row3 = 0
row4 = 0 
row5 = 0
row6 = 0
row7 = 0
row8 = 0
row9 = 0 
row10 = 0
row11 = 0
row12 = 0
row13 = 0
row14 = 0 
row15 = 0
row16 = 0
row17 = 0
row18 = 0
row19 = 0 
row20 = 0
row21 = 0
row22 = 0
row23 = 0
row24 = 0 
row25 = 0
row26 = 0
row27 = 0
row28 = 0
row29 = 0 
row30 = 0

ACTIVES="EURUSD"
duration=1#minute 1 or 5
default_Amt=1
amount=1
action="call"#put
polling_time=3
counter=1
expirations_mode=1
amount_list = []
action = "GREEN"
lossCounter = 0
winCounter = 0
result = ""
default_Amt = 1
compundingAmt = 1
amount = 1 
martingle = False 
total_Amt = 0
amount_list = []
final_win = 0
counter = 0
wait_for_2_win = False


for x in masterlist.list_oct_nov_dec:    
    #MM 
    if x == action :
        print("WIN")
        result = "WIN"
        lossCounter = 0
        winCounter = winCounter + 1
        action = action
        final_win = final_win + amount
    else :
        print("LOSS")
        result = "LOSS"
        winCounter = 0
        lossCounter = lossCounter + 1
        final_win = final_win - amount
        if action == "GREEN" :
           action = "RED"
        else :
           action = "GREEN"

   #AM
    if counter == 1 :
      if result == "WIN" :
        print("Win Row1")
        row1 = 0
      else :
        print("Loss Row1")
        row1 = row1 + 1
      amount = Martingle_Arr[row1]
      print("Amount Counter 1 :" + str(amount))
    
    elif counter == 2 :
      if result == "WIN" :
        print("Win Row 2")
        row2 = 0
      else :
        print("Loss Row 2 ")
        row2 = row2 + 1
      amount = Martingle_Arr[row3]
      print("Amount Counter 2 :" + str(amount))
    
    elif counter == 3 :
      if result == "WIN" :
        print("Win Row 3")
        row3 = 0
      else :
        print("Loss Row 3 ")
        row3 = row3 + 1
      amount = Martingle_Arr[row4]
      print("Amount Counter 3 :" + str(amount))
    
    elif counter == 4 :
      if result == "WIN" :
        print("Win Row 4")
        row4 = 0
      else :
        print("Loss Row 4 ")
        row4 = row4 + 1
      amount = Martingle_Arr[row5]
      print("Amount Counter 4 :" + str(amount))
    
    elif counter == 5 :
      if result == "WIN" :
        print("Win Row 5")
        row5 = 0
      else :
        print("Loss Row 5 ")
        row5 = row5 + 1
      amount = Martingle_Arr[row6]
      print("Amount Counter 5 :" + str(amount))
    
    elif counter == 6 :
      if result == "WIN" :
        row6 = 0
      else :
        row6 = row6 + 1
      amount = Martingle_Arr[row7]
    
    elif counter == 7 :
      if result == "WIN" :
        row7 = 0
      else :
        row7 = row7 + 1
      amount = Martingle_Arr[row8]
    
    elif counter == 8 :
      if result == "WIN" :
        row8 = 0
      else :
        row8 = row8 + 1
      amount = Martingle_Arr[row9]
    
    elif counter == 9 :
      if result == "WIN" :
        row9 = 0
      else :
        row9 = row9 + 1
      amount = Martingle_Arr[row10]
    
    elif counter == 10 :
      if result == "WIN" :
        row10 = 0
      else :
        row10 = row10 + 1
      amount = Martingle_Arr[row11]
    
    elif counter == 11 :
      if result == "WIN" :
        row11 = 0
      else :
        row11 = row11 + 1
      amount = Martingle_Arr[row12]
    
    elif counter == 12 :
      if result == "WIN" :
        row12 = 0
      else :
        row12 = row12 + 1
      amount = Martingle_Arr[row13]
    
    elif counter == 13 :
      if result == "WIN" :
        row13 = 0
      else :
        row13 = row13 + 1
      amount = Martingle_Arr[row14]
    
    elif counter == 14 :
      if result == "WIN" :
        row14 = 0
      else :
        row14 = row14 + 1
      amount = Martingle_Arr[row15]
    
    elif counter == 15 :
      if result == "WIN" :
        row15 = 0
      else :
        row15 = row15 + 1
      amount = Martingle_Arr[row16]
    
    elif counter == 16 :
      if result == "WIN" :
        row16 = 0
      else :
        row16 = row16 + 1
      amount = Martingle_Arr[row17]
    
    elif counter == 17 :
      if result == "WIN" :
        row17 = 0
      else :
        row17 = row17 + 1
      amount = Martingle_Arr[row18]
    
    elif counter == 18 :
      if result == "WIN" :
        row18 = 0
      else :
        row18 = row18 + 1
      amount = Martingle_Arr[row19]
    
    elif counter == 19 :
      if result == "WIN" :
        row19 = 0
      else :
        row19 = row19 + 1
      amount = Martingle_Arr[row20]
    
    elif counter == 20 :
      if result == "WIN" :
        row20 = 0
      else :
        row20 = row20 + 1
      amount = Martingle_Arr[row21]
    
    elif counter == 21 :
      if result == "WIN" :
        row21 = 0
      else :
        row21 = row21 + 1
      amount = Martingle_Arr[row22]
    
    elif counter == 22 :
      if result == "WIN" :
        row22 = 0
      else :
        row22 = row22 + 1
      amount = Martingle_Arr[row23]
    
    elif counter == 23 :
      if result == "WIN" :
        row23 = 0
      else :
        row23 = row23 + 1
      amount = Martingle_Arr[row24]
    
    elif counter == 24 :
      if result == "WIN" :
        row24 = 0
      else :
        row24 = row24 + 1
      amount = Martingle_Arr[row25]

    elif counter == 25 :
      if result == "WIN" :
        row25 = 0
      else :
        row25 = row25 + 1
      amount = Martingle_Arr[row26]

    elif counter == 26 :
      if result == "WIN" :
        row24 = 0
      else :
        row26 = row26 + 1
      amount = Martingle_Arr[row27]

    elif counter == 27 :
      if result == "WIN" :
        row27 = 0
      else :
        row27 = row27 + 1
      amount = Martingle_Arr[row28]

    elif counter == 28 :
      if result == "WIN" :
        row28 = 0
      else :
        row28 = row28 + 1
      amount = Martingle_Arr[row29]

    elif counter == 29  :
      if result == "WIN" :
        row29 = 0
      else :
        row29 = row29 + 1
      amount = Martingle_Arr[row30]

    elif counter == 30 :
      if result == "WIN" :
        row30 = 0
      else :
        row30 = row30 + 1
      amount = Martingle_Arr[row1]

  

    #file1 = open("test.txt", "a")
    #print("--------------------------------------------")
    #print("Amount :- " , amount)
    #amount_list.append(amount)
    #print("--------------------------------------------")
    #file1.write(x + " | ")
    #file1.write(" | " + result + " | ")
    #file1.write(" | " + str(row1) + " | ")
    #file1.write(" | " + str(lossCounter) + " | ")
    #file1.write(action + " | ")
    #file1.write(str(round(amount)))
    #total_Amt = total_Amt + amount
    #file1.write("\n")
    #file1.close()


    if counter == 1 :
      counter = 1
      print("counter" + str(counter))
    else :
      counter = counter + 1
      print("counter" + str(counter)) 

print(total_Amt)
print(final_win)
print(max(amount_list))
    
          