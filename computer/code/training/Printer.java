/**
 * file: Printer.java
 */
package code.training;

public class Printer implements IOutput {

    public void output(String content) {
        System.out.println("Printer:" + content);

    }
}
