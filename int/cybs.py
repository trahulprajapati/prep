
#
# *****
#  ***
#   *

#       * *  * * *
#      <> * * *  <>
#      <>  * * <>
#      <> <> * <>


n = 8
o = 0
for i in range(n, 0, -2):
    k = 0
    while k < o:
        print(" ", end='')
        k +=1
    for j in range(0, i):
        print("*", end='')
    k = 0
    while k < o:
        print(" ", end='')
        k+=1
    print('\n')
    o += 1

