package DSA.Arrays.Theoretical;
import java.util.Scanner;
import java.util.Arrays;
public class Intro{
    public static void main(String[] args){
        // Syntax for declaration and initialisation
        int[] arr = new int[5];
        int[] arr2 = new int[] {1,2,3,4};
        int[] arr3 = {4,6,1,5,3};
        int arr4[] = new int[9];

        System.out.println("By default value in array without initialisation is "+arr[0]);
        // length of an array can be fetched by arr.length
        // printing array elements
        for(int i=0;i<arr2.length;i++){
            System.out.print(arr2[i]+" ");
        }
        
        Scanner sc = new Scanner(System.in);
        // taking input and printing
        System.out.println("\nEnter array elements: ");
        /*
         * You cannot use for each loop while taking input
         * This is because the variabke used in for each loop
         * acts as a copy of the original element
         * Not as a reference variable
         * We should use for each loop only while doing some 
         * operations
         */

        for(int i=0;i<arr4.length;i++){
            arr4[i] = sc.nextInt();
        }
        System.out.print("Array elements: ");
        for(int x:arr4){
            System.out.print(x+" ");
        }
        sc.close();

        // printing using Arrays.toString(arr) method
        System.out.print("\n");
        System.out.print(Arrays.toString(arr4));

    }
}