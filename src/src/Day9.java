import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Arrays;

public class Day9 {

    public static long day9SolverPart1(String pathToInput) throws IOException {
        // read file
        int[][] tiles = new int[1000][2];
        int count = 0;
        long maxArea= -1;
        try(BufferedReader br = Files.newBufferedReader(Paths.get(pathToInput))){
            String line;
            while ((line = br.readLine()) != null){ // reading file via buffered reader
                String[] inp = line.split(",");
                tiles[count][0] = Integer.parseInt(inp[0]);
                tiles[count][1] = Integer.parseInt(inp[1]);

                // calculating largest area
                for(int i=0; i< count; i++){
                    long area = calcArea(tiles[count][0],tiles[count][1],tiles[i][0],tiles[i][1]);
                    if (area > maxArea){
                        System.out.println(tiles[count][0]+" "+ tiles[count][1]+" "+ tiles[i][0]+" "+tiles[i][1]);
                        maxArea = area;
                    }
                }
                count++;
            }
        }
        return maxArea;
    }

    public static long calcArea(int x1,int y1, int x2,int y2){
        int dx = x1-x2;
        dx = (dx < 0) ? -dx +1 : dx+1;
        int dy = y1-y2;
        dy = (dy < 0) ? -dy +1 : dy+1;
        return (long)dx*dy;
    }

    public static long day9SolverPart2(String pathToInput) throws IOException {
        // read file
        Path path = Paths.get(pathToInput);
        long lineAmm = Files.lines(path).count();
        int[][] tiles = new int[(int)lineAmm][2];
        int count = 0;
        long maxArea= -1;

        // load polygon into tiles
        try(BufferedReader br = Files.newBufferedReader(path)){
            String line;
            while ((line = br.readLine()) != null){ // reading file via buffered reader
                String[] inp = line.split(",");
                tiles[count][0] = Integer.parseInt(inp[0]);
                tiles[count][1] = Integer.parseInt(inp[1]);
                count++;
            }
        }

        // need to check if rectangle is contained in this wierd polygon
        // need to check none of the polygon edges intersect the rectangle edges

        // generating rectangle
        for(int i=0;i< tiles.length-1;i++){
            for(int j=i+1; j<tiles.length; j++){

                // reordering
                int x1 = tiles[i][0];
                int x2 = tiles[j][0];
                int y1 = tiles[i][1];
                int y2 = tiles[j][1];
                if(y1 > y2){
                    int temp = y1;
                    y1 = y2;
                    y2 = temp;
                }
                if(x1 > x2){
                    int temp = x1;
                    x1 = x2;
                    x2 = temp;
                }

                // check area
                long area = calcArea(tiles[i][0],tiles[i][1],tiles[j][0],tiles[j][1]);

                System.out.println(x1+" "+x2+" "+y1+" "+y2);
                System.out.println(Arrays.toString(tiles[i]) +" "+ Arrays.toString(tiles[j]));
                System.out.println("Area: "+area);

                if(area > maxArea){
                    // rectangle is a contender if valid

                    boolean valid = true;
                    // checking intersections
                    for(int k=0; k< tiles.length; k++){
                        // check intersection
                        int[] u1 = tiles[(k + 1) % tiles.length];
                        int[] u2 = tiles[k];

                        if (checkIntersection(x1,y1,x2,y2,u1,u2)){
                            valid = false;
                            break;
                        }
                    }

                    if(valid){
                        maxArea = area;
                    }

                }
            }
        }

        return maxArea;
    }

    public static boolean checkIntersection(int x1, int y1, int x2, int y2,int[] u1,int[] u2){
        // ordering u1 and u2
        int ux1 = u1[0];
        int ux2 = u2[0];
        int uy1 = u1[1];
        int uy2 = u2[1];
        if(ux1>ux2){
            int temp = ux1;
            ux1 = ux2;
            ux2 = temp;
        }
        if(uy1>uy2){
            int temp = uy1;
            uy1 = uy2;
            uy2 = temp;
        }

        // vertical intersector
        if(ux1 == ux2){
            return checkHor(x1, x2, y1, y2, ux1, uy1, uy2);
        } // horizontal intersector
        else if(uy1 == uy2){
            return checkVer(x1, x2, y1, y2, uy1, ux1, ux2);
        }
        // horizontal
        return false;
    }

    public static boolean checkHor(int x1,int x2,int y1,int y2,int ux,int uy1,int uy2){
        if(x1<ux && ux<x2){
            if(uy1 <= y1 && y1 < uy2){
                return true;
            }
            return uy1 < y2 && y2 <= uy2;
        }
        return false; // no intersection
    }

    public static boolean checkVer(int x1,int x2,int y1,int y2,int uy,int ux1,int ux2){
        if(y1 < uy && uy < y2){
            if(ux1 <= x1 && x1 < ux2){
                return true;
            }
            return ux1 < x2 && x2 <= ux2;
        }
        return false;
    }

}
