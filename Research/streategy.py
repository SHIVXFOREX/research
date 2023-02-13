import nov
import sep
import oct
import dec
import masterlist
    



action = "RED"
lossCounter = 0
lossCounter_list = []
winCounter = 0
winCounter_list = []
result = ""
counter = 1
work = False


for x in  masterlist.list_oct_nov_dec :    
    #MM 
    if x == action :
        print("WIN")
        result = "WIN"
        lossCounter = 0
        winCounter = winCounter + 1
        winCounter_list.append(winCounter)
        action = action
    else :
        print("LOSS")
        result = "LOSS"
        winCounter = 0
        lossCounter = lossCounter + 1
        lossCounter_list.append(lossCounter)
        
    

    if counter == 3 :
      action = "RED"
      counter = 1
    else : 
      action = "GREEN"
      counter  = counter + 1     
    

print("max win:- ", max(winCounter_list))
print("max loss :- ", max(lossCounter_list))
          