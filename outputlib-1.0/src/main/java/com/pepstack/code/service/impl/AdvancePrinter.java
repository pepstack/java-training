/**
 * file: AdvancePrinter.java
 */
package com.pepstack.code.service.impl;

import com.pepstack.code.service.IOutput;


public class AdvancePrinter implements IOutput {

    public void output(String content) {
        System.out.println("AdvancePrinter:" + content);

    }
}
