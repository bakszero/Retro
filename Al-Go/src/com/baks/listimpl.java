package com.baks;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/**
 * Created by baks on 25/6/17.
 */
public class listimpl {
    public static void main(String[] args){
        List<String> list = new ArrayList<String>();

        list.add("hssjd");
        list.add("hsssjd");
        list.add("hsssssjd");
        list.add("hsssssssssjd");
        list.add("hssssssjd");
        list.add("hssssjd");
        list.add("hsssssjd");


        System.out.println(list.contains("hssjd"));

        //iterating through the collection
        for(int i= 0; i < list.size(); i++)
        {
            System.out.println(list.get(i));
        }
    }
}
