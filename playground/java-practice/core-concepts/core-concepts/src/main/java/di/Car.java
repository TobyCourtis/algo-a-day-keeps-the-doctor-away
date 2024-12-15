package di;

public class Car {

    private Engine engine;

    public Car(Engine engine){
        this.engine = engine;
    }

    public void turnIgnition(){
        System.out.println("Starting car");
        engine.start();
    }
}
