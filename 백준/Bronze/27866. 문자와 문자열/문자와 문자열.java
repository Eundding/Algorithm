import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in); // in으로 입력 받음
        String[] s = input.next().split("");
        int N = input.nextInt();
        System.out.println(s[N-1]);

        input.close();
    }
}