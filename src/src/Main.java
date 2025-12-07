import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        String pathToInput = "Input/Day7.txt";
        String pathToInputTest = "Input/Day7test.txt";
        String inp = pathToInput;
        try{
            System.out.println("Part1 solution: "+Day7.day7SolverPart1(inp));
            System.out.println("Part2 solution: "+Day7.day7SolverPart2(inp));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}