// leetcode 1672
package DSA.Arrays.Problems;
import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;
public class Q7MaxWealth {
    public static int maximumWealth(int[][] accounts) {
        int n = accounts.length;
        int m = accounts[0].length;
        
        int currentSum=0;
        for(int i=0;i<n;i++){
            int sum=0;
            for(int j=0;j<m;j++){
                sum += accounts[i][j];
            }
            if(currentSum<sum) currentSum = sum;
        }
        return currentSum;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number of rows: ");
        int n = sc.nextInt();
        System.out.println("Enter number of columns: ");
        int m = sc.nextInt();
        int[][] accounts = new int[n][m];
        System.out.println("Enter array elements: ");
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                accounts[i][j] = sc.nextInt();
            }
        }

        int maxWealth = maximumWealth(accounts);
        System.out.println("Maximum wealth: "+maxWealth);
        sc.close();
    }
}
