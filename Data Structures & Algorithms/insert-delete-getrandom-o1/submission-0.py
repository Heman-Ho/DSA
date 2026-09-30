import random 

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.num_to_i = {}

    def insert(self, val: int) -> bool:
        if val in self.num_to_i:
            return False
        self.nums.append(val)
        self.num_to_i[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.num_to_i:
            return False
        target_i = self.num_to_i.pop(val)
        if len(self.nums) != 1:
            self.num_to_i[self.nums[-1]] = target_i
            self.nums[target_i], self.nums[-1] = self.nums[-1], self.nums[target_i]
            
        self.nums.pop()
        return True


    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()