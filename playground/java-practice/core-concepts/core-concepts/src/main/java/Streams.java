import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class Streams {

    public Streams() {
    }

    public Map<String, Integer> listToMap(List<String> stringList) {
        Map<String, Integer> map = stringList.stream()
                .collect(Collectors.toMap(
                        str -> str,
                        String::length
                ));

        return map;
    }

    public List<Integer> listFilterSortCollect(List<Integer> integers) {
        return integers.stream()
                .filter(integer -> integer < 10)
                .sorted() // todo custom comparator
                .toList();
    }
}
