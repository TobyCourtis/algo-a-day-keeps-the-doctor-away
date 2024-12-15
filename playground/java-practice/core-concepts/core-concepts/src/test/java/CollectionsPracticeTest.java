import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

import static org.junit.jupiter.api.Assertions.assertEquals;

class CollectionsPracticeTest {

    @Test
    void intersections() {
        CollectionsPractice c = new CollectionsPractice();
        Set<Integer> actualSet = c.findIntersections(
                new HashSet<>(Arrays.asList(1, 2)),
                new HashSet<>(Arrays.asList(2, 3)));
        assertEquals(Set.of(2), actualSet);
    }
}