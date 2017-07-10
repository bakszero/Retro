package com.baks;

import java.util.*;
import java.util.LinkedList;

/**
 * Created by baks on 25/6/17.
 */
public class bfs {

    static void do_bfs(int x, Graph g, int[] visited)
    {
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.add(x);

        while(!queue.isEmpty()){
            int y = queue.remove();
            visited[y]=1;
            System.out.println(y);

            List<Integer> list = g.getEdges(y);

            for(int edge : list){
                if (visited[edge]==0)
                    queue.add(edge);

            }

        }

    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter the no. of vertices");
        int v = scan.nextInt();
        System.out.println("Enter the no. of edges");
        int e = scan.nextInt();

        //Define your Graph
        Graph g = new Graph(v);
        int[] visited = new int[v+1];

        System.out.println("Now enter the edges one-by-one");
        //edges
        for (int i = 0; i < e; i++) {
            int src = scan.nextInt();
            int dest = scan.nextInt();
            g.addEdge(src, dest);
        }
        System.out.println("BFS Order is: ");

        do_bfs(5,g, visited);



    }
}
