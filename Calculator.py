import json

def get_input(filename):
    results={}
    try:
        with open(filename, 'r') as f:
            print(f"The file({filename}) is being printed below...")
            print("x----x----x")
            lines = f.readlines()
            for l in lines:
                print(l.rstrip())
                if("Add" in l):
                    results["addition"] = addition(l.rstrip())
                elif("Sub" in l):
                    results["subtraction"] = subtraction(l.rstrip())
                elif("Mul" in l):
                    results["multiplication"] = multiplication(l.rstrip())
                elif("Div" in l):
                    results["division"] = division(l.rstrip())  
                elif("Mod" in l):
                    results["modulus"] = modulus(l.rstrip())
                else:
                    print("Wrong choice!")
    except Exception:
        print("Error! can't find file")
    else:
        print("x----x----x")
        print("Read the file and got the input")
        with open("Results.json",'w') as f:
            json.dump(results, f)

def addition(l):
    l_arr=l.split(' ')
    for i in l_arr:
        if i.isdigit() == True:
            add_res = int(i) + int(l_arr[-1])
            break
    return add_res  

def subtraction(l):
    l_arr=l.split(' ')
    for i in l_arr:
        if i.isdigit() == True:
            sub_res = int(i) - int(l_arr[-1])
            break
    return sub_res
        
    
def multiplication(l):
    l_arr=l.split(' ')
    for i in l_arr:
        if i.isdigit() == True:
            mul_res = int(i) * int(l_arr[-1])
            break
    return mul_res
        

def division(l):
    l_arr=l.split(' ')
    for i in l_arr:
        if i.isdigit() == True:
            div_res = int(i) // int(l_arr[-1])
            break
    return div_res
        
def modulus(l):
    l_arr=l.split(' ')
    for i in l_arr:
        if i.isdigit() == True:
            mod_res = int(i) % int(l_arr[-1])
            break
    return mod_res
        

def display_output(filename):
    
    with open(filename) as f:
        results = json.load(f)
        for k,v in results.items():
            print(f"{k} : {v}")
    

if __name__ == '__main__':
    get_input("calculator_input.txt")
    display_output("Results.json")
    