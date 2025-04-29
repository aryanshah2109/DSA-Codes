// Leetcode 1

package DSA.Arrays.Problems;
import java.util.Scanner;
import java.util.Arrays;
public class Q5TwoSum {
    public static int[] twoSum(int[] arr,int target){
        int n = arr.length;
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                if(arr[i]+arr[j] == target){
                    return new int[]{i,j};
                }
            }
        }
        return new int[]{};
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number of elements: ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter array elements: ");
        for(int i=0;i<n;i++){
            arr[i] = sc.nextInt();
        }
        System.out.println("Enter target: ");
        int target = sc.nextInt();

        int[] result = twoSum(arr,target);
        if(result.length == 0) System.out.println("No matches found");
        else System.out.println(Arrays.toString(result));
        sc.close();
    }
}
