package king.basics;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        List<Integer> integers = Arrays.asList(1, 2, 3);
        ArrayList<Integer> ints = new ArrayList<Integer>();

        ArrayList<Integer> ints2 = new ArrayList<Integer>(Arrays.asList(1, 2, 3));

        for (Integer i : integers) {
            System.out.println(i);
        }

        integers.forEach(i -> {
            System.out.println(i);
        });


        String day = "Monday";

        switch (day) {
            case "Monday":
                System.out.println("discount day");
                break;
            default:
                System.out.println("No discount");
                break;
        }

        System.out.println(1 == 2);
        Object o = "here";
    }
}
