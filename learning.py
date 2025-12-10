class Numbers:

    def even_odd(self, start, end):
        for num in range(start, end):
            if num%2==0:
                print(f"{num} is even")
            else:
                print(f"{num} is odd")

    def prime_num(self):
        pass

    
num = Numbers()
num.even_odd(100, 200)

print("Hello world!")

