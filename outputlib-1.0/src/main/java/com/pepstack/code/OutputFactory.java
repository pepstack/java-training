/**
 * file: OutputFactory.java
 */
package com.pepstack.code;

import com.pepstack.code.service.IOutput;

import com.pepstack.code.service.impl.Printer;
import com.pepstack.code.service.impl.AdvancePrinter;


public class OutputFactory {

    public static IOutput createOutput() {
        // 1.0
        //    return new Printer();

        // 2.0
        return new AdvancePrinter();
    }
}
