
# def print_hello(name):
#     print('hello ', name)

# print_hello('ddd')

# def factorial(x):
#     """dasdasdasd"""
#     answer = 1
#     for i in range(1, x + 1):
#         answer *= i
#     return answer

# for x in range(1, 10 + 1):
#     print(str(x) +'\t!%x\t' + str(factorial(x)))

# def create_record(name, telephone, adress):
#     record = {
#         'name': name,
#         'phone': telephone,
#         'adress': adress
#     }
#     return name, telephone

# user1 = create_record('pasha', '+23123', 'gomel')
# user2 = create_record('faf', '+22352123', 'osfsefel')
# print(user1)
# print(user2)

def give_award(award, *name):
    for peson in name:
        print('afa', peson.title(), 'медаль', award)
give_award('za stalina', 'pasha', 'dima')