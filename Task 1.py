import sys

def total_salary(path):
    try:
        total_salary = 0
        num_developers = 0
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 2:
                    try:
                        salary = int(data[1])
                    except ValueError:
                        print(f"Error: Invalid salary format in line: {line}", file=sys.stderr)
                        continue
                    total_salary += salary
                    num_developers += 1
                else:
                    print(f"Error: Invalid format in line: {line}", file=sys.stderr)
            if num_developers > 0:
                average_salary = total_salary / num_developers
                return total_salary, average_salary
            else:
                return 0, 0
    except FileNotFoundError:
        print("Error: File is not found", file=sys.stderr)
        return 0, 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 0, 0

total, average = total_salary("C:\\Users\\maria\\OneDrive\\Documents\\GitHub\\goit-algo-hw-04\\salary.txt")
print(f"Total salary: {total}, Average salary: {average}")

   

