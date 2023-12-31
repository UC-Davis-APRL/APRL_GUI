# APRL-GUI 
A frontend application for viewing engine telemetry and controlling engine systems, built in Qt 5.

![A screenshot of the GUI in use](img/GUI.png)

## Index
* [Install](#install)
    * [Stable Release](#stable-release)
    * [Unstable Release](#unstable-release)

* [Use](#use)

* [Contributing](#contributing)
    * [Dependencies](#dependencies)
    * [Workflow](#workflow)
   


## Install 

### Stable Release
To install the latest stable version of APRL GUI, go to <https://github.com/UC-Davis-APRL/APRL_GUI/releases> and download the appropriate version for your operating system.

### Unstable Release
If you are interested in the unstable version, clone the Git repository and use the executables in there. At that point, you're probably already a contributor or helping contribute to the code.

## Use

For now, we are using a Serial connection to a microcontroller board (Arduino / Teensy) to control the valves on the test stand. As such, **please make sure the board is plugged in to your computer, or else the executable will crash!**

![Laptop running GUI plugged into an Arduino](./img/GUISetup.jpg)
*(What the setup should look like)*


## Contributing
If you are interested in contributing, message me on Discord ```(@Jason H/@nuclearfizzler)``` and and we'll go from there.

### Dependencies
The following libraries are required for the Python script to run.
* PyQt5
* qtwidgets
* qtpy
* PySerial (serial)
* pglive
* pyqtgraph
* pandas

The ```pyinstaller``` library is neccesary to compile the Python script into a Windows executable/Linux binary depending on which OS your Python is installed in.

Run the following command to install neccesary packages for development.
```shell
pip install pyqt5 qtwidgets qtpy pyserial pglive pandas pyinstaller 
``` 
I also recommend you install Qt 5 Designer to be able to work on the UI. 


### Workflow
Creating the elements of the GUI involves using Qt5 Designer to create the ```APRL_GUIvX_X.ui``` file. This allows you to create the GUI in a visual manner, without needing to worry too much about the code.

![Image of the .ui file open in Qt5 Designer](./img/QT_Designer.png)

To compile the ```.ui``` file into a runnable Python script, run
```shell
pyuic5 -x APRL_GUIvX_X.ui -o name_of_output_file.py
```

All functionality for the program is contained in the ```controls.py``` file; to include your compiled UI file in the program, put the file in an import statement.