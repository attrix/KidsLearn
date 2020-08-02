/**
 * Write a description of class SomeRandomSeries1 here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.Scanner;
public class SomeRandomSeries1
{
    public static void main(String [] args)
    {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter Number:");
        int userinput = s.nextInt();
        int num = 1, den;
        double sum = 0;
        for (den = 1; den <= userinput; den++)
        {
            sum = sum + (num/den);
        }
        System.out.println("The FINAL answer is: " + sum);
    }
}