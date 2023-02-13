

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
Martingle_Arr = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384]
Reg_Arr = [2,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]


row1 = 0
Reg_row = 0



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
counter = 0
balance = 10000
correctionAmt = 0
sso_Pattern = [1,0,1,0,1,0]
maxLoss = 0
maxWin = 0
stoploss = 1900



for x in jan.list_jan:    
    #MM 
    if x == action :
        result = "WIN"
        lossCounter = 0
        winCounter = winCounter + 1
        action = action
        correctionAmt = amount * 0.2
        final_win = final_win + amount - correctionAmt
        balance = balance + amount - correctionAmt
    else :
        result = "LOSS"
        winCounter = 0
        lossCounter = lossCounter + 1
        final_win = final_win - amount
        balance = balance - amount
        counter = counter + 1
     

    if balance < 0 :
      print("blownup")
      exit()

    if maxLoss < lossCounter :
        maxLoss = lossCounter
    

   #AM
    if result == "WIN" :
        if winCounter > 1 :
            compundingAmt = default_Amt
            amount = default_Amt
        if winCounter == 1 :
            if compundingAmt > stoploss :
                compundingAmt = default_Amt
                amount = default_Amt 
            else :
                amount = compundingAmt * 0.19 + compundingAmt
        else :
            amount = default_Amt
    else :
        compundingAmt = compundingAmt + amount
        amount = default_Amt * 0.19 + default_Amt
        
        
 

    amount_list.append(amount)
    total_Amt = total_Amt + amount

     
 #   file1 = open("EURUSD.txt", "a")
  #  file1.write(x + " \t ")
 ##  file1.write(action + " \t ")
  #  file1.write(str(correctionAmt) + " \t ")
  #  file1.write(str(amount))
  #  file1.write(" \t " + str(balance) + " \t ")
  #  file1.write("\n")
  #  file1.close()


print("total volumer :- ", total_Amt)
print("final Win :- ", final_win)
print("Compunding AMt :- ", compundingAmt)
print("max amount :- " , max(amount_list))
print("FInal Bal :- ",balance)
print("Max Loss :- ",maxLoss)
    
          