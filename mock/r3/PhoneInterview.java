import java.util.HashSet;
import java.util.Collections;
import java.io.IOException;

// javac PhoneInterview.java && java -cp . PhoneInterview
//
// wallet - spend & get balance
//
// example file contents: 1,100,200,200,1000,1
//
// built in kotlin

interface Wallet {

    // Iteration 1
    /**
     * Load money into my wallet (fixed sized denominations of any kind are acceptable)
     */
    void load(String filename);

    /**
     * Return current balance of my wallet
     */
    Long getBalance();

    /**
     * Return the coins in the wallet.
     * (peek does NOT need to be performant as to be used solely for testing)
     */
    Collection<Long> peek();
}

public class PhoneInterview implements Wallet
{
    // 1,100,200,200,1000,1
    Map<String, Integer> balanceWithFrequency = new HashMap<String, Integer>();
    public Long balance = new Long(0);

    public static void main(String [] args)
    {
        String input = "input.txt";
        load(input);
        Long myBalance = getBalance();
        System.out.println("myBalance = "+ myBalance);
    }

    Long getBalance(){
        // check that file exists and is not empty
        // then return the sum of all numbers
        return balance;
    }

    void load(String filename){
        // check file exists
        if(filename != null) {
            try (Stream<String> stream = Files.lines(Paths.get(filename), StandardCharsets.UTF_8)) {
                stream.forEach(s -> {
                  if (s != null){
                  balanceWithFrequency.put(s, balanceWithFrequency.get(s) + 1);
              } else {
                Integer one = new Integer(1);
                balanceWithFrequency.put(s, one);
              }});
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    public Collection<Long> peek(){
        List<Long> myBalance = new ArrayList<Long>();
        for(String s : balanceWithFrequency.entrySet()) {
            Long current = new Long(Long.parseInteger(s.getKey()));
            myBalance.add(current);
        }
        return myBalance;
    }
}
