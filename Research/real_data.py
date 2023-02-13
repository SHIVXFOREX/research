import eurusdotc 
import jan
import feb
import march
import april
import may
import jun
import july
import aug
import sep
import oct
import nov
import dec
    


amount_list = []
action = "RED"
lossCounter = 0
winCounter = 0
result = ""
default_Amt = 30
amount = 10
total_Amt = 0
final_win = 0
counter = 1
balance = 5000
lossper = 0
command = False
row1 = 0





for x in eurusdotc.list_28jan:    
    #MM 
    if x == "WIN" :
        result = "WIN"
        lossCounter = 0
        winCounter = winCounter + 1
        action = action
        lossper = amount * 0.15
        final_win = final_win + amount - lossper
        balance = balance + amount - lossper
    else :
        result = "LOSS"
        winCounter = 0
        lossCounter = lossCounter + 1
        final_win = final_win - amount
        balance = balance - amount
        if command :
          if action == "RED" :
             action = "GREEN"
          else :
             action = "RED"
    

    if balance > 5100 :
        print("sucess")
        break
   
   #AM
    if result == "WIN" :
         amount = amount * 2.1
    else :
        amount = default_Amt



    amount_list.append(amount)
    total_Amt = total_Amt + amount
    counter = counter + 1
    

     
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
print(counter)
    
          