package practice.inheritance;

public class Dog extends Animal implements Canine {

    public Dog(String name) {
        super(name);
    }

    @Override
    public void speak() {
        System.out.println("woof");
    }

    @Override
    public void howl() {
        System.out.println("hooooowl");
    }
}
