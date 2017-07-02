import java.util.*;


class Person{
    private String firstname;
    private String lastname;
    private int age;

    public Person(String last, String first, int a)
    {
        lastname = last;
        firstname = first;
        age=a;

    }
    public void getName()
    {
        System.out.println("First name is: "+firstname);
    }


}

class Hello{

public static void main(String[] args)
{
Person a = new Person("Syed", "bakhtiyar", 20);
a.getName();
}

}