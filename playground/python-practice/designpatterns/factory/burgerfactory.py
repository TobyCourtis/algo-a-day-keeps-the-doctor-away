from burger import Burger


class BurgerFactory:

    @staticmethod
    def create_cheese_burger():
        b = Burger()
        b.add_ingredient("Bun")
        b.add_ingredient("Patty")
        b.add_ingredient("Cheese")
        b.add_ingredient("Bun")
        return b
