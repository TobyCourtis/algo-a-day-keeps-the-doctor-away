package designpatterns.singleton;

public class Main {

    public static void main(String[] args){
        System.out.println("Main");
        DatabaseConnector dbConn = DatabaseConnector.getInstance();

        System.out.println(dbConn.hashCode());
        System.out.println(DatabaseConnector.getInstance().hashCode());
    }
}
