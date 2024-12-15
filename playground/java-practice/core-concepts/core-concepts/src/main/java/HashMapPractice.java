import java.util.Map;
import java.util.Objects;

public class HashMapPractice {

    public HashMapPractice() {

    }

    class CustomKey {
        private final String id;

        public CustomKey(String id) {
            this.id = id;
        }

        @Override
        public int hashCode() {
            return id != null ? id.hashCode() : 0;
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            CustomKey other = (CustomKey) obj;
            return Objects.equals(this.id, other.id);
        }
    }

    public Map<CustomKey, String> getCustomKeyMap(){
        CustomKey c = new CustomKey("id one");
        CustomKey c2 = new CustomKey("id two");

        boolean b = c.equals(c2);
        return Map.of(c, "first val", c2, "second val");
    }
}
