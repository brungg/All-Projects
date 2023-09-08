import java.util.*;
public class AscendingDescending {
	public static void main(String[] args) {
		float[] arr = new float[50];
		float[] newArr = new float[50];
		Random r = new Random();
		int i;
		for(i = 0; i < arr.length; i++) {
			float a = r.nextFloat(0, 1000);
			arr[i] = a;
			newArr[i] = a;
		}
		for(i = 0; i < arr.length; i++) {
			for (int j = i + 1; j < arr.length; j++) {
                float temp = 0f;
                if (arr[j] < arr[i]) {
                    temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
                float temp1 = 0f;
                if (newArr[j] > newArr[i]) {
                    temp1 = newArr[i];
                    newArr[i] = newArr[j];
                    newArr[j] = temp1;
                }
            }
		}
		for(i = 0; i < arr.length; i++) {
			if(i == 0) { System.out.print("First: " + arr[i] + ", "); }
			else if(i % 10 == 0) { System.out.print("\n"); }
			else if(i != arr.length - 1) { System.out.print(arr[i] + ", "); }
			else { System.out.print(arr[i]); }
		}
		for(i = 0; i < arr.length; i++) {
			if(i == 0) { System.out.print("\n\nSecond: " + newArr[i] + ", "); }
			else if(i % 10 == 0) { System.out.print("\n"); }
			else if(i != arr.length - 1) { System.out.print(newArr[i] + ", "); }
			else { System.out.print(newArr[i]); }
		}
	}
}
