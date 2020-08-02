/**
 * Write a description of class StarsThing2 here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.Scanner;
public class StarsThing2
{
    public static void main(String []args)
    {
        Scanner usernum = new Scanner(System.in);
        System.out.println("Enter number:");
        int num = usernum.nextInt();
        int i,j;
        for(i = 0 ; i < num; i++)
        {
            for(j = num; j > i; j--)
            {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
