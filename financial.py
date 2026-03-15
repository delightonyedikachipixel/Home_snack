loan_amount = int(input("Enter loan amount:"))
years = int(input("Enter the loan duration:"))
total_months = years * 12
rate = 5.0
while rate <= 10.00:
    monthly_rate = rate/ 100/12
    monthly_payment = (loan_amount * monthly_rate)/ \
        (1-(1+monthly_rate)**(-total_months))
    total_payment = monthly_payment * total_months
    print (rate , monthly_payment, total_payment)






