// Reuben Thorpe (2016), CodeEval [Reverse Words v1.2]
import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        Scanner scanner = new Scanner(file);

        while (scanner.hasNext()){
            String[] line = scanner.nextLine().split(" ");
            for (int i = (line.length-1); i > 0; i--) {
                System.out.print(line[i] + " ");
            }
            System.out.println(line[0]);
        }
    }
}
