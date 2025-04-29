package DSA.Arrays.Problems;
import java.util.Scanner;
import java.util.Arrays;
public class Q1MaximumElement {
    public static int maxElement(int[] arr){
        int max = arr[0];
        for(int x:arr){
            if(max<x)   max = x;
        }
        return max;
    }
    // Method to find minimum element
    // public static int minElement(int[] arr){
    //     int min = arr[0];
    //     for(int x:arr){
    //         if(min>x) min = x;
    //     }
    //     return min;
    // }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        System.out.print("Enter array elements: ");
        for(int i=0;i<n;i++){
            arr[i] = sc.nextInt();
        }

        int maximum = maxElement(arr);
        System.out.print("Maximum element in the array: "+maximum);
        sc.close();    
    }
}
