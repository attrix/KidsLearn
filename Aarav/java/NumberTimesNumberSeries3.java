/**
 * Write a description of class NumberTimesNumberSeries3 here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.*;
public class NumberTimesNumberSeries3
{
    public static void main()
    {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter Number:");
        int userinput = s.nextInt();
        int num;
        int solu = 0;
        for (num = 1; num <= userinput; num++)
        {
            solu = solu + (num * num);
        }
        System.out.println("The answer is: " + solu);
    }
}
