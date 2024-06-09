class FirstUnique:
    def __init__(self, nums):
        self.queue = []
        self.freq = {}
        self.unique = set()
        
        for num in nums:
            self.add(num)
    
    def showFirstUnique(self):
        while self.queue and self.freq[self.queue[0]] > 1:
            self.queue.pop(0)
        
        return self.queue[0] if self.queue else -1
    
    def add(self, value):
        self.queue.append(value)
        if value in self.freq:
            self.freq[value] += 1
        else:
            self.freq[value] = 1
        if self.freq[value] == 1:
            self.unique.add(value)
if __name__ == "__main__":
    first_unique = FirstUnique([2, 3, 5])
    print(first_unique.showFirstUnique()) 
    first_unique.add(5)
    print(first_unique.showFirstUnique())  
    first_unique.add(2)
    print(first_unique.showFirstUnique())  
    first_unique.add(3)
    print(first_unique.showFirstUnique())