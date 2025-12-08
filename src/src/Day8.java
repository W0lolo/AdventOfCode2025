import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

public class Day8 {

    public static long day8SolverPart1(String pathToInput,int noOfShortestEdges) throws IOException {
        List<String> file = Files.readAllLines(Paths.get(pathToInput));

        // read file contents into array
        int junctionBoxNo = file.size();

        // array to store junction boxes
        // first 3 ints in a row store the x,y,z coordinates, the other contains the circuit no
        int[][] boxes = new int[junctionBoxNo][4];

        int i=0;
        for(String line: file){
            String[] spl = line.split(",");
            boxes[i][0] = Integer.parseInt(spl[0]); // x
            boxes[i][1] = Integer.parseInt(spl[1]); // y
            boxes[i][2] = Integer.parseInt(spl[2]); // z
            boxes[i][3] = 0; // circuit no
            i++;
        }

        // maxheap
        PriorityQueue<long[]> shortest = new PriorityQueue<>(noOfShortestEdges,(a,b)->Long.compare(b[0],a[0]));

        // generate all connections and see if they belong in the 1000 shortest connections
        for(i=0;i<boxes.length;i++){
            for(int j=i+1; j<boxes.length;j++){
                
                long dist = calc2Distance(i,j,boxes);

                if(shortest.size()<noOfShortestEdges){ // add element if queue isn't filled
                    long[] entry = {dist,i,j};
                    shortest.add(entry);
                } else if (dist < shortest.peek()[0]) { // add element if smaller than max
                    long[] entry = {dist,i,j};
                    shortest.poll();
                    shortest.add(entry);
                }

            }
        }

        HashMap<Integer,ArrayList<Integer>> circuits = new HashMap<>();
        // circuit No, circuit junction box indices
        int nextCircuit = 1;

        for(long[] conn: shortest){

            int j1 = (int)conn[1];// boxes indexes
            int j2 = (int)conn[2];
            int j1c = boxes[j1][3];// circuit numbers
            int j2c = boxes[j2][3];

            if(j1c == 0 && j2c == 0){// j1,j2 not in circuit
                boxes[j1][3] = nextCircuit;
                boxes[j2][3] = nextCircuit;
                // creating circuit array
                ArrayList<Integer> nCirc = new ArrayList<>(2);
                nCirc.add(j1);
                nCirc.add(j2);

                circuits.put(nextCircuit,nCirc);
                nextCircuit++;
            } else if (j1c == j2c) {
                // do nothing
            } else if (j1c ==0) {// j1 not in circuit, j2 in circuit
                boxes[j1][3] = j2c;
                circuits.get(j2c).add(j1);
            }  else if (j2c ==0) {// j2 not in circuit, j1 in circuit
                boxes[j2][3] = j1c;
                circuits.get(j1c).add(j2);
            } else { // j2 and j1 in different circuits
                ArrayList<Integer> circuit2 = circuits.get(j2c);
                for(int ind: circuit2){// set boxes in circuit j2 to belong in circuit of j1
                    boxes[ind][3] = j1c;
                }
                circuits.get(j1c).addAll(circuit2); // appending circuit2 to circuit1
                circuits.remove(j2c); // removing circuit2 entry
            }
        }

        // getting largest 3 circuits
        long[] largest = {1,1,1};

        for(ArrayList<Integer> circuit: circuits.values()){

            for (i=0;i<largest.length;i++){

                if(circuit.size() > largest[i]){
                    for(int j= largest.length-1; j>i; j--){ // shift
                        largest[j] = largest[j-1];
                    }
                    largest[i] = circuit.size();
                    break;
                }
            }
        }

        long res = 1;
        for(long cs: largest){
            res *= cs;

        }
        return res;
    }

    public static long calc2Distance(int i,int j,int[][] boxes){
        long dx = boxes[i][0]-boxes[j][0];
        long dy = boxes[i][1]-boxes[j][1];
        long dz = boxes[i][2]-boxes[j][2];
        return dx*dx+dy*dy+dz*dz;
    }




