package com.baks;

import java.util.*;
import java.util.LinkedList;

/**
 * Created by baks on 25/6/17.
 */
public class dfs {

    static  void do_bfs(int x, Graph g)
    {
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.add(x);

        while(!queue.isEmpty())
        {
            int y = queue.remove();
            System.out.println(y);
            List<Integer> list = g.getEdges(y);
            for(int edge : list)
            {
                queue.add(edge);
            }
        }
    }


    static void do_dfs(int x, Graph g)

    {
        System.out.println(x);

        List<Integer> list = g.getEdges(x);
        for(int i =0 ; i < list.size(); i++)
        {
            do_dfs(list.get(i), g);
        }
    }

    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        System.out.println("Enter the no. of vertices");
        int v = scan.nextInt();

        System.out.println("Enter the no. of edges");
        int e = scan.nextInt();

        //create graph
        Graph g = new Graph(v);

        System.out.println("Now add the edges ^_^");

        for(int i =0; i < e; i++){
            int src = scan.nextInt();
            int dest = scan.nextInt();

            g.addEdge(src,dest);

        }

        System.out.println("DFS order of vertices is:");
        //apply dfs on node
        do_dfs(1, g);
    }
}
