#Developed by Lance

#Getting the random library
import random 

#Initializing the length of password
length=10;

#Getting all the individual characters we want in our password
lower="abcdefghijklmnopqrstvuwxyz"
upper="QWERTYUIOPASDFGHJKKLZXCVBNM"
symbols=",./\';[]=-_+{}:?><"
numbers="1234567890"
all=lower+upper+symbols+numbers

#using the sample method of random for our combination
password="".join(random.sample(all,length))

#You now have a password
print(password)

#The program can be modified to accept the length of the password by prompting the user to enter it.