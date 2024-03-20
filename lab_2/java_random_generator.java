import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Random random = new Random();

        for (int i = 0; i < 2; ++i) { // Генерируем 2 последовательности
            StringBuilder bits = new StringBuilder();
            for (int j = 0; j < 128; j += 64) {
                long randomNum = random.nextLong();
                bits.append(String.format("%64s", Long.toBinaryString(randomNum)).replace(' ', '0'));
            }

            System.out.println("Sequence " + (i + 1) + ":\n" + bits.toString());
        }
    }
}
