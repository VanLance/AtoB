test = {'abc':123}
class Test:
    def __init__(self):
        self.abc = True
my_test = Test()
print(my_test.abc)

print(''.join(a for a in dir(my_test) if my_test.a == True))