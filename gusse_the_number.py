a = 55 
num_gusses =  9
count = 0
while True:
	x = int(input("gusse the number = "))
	if a < x:
	  num_gusses = num_gusses - 1
	  count = count+1
	  print("you enter greater number you left ", num_gusses ,"attempt")
	elif a > x:
	   count = count+1
	   num_gusses = num_gusses - 1
	   print("you enter less number " , num_gusses ,"you left") 
	elif a==x :
		 count = count+1
		 print("congrates you won!!! you complet the task in" , count , "stseps\n you have left the chance", num_gusses)
		 break
	elif num_gusses ==0 :  
         print("game over!!") 
		 