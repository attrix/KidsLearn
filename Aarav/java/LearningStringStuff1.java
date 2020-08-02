
/**
 * Write a description of class LearningStringStuffOne here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.Scanner;
public class LearningStringStuff1
{
    public static void main()
    {
        Scanner a = new Scanner (System.in);
        System.out.println("Enter String: ");
        String userinput = a.nextLine();
        System.out.println("Enter Character number place: ");
        int location = a.nextInt();
        int l = userinput.length();
        System.out.println("Length is: " + l);
        char ch = userinput.charAt(location);
        System.out.println("Character is at: " + ch);
        String str1 = "Hello";
        String str2 = "Hola";
        System.out.println("The two strings are: " + str1.equals(str2));
    }
}
