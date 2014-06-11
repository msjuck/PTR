#이런식으로 사용
#usage

#-------------------------------\

def sum(a,b):
    retrurn a+b;

i = interface(func=sum)

#--------------------------------/


#-------------------------------\

i = interface()
ret_json = i.get(func=sum, args='{"a": 1, "b":2}')

print ret_json
#"{'code': 200, 'return' : 3 }"

#--------------------------------/



