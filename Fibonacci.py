def isFibonacci(inputNumber):
   firstTerm:int=0
   secondTerm: int=1
   thirdTerm:int=0
   while (thirdTerm < inputNumber):
       thirdTerm = firstTerm + secondTerm
       firstTerm = secondTerm
       secondTerm = thirdTerm
   if(thirdTerm==inputNumber):
    return "Yes"
   else:
    return "No"

inputNumber=5
if(isFibonacci(inputNumber) == "Yes"):
         print (inputNumber,"is a Fibonacci Number")
else:
         print (inputNumber,"is a not Fibonacci Number ")

