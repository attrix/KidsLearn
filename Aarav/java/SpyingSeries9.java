/**
 * Write a description of class SpyingSeries9 here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.Scanner;
public class SpyingSeries9
{
   public static void main(String[] args)
   {
       	Scanner s = new Scanner(System.in);
       	System.out.print("Enter the number:" );
       	int userinput = s.nextInt();
       	int fact = 1;
       	int sum = 0;
       	int a;
       	while(userinput > 0)
       	{
       	   a = userinput % 10;
       	   sum = sum + a;
       	   fact = fact * a;
       	   userinput = userinput / 10;
       	}
       	if(sum == fact)
       	{
       	   System.out.println("The number is a spy number");
        }
        else
       	{
       	   System.out.println("The number is not a spy number");
        }
   }
}
