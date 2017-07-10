package com.baks;

//import java.util.LinkedList;
//import javafx.util.Pair;
/**
 * Created by baks on 23/6/17.
 */

class Node
{
    int val;
    Node next, prev;

    Node(){
        next = null;
        prev = null;
    }
}


class LinkedList
{
    Node head =null;
    Node temp =null;
    Node tail = null;

    int size =0;

    //Add a new element at the end of the list
    public void add(int x){

        size++;

        if (head == null) {
            head =  new Node();
            tail = head;
            head.val = x;
            head.next=null;
        }
        else
        {
            Node y = new Node();
            y.next=null;
            tail.next=y;
            y.val=x;
            y.prev=tail;
            tail = y;
        }
    }

    //get the size of the ll
    public int getSize()
    {
        return this.size;
    }


    public int add(int x, int index) //Add x at index position, return 1:s, -1:f
    {
        //Check errors
        if(index < 0 || index >= getSize())
            return -1;
        //if index is 0
        size++;
        if(index == 0) {
            Node y = new Node();
            y.val = x;
            y.next = head;
            y.prev = null;
            head = y;

            return 1;
        }

        //if index is size of the linked list
        if(index == getSize()-1){
            Node y = new Node();
            y.val=x;
            y.next=null;
            y.prev=tail;
            tail.next=y;
            tail = y;

            return 1;

        }

        //normal iteration
        Node y = new Node();
        y.val=x;

        temp=head;

        for(int i =0; i < index-1; i++)
        {
            temp=temp.next;
        }

        y.prev=temp;
        y.next=temp.next;
        temp.next.prev=y;
        temp.next=y;

        return 1;

    }

    public int remove(int index) //Return 1 for success, -1 for failure.
    {

        //Error conditions

        if (index < 0 || index >= getSize())
            return -1;

        if(head==null)
            return -1;

        //if index is 0
        if (index == 0){
            int x = head.val;
            head = head.next;
            head.prev=null;
            size--;

            return 1;

        }

        //if index is size of the ll

        if(index == getSize()-1){
            int x = tail.val;
            tail = tail.prev;
            tail.next=null;
            size--;

            return 1;
        }


        temp = head;
        for(int i =0;i < index-1; i++){
            temp = temp.next;

        }

        temp.next =temp.next.next;
        temp.next.prev=temp;
        size--;

        return 1;


    }


}


public class testgraph {
    public static void main(String[] args)
    {
        LinkedList ll = new LinkedList();
        ll.add(5);
        ll.add(10);
        ll.add(34);
        ll.add(454);

        int y =ll.getSize();
        System.out.println("Size: "+y);
        int x =ll.add(6, 1);
        ll.remove(3);
        y= ll.getSize();
        System.out.println("Size: "+y);


        //Printing the elements of the list
        System.out.println("Elements of the list are: ");
        Node temp = ll.head;

        for(int i = 0; i < ll.getSize(); i++){
            System.out.println("Index "+i+": "+temp.val);
            temp=temp.next;

        }

    }

}
