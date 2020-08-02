
/**
 * Write a description of class WordPattern here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.Scanner;
public class WordPattern
{
    public static void main()
    {
        Scanner s = new Scanner(System.in);
        System.out.print("Enter Number: ");
        String userinput = s.nextLine();
        int l = userinput.length();
        System.out.print("Length of string is: " + l + "\n");
        int i,j;
        for (i = 0; i < l; i++)
        {
            for(j = 0; j <= i; j++)
            {
                System.out.print(userinput.charAt(j));
            }
            System.out.println();
        }
    }
}
