#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

x= input("Welcome to the tip calculator . Please write the bill: ")  #str . "type" komutuyla kontrol ettim
y= input("How many people will pay: ") #str
tip= input("What is the tip percentage :")
x1=float(x)
y1=float(y)
tip1=float(tip)/100
bill_per_person=((x1+x1*tip1)/y1)    #aslında sonuç bu, yani kişi başına düşeni burda buluyoruz
final_amount=round(bill_per_person, 2)         #ancak son 2 basamağını yuvarlamamızı istediğinden round yaptık

print(f"Each person should pay:  {final_amount}")
