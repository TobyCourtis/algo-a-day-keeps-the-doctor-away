plugins {
    id("java")
}

group = "org.example"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

dependencies {
    testImplementation("org.junit.jupiter:junit-jupiter-api:5.7.0")
    testImplementation("org.junit.jupiter:junit-jupiter-engine:5.7.0")
    testImplementation("org.mockito:mockito-junit-jupiter:3.12.4")
    testImplementation("org.mockito:mockito-core:3.12.4")
}

tasks.test {
    useJUnitPlatform()
}