    public static long day8SolverPart2(String pathToInput) throws IOException {
        List<String> file = Files.readAllLines(Paths.get(pathToInput));

        // read file contents into array
        int junctionBoxNo = file.size();

        // array to store junction boxes
        // first 3 ints in a row store the x,y,z coordinates, the other contains the circuit no
        int[][] boxes = new int[junctionBoxNo][4];

        int i=0;
        for(String line: file){
            String[] spl = line.split(",");
            boxes[i][0] = Integer.parseInt(spl[0]); // x
            boxes[i][1] = Integer.parseInt(spl[1]); // y
            boxes[i][2] = Integer.parseInt(spl[2]); // z
            boxes[i][3] = 0; // circuit no
            i++;
        }

        // maxheap
        int noOfShortestEdges = 50000;
        PriorityQueue<long[]> shortest = new PriorityQueue<>(noOfShortestEdges,(a,b)->Long.compare(b[0],a[0]));

        // generate all connections and see if they belong in shortest, (limit of 50000 prob enough)
        for(i=0;i<boxes.length;i++){
            for(int j=i+1; j<boxes.length;j++){

                long dist = calc2Distance(i,j,boxes);

                if(shortest.size()<noOfShortestEdges){ // add element if queue isn't filled
                    long[] entry = {dist,i,j};
                    shortest.add(entry);
                } else if (dist < shortest.peek()[0]) { // add element if smaller than max
                    long[] entry = {dist,i,j};
                    shortest.poll();
                    shortest.add(entry);
                }

            }
        }

        HashMap<Integer,ArrayList<Integer>> circuits = new HashMap<>();
        // circuit No, circuit junction box indices
        int nextCircuit = 1;
        //TODO reverse
        PriorityQueue<long[]> shortestFirst = new PriorityQueue<>(noOfShortestEdges,(a,b)->Long.compare(a[0],b[0]));
        shortestFirst.addAll(shortest);

        while(!shortestFirst.isEmpty()){
            long[] conn = shortestFirst.poll();
            int j1 = (int)conn[1];// boxes indexes
            int j2 = (int)conn[2];
            int j1c = boxes[j1][3];// circuit numbers
            int j2c = boxes[j2][3];

            if(j1c == 0 && j2c == 0){// j1,j2 not in circuit
                boxes[j1][3] = nextCircuit;
                boxes[j2][3] = nextCircuit;
                // creating circuit array
                ArrayList<Integer> nCirc = new ArrayList<>(2);
                nCirc.add(j1);
                nCirc.add(j2);

                circuits.put(nextCircuit,nCirc);
                nextCircuit++;
            } else if (j1c == j2c) {
                // do nothing
            } else if (j1c ==0) {// j1 not in circuit, j2 in circuit
                boxes[j1][3] = j2c;
                circuits.get(j2c).add(j1);
            }  else if (j2c ==0) {// j2 not in circuit, j1 in circuit
                boxes[j2][3] = j1c;
                circuits.get(j1c).add(j2);
            } else { // j2 and j1 in different circuits
                ArrayList<Integer> circuit2 = circuits.get(j2c);
                for(int ind: circuit2){// set boxes in circuit j2 to belong in circuit of j1
                    boxes[ind][3] = j1c;
                }
                circuits.get(j1c).addAll(circuit2); // appending circuit2 to circuit1
                circuits.remove(j2c); // removing circuit2 entry
            }

            // check if graph is connected
            // conditions circuits has 1 entry of size 1000
            if(circuits.size() == 1){
                if(circuits.values().iterator().next().size() == boxes.length){
                    System.out.println("Index: "+j1+ "  j1: "+ Arrays.toString(boxes[j1]) +" Index: "+ j2+" j2: "+ Arrays.toString(boxes[j2]));
                    return (long) boxes[j1][0] * boxes[j2][0];
                }
            }
        }

        return -1;
    }
}
