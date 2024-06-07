class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age


class Dog(Animal):
    def __init__(self, species, age):
        super().__init__(species, age)
        


class Cat(Animal):
    def __init__(self, species, age):
        super().__init__(species, age)
       


choice = input("Хотите создать собаку или кошку? Введите 'собака' или 'кошка': ")

if choice.lower() == 'собака':
    dog_species = input("Введите вид собаки: ")
    dog_age = int(input("Введите возраст собаки: "))

    dog = Dog(dog_species, dog_age)
    print(f'Собака: Вид - {dog.species}, Возраст - {dog.age}')

elif choice.lower() == 'кошка':
    cat_species = input("Введите вид кошки: ")
    cat_age = int(input("Введите возраст кошки: "))
    
    cat = Cat(cat_species,cat_age)
    print(f'Кошка: Вид - {cat.species}, Возраст - {cat.age}')
else:
    print("Ошибка: неправильный выбор животного. Пожалуйста, выберите 'собака' или 'кошка'.")