package designpatterns.singleton;

public class DatabaseConnector {

    private static DatabaseConnector singletonDatabaseConnector;

    private DatabaseConnector() {
    }

    public static DatabaseConnector getInstance() {
        if (singletonDatabaseConnector == null) {
            singletonDatabaseConnector = new DatabaseConnector();
        }
        return singletonDatabaseConnector;
    }
}
