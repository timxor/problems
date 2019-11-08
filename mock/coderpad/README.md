# coderpad java details


# python interpreter details
Python 3
Running CPython 3.6 - Autocomplete is enabled
Python 3 in CoderPad is generally identical to the Python 2.x environment.

One small difference is that mock is available in Python 3 in the stdlib, as unittest.mock.

Information about the Python 2.x environment is reproduced below:

The Python environment is augmented with a few REPL features as well as some helpful libraries.

The REPL uses IPython to provide a REPL with history, highlighting, and autocomplete. Additionally, whenever you run scripts in CoderPad’s editor, the REPL will deposit you at the exact line and state of any exceptions. If there were no errors, you will have a REPL with access to all of the variables and functions defined in your script.

The libraries included and ready for importing are:

requests for simpler HTTP requests.
numpy, scipy, pandas, and scikit-learn for advanced numerical analysis. Unfortunately, plotting does not work in CoderPad’s purely textual interface at this time.
Testing

We’ve got a few ways you can test your Python code in CoderPad:

The excellent unittest library that ships with Python by default. Here’s a quick example:

import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # s.split should throw when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

unittest.main(exit=False)
The versatile pytest. The above snippet of code would look like the following when written for pytest:

import pytest

def test_upper():
    assert 'foo'.upper() == 'FOO'

def test_isupper():
    assert 'FOO'.isupper()
    assert not 'Foo'.isupper()

def test_split():
    s = 'hello world'
    assert s.split() == ['hello', 'world']
    # s.split should throw when the separator is not a string
    with pytest.raises(TypeError):
        s.split(2)

pytest.main()
mock is also available if you need to stub out some behavior. Here’s a quick usage example:

from mock import Mock

mock = Mock()
mock.method(1, 2, 3)
mock.method.assert_called_with('this should break')
mock can of course be combined with unittest and pytest for even more fun.

hypothesis is available for property-based testing in Python. You can read more about it on their website, but here’s a stubbed example of how you might test that an encoding and decoding function both work:

from hypothesis import given
from hypothesis.strategies import text

def encode(string):
    # return encoded string

def decode(string):
    # return decoded string

@given(text())
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s

test_decode_inverts_encode()
Calling test_decode_inverts_encode() fires up Hypothesis and tries to find an input that breaks your code.

Are there any libraries or settings we missed? Feel free to email us with suggestions!




# java runtime/compiler details

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
