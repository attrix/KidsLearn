
/**
 * Write a description of class ForLoop here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class StarsThing
{
    public static void main(String [] args)
    {
        int i,j;
        for(i = 0 ; i < 5; i++)
        {
            for(j = 5; j > i; j--)
            {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
