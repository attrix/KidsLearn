
/**
 * Write a description of class LotOfOneAndZeroSeries8 here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.Scanner;
public class LotOfOneAndZeroSeries8
{
    public static void main()
    {
        Scanner s = new Scanner (System.in);
        System.out.println("Enter number: ");
        int userinput = s.nextInt();
        boolean fact = true;
        int a, b;
        for (a = 1; a <= userinput; a++)
        {
            for (b = 1; b <= a; b++)
            {
                if (b % 2 == 0)
                {
                    System.out.print("0");
                }
                else
                {
                    System.out.print("1");
                }
            }
            System.out.println();
        }
    }
}
