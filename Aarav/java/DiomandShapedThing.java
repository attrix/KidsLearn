/**
 * Write a description of class DiomandShapedThing here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class DiomandShapedThing
{
    public static void main()
    {
        int a,b,c;
        int s = 5;
        int d = 1;
        for(a = 1; a < 5; a++)
        {
            for(b = 1; b <= s; b++)
            {
                System.out.print(" ");
            }
            for(c = 1; c <= a; c++)
            {
                System.out.print(d + " ");
            }
            System.out.println();
            d++;
        }
        int v,w,x;
        int y = 5;
        int z = 3;
        for(v = 1; v < 4; v++)
        {
            for(w = 1; w <= y; w++)
            {
                System.out.print(" ");
            }
            for(x = 1; x <= v; x++)
            {
                System.out.print(z + " ");
            }
            System.out.println();
            z--;
        }
    }
}
