/**
 * file: Printer.java
 */
package com.pepstack.code.service.impl;

import com.pepstack.code.service.IOutput;


public class Printer implements IOutput {

    public void output(String content) {
        System.out.println("Printer:" + content);

    }
}
