/**
 * Write a description of class Multiples here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.Scanner;
public class Multiples
{
      public static void main()
      {
             Scanner s = new Scanner(System.in);
             System.out.println("Enter number:");
             int num = s.nextInt();
             int j = 0;
             int mult = 1;
             while (j < 13)
             {
                 j++;
                 mult++;
                 num = num * mult;
                 System.out.println(num);
                 num = num / mult;
             }
      }
}