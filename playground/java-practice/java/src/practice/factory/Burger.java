package practice.factory;

import java.util.ArrayList;
import java.util.List;

public class Burger {

    private List<String> ingredients = new ArrayList<>();

    public Burger() {

    }

    public void addIngredient(String ingredient) {
        ingredients.add(ingredient);
    }

    public List<String> getIngredients() {
        return this.ingredients;
    }
}
