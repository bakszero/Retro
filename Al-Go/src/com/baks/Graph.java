package com.baks;

import java.util.*;

/**
 * Created by baks on 25/6/17.
 */
public class Graph {

        private Map<Integer, List<Integer>> adjlist;

        //Initialise graph
        public Graph(int n)
        {
            adjlist = new HashMap<Integer, List<Integer>>();
            for(int i =1; i <= n;i++)
            {
                adjlist.put(i, new java.util.LinkedList<Integer>());

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

