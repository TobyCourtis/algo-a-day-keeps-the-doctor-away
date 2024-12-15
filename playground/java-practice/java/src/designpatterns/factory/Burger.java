package designpatterns.factory;

import java.util.ArrayList;

public class Burger {

    private ArrayList<String> ingredients = new ArrayList<>();

    public Burger() {
    }

    public void addIngredient(String ingredient) {
        this.ingredients.add(ingredient);
    }

    public ArrayList<String> getIngredients() {
        return ingredients;
    }
}