package DSA.Linear_Search.Problems;
import java.util.Scanner;
public class Q1SearchInString {
    public static int searchString(String str,char ch){
        int n = str.length();
        for(int i=0;i<n;i++){
            char current = str.charAt(i);
            if(current == ch) return i;
        }
        return -1;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter string to search from: ");
        String str = sc.next();
        System.out.println("Enter character to search in string: ");
        char ch = sc.next().charAt(0);
        int key = searchString(str,ch);
        if(key == -1) System.out.println("Character not found");
        else System.out.println("Character "+ ch +" found at index "+key);
        sc.close();
    }
}
