# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)

class Unit:
    dir_list = {'x_axis': {'UP': 1, 'DOWN': -1}, 'y_axis': {'LEFT': 1, 'RIGTH': -1}}
    state = {'fly': 1.2, 'crawl': 0.5}
    # ...
    def __init__(self):
        pass

    def move(self, direction):
        speed = self._get_speed()
        x = self.x + Unit.dir_list['x_axis'].get(direction, 0) * speed
        y = self.y + Unit.dir_list['y_axis'].get(direction, 0) * speed

        self.field.set_unit(y=y, x=x, unit=self)

    def _get_speed(self, unit_state=1):
        if unit_state not in Unit.state:
            raise ValueError('Эк тебя раскорячило')
        return Unit.state[unit_state]

