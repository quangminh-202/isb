import java.util.Random;

public class JavaRandomGenerator {
    private static final int SIZE = 128;

    /**
     * Generate a random binary sequence and print it to the standard output.
     */
    public static void random() {
        Random random = new Random();
        for (int i = 0; i < SIZE; i++) {
            System.out.print(random.nextInt(2));
        }
    }

    /**
     * The main method.
     *
     * This method is the entry point of the program. It calls the random() method
     * to generate a random binary sequence and prints it to the standard output.
     *
     * @param args Command line arguments (not used).
     */
    public static void main(String[] args) {
        random();
    }
}