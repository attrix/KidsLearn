/**
 * Write a description of class SomeRandomSeries5 here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.Scanner;
public class SomeRandomSeries5
{
   public static void main()
   {
       Scanner s = new Scanner(System.in);
       System.out.println("Enter Number:");
       int userinput = s.nextInt();
       int a = 2;
       int fact;
       int sum = 0;
       for (fact = 1; fact <= userinput; fact++, a += 2)
       {
           if (fact % 2 == 0)
           {
               sum = sum - a;
               System.out.print(" - " + a);
           }
           else
           {
               sum = sum + a;
               System.out.print(" + " + a);
           }
       }
       System.out.print(" Solution is: " + sum);
   }
}