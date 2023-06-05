
# FROM python3.7
# COMMAND:
#     RUN /opt/python/bin/python/activate
# RUN:
#     python manage.py runserver
# EXPOSE: 8080
# cp . .
# RUN


# SERVICE:
#     dbss
#     mysqlk
#     redis
#


# 10.10.21.11
# 10.10.


input = [2, 5, 6, 3, 5, 7, 3, 5, 6, 3, 5, 7, 6]

indexs = []
print(input)
for number in range(len(input)):
    if input[number] == 3:
        indexs.append(number)

for i in indexs:
    input.remove(3)
    input.append(3)

print(input)



input = [4,6,8,4,1,9]

output = [6*8*4*1*9, 4*8*4*1*9, 4*6*4*1*9, 4*6*8*1*9, 4*6*8*4*9, 4*6*8*4*1]

def get_prod(ignore, li):
    prod = 1
    for i in range(len(li)):
        if i != ignore:
            prod = prod*li[i]
    return prod

output = []
for i in range(len(input)):
    output.append(get_prod(i, input))

print(output)


