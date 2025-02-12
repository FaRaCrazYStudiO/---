print('Правила игры:')
print('Ты можешь произвадить и продовать ресурсы')
print('в это beta игре нет кнопак сохранить и загрузить')
print('Если Вы хотите поддержать автора, то вот вам ссылка на boosty: https://boosty.to/farazerelli_firm_production')
print('Приятной Вам игры!')
class Company:
    def __init__(self, name):
        self.name = name
        self.money = 1000  # Начальные деньги
        self.products = {
            'водка': 0,
            'пиво': 0,
            'коньяк': 0,
            'хлеб': 1,
            'вода': 1,
            'книги': 1, 
            'транспортные услуги': 1, 
            'коммунальные услуги': 0, 
            'карандаши': 1, 
            'монитор': 1, 
            'мышки': 1, 
            'компьютеры': 1, 
            'клавиатура': 1, 
            'вино': 0, 
            'виски': 0,
            'сериалы 2Д': 0,
            'сериалы 3Д': 0,
            'мультики': 0,
            'драмы': 0,
            'комедии': 0,
            'золото': 0,
            'природный газ': 0,
            'нефть': 0,
            'каменный уголь': 0,
            'алмаз': 0,
            'рубин': 0,
            'изумруд': 0,
            'музыка': 0,
            'инструменты': 0,

        }
        self.sold = {
            'водка': 0,
            'пиво': 0,
            'коньяк': 0,
            'хлеб': 0,
            'вода': 0,
            'книги': 0, 
            'транспортные услуги': 0, 
            'коммунальные услуги': 0, 
            'карандаши': 0, 
            'монитор': 0, 
            'мышки': 0, 
            'компьютеры': 0, 
            'клавиатура': 0, 
            'вино': 0, 
            'виски': 0,
            'сериалы 2Д': 0,
            'сериалы 3Д': 0,
            'мультики': 0,
            'драмы': 0,
            'комедии': 0,
            'золото': 0,
            'природный газ': 0,
            'нефть': 0,
            'каменный уголь': 0,
            'алмаз': 0,
            'рубин': 0,
            'изумруд': 0,
            'музыка': 0,
            'инструменты': 0,
        }

    def produce(self, product, amount):
        if self.money < amount * 100:  # Стоимость производства 100 рублей за продукт
            print("Не хватает средств для производства.")
            return

        self.money -= amount * 100
        self.products[product] += amount
        print(f"Произведено {amount} {product}. Текущий запас: {self.products[product]} {product}.")

    def produce(self,золото,amount):
        if self.money < amount * 1000:  # Стоимость производства 1000 рублей за золото
            print("Не хватает средств для производства.")
            return

        self.money -= amount * 1000
        self.products[золото] += amount
        print(f"Произведено {amount} {золото}. Текущий запас: {self.products[золото]} {золото}.")

    def produce(self,алмаз,amount):
        if self.money < amount * 10000:  # Стоимость производства 1000 рублей за золото
            print("Не хватает средств для производства.")
            return

        self.money -= amount * 10000
        self.products[алмаз] += amount
        print(f"Произведено {amount} {алмаз}. Текущий запас: {self.products[алмаз]} {алмаз}.")
        

    def sell(self, product, amount):
        if self.products[product] < amount:
            print(f"Недостаточно {product} для продажи.")
            return

        self.products[product] -= amount
        self.sold[product] += amount
        self.money += amount * 150  # Продаем по 150 рублей за продукт
        print(f"Продано {amount} {product}. Текущие деньги: {self.money}.")

    def sell(self, золото, amount):
        if self.products[золото] < amount:
            print(f"Недостаточно {золото} для продажи.")
            return

        self.products[золото] -= amount
        self.sold[золото] += amount
        self.money += amount * 1500  # Продаем по 1500 рублей за продукт
        print(f"Продано {amount} {золото}. Текущие деньги: {self.money}.")


        # Проверка на премию
        if self.sold['золото'] == 10:
            self.money += 10000  
            print(f"'Атчивка', /n 'Поздравляем! Санитары с дипломами говорят: У вас золотая лихорадка! За это вам премия 10000 рублей!'")

        elif self.sold['монитор'] == 100 and self.sold['компьютеры'] == 100 and self.sold['мышка'] == 100 and self.sold ['клавиатура'] == 100:
            self.money += 10000
            print("'Атчивка', /n 'Поздравляем! Вы стали огромным компьютерным магнатом по типу Microsoft или Apple! За это вам премия 10000 рублей!'" )

        elif self.sold['вино'] == 100 and self.sold ['виски'] == 100 and self.sold['водка'] == 100 and self.sold ['пиво'] == 100 and self.sold ['коньяк'] == 100:
            self.money + 10000
            print("'Атчивка', /n 'Поздравляем! Вы стали огромной Алкотой! За это вам премия 10000 рублей!'" )

        elif self.sold['коммунальные услуги'] == 100 and self.sold ['транспортные услуги',] == 100:
            self.money + 10000
            print("'Атчивка', /n 'Поздравляем! Вы стали огромной медвежьей услугой! За это вам премия 10000 рублей!'" )

        elif self.sold['сериалы 2Д'] == 100 and self.sold ['сериалы 3Д'] == 100 and self.sold ['мультики'] == 100 and self.sold ['драмы'] == 100 and self.sold  ['комедии'] == 100:
            self.money + 10000
            print("'Атчивка', /n 'Поздравляем! Вы стали как Netflix! Снимаете игру в кальмара и одебиливающие мультики для детей! За это вам премия 10000 рублей!'" )

        elif self.sold['книги'] == 1000 and self.sold ['карандаши',] == 1000:
            self.money + 100
            print("'Атчивка', /n 'Поздравляем! Вы создали ОГЭ и ЕГЭ! За вами объявлена охота! За это вам премия 100 рублей!'" )


    def check_game_over(self):
        if self.money <= 0:
            return True    
        for product, count in self.products.items():
            if count < 1000:
                return False
        print("Поздравляем! Вы достигли 1000 товаров каждого вида! Ого! Я даже это не прошёл бы!")
        return True

