
/**
 * Write a description of class TriangularLetters here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class TriangularStars
{
    public static void main()
    {
        int i,j,k;
        for(i = 1; i < 5; i++)
        {
            for(k = 5; k >= i; k--)
            {
                System.out.print(" ");
            }
            for(j = 0; j < i; j++)
            {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}
