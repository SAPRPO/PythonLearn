
def build_profile(first,last,**user_info):  #**user_info - empty dictionary
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info

user_profile=build_profile('ivan','ivanov',location='moscow',field='programmer', sex='male')
print (user_profile)