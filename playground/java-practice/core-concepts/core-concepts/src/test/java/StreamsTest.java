import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.assertEquals;

class StreamsTest {

    @Test
    void testStreams() {
        Streams s = new Streams();
        Map<String, Integer> actualMap = s.listToMap(Arrays.asList("one", "two", "three"));
        assertEquals(Map.of("one", 3, "two", 3, "three", 5), actualMap);
    }

    @Test
    void testFilterSort() {
        Streams s = new Streams();
        List<Integer> actualList = s.listFilterSortCollect(List.of(9, 1, 6, 10, 12));
        assertEquals(List.of(1, 6, 9), actualList);
    }
}
