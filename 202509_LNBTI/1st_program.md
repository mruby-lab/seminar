# Try Block Programming

**Block programming** is one of a visual programming method, we select blocks from the tool panel and place them (or arrange them) on the programming field.

Several type blocks are ready. `Control`, `Operators` and `Variabes` are the basic blocks.

In addition, we use `Microcom` blocks that control microcontroller functions.

## Include `Microcom` blocks

Press `Add Extension` ![Add Extension](/images/extention.png) (Bottom-left of the window), then open extensions panel. Choose `Microcom` blocks.

![Microcom Extension](/images/extension_microcom.png)

## 1st Block Program

Let's implement the 1st block program.

The 1st program is blinking an LED, which is the simplest program using microcontroller.

- Place `forever` block into programming field.<br>
![step 1](/images/step1.png)

- Place blocks as follows:<br>
![step 2](/images/step2_microcom.png)

Note that the block colors are different for each block group. `Control` is orange, `Microcom` is green, and so on.

The functions of the blocks are explained later.

- To execute, select "File"-"Send to MicroComputer" menu.<br>
![step3](/images/step3.png)

This will open a new window where you can transfer your program to your microcontroller.

## Transfer your program

If you want to change the language, select the language selection icon at the top-right as follows:<br>
![step4](/images/step4.png)

You can ready to transfer and execute your program.

Is you see connect button ![connect button](/images/connect_button.png), click this button. Then you see the device selection window. Choose `STM32 STLink`. "Connection established" message will be shown.

Press **Reset button(Black Button) on microcontroller**, then you will see as follows:<br>
![step5](/images/step5.png)

Click "Write". Your program will be written to the microcontroller.

Click "Execute". Your program will run on the microcontroller.

You will see blinking green LED on your microcontroller.


## Exercise

1. Change the blinking speed, more faster.

<hr size="10" color="Gray">

[**Move to next**](./2nd_circuit.md)

<!-- [**Move to next**](./2nd_circuit.md) -->

[**Back to top**](./README.md)
