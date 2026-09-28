print("\n Welcome To The Data Analyzer And Transformer Program. ")

data = []

def input_Data():
    """1D Array and 2D Array """
    global data 
    print("select option :")
    print("1. 1D Array ")
    print("2. 2D Array ")
    
    num = input("Enter The Number (1 or 2)")

    if num == "1":
        num = input("Enter The Number (Separated By Spaces) : \n")
        data = list(map(int,num.split()))
        print ("Data been Stored Successfully!!")

    elif num == "2":
        row = int(input("Enter The Number Of Rows : "))
        Columns = int(input("Enter The Number Of Columns : "))
        
        data = []
        for n in range(row):
            n=[]
            for c in range(Columns):
                num = int(input("Enter a Number: "))
                n.append(num)
            data.extend(n)
            
        print("2D Array Are Store!")

        
def Summary(data):
    
    """Summary Of Data (1D and 2D)"""
    
    
    new_data = []

    for row in data:

        if type(row) == list:
            new_data.extend(row)
        else:
            new_data.append(row)

    print("\nData Summary")
    print(f"- Total Element :- {len(new_data)}")
    print(f"- Minimum Value :- {min(new_data)}")
    print(f"- Maximum Value :- {max(new_data)}")
    print(f"- Sum Of All Element :- {sum(new_data)}")
    print(f"- Average Value :- {sum(new_data) / len(new_data)}")


def fact(n):
    """Calculate the factorial of a number using recursion."""
    if n<=0:
        return 1
    return n*fact(n-1)
    
 
def Factorial():
    """Calculate the factorial of a number using recursion."""
    num = int(input("Enter a Number To Calculate Factorial :  "))
    print(f"Factorial of {num} is {fact(num)}")
    return num

def threshold(data):
    """Filter data based on a threshold value."""
    
    data_input = int(input("Enter A Threshold Value To Filter Out Data About This Value: \n "))
    print(f"Filtered Data (Values >= {data_input})")
    data_input = list(filter(lambda x : x > data_input , data ))
    print(data_input)

def sort(data):
    """Sort data in ascending or descending order."""
    print("Choice Sorting option : ")
    print("1. Ascending Order")
    print("2. Descending Order")
    
    choose = int(input("Enter Your Choice (1-2) : "))
    
    if choose == 1:
        accending= sorted(data)
        print(accending)
    elif choose == 2 :
        descending = sorted(data, reverse=True)
        print(descending)        

def data_statistics(data):
    """Calculate and return statistics of the data."""
    Minimum = min(data)
    maximum = max(data)
    total = sum(data)
    average = total/len(data)
    return Minimum,maximum,total,average

def statistics():
    """Display statistics of the data."""
    if len(data) == 0:
        print("No Data Store!")
        return 
    
    Minimum,maximum,total,average = data_statistics(data)
    print(f"-Minimun Value: {Minimum}")
    print(f"- Maximun Value: {maximum}")
    print(f"- Sum Of All Value: {total}")
    print(f"- Average  Value: {average}")
    print()


while True:
    print("\n === Main Menu === ")
    print("1. Input Data ")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data By Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Value) ")
    print("7. Exit ")
    
    
    choice = int(input("Please Enter Your Choice: "))
    
    if choice == 1 :
        input_Data()
    elif choice == 2 :
        Summary(data)
    elif choice == 3 :
        Factorial()
    elif choice == 4:
        threshold(data)
    elif choice == 5 :
        sort(data)
    elif choice == 6:
        statistics()
    elif choice == 7 :
        print("Thank You !!")
        break

    else:
        print("invalid Choice")