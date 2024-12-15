package king.di;

// Service Implementation
public class EmailService implements NotificationService {
    public void sendMessage(String message) {
        System.out.println("Email: " + message);
    }
}
