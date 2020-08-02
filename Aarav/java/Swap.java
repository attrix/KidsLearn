/**
 * Write a description of class Swap here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.Scanner;
public class Swap
{
   public static void main()
   {
       Scanner input = new Scanner(System.in);
       System.out.println("Enter first number (one digit):");
       int a = input.nextInt();
       System.out.println("Enter second number (one digit):");
       int b = input.nextInt();
       System.out.println(a + "" + b);
       a = a + b;
       b = a - b;
       a = a - b;
       System.out.println(a + "" + b);
   }
}
