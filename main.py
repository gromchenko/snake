import pygame, pygame_menu
import time
import random
import math

class Snake:
    pygame.init()
    menu = ''
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)
    dis_width = 820
    dis_height = 600
    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Змейка студента Громченко')
    clock = pygame.time.Clock()
    snake_block = 10
    start_time = time.time()
    snake_speed = 10
    user_name = ''
    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)
    mode_time = False
    t = ''

    def Your_score(self, score): # метод Your_score выводит количество очков для игрока
        t = str(math.ceil(time.time() - self.start_time))
        value = self.score_font.render("Это ваши очки: " + str(score) + ' Время игры: ' + t + ' Имя: ' + str(self.user_name.get_value()), True, self.blue)
        self.dis.blit(value, [0, 0])

    def our_snake(self, snake_block, snake_list): # метод our_snake рисует змейку
        for x in snake_list:
            pygame.draw.circle(self.dis, (0, 0, 0), (x[0], x[1]),snake_block)  # изменили геометрическую фигуру змейки на круг и поменяли на красный цвет
            # pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

    def message(self, msg, color): # метод message для вывода сообщений
        mesg = self.font_style.render(msg, True, color)
        self.dis.blit(mesg, [self.dis_width / 6, self.dis_height / 3])

    def __init__(self): # это конструктор который вызвает основной метод gameLoop
        self.gameLoop()

    def start_the_game(self):
        #if self.mode_time == False:
        self.start_time = time.time()
         #   self.mode_time == True
        print('close')
        self.menu.disable()
        pass
    def gameLoop(self): # метод gameLoop это метод с которого начинается программа
        #surface = pygame.display.set_mode((600, 400))
        self.menu = pygame_menu.Menu('Добро пожаловать', 400, 300, theme=pygame_menu.themes.THEME_BLUE)
        #menu = pygame_menu.Menu('Добро пожаловать', 400, 300,theme=pygame_menu.themes.THEME_BLUE)
        self.user_name = self.menu.add.text_input('Имя игрока :', default=' ')
        #self.user_name.get_value()
        self.menu.add.button('Играть', self.start_the_game)

        self.menu.mainloop(self.dis)
        game_over = False
        game_close = False

        x1 = self.dis_width / 2
        y1 = self.dis_height / 2
        x1_change = 0
        y1_change = 0
        snake_List = []
        Length_of_snake = 1
        foodx = round(random.randrange(100, self.dis_width - self.snake_block) / 10.0) * 10.0 - 10
        foody = round(random.randrange(100, self.dis_height - self.snake_block) / 10.0) * 10.0 - 10
       # i = 0
        while not game_over:


            # print(Length_of_snake)
            while game_close == True:
                self.dis.fill(self.blue)

                if self.mode_time == False:
                    self.t = str(math.ceil(time.time() - self.start_time))
                    self.mode_time = True
                self.message("ВЫ ВЫИГРАЛИ ВРЕМЯ ИГРЫ: "+self.t, self.green)
                self.Your_score(Length_of_snake - 1)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            self.gameLoop()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_LEFT:

                        x1_change = -self.snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = self.snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -self.snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = self.snake_block
                        x1_change = 0

            if x1 >= self.dis_width:  # если змейка выходит за границу игрового окна по оси X (с правой стороны), то снова начинает своё движение по по оси X с начала с другой стороны (слева) (8 строк кода вниз)
                x1 = 0
            if y1 >= self.dis_height:
                y1 = 0
            if x1 < 0:
                x1 = self.dis_width
            if y1 < 0:
                y1 = self.dis_height
            # if (x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0):
            #  pass
            # game_close = True
            if Length_of_snake == self.snake_block + 1:  # если змейка съела пять единиц еды, то тогда завершается игра (True)
                game_close = True
            x1 += x1_change
            y1 += y1_change
            self.dis.fill(self.green)

            #pygame.draw.rect(self.dis, self.black, [foodx, foody, self.snake_block, self.snake_block])
            dog_surf = pygame.image.load('12.png')
            dog_rect = dog_surf.get_rect(bottomright=(foodx, foody))
            self.dis.blit(dog_surf, dog_rect)
            pygame.display.update()
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]
            for x in snake_List[:-1]:
                if x == snake_Head:
                    pass
                    #game_close = True
            self.our_snake(self.snake_block, snake_List)
            self.Your_score(Length_of_snake - 1)
            pygame.display.update()
            #print(str(x1) +':'+str(foodx))
            if ((x1 >= foodx-20)  and (x1 <= foodx+20)) and ((y1 >= foody-20)  and (y1 <= foody+20)):
                foodx = round(random.randrange(100, self.dis_width - self.snake_block) / 10.0) * 10.0 - 10
                foody = round(random.randrange(100, self.dis_height - self.snake_block) / 10.0) * 10.0 - 10
                #print(foodx)
                #print(foody)
                Length_of_snake += 1
            self.clock.tick(self.snake_speed)
        pygame.quit()
        quit()

s = Snake()
