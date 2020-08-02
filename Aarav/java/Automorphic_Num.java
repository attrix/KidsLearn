
/**
 * Write a description of class Automorphic_Num here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Automorphic_Num
{
    public static void main()
    {
        int n = 10,r,count = 0,sq,p;
        sq = n * n;
        int copyof_n = n;
        
        while(n > 0)
        {
            r = n % 10;
            count = count + 1;
            n = n/10;
        }
        p = (int) Math.pow(10,count);
        
        if (sq % p == copyof_n)
        System.out.print("Number is automorphic");
        else
        System.out.print("Number is not automorphic");
    }
}
