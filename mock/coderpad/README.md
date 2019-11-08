coderpad java details



Java
Running OpenJDK 11 - Autocomplete is enabled
You should define a public class named Solution with a public static void main. Your code is compiled with -Xlint (linting) and run with -ea (assertions enabled).
A few libraries are included for your convenience, and are available on the classpath with no additional work from you. Simply import and fire away:
* json-simple for parsing/encoding JSON.
The google code project page has some useful examples.
* guava provides immutable collections and other handy utility classes.
* Apache Commons Lang for assorted utilities.
Has a bunch of useful stuff like date parsing. The import prefix is org.apache.commons.lang3, so you can perform imports by writing import org.apache.commons.lang3.ArrayUtils.
* JUnit, the gold standard for testing in Java. If you want to ask your candidate to write JUnit-style tests during the interview, please format your Java code like so:
  import org.junit.*;
  import org.junit.runner.*;

  public class Solution {
    @Test
    public void testNoop() {
      Assert.assertTrue(true);
    }

    public static void main(String[] args) {
      JUnitCore.main("Solution");
    }
  }
Stack traces originating from JUnit errors are trimmed for brevity.
In the future we may auto-detect the existence of @Test annotations, so stay tuned.
* jMock, a library to assist with mocking in Java. Combining jMock with the previous JUnit example:
  import org.jmock.*;
  import org.junit.*;
  import org.junit.runner.*;

  interface Receiver {
    void receive(String message);
  }

  public class Solution {
    @Test
    public void testMock() {
      Mockery context = new Mockery();
      Receiver receiver = context.mock(Receiver.class);
      context.checking(new Expectations() {{
        oneOf (receiver).receive("hello");
      }});
      receiver.receive("hello");
      context.assertIsSatisfied();
    }

    public static void main(String[] args) {
      JUnitCore.main("Solution");
    }
  }
Are there any libraries or settings we missed? Feel free to email us with suggestions!
