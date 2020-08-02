/**
 * Write a description of class FibonacciSequence here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.Scanner;
public class FibonacciSequence
{
    public static void main()
    {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter Number:");
        int userinput = s.nextInt();
        int a,b;
        int sum = 0;
        a = 0;
        b = 1;
        System.out.println(a);
        System.out.println(b);
        while (sum < userinput)
        {
            sum = a + b;
            if (sum < userinput)
            System.out.println(sum);
            a = b;
            b = sum;
        }
    }
}