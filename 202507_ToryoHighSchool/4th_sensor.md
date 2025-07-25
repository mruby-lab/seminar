# センサーを使ってみる

明るさセンサーを使ってみます。

今回、明るさセンサとして、CdSセンサを使います。このセンサは、明るさによって抵抗値が変化する特性があります。

## 明るさセンサーの使い方

GPIOを使って、CdSセンサーの抵抗値を計測します。マイコンのGPIO機能は、抵抗値を計測するようには作られておらず、**電圧値を計測する**ようになっています。

そこで、抵抗値を電圧値として計測できるようにする回路を作成します。この回路は、次のようになります。<br>
図中の、3V3は電源で、3.3Vの電圧がかかっています（電源の＋極と考えてください）。GNDは0Vの電圧がかかっています（電源の－極と考えてください）。

![](/images/curcuit_adc.drawio.png)

CdSの抵抗値が変化すると、1Kの抵抗を流れる電流も変化します。オームの法則から、P20の電圧値も変化することになります。

## 明るさの計測

次のようなプログラムで、電圧値を計測します。プログラム中のADC1は、マイコンボードのP20に割り当てられています。

![alt text](/images/adc_program_ja.png)

CdSを手で覆うなどして、明るさを変化させてみて、電圧値も変化していることを確認してください。


# 練習

- CdSを使って、明るさによってLEDの点灯・消灯をさせるプログラムを作成してみてください。
    - 以下の「もし」という機能を使うことで、値を判定できます。

![alt text](/images/if_syntax_ja.png)


<hr/>


[**Back to top**](./README.md)
