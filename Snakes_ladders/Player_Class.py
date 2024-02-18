from Snakes_ladders.snl import snakes, ladders


class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def greet(self):
        print("Hello " + self.name + "!")

    def move(self, roll_num):
        self.position += roll_num
        if self.position > 100:
            print(f"{self.name} you can't go above 100 spaces, position not updated")
            self.position -= roll_num
        else:
            print(f'{self.name} has rolled a {roll_num}, your position is now {self.position}')

    def check_win(self):
        if self.position == 100:
            print(f'Congratulations,{self.name} has won!')
            return True
        else:
            return False

    def check_snakes(self):
        if self.position in snakes:
            self.position = snakes[self.position]
            print(f'{self.name} you have been eaten by a snake!, you have been sent down to {self.position}')

    def check_ladders(self):
        if self.position in ladders:
            self.position = ladders[self.position]
            print(f'{self.name} you have climbed a ladder, you have gone up to {self.position}')

