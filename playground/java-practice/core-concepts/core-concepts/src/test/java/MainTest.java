import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MainTest {

    @Test
    void testAdd() {
        assertEquals(5, Main.add(2, 3));

        assertEquals(0, Main.add(0, 0));

        assertEquals(-5, Main.add(-2, -3));
    }
}
