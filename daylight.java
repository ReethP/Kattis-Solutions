import java.util.Scanner;

class daylight{
	public static void main(String[]args){
		Scanner sc = new Scanner(System.in);
		while(true){
				try{
						String rawinp = sc.nextLine();
						String [] userint = rawinp.split(" ");
						String [] time1 = userint[3].split(":");
						String [] time2 = userint[4].split(":");
						int [] inttime1 = new int[2];
						int [] inttime2 = new int[2];
						int iterator = 0;
						int iterator2 = 0;
						for(String w:time1){
							inttime1[iterator] = Integer.parseInt(w);
							iterator += 1;}
				
						for(String x:time2){
							inttime2[iterator2] = Integer.parseInt(x);
							iterator2 += 1;}
						if(inttime2[1] < inttime1[1]){
							inttime2[0] = inttime2[0] - 1;
							inttime2[1] = inttime2[1] + 60;
						}
				
						int hours = inttime2[0] - inttime1[0];
						int minutes = inttime2[1] - inttime1[1];
				
						for(int i = 0; i<3;i++){
							System.out.print(userint[i]+" ");
						}
						System.out.print(hours+" hours "+ minutes+ " minutes");
						System.out.println();}catch(Exception e){break;}}
	}
}