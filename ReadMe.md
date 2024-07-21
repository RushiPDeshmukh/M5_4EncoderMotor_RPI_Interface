This library can be used to control and interface with the M5_4EncoderMotor_Controller via I2C.

### How to enable I2C on Raspberry Pi 
Step1: Download raspi-config deb - (https://archive.raspberrypi.org/debian/pool/main/r/raspi-config/)  
Step2: Install the pkg  `sudo dpkg -i /tmp/raspi-config_*INSERT DATE*_all.deb `   
Step3: Run raspi-config and enable I2C.  
Step4: `sudo i2cdetect -y 1 ` 

## Resources

- Mecanum wheel kinematics : [Eurobot Mecanum Kinematics](https://ecam-eurobot.github.io/Tutorials/mechanical/mecanum.html)
