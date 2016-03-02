// Reuben Thorpe (2016), CodeEval [Decimal To Binary v1.1]
import java.io.*;
import java.util.Scanner;

public class Main {
  public static void main (String []args) throws IOException {
    File file = new File(args[0]);
    Scanner s = new Scanner(file);
    while (s.hasNext()){
      System.out.println(Integer.toBinaryString(s.nextInt()));
    }
  }
}
