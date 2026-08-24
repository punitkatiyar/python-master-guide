# loop with list
# example 1
# techs=["A","B","C","D","E"]
# print(techs[0])

# for i in techs:
#     print(i)

# example 2

# for index,tech in enumerate(techs):
#     print(index+1,tech)


# example 3 zip()

# modules=["10Hr","12Hr","15Hr","20Hr","25Hr"]

# for tech,module in zip(techs,modules):
#     print(tech,module)


nums=[1,2,3,4,5,6]

res=0

for num in nums:
    res+=num

print(res)

