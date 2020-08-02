/**
 * Write a description of class Positive_Negative here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */

// VAIBHAV HElPED ME IN THIS

import java.util.Scanner;
public class Between_Numbers
{
    public static void main(String []args)
    {
        Scanner a = new Scanner(System.in);
        System.out.println("Enter first number:");
        int first = a.nextInt();
        System.out.println("Enter second number:");
        int second  = a.nextInt();
        int i = second - first;
        int n = first - second;
        int j = 0;

        while (second > first && j < i)
        {
             j++;
             first += 1;
             System.out.println (first + "\n");
        }
        while (first > second && j < n)
        {
           
            j++;
            first -= 1;
            System.out.println (first + "\n");
            
        }
    }   
}
