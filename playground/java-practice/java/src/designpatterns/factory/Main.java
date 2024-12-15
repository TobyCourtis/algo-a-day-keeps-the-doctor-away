package designpatterns.factory;

import java.util.List;

public class Main {

    public static void main(String[] args) {
        Burger b = new Burger();
        b.addIngredient("Bun");
        b.addIngredient("Patty");
        b.addIngredient("Bun");
        System.out.println(b.getIngredients());


        System.out.println(
                BurgerFactory
                        .createBurger(List.of("Bun", "Lettuce", "Tomato", "Cheese", "Bun"))
                        .getIngredients());

        System.out.println(BurgerFactory.cheeseCheeseBurger().getIngredients());

        System.out.println(BurgerFactory.plainBurger().getIngredients());
    }

}