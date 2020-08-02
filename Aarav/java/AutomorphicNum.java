/**
 * Write a description of class AutomorphicNum here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.*;
public class AutomorphicNum
{
    public static void main(String []args)
    {
        Scanner usernum = new Scanner(System.in);
        System.out.print("Enter a number:");
        int num = usernum.nextInt();
        int squared = num^2;
        String num1 = Integer.toString(num);
        String squared1 = Integer.toString(squared);
        if(squared1.endsWith(num1))
        {
         System.out.println("It is not an Automorphic Number");
        }
        else
        {
         System.out.println("It is an Automorphic Number");
        }
    }
}
