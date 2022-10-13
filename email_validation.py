email=input('Enter your email address: ') # g@g.in
j,k,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ('@' in email) and (email.count('@')==1):
            if (email[-3]=='.') ^ (email[-4]=='.'):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=='_' or i=='.' or i=='@':
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print('Wrong email address')
            else:
                print('Wrong email address because . is not placed correctly')
        elif email.count('@')>1:
            print('Wrong email address. @ should not be greater than 1')
        else:
            print('Wrong email address because there is no @ in the email address')
    else:
        print('Wrong email address because first character is a digit')
else:
    print('Wrong email address because the lenght of email is not greater than or equal to 6')

