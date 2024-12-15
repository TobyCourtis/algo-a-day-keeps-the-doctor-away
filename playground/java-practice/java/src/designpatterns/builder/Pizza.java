package designpatterns.builder;

public class Pizza {

    private String sauce;
    private String topping;

    public static class PizzaBuilder {

        private String sauce;
        private String topping;

        public PizzaBuilder setSauce(String sauce) {
            this.sauce = sauce;
            return this;
        }


        public PizzaBuilder setTopping(String topping) {
            this.topping = topping;
            return this;
        }

        public Pizza build() {
            Pizza p = new Pizza();
            p.sauce = this.sauce;
            p.topping = this.topping;
            return p;
        }
    }

    @Override
    public String toString() {
        return String.format("Pizza with: %s and %s", this.sauce, this.topping);
    }
}
