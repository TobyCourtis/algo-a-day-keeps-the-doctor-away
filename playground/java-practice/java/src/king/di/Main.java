package king.di;

public class Main {

    public static void main(String[] args) {
        NotificationService service = new EmailService();
        UserController controller = new UserController(service); // service is injected
        controller.notifyUser(); // Email: Hello, user!
    }
}
