'''
1. Password should be at least 8 char length.
2. At least 1 Upper case.
3. At least 1 Lower case.
4. At least 1 number.
5. At least 1 special char.
'''

import random
alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = [1,2,3,4,5,6,7,8,9,0]
specialChar = ['!','@','#','$','%','^','&','*','?']
ran_1 = random.choice(alphabets)+random.choice(small)+str(random.choice(numbers))+random.choice(specialChar)
ran_2 = random.choice(alphabets)+random.choice(small)+str(random.choice(numbers))+random.choice(specialChar)
print('Your Random password: ',ran_1+ran_2)
