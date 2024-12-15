package king.di;

public class UserController {
    private final NotificationService service;

    public UserController(NotificationService service) {
        this.service = service;
    }

    public void notifyUser() {
        service.sendMessage("Hello, user!");
    }
}
