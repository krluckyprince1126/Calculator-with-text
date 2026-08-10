
HISTORY="history.txt"
def history():
    file=open(HISTORY,"r")
    lines=file.readlines()
    if len(lines)==0:
        print("NO HISTORY FOUND")
    else:
        for i in reversed(lines):
            print(i.strip())

    file.close()
def clear_history():
    file=open(HISTORY,"w")
    file.close()
    print("HISTORY CLEARED.")
result = None
user_input = None
def save_history(equation,result):
    file=open(HISTORY,"a")
    file.write(equation + "=" + str(result)+"\n")

def calculator(user_input):
    global result
    parts=user_input.split()
    if len(parts)==3:
        num1=float(parts[0])
        op=parts[1]
        num2=float(parts[2])
        
        if op=="+":
            result=num1+num2
        elif op=="-":
            result=num1-num2
        elif op=="*":
            result=num1*num2
        elif op == "/":
            if num2 == 0:
                print("Cannot divide by zero")
            else:
                result = num1 / num2
        else:
            print("Invalid operator")
            
        
    
    else:
        print("INVlid input. use formate x+y")
         
while True:
    print("Enter 1 for calculation ")
    print("Enter 2 for History ")
    print("Enter 3 for Clear histroy ")
    print("Enter 4 save histroy ")
    print()
    user_choice=input("Enter your choice :")
    if user_choice=="1":
        user_input=input("Enter operation for calculate :")
        calculator(user_input)
    elif user_choice=="2":
        history()
    elif user_choice=="3":
        clear_history()
    elif user_choice=="4":
        save_history(user_input,result)
    else:
        print("Please enter a valid input ")
print("THANKYOU")