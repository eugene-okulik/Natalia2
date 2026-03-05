import operator


class Flower:
    def __init__(self, name, freshness, length, price, lifespan):
        self.name = name
        self.freshness = freshness
        self.length = length
        self.price = price
        self.lifespan = lifespan

    def __str__(self):
        return (f' Flower name = {self.name}, freshmess = {self.freshness} days,'
                f' length = {self.length}, price = {self.price} euro, life = {self.lifespan} days')

    def __repr__(self):
        return (f' Flower name = {self.name}, freshmess = {self.freshness} days,'
                f' length = {self.length}, price = {self.price} euro, life = {self.lifespan} days')


class Rose(Flower):
    def __init__(self, freshness, length, price, lifespan, color):
        super().__init__('rose', freshness, length, price, lifespan)
        self.color = color


class Peony(Flower):
    def __init__(self, freshness, length, price, lifespan, country):
        super().__init__('peony', freshness, length, price, lifespan)
        self.country = country


first_rose = Rose(3, 15, 55, 10, 'red')
second_rose = Rose(2, 16, 53, 11, 'white')
first_peony = Peony(2, 20, 25, 5, 'Holland')
second_peony = Peony(1, 19, 21, 6, 'Greece')
third_peony = Peony(4, 21, 56, 3, 'Cyprus')


class Bunch:
    def __init__(self, flowers):
        self.flowers = flowers
        self.avg_life = self.average_life()

    def total_price(self):
        summa = 0
        for i in self.flowers:
            summa += i.price
        return summa

    def average_life(self):
        return round(sum(i.lifespan for i in self.flowers) / len(self.flowers), 2)

    def sort_by(self, key):
        return sorted(self.flowers, key=operator.attrgetter(key))

    def find_by_life(self):
        return [f for f in self.flowers if f.lifespan >= self.avg_life]


print(first_rose)
print(second_rose)
print(first_peony)
print(second_peony)
print(third_peony)
bouquet = Bunch([first_rose, second_rose, first_peony, second_peony, third_peony])
print(bouquet.total_price())
print(bouquet.average_life())
print(bouquet.sort_by('price'))
print(bouquet.sort_by('length'))
print(bouquet.sort_by('freshness'))
print(bouquet.find_by_life())
