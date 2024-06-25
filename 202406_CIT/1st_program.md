# Try Block Programming

**Block programming** is one of a visual programming method, we select blocks from the tool panel and place them (or arrange them) on the programming field.

Several type blocks are ready. `Control`, `Operators` and `Variabes` are the basic blocks.

In addition, we use `RBoard` blocks that control RBoard functions.

## Include `RBoard` blocks

Press `Add Extension` ![Add Extension](./images/extention.png), then open extentions panel. Choose `RBoard` blocks.

![RBoard Blocks](./images/rboard_blocks.png)

## 1st Block Program

Let's implement the 1st block program.

The 1st program is blinking an LED, which is the simplest program using RBoard.

- Place `forever` block into programming field.<br>
![step 1](./images/step1.png)

- Place blocks as follows:<br>
![step 2](./images/step2.png)

Note that the block colors are different for each block group. `Control` is orange, `RBoard` is green, and so on.

The functions of the blocks are explained later.

- To execute, select "File"-"Send to MicroComputer" menu.<br>
![step3](./images/step3.png)

This will open a new window where you can transfer your program to RBoard.

## Transfer your program

If you want to change the language, select the language selection icon at the top right as follows:<br>
![step4](./images/step4.png)

You can ready to transfer and execute your program.

Is you see connect button ![connect button](./images/connect_button.png), click this button. Then you see the device selection window. Choose `MCP2221 USB-I2C/UART Combo (COMxx)`. "Connection established" message will be shown.

Press **RS button(Red Button) on RBoard**, then you will see as follows:<br>
![step5](./images/step5.png)

Click "Write". Your program will be written to RBoard.

Click "Execute". Your program will run on RBoard.

You will see blinkng green LED on RBoard.


<hr/>

[**Move to next**](./1st_program_details.md)

[**Back to top**](./README.md)
