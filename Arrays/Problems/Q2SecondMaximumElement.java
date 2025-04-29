package DSA.Arrays.Problems;
import java.util.Scanner;
public class Q2SecondMaximumElement {
    public static int secondMax(int[] arr){
        int max = arr[0];
        int smax = arr[0];
        
        // for(int x:arr){
        //     if(max<x) max = x;
        // }
        // for(int x:arr){
        //     if(smax<x && x!=max) smax=x;
        // }

        for(int x:arr){
            if(max<x) {
                smax = max;
                max = x;
            }
        }
        return smax;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter array elements: ");
        for(int i=0;i<n;i++){
            arr[i] = sc.nextInt();
        }

        int smax = secondMax(arr);
        System.out.println("Second maximum element: "+smax);
        sc.close();
    }
}
