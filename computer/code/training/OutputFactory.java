/**
 * file: OutputFactory.java
 */
package code.training;

public class OutputFactory {

    public static IOutput createOutput() {
        // 1.0
        //    return new Printer();

        // 2.0
        return new AdvancePrinter();
    }
}
