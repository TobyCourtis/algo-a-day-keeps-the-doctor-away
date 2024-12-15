package practice;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class CollectionsPractice {

    public static void main(String[] args) {
        List<String> l = List.of("foo", "bar");
        l.forEach(s -> System.out.println(s));

        for (String s : l) {
            System.out.println(s);
        }

        List<String> yeet = l.stream()
                .map(s -> s + " yeet")
                .collect(Collectors.toList());

        System.out.println(yeet);

        HashMap<String, Integer> nameAge = new HashMap<>(Map.of("Toby", 27));

        System.out.println(nameAge);
    }
}
