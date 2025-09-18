import java.time.LocalDateTime;

public class XZ {
    public static void main(String[] args) {
        System.out.println("pupu");
        os();
    }
    
    private static void os() {
        System.out.println("System information:");
        System.out.print("Operating system: ");
        System.out.print(System.getProperty("os.name") + " ");
        System.out.println(System.getProperty("os.version"));
        System.out.print("Processor cores: ");
        System.out.println(Runtime.getRuntime().availableProcessors());
        System.out.print("Ram for JVM: ");
        System.out.println(
            Runtime.getRuntime().maxMemory() / 1024 / 1024 +
            "Mb");
        System.out.println("Current time: " + LocalDateTime.now());
    }
}