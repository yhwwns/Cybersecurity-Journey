# conditionals if statements

status = 100
if status == 200:
    print("OK")

status = 500
if status == "200":
    print("Updates needed")

#else if statements (precedes a condition that is only evaluated when previous condition evaluate to false)
elif status == "400":
    print("Bad request")
elif status == 500:
    print("Internal Server Error!")
else: 
    print("Check other status") 

#logical operators and or not (check for successful http response) and
if status <= 200 and  status >= 226: 
    print("Successful response")

#or
if status == 100 or status == 102:
    print("Gateway! Internal server err")

#not 
if not status == 100:
    print("Check the servers")


#run a for loop with range
for i in range(0,10):
    print("Firewall broken!")
