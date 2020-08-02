/**
 * Write a description of class FactorialAddingThing2Series4 here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.Scanner;
public class FactorialAddingThing2Series4
{
    public static void main()
    {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter Number:");
        double userinput = s.nextDouble();
        double sum = 0;
        double fact, numer = 1, den = 1;
        for(fact = 1; fact <= userinput; fact++, den++)
        {
            if (fact % 2 == 0)
            {
                sum = sum - (numer / (den*den*den));
            }
            else
            {
                sum = sum + (numer / (den*den*den));
            }
        }
        System.out.println("Solution is: " + sum);
    }
}