
/**
 * Write a description of class PascalsTriangle here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class PatternTriangle
{
    public static void main()
    {
        int i,j,k,sp;
        for(i = 1; i < 7; i++)
        {
            sp = 7 - i;
            sp = (sp * 2) - 1;
            for(k = 1; k <= sp; k++)
            {
                System.out.print(" ");
            }
            for(j = 1; j <= i; j++)
            {
                System.out.print(j + " ");
            }
            j = j-2;
            while(j >= 1)
            {
                System.out.print(j + " ");
                j--;
            }
            System.out.println();
        }
    }
}
