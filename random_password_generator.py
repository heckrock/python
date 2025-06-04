import random
print("*************************************")
print("* Welcome to the Password Generator *")
print("*************************************")
alphac_array=[]
specialc_array=[]
numc_array=[]
pass_array=[]
scrambled_pass=[]

for i in range(65,91):
    alphac_array.append(chr(i))
    #print(chr(i))

for i in range(97,123):
    alphac_array.append(chr(i))
    #print(chr(i))

for i in range(48,58):
    numc_array.append(chr(i))
    #print(chr(i))

for i in range(33,47):
    if i!=34 and i!=39:
        specialc_array.append(chr(i))
        #print(chr(i))

for i in range(58,65):
    specialc_array.append(chr(i))
    #print(chr(i))

for i in range(91,95):
    if i!=92:
        specialc_array.append(chr(i))
        #print(chr(i))    

alphac=int(input("How many letters are required? "))
specialc=int(input("How many special characters are required? "))
numc=int(input("How many numbers are required? "))

for i in range(alphac):
    pass_array.append(random.choice(alphac_array))

for i in range(specialc):
    pass_array.append(random.choice(specialc_array))

for i in range(numc):
    pass_array.append(random.choice(numc_array))


random.shuffle(pass_array)

secure_password=''.join(str(x) for x in pass_array)

print(f"The Secure Password is: {secure_password}")

