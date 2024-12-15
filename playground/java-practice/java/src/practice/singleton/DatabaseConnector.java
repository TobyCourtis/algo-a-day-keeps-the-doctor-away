package practice.singleton;

public class DatabaseConnector {

    private static DatabaseConnector dbConn = null;

    private DatabaseConnector() {

    }

    public static DatabaseConnector getInstance() {
        if (dbConn == null) {
            dbConn = new DatabaseConnector();
        }
        return dbConn;
    }
}
