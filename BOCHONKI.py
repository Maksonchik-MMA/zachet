import random

class Card:
    def __init__(self, player_name):
        self.player_name = player_name
        self.rows = []
        self._generate()

    def _generate(self):
        numbers = random.sample(range(1, 91), 15)
        numbers.sort()
        for i in range(0, 15, 5):
            row = numbers[i:i+5]
            for _ in range(4):
                pos = random.randint(0, len(row))
                row.insert(pos, None)
            self.rows.append(row)

    def has_number(self, number):
        return any(number in row for row in self.rows)

    def cross_out(self, number):
        for row in self.rows:
            if number in row:
                row[row.index(number)] = '-'
                return True
        return False

    def is_empty(self):
        return all(num == '-' or num is None for row in self.rows for num in row)

    def __str__(self):
        card_str = f"-- Карточка {self.player_name} ---\n"
        for row in self.rows:
            row_str = []
            for num in row:
                if num is None: row_str.append('  ')
                elif num == '-': row_str.append(' -')
                else: row_str.append(f"{num:2}")
            card_str += ' '.join(row_str) + '\n'
        return card_str + '--------------------------'

class BarrelBag:
    def __init__(self):
        self.barrels = list(range(1, 91))
        random.shuffle(self.barrels)

    def draw(self):
        return self.barrels.pop() if self.barrels else None

    def left(self):
        return len(self.barrels)

class Player:
    def __init__(self, name):
        self.name = name
        self.card = Card(name)

    def decide(self, number):
        raise NotImplementedError

class HumanPlayer(Player):
    def decide(self, number):
        while True:
            answer = input("Зачеркнуть цифру? (y/n): ").lower()
            if answer in ('y', 'n'): return answer == 'y'

class ComputerPlayer(Player):
    def decide(self, number):
        return self.card.has_number(number)

    def __str__(self):
        return str(self.card)

class Game:
    def __init__(self):
        self.human = HumanPlayer("Ваша")
        self.computer = ComputerPlayer("компьютера")
        self.bag = BarrelBag()
        self.current = None

    def start(self):
        print("Игра Лото началась!")
        while True:
            self.current = self.bag.draw()
            if not self.current:
                print("Бочонки закончились! Ничья.")
                return

            print(f"\nНовый бочонок: {self.current} (осталось {self.bag.left()})")
            print(self.human.card)
            print(self.computer)

            human_decision = self.human.decide(self.current)
            human_has = self.human.card.has_number(self.current)

            if human_decision and not human_has:
                print(f"Числа {self.current} нет на вашей карточке. Вы проиграли!")
                return
            elif not human_decision and human_has:
                print(f"Вы пропустили число {self.current}. Вы проиграли!")
                return
            elif human_decision:
                self.human.card.cross_out(self.current)

            if self.computer.card.has_number(self.current):
                self.computer.card.cross_out(self.current)

            if self.human.card.is_empty():
                print("Поздравляем! Вы выиграли!")
                return
            if self.computer.card.is_empty():
                print("Компьютер выиграл!")
                return

if __name__ == "__main__":
    Game().start()
