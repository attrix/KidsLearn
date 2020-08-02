/**
 * Write a description of class ArmstrongNum here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.Scanner;
public class ArmstrongNum
{
    public static void main()
    {
       Scanner input = new Scanner(System.in);
       System.out.println("Enter Number:");
       int usernum = input.nextInt();
       int rev = 0;
       int newx = usernum;
       while (usernum > 0)
       {
         int rem = usernum % 10;
         usernum = usernum / 10;
         rev = rev + (rem*rem*rem);
         
        
       }
       if (rev == newx)
         {
             System.out.println ("Yes it is an armstrong number");
             
         }
         else
         {
            System.out.println ("Not an armstrong number");
         }
       }
}