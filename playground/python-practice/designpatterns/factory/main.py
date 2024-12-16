from burgerfactory import BurgerFactory

if __name__ == "__main__":
    cheese_burger = BurgerFactory().create_cheese_burger()
    print(cheese_burger.get_ingredients())
