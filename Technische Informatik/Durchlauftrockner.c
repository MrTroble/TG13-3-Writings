void interruptInitialisierung() {
    IT0 = 1; // Low active
    EX0 = 1; // Enable interrupt 0
    EA = 1; // Enable all
    IT01CF = 0; // Wir gehen davon aus das P3.2 Standard Interrupt input ist.
    // Und lowedge sensitive
}

/* Unser Mikrokontroller supportet standardmaessig den Port 0.0 bis 0.7
 * ohne Crossbar, daher macht es sinn hier Port 0.0 verwenden da dies der Standard
 * port bei Externen Interrupt 1 ist (Bei unserem Controller)
 */
