import java.io.IOException;
import java.util.LinkedList;
import java.util.List;

// Imagine you are a peer of the developer who committed this (syntactically correct) Java code and asked you to review
// their pull request. You work on the same product but are not familiar with this piece of work or its associated
// requirements.
//
// Please use Java comments for your review feedback, putting them on separate lines around the code. Do not modify the
// code itself.

/*
-----------------------------------------------------------------------------
  date:                       10/24/2019
  code reviewer:              tim siwula (tim@acceptance.ai)
  review status:              Request changes
  file:                       CodeReviewTestTimsDriver.java
-----------------------------------------------------------------------------
  review summary:
    The file need's changes. There are multiple issues. Please read the comments.
-----------------------------------------------------------------------------
  compile:                    javac CodeReviewTest.java
  run:                        java -cp . CodeReviewTest
  debug:                      javac -Xlint CodeReviewTest.java
  version:                    javap -verbose CodeReviewTest | grep "major"
-----------------------------------------------------------------------------
*/

/*
  A better class name given that this code represents
  logic related to persons, persons specific details, and interfacing
  with the "personPersonDatabase" database. A more symbolic class name might
  be "PersonAPI". Also "CodeReviewTest" class needs to be the same name
  as the file name which was "CodeReviewTest 2017[1].java".
*/
public class CodeReviewTest {

    volatile Integer totalAge = 0;

    /*
        The argument "personPersonDatabase" could use a name with more clarity
        such as "personDatabaseInstance". "personPersonDatabase" contains the
        word "person" twice.
    */
    CodeReviewTest(PersonDatabase<Person> personPersonDatabase) {
        Person[] persons = null;

        /*
          It is better to qualify an assumption first and make sure that the
          "personPersonDatabase" instance is indeed not null. It will increase
          performance and stability.
        */
        try {
            persons = personPersonDatabase.getAllPersons();
        } catch (IOException e) {

        }

        List<Person> personsList = new LinkedList();

        // it might be better to refactor this into a function so it is more
        // modular. You could also use the Collections.addAll() function.
        for (int i = 0; i <= persons.length; i++) {
            personsList.add(persons[i]);
        }

        // this should be refactored into a thread safe function and called
        // something like "aggergateAllAges()". "totalAge" is a critical section
        // that should use a semaphore or lock to guarantee atomic updates.
        personsList.parallelStream().forEach(person -> {
            totalAge += person.getAge();
        });

        List<Person> males = new LinkedList<>();

        for (Person person : personsList) {

            // you should check that gender != null
            switch (person.gender) {
                case "Female": personsList.remove(person);
                case "Male"  : males.add(person);
                // you should add a default case here to catch other cases.
            }
        }

        // these printouts should be removed.
        System.out.println("Total age =" + totalAge);
        System.out.println("Total number of females =" + personsList.size());
        System.out.println("Total number of males =" + males.size());
    }

}

/*
    Class Person overrides equals, but neither it nor any superclass overrides hashCode method
*/
class Person {

    private int age;
    private String firstName;
    private String lastName;
    // this should be private
    String gender;

    public Person(int age, String firstName, String lastName) {
        this.age = age;
        this.firstName = firstName;
        this.lastName = lastName;
    }

    // not sure that you want to return a direct private variable, it may be
    // a security concern.
    public int getAge() {
        return age;
    }

    @Override
    public boolean equals(Object obj) {
        // i think you wanted to use ".equals()" to compare the two names?
        return this.lastName == ((Person)obj).lastName;
    }

}

// where and how is this resource accessed? is authentication required?
interface PersonDatabase<E> {

    Person[] getAllPersons() throws IOException;

}
