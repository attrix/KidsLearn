
/**
 * Write a description of class Equations here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.Scanner;
public class Equations
{
    public static void main(String []args)
    {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter first number:");
        int a = s.nextInt();
        System.out.println("Enter second number:");
        int b = s.nextInt();
        int add = a+b;
        System.out.println("Addition is: " + add);
        int sub = a-b;
        System.out.println("Subtraction is: " + sub);
        int multi = a*b;
        System.out.println("Multiplication is: " + multi);
        int div = a/b;
        System.out.println("Division is: " + div);
        int mod = a%b;
        System.out.println("Modulas is: " + mod);
    }
}
