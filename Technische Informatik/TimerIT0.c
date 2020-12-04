/**
 * Timer 8 bit auto reloade
 * Wert 56
 * ISR_T0 Bitflip
 */

void init() {
    TMOD = 2;
    TH0 = 55;
    TL0 = 55;
    ET0 = 1;
    EA = 1;
}

void isrt() interrupt 1 {
    S = !S;
}