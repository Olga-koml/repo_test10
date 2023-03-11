import pygame
b = 4
c = 5
a = b + c
print(a)
#тестовый комментарий
 
pygame.init()
 
dis=pygame.display.set_mode((500,400))
pygame.display.update()
pygame.display.set_caption('Змейка от Skillbox') #Добавляем название игры.
 
game_over=False #Создаём переменную, которая поможет нам контролировать 
статус игры — завершена она или нет. Изначально присваиваем значение False,
 то есть игра продолжается.
 
while not game_over:
   for event in pygame.event.get():
       print(event)  #Выводить в терминал все произошедшие события.
 
pygame.quit()
quit()






