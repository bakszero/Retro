package com.baks;

/**
 * Created by baks on 23/6/17.
 */

class A{
    int x = 0;

    void setX(int n){
        x =n;
    }

    void inc(int n){
        x+=n;
    }
}



class B extends A{
    void inc(int d){
        x+=d;
    }
}
public class inheritance {
    public static void main(String[] args){
        A a = new A();
        a.setX(4);
        System.out.println(a.x);

        B b = new B();
        b.setX(3);
        System.out.println(b.x);
    }




}
