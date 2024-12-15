package practice.factory;

public class BurgerFactory {

    public static Burger createCheeseBurger() {
        Burger b = new Burger();

        b.addIngredient("Bun");
        b.addIngredient("Patty");
        b.addIngredient("Cheese");
        b.addIngredient("Bun");
        return b;
    }
}
