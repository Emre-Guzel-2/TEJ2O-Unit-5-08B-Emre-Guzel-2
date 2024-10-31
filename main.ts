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

while (1==1){
    // Setting the motors 
   distacneToObject = sonar.ping(
    // Setting the sonar
    DigitalPin.P1,
    DigitalPin.P2,
    PingUnit.Centimeters
)
      basic.showNumber(distacneToObject)
    //If distacneToObject is biiger than 10 makes the motros go forward 
    if (distacneToObject > 10){
        robotbit.MotorRunDual(robotbit.Motors.M1A, 150, robotbit.Motors.M2A, 150)
        robotbit.StpCarMove(10, 48)
    }
    else {
//If distacneToObject is smaller than 10 it stops the mootrs
        robotbit.MotorStopAll()
        // Moves backward for  10 cm
        robotbit.StpCarMove(-10, 48)
        // Turning 90 degreese 
        robotbit.StepperTurn(robotbit.Steppers.M1, robotbit.Turns.T1B4)
        robotbit.StepperTurn(robotbit.Steppers.M2, robotbit.Turns.T1B4)
        // Setting the speed of the motors and seting the motors
        robotbit.MotorRunDual(robotbit.Motors.M1A, 150, robotbit.Motors.M2A, 150)
        robotbit.StpCarMove(10, 48)

    }
}
})
