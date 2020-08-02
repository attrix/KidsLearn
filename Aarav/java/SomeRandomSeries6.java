
/**
 * Write a description of class SomeRandomSeries6 here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.Scanner;
public class SomeRandomSeries6
{
    public static void main()
    {
       Scanner s = new Scanner(System.in);
       System.out.println("Enter Number:");
       int userinput = s.nextInt();
       int sum = 0;
       int fact;
       int a;
       for (fact = 1; fact <= userinput; fact++)
       {
           for (a = 1; a <=fact; a++)
           {
               sum = sum + a;
           }
       }
       System.out.println("Answer is: " + sum);
    }
}
