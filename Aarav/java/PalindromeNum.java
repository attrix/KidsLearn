
/**
 * Write a description of class PalindromeNum here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.Scanner;
public class PalindromeNum
{
    public static void main()
    {
      Scanner usernum = new Scanner(System.in);
      System.out.println("Enter number:");
      int num = usernum.nextInt();
      int copynum = num;
      int rev = 0;
      while (num > 0)
      {int rem = num % 10;
       rev = rev * 10 + rem;
       num = num / 10;
      }
      if(copynum == rev)
      {
          System.out.println("This number is a palindrome");
      }
      else
      {
          System.out.println("This number is not a palindrome");
      }
    }
}
