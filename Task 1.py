fh=open('salary.txt','w')
symbols_written = fh.write('Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000')

def total_salary(path):
    try:
        total_salary=0
        num_developers = 0
        with open(path, 'r', encoding = 'utf-8') as file:
            for line in file:
                data=line.strip().spilt(',')
                if len(data)==2:
                    salary=int(data[1])
                    total_salary +=salary
                    num_developers +=1
                else:
                    print(f"Error in formate line :{line}")
            if num_developers>0:
                average_salary = total_salary/num_developers
                return total_salary, average_salary
            else:
                return 0,0
    except FileNotFoundError:
        print("File is not found")
        return 0,0
    except Exception as e:
        print(f"Error :{e}")
        return 0,0
 
 from pathlib import Path
 path= Path("goit-algo-hw-04/salary.txt")
 abs_path=path.absolute()
 print(abs_path)  

total, average = total_salary("goit-algo-hw-04/to/salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
   

