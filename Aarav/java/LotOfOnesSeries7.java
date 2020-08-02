/**
 * Write a description of class LotOfOnesSeries7 here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.Scanner;
public class LotOfOnesSeries7
{
    public static void main()
    {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter number: ");
        int userinput = s.nextInt();
        int fact;
        int sum = 1;
        for (fact = 1; fact <= userinput; fact++)
        {
            System.out.print(sum + " ");
            sum = sum * 10 + 1;
        }
    }
}