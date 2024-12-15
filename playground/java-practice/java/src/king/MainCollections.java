package king;

import java.util.*;
import java.util.stream.Collectors;

public class MainCollections {

    public static void main(String[] args) {
//        streams();
//        testCollections();
        hashMap();
    }


    // streams
    public static void streams(){
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
        List<Integer> squared = numbers.stream()
                .map(n -> n * n)
                .filter(n -> n != 9)
                .collect(Collectors.toList());
        System.out.println(squared); // [1, 4, 9, 16, 25]


    }

    public static void testCollections(){
        // List extends Collection extends Iterable
        List<String> list = new ArrayList<>(Arrays.asList("apple", "banana", "cherry"));
        Set<String> set = new HashSet<>(list);
        Queue<String> queue = new LinkedList<>(list);

        System.out.println(list);  // ArrayList
        System.out.println(set);   // HashSet
        System.out.println(queue); // LinkedList as Queue
        System.out.println();
    }

    public static void hashMap(){
        Map<String, Integer> map = new HashMap<>();
        map.put("apple", 1);
        map.put("banana", 2);

        System.out.println(map.get("apple")); // 1
    }
}
