class CachedSum:

    def __init__(self, value):
        self.value = value
        self.calculatedValue = None
        self.use_count = 0

    def get_calculated_value(self):
        if self.calculatedValue is None:
            print("value will calculate")
            self.calculatedValue = 0
            for number in self.value:
                self.calculatedValue += number
        return self.calculatedValue


class Cache:

    def __init__(self, limit):
        self.limit = limit
        self.values = {}
        self.values_by_use = []

    def get_cached_value(self, value):
        cachedValue = self.values.get(value)
        if cachedValue is None:
            if len(self.values_by_use) >= self.limit + 1:
                unusedValue = self.values_by_use[len(self.values_by_use) - 1]
                self.values.pop(unusedValue.value)
                self.values_by_use.remove(unusedValue)

            cachedValue = CachedSum(value)
            self.values[value] = cachedValue
            self.values_by_use.append(cachedValue)
        else:
            cachedValue.use_count += 1

        self.values_by_use.sort(key=lambda cachedValue: cachedValue.use_count, reverse=True)
        return cachedValue

class Calculator:

    def __init__(self, limit):
        self.cache = Cache(limit=limit)

    def sum(self, *args):
        value = self.cache.get_cached_value(value=args)
        return value.get_calculated_value()



calculatorOfGods = Calculator(limit=2)
print(calculatorOfGods.sum(1,2))
print(calculatorOfGods.sum(3,2))
print(calculatorOfGods.sum(1,2))
print(calculatorOfGods.sum(1,5))
print(calculatorOfGods.sum(1,5))
print(calculatorOfGods.sum(1,6))
print(calculatorOfGods.sum(1,6))
print(calculatorOfGods.sum(1,7))
print(calculatorOfGods.sum(1,7))

print(calculatorOfGods.sum(3,2))

