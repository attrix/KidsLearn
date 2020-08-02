/**
 * Write a description of class ReverseOrder here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.Scanner;
public class ReverseOrder
{
    public static void main()
    {
      Scanner usernum = new Scanner(System.in);
      System.out.println("Enter number to be reversed:");
      int num = usernum.nextInt();
      int rev = 0;
      while (num > 0)
      {int rem = num % 10;
       rev = rev * 10 + rem;
       num = num / 10;
      }
      System.out.println(rev);
    }
}