import pathlib

def total_salary(path:str) -> tuple[float, float]:
    '''returns tuple (total, average) salary'''
    salary_path = pathlib.Path(path) # getting salary doc
    
    with open(salary_path, 'r', encoding="utf-8") as s:
        name_salary = [line.strip().split(',') for line in s.readlines() if ',' in line] # create list of salaries 
    
        try:
            salary = [float(money[1]) for money in name_salary]  # extract salaries and convert to float
        except (ValueError, IndexError):
            raise ValueError(f'Please, {salary_path}. Failed to convert the salary into a number. ') # return error if found 
        
        total = sum(salary) 
        average = total / len(salary)
        return (total, average)

total, average = total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
