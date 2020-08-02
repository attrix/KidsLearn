/**
 * Write a description of class SumOfDigits here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.Scanner;
public class SumOfDigits
{
    public static void main()
    {
      Scanner usernum = new Scanner(System.in);
      System.out.println("Enter number:");
      int num = usernum.nextInt();
      int rev = 0;
      while ( num > 0)
      {
       int rem = num % 10;
       rev = rev + rem; 
       num = num / 10; 
      }
      System.out.println(rev);
    }
}
