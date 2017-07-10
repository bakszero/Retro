package com.baks;


import java.util.*;
import java.util.LinkedList;

/**
 * Created by baks on 25/6/17.
 */

class Graphx
{
    private Map<Integer, List<Integer>> adjlist;

    //Initialise graph
    public Graphx(int n)
    {
        adjlist = new HashMap<Integer, List<Integer>>();
        for(int i =1; i <= n;i++)
        {
            adjlist.put(i, new LinkedList<Integer>());

        }

    }

    void addEdge(int src, int dest){
        List<Integer> list = adjlist.get(src);
        list.add(dest);
    }

    List<Integer> getEdges(int src){

        return adjlist.get(src);

    }



}
public class impladjlist {


    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter the no. of vertices");
        int v = scan.nextInt();
        System.out.println("Enter the no. of edges");
        int e = scan.nextInt();

        //Define your Graph
        Graphx g = new Graphx(v);


        System.out.println("Now enter the edges one-by-one");
        //edges
        for(int i =0 ; i < e; i++)
        {
            int src = scan.nextInt();
            int dest = scan.nextInt();
            g.addEdge(src,dest);
        }

        //print adjacency list
        for(int i =1; i <=v; i++)
        {
            System.out.print(i+" -> " );
            List<Integer> edges = g.getEdges(i);

            System.out.println(edges);
        }
        scan.close();

    }
}
