from random import choice

class RandomWalk:
    def __init__(self, num_points=5000):
        #атрибуты блуждания
        self.num_points = num_points
        #координаты стартовые (0,0):
        self.x_values=[0]
        self.y_values=[0]

    #вычисление точек блуждания
    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            #определение направления и длины перемещения

            x_step = self.get_step()
            y_step = self.get_step()

            #Отклонение нулевых перемещений
            if x_step == 0 and y_step == 0:
                continue
            
            #вычисление следующей позиции:
            x = self.x_values[-1] + x_step #-1 ?
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        direction = choice([1,-1])
        distance = choice([0,1,2,3,4,5,6,7,8])
        step = direction*distance
        return step