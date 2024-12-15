package designpatterns.builder;

public class Main {

    public static void main(String[] args) {
        Pizza p = new Pizza.PizzaBuilder()
                .setSauce("Tomato")
                .setTopping("ham")
                .build();
        System.out.println(p);

        int foo = 1;
        Integer foo2 = null;
    }
}
