class Kareler:
    def __init__(self, max):
        self.max = max
  
    def __iter__(self):
        self.n = 1
        return self
    
    def __next__(self):
        if self.n <= self.max:
            val = self.n * self.n
            self.n +=1
            return val
        else:
            raise StopIteration


kare = Kareler(5)

iteration = iter(kare)

print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))
