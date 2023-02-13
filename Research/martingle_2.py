

import jan
import feb
import march
import april
import may
import jun
import sep_jun
import july
import aug
import sep
import masterlist #octnovdec
    
#variables
#passes all month , master month also Martingle_Arr = [1,4,90,5,10,10,9,2,10,2,4,6,7,6,1,3,1,4,8,8]
Martingle_Arr = [12,5,9,5,5,4,5,4,10,2,4,6,7,6,10,3,1,4,8,8]


row1 = 0



amount_list = []
action = "RED"
lossCounter = 0
winCounter = 0
result = ""
default_Amt = 1
compundingAmt = 1
amount = 1 
martingle = False 
total_Amt = 0
final_win = 0
counter = 1
balance = 10000
sso_Pattern = [1,1,0,1,0,0]



for x in jan.list_jan:    
    #MM 
    if x == action :
        print("WIN")
        result = "WIN"
        lossCounter = 0
        winCounter = winCounter + 1
        action = action
        final_win = final_win + amount
        balance = balance + amount 
        if sso_Pattern[counter] == 1 :
            if action == "RED" :
                action = "RED"
            else :
                action = "GREEN"
        else :
            if action == "RED" :
                  action = "GREEN"
            else:
                  action = "RED"
    else :
        print("LOSS")
        result = "LOSS"
        winCounter = 0
        lossCounter = lossCounter + 1
        final_win = final_win - amount
        balance = balance - amount
        counter = counter + 1
        if counter > 5 :
              counter = 1
        if sso_Pattern[counter] == 1 :
            if action == "RED" :
                action = "RED"
            else :
                action = "GREEN"
        else :
            if action == "RED" :
                  action = "GREEN"
            else:
                  action = "RED"      


    if balance < 0 :
      print("blownup")
      exit()

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
    
 

    amount_list.append(amount)
    total_Amt = total_Amt + amount

     
    file1 = open("EURUSD.txt", "a")
    file1.write(x + " | ")
    file1.write(" | " + result + " | ")
    file1.write(action + " | ")
    file1.write(str(amount))
    file1.write(" | " + str(balance) + " | ")
    file1.write("\n")
    file1.close()


print("total volumer :- ", total_Amt)
print("final Win :- ", final_win)
print("max amount :- " , max(amount_list))
print("FInal Bal :- ",balance)
    
          