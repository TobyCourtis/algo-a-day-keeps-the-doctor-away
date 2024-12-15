package practice.factory;

public class Main {

    public static void main(String[] args) {
        Burger cb = BurgerFactory.createCheeseBurger();
        System.out.println(cb.getIngredients());
    }
}
