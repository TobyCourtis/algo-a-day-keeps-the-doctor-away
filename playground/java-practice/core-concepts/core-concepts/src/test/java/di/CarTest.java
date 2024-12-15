package di;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;

import static org.junit.jupiter.api.Assertions.*;
import org.mockito.junit.jupiter.MockitoExtension;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
class CarTest {

    @Mock
    private Engine mockEngine;

    @Test
    void turnIgnition() {
        doNothing().when(mockEngine).start();
        Car c = new Car(mockEngine);
        c.turnIgnition();
    }
}