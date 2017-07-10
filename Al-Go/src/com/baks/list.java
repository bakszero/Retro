package com.baks;

import java.util.LinkedList;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.*;

/**
 * Created by baks on 23/6/17.
 */
public class list {
    public static void main(String[] args){
        //create a collection of linked list array.
        LinkedList<String> ll = new LinkedList<String>();

        ll.add("sunday");
        ll.add("monday");
        ll.add("tuesday");
        ll.add("wednesday");


        //Add to the list
        //String[] toys = {"Shoe", "Ball", "Frisbee"};
        //list.addAll((Arrays.toList(toys)));
        for (String str: ll){ //THIS WORKS JUST LIKE PYTHON!!!{
            System.out.println(str);

         }

         ll.remove(3);

        String var = ll.getFirst();
        System.out.println(var);
    }
}
