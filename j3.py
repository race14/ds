
import java.util.*;

public class four {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of peers: ");
        int numPeers = scanner.nextInt();

        double localTime = System.currentTimeMillis() / 1000.0;
        List<Double> remoteTimes = new ArrayList<>();
        Random random = new Random();
        
        for (int i = 0; i < numPeers; i++) {
            remoteTimes.add(localTime + (random.nextDouble() * 2 - 1));
        }

        System.out.println("Local time: " + localTime);
        System.out.println("Remote times: " + remoteTimes);

        double offset = remoteTimes.stream().mapToDouble(time -> time - localTime).average().orElse(0.0);
        double adjustedTime = localTime + offset;

        System.out.println("Adjusted local time: " + adjustedTime);
        scanner.close();
    }
}


# In[ ]:





# In[ ]:




