import random
import pygame


class Coordinate:
    def __init__(self):
        self.x = 0
        self.y = 0


class Controller:
    def __init__(self, x, y, share):
        self.size = Coordinate()
        self.size.x = x
        self.size.y = y
        self.share = share
        self.count_of_cells = 0
        self.centre = Coordinate()
        self.random = Coordinate()
        self.cords = Coordinate()
        self.step = Coordinate()
        self.field = [[0 for i in range(self.size.x)] for j in range(self.size.y)]

    def random_cords(self):
        self.random.x = random.randint(0, self.size.x-1)
        self.random.y = random.randint(0, self.size.y-1)
        self.cords.x = self.random.x
        self.cords.y = self.random.y

    def initialization(self):
        self.centre.y = self.size.y // 2
        self.centre.x = self.size.x // 2
        self.field[self.centre.y-1][self.centre.x - 1] = 2
        self.random_cords()
        self.field[self.cords.y][self.cords.x] = 1

    def checking(self):
        if self.cords.x >= 1 and self.cords.x <= self.size.x -2 and self.cords.y >= 1 and self.cords.y <= self.size.y -2:
            if self.field[self.cords.y-1][self.cords.x] == 2 or self.field[self.cords.y][self.cords.x-1] == 2 \
                    or self.field[self.cords.y+1][self.cords.x] == 2 or self.field[self.cords.y][self.cords.x+1] == 2:
                self.field [self.cords.y][self.cords.x] = 2
                self.random_cords()
                self.field[self.cords.y][self.cords.x] = 1
            else:
                self.field[self.cords.y][self.cords.x] = 0
                self.step.x = random.randint(-1, 1)
                self.step.y = random.randint(-1, 1)
                while self.cords.y + self.step.y < 0 or self.cords.x + self.step.x < 0 \
                        or self.cords.y + self.step.y > self.size.y - 1 or self.cords.x + self.step.x > self.size.x - 1:
                    self.step.x = random.randint(-1, 1)
                    self.step.y = random.randint(-1, 1)
                self.cords.x += self.step.x
                self.cords.y += self.step.y
                self.field[self.cords.y][self.cords.x] = 1
            self.count_of_cells = 0
            for i in range(self.size.y):
                for j in range(self.size.x):
                    if self.field[i][j] == 2:
                        self.count_of_cells += 1
        else:
            self.field[self.cords.y][self.cords.x] = 0
            self.random_cords()
            self.field[self.cords.y][self.cords.x] = 1


class Process:
    def __init__(self, x, y, share):
        self.update = Controller(x, y, share)
    def processing(self,x,y):
        self.update.initialization()
        print()
        pygame.init()
        WHITE = (255, 255, 255)  # ввод цветов по rgb
        LIGHT = (173, 216, 230)
        DARK = (95, 158, 160)
        scale = 10
        form = pygame.display.set_mode((500, 500))  # создание окна
        form.fill(WHITE)  # закрашиваю окно в белый цвет
        pygame.display.update()  # отображение изменений
        pygame.display.set_caption('DLA')
        a = True
        while a == True:
            while self.update.count_of_cells <= self.update.size.x * self.update.size.y * self.update.share / 100:
                self.update.checking()
                for i in range(y):
                    for j in range(x):
                        if self.update.field[i][j] == 0:
                            pygame.draw.rect(form, WHITE, [i * scale, j * scale, scale, scale])
                        if self.update.field[i][j] == 1:
                            pygame.draw.rect(form, LIGHT, [i * scale, j * scale, scale, scale])
                        if self.update.field[i][j] == 2:
                            pygame.draw.rect(form, DARK, [i * scale, j * scale, scale, scale])
                pygame.display.update()  # отображение изменений

                for event in pygame.event.get():
                    pygame.display.update()
                    if event.type == pygame.QUIT:  # quit - нажать на крестик
                        a = False
        pygame.quit()
        quit()

def main():
    x = 50 #int(input('Введите размеры поля: '))
    y = 50 #int(input())
    share = int(input('Введите процент клеток: '))
    ca = Process(x, y, share)
    print()
    ca.processing(x,y)
main()