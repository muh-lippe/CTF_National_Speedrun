message=["75","5b","5f","12","4d","12","51","50","47","15","5b","58","42","5e","5b","46","12","18","60","5e","5b","45","14","5a","40","18","47","5a","52","19","53","5c","53","5f","02","14","77","50","59","55","7f","6d","70","6d","7f","48","44","06","53","04","7c","73","5c","69","0d","68","5e","0d","5a","0d","74","57","6d","67","03","45","54","05","5a","61","6f","0f","77","5f","02","70","04","50","44"]
pi='1415926535897932384626433832795028841971693993751058209749445923078164062862089'
for i in range(len(message)):
    message[i]=int(message[i], 16)

pi_list=[]
for j in pi :
    pi_list.append(j)

flag=[]
for i in range(len(message)):
    flag.append(str(hex(message[i]^ord(pi_list[i]))[2:]))

flag="".join(flag)

print(bytes.fromhex(flag))
