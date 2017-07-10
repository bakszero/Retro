package com.baks;

import java.util.*;

/**
 * Created by baks on 21/6/17.
 */


class Hello {

    public static void main(String[] args)
    {


        Scanner scan = new Scanner(System.in);

        System.out.println("Enter a new number");
        int input = scan.nextInt();

        //System.out.print("The entered value is"+"\n"+input);

        int[] arr = new int[input];
        for (int i =0;i < arr.length; i++)
        {
            arr[i]=scan.nextInt();
        }
        for(int i =0 ; i < arr.length; i++)
        {
            System.out.println("Arr values are : "+ arr[i] );
        }

    }
}
