/**
 * Write a description of class TribonacciSequence here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.Scanner;
public class TribonacciSequence
{
    public static void main()
    {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter Number:");
        int userinput = s.nextInt();
        int a,b,c;
        int sum = 0;
        a = 1;
        b = 2;
        c = 3;
        System.out.print(a + " ");
        System.out.print(b + " ");
        System.out.print(c + " ");
        while (sum < userinput)
        {
            sum = a + b + c;
            if (sum < userinput)
            System.out.print(sum + " ");
            a = b;
            b = c;
            c = sum;
        }
    }
}
