class Animal:
    name = ''
    weight = 0
    food = 0
    all_animals = {}

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.all_animals[self.name] = self.weight
        self.representatives.append(self.name)

    def eat(self, food):
        self.weight += food
        print(f'{self.name} накормлен')
        print(f'Вес {self.name} {self.weight} кг.')
        self.all_animals[self.name] = self.weight


class GiveEggs(Animal):
    def collect_eggs(self, count):
        print(f'{self.name} снесла {count} яиц')


class Goose(GiveEggs):
    voice = 'Га-га-га'
    representatives = []


class Chicken(GiveEggs):
    voice = 'Ко-ко-ко'
    representatives = []


class Duck(GiveEggs):
    voice = 'Кря-кря-кря'
    representatives = []


class GiveMilk(Animal):
    def milking(self, volume):
        print(f'{self.name} дала {volume} литра(ов) молока')
        self.weight -= volume
        self.all_animals[self.name] = self.weight


class Cow(GiveMilk):
    voice = 'Му-му-му'
    representatives = []


class Goat(GiveMilk):
    voice = 'Ме-ме-ме'
    representatives = []


class GiveWool(Animal):
    def haircut(self, value):
        print(f'{self.name} пострижена')
        self.weight -= value
        self.all_animals[self.name] = self.weight


class Sheep(GiveWool):
    voice = 'Бе-бе-бе'
    representatives = []


goose_1 = Goose('Серый', 5)
print(goose_1.voice)
goose_1.eat(0.5)
goose_1.collect_eggs(3)
print()

goose_2 = Goose('Белый', 4)
print(goose_2.voice)
goose_2.eat(0.7)
goose_2.collect_eggs(2)
print()

cow_1 = Cow('Манька', 100)
print(cow_1.voice)
cow_1.eat(10)
cow_1.milking(5)
print()

sheep_1 = Sheep('Барашек', 50)
print(sheep_1.voice)
sheep_1.eat(10)
sheep_1.haircut(1)
print()

sheep_2 = Sheep('Кудрявый', 55)
print(sheep_2.voice)
sheep_2.eat(10)
sheep_2.haircut(1.8)
print()

chicken_1 = Chicken('Ко-Ко', 2)
print(chicken_1.voice)
chicken_1.eat(0.1)
chicken_1.collect_eggs(1)
print()

chicken_2 = Chicken('Кукареку', 1.5)
print(chicken_2.voice)
chicken_2.eat(0.3)
chicken_2.collect_eggs(2)
print()

goat_1 = Goat('Рога', 25)
print(goat_1.voice)
goat_1.eat(3)
goat_1.milking(1.5)
print()

goat_2 = Goat('Копыта', 22)
print(goat_2.voice)
goat_2.eat(3)
goat_2.milking(1.9)
print()

duck_1 = Duck('Кряква', 3)
print(duck_1.voice)
duck_1.eat(0.3)
duck_1.collect_eggs(1)
print()

heaviest = ''
weight = 0
all_weight = 0

for key, value in Animal.all_animals.items():
    all_weight += value
    if value > weight:
        heaviest = key
        weight = value

print(f'Общий вес животных на ферме - {all_weight} кг.')
print(f'Самое тяжелое животное - {heaviest}')