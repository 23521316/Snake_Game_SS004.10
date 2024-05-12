def _place_special_food(self):
    x = random.randint(0, (self.w - SPECIAL_FOOD_SIZE) // SPECIAL_FOOD_SIZE) * SPECIAL_FOOD_SIZE
    y = random.randint(0, (self.h - SPECIAL_FOOD_SIZE) // SPECIAL_FOOD_SIZE) * SPECIAL_FOOD_SIZE
    self.special_food = Point(x, y)
    if self.special_food in self.snake or self.special_food == self.food:
        self._place_special_food()