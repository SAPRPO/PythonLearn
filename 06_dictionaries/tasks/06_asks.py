favourite_languages = {
'jen' : 'python',
'sarah' : 'с',
'edward' : 'rust',
'phil' : ' python',
'alex' : 'java',
'mike' : 'go',
'greg' : 'c++',
'ann' : 'c#',
}

new_users = ['jen','sarah','john', 'greg', 'alex', 'lucy', 'ann']
count = 1
for name, language in favourite_languages.items():
    #print(f'{name.title()} prefers language {language.title()}')
    
    if name in new_users:
        print(f'{count}. {name.title()}, thank you for speaking! Your favourite language {language.title()}')
        count +=1
    else:
        print(f'{count}. {name.title()}, want to speak about languages!')
        count +=1
