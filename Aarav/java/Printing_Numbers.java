/**
 * Write a description of class PrintNumbers here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Printing_Numbers
{
    public static void main()
    {
        int a = 1;
        while(a < 100)
        {
            a++;
            if (a % 5 == 0 && a % 7 == 0)
            {
                System.out.println(a);
            }
        }
    }
}   