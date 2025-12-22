import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class Day7 {


    public static int day7SolverPart1(String pathToInput) throws IOException {
        // read file
        List<String> file = Files.readAllLines(Paths.get(pathToInput));
        // true if there is a beam at that index
        boolean[] beam = new boolean[(file.getFirst()).length()];

        int count = 0;
        for (String line: file){ // loop through lines
            for(int i=0;i<line.length();i++){// loop through characters
                char syb = line.charAt(i);

                if(syb == 'S'){
                    beam[i] = true;
                } else if (syb == '^' && beam[i]) {
                    beam[i] = false;

                    if(!beam[i-1]){
                        beam[i-1] = true;
                    }
                    if(!beam[i+1]){
                        beam[i+1] = true;
                    }

                    count++;

                }
            }
            /*
            // print line for debugging
            System.out.println(" ");
            for(int i=0;i<line.length();i++){
                if(beam[i]){
                    System.out.print("|");
                }
                else{
                    System.out.print(line.charAt(i));
                }
            }
            System.out.print(" "+line);
             */
        }
        return count;
    }

    public static long day7SolverPart2(String pathToInput) throws IOException {
        // read file
        List<String> file = Files.readAllLines(Paths.get(pathToInput));
        // true if there is a beam at that index
        //boolean[] beam = new boolean[(file.getFirst()).length()];
        // keeps count of how many ways this column can have a beam
        long[] ways = new long[(file.getFirst()).length()];

        for (String line: file){ // loop through lines
            for(int i=0;i<line.length();i++){// loop through characters
                char syb = line.charAt(i);

                if(syb == 'S'){

                    ways[i] =1;
                } else if (syb == '^' && ways[i]>0) {

                    ways[i-1] += ways[i]; // ways[i] ways a beam could hit the splitter
                    ways[i+1] += ways[i]; // ways[i] ways a beam could hit the splitter
                    ways[i] = 0; // no possible way for previous paths to have a beam directly after

                }
            }

        }
        long count =0;
        for(long c: ways){
            count+=c;
        }
        return count;
    }
}
