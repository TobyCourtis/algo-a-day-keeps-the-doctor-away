package practice.inheritance;

public abstract class Animal {

    private String name;

    public Animal(String name) {
        this.name = name;
    }


    public abstract void speak();

    public void sleep() {
        System.out.println("zzzz");
    }

    public String getName() {
        return this.name;
    }
}
