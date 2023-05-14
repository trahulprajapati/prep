
#input- abcdeefgejklee ,e

input = input()

string, char = input.split(',')

count = 0
for c in string:
    if c == char:
        count += 1

print(f'{char} is present {count} times')

[3:09 pm] Dhandar, Pooja Macchindra
emp: empid,empnm,salary,deptid -

[3:10 pm] Dhandar, Pooja Macchindra
dept: deptid,deptnm

[3:10 pm] Dhandar, Pooja Macchindra
deptnm,empnm,salary


select  emp.empnm, emp.salary, dept.deptnm from emp inner join dept on emp.deptid= dept.depid
group by dept.deptnm


select max(emp.salary), dept.deptnm from (select emp.salary, dept.deptnm from emp order by salary desc limit 2)
inner join  dept on emp.deptid= dept.depid



