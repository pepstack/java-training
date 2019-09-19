/**
 * file: Computer.java
 */
package code.training;

public class Computer {
    private final IOutput output;

    public Computer(IOutput output) {
        this.output = output;
    }


    public IOutput getOutput() {
        return output;
    }


    public static void main(String[] args) {
        Computer comp = new Computer(OutputFactory.createOutput());

        comp.getOutput().output(args[0]);
    }
}
