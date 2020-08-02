/**
 * Write a description of class LeapYear here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.Scanner;
public class LeapYear
{
    public static void main()
    {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter Year:");
        int year = s.nextInt();
        
        boolean forever = true;
        while (forever == true)
        {
            if ((year % 4== 0))
            {
                System.out.println(year + " is a leap year");
            }
            else
            {
                System.out.println(year + " is not a leap year");
            }
            forever = false;
        }
    }
}
