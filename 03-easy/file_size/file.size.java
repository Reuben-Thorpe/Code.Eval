// Reuben Thorpe (2016), CodeEval [File Size v1.0]
import java.io.File;

public class Main {
    public static void main (String []args) {
        File file = new File(args[0]);
        if (file.exists()) {
            System.out.println((int)file.length());
        }
        else {
            System.out.println("Could not find file : " + args[0]);
        }
    }
}
