/* Leap year or Not Leap year */

// Code:

import java.util.Scanner;
class Hari{
public static void main(String hari[]){
Scanner input=new Scanner(System.in);
int a=input.nextInt();
int ans=a%4;
if (ans==0){
	System.out.println("leap year");
}
else{
	System.out.println("Not leap year");
}


}
}