def main():
    name = str(input("Введите название вашей компании: "))
    company = Company(name)

    while True:
        print(f"\nВаши деньги: {company.money}")
        print(f"Запасы: {company.products}")
        action = input("Выберите действие: (1 - Производить, 2 - Продавать, 3 - Проверить окончание игры, 0 - Выйти): ")

        if action == '1':
            product = input("Какой продукт производить? (водка, пиво, коньяк, хлеб, воду, книги, транспортные услуги, коммунальные услуги, карандаши, мониторы, мышки, компьютеры, клавиатуры, вино, виски, сериалы 2Д, сериалы 3Д, мультики, драмы, комедии, золото, природный газ, нефть, каменный уголь, алмаз, рубин, изумруд, музыка, инструменты): ")
            amount = int(input("Сколько производить? "))
            if product in company.products:
                company.produce(product, amount)
            else:
                print("Некорректный продукт.")

        elif action == '2':
            product = input("Какой продукт продавать? (водка, пиво, коньяк, хлеб, воду, книги, транспортные услуги, коммунальные услуги, карандаши, мониторы, мышки, компьютеры, клавиатуры, вино, виски, сериалы 2Д, сериалы 3Д, мультики, драмы, комедии, золото, природный газ, нефть, каменный уголь, алмаз, рубин, изумруд, музыка, инструменты): ")
            amount = int(input("Сколько продавать? "))
            if product in company.products:
                company.sell(product, amount)
            else:
                print("Некорректный продукт.")

        elif action == '3':
            if company.check_game_over():
                break

        elif action == 'need_money':
            company.money += 1000000

        elif action == 'need_{company.product}':
            company [company.products] += 1000000

        elif action == '0':
            print("Спасибо за игру!")
            break
        else:
            print("Некорректный ввод. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
