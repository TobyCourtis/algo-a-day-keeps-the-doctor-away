package designpatterns.factory;

import java.util.List;

public class BurgerFactory {
    public static Burger createBurger(List<String> ingredients) {
        Burger b = new Burger();
        for (String ingredient : ingredients) {
            b.addIngredient(ingredient);
        }
        return b;
    }

    public static Burger cheeseCheeseBurger() {
        return BurgerFactory.createBurger(List.of("Bun", "Patty", "Cheese", "Bun"));
    }

    public static Burger plainBurger() {
        return BurgerFactory.createBurger(List.of("Bun", "Patty", "Bun"));
    }

}