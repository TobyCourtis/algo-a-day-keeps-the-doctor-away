package king.inheritance;

public abstract class Animal {

    public final int age = 10; // cannot be re-assigned

    public final void sleep(){
        System.out.println("zzzzz");
    }

    public abstract void speak();

    public final void cannotOverride() {
        System.out.println("Cannot be overridden");
    }
}
