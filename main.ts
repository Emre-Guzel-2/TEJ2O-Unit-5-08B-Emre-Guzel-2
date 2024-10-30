/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Emre Guzel
 * Created on: Oct 30 2024
 * This program tuns 2 mootrs and stops them when the distacne is smaler tahn 10 cm
*/
// Setting the varibels 
let distacneToObject: number = 0

// Setting the screen
basic.clearScreen()
basic.showIcon(IconNames.Happy)

// When it is clikes a it will going to mesuare the distacne and make the mootrs work 
input.onButtonPressed(Button.A,function(){
basic.clearScreen()

// Setting the sonar
distacneToObject = sonar.ping(
    DigitalPin.P1,
    DigitalPin.P2,
    PingUnit.Centimeters
)
    // Setting the motors 
    robotbit.StepperTurn(robotbit.Steppers.M1, robotbit.Turns.T1B4)
    robotbit.StepperTurn(robotbit.Steppers.M2, robotbit.Turns.T1B4)
    
    basic.showNumber(distacneToObject)
})


