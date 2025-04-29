package DSA.Linear_Search.Problems;
import java.util.Scanner;
public class Q2SearchInRange {
    public static int searchRange(int[] arr, int target, int start, int end){
        if(arr.length == 0) return -2;
        for(int i=start;i<=end;i++){
            if(arr[i] == target) return i-start;
        }
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter size of array: ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter array elements to search from: ");
        for(int i=0;i<n;i++)    arr[i] = sc.nextInt();
        System.out.println("Enter starting index: ");
        int start = sc.nextInt();
        System.out.println("Enter ending index: ");
        int end = sc.nextInt();
        if(start>n || start<0 || end>n || end<0) System.out.println("Invalid index! Exiting the program");
        else{
            System.out.println("Enter target element: ");
            int target = sc.nextInt();
            int key = searchRange(arr,target,start,end);
            if(key == -1) System.out.println("Element not found");
            else System.out.println("Element "+ target +" found at index "+key+" from start");
        }
        sc.close();
    }
}

