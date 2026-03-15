sum_number = 0
sum_even = 0
sum_odd = 0
sum_square_even = 0
sum_square_odd = 0


for number in range(1,11):
    number = int(input("Enter a number:"))
    sum_number += number
   
   
    
    if number % 2 == 0:
        print ("even")
        print(number*number)
        sum_even += number
        

      
        

    else:
        print ("odd")
        print (number*number)
        sum_odd += number
       

print ("The sum of number is ", sum_number)
print ("The sum of even  number is ", sum_even)
        
sum_square_even += number
   
print ("The sum square of even  number is ", sum_square_even)
print ("The sum of odd  number is ", sum_odd)
sum_square_odd += number
print ("The sum square of odd  number is ", sum_square_odd)


    


 
   

   

    


