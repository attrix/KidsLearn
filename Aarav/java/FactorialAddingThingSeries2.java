/**
 * Write a description of class FactorialAddingThing here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.Scanner;
public class FactorialAddingThingSeries2
{
    public static void main()
    {
        Scanner s = new Scanner (System.in);
        System.out.println("Enter number:");
        double userinput = s.nextDouble();
        double solu = 0;
        double fact = 1;
        double top = 1;
        for (double a = 1; a <= userinput; a++)
        {
            fact = fact * a;
            solu = solu + (top/fact);
        }
        System.out.println("The solution is: " + solu);
    }
}