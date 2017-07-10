package com.baks;

import java.util.*;

/**
 * Created by baks on 23/6/17.
 */

class square{

     public double squaring(int n){
        return Math.pow(n,2);
    }
}
public class power {
    public static void main(String[] args)
    {
        Scanner scan;
        scan = new Scanner(System.in);
        System.out.println("Enter a no. whose square you wish to see");

        int n;
        n = scan.nextInt();

        square s = new square();
        System.out.println(s.squaring(n));

    }
}
