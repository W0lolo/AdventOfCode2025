import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        // TODO file inputs paths changed
        /* // day 7
        String pathToInput = "Input/Day7.txt";
        String pathToInputTest = "Input/Day7test.txt";
        String inp = pathToInput;
        try{
            System.out.println("Part1 solution: "+Day7.day7SolverPart1(inp));
            System.out.println("Part2 solution: "+Day7.day7SolverPart2(inp));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
         */
        /*
        String pathToInput = "Input/Day8.txt";
        String pathToInputTest = "Input/Day8test.txt";
        String inp = pathToInput;
        try{
            //System.out.println(Day8.day8SolverPart1(inp,1000));
            System.out.println(Day8.day8SolverPart2(inp));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
         */
        try{
            //System.out.println(Day8.day8SolverPart1(inp,1000));
            System.out.println(Day9.day9SolverPart2("Input/Day9.txt"));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}