#이런식으로 사용
#usage

#-------------------------------\
#REMOTE.py
def sum(a,b):
    retrurn a+b;

i = interface('localhost',5000)
i.set(func=sum)

#--------------------------------/


#-------------------------------\
#LOCAL.py
i = interface('localhost', 5000)
ret_json = i.get(func=sum, args='{"a": 1, "b":2}')

print ret_json
#"{'code': 200, 'return' : 3 }"

#--------------------------------/



