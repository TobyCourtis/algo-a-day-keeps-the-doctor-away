import java.util.Set;

public class CollectionsPractice {

    public CollectionsPractice() {

    }

    /*
     * How does the ArrayList differ from LinkedList, and in which scenarios would you choose one over the other?
     *
     * A:
     * Elem access = O(1) for array, O(n) LinkedList
     * Insert = O(n) for array, O(1) linkedList
     */

    public Set<Integer> findIntersections(Set<Integer> setOne, Set<Integer> setTwo) {
        setOne.retainAll(setTwo);
        return setOne;
    }
}
