## Installation

First command is optional if `pip` is already up-to-date.
```commandline
python -m pip install --upgrade pip
pip install libpybee
```
## MusicBee settings requirements and Disclaimers

* To use this package, you need to enable MusicBee to export the library in XML format for iTunes (`Edit` > `Edit Preferences` > `Library`), as shown in the image below.

![](https://raw.githubusercontent.com/Dyl-M/libpybee/main/_media/MB_Preferences_Screenshot.jpg)

* The file should end up in the same place as your library's `.mbl` file.
* The language in which this file is exported depends on the language set in MusicBee. For the time being, this package will only support library XML files written in English, so you'll need to set MusicBee's language to English (`Edit` > `Edit Preferences` > `General`). "English (US)" is recommended.
* Before using `libpybee`, it is also recommended to back up / to copy this XML file associated to your MusicBee Library elsewhere. I cannot guarantee at this time that no damage will occur to your file while using the package.
* Runs on Python 3.8 and above.

## Acknowledgements

All contributors from the legacy project [`libpytunes`](https://github.com/liamks/libpytunes) are listed [here](https://github.com/liamks/libpytunes/graphs/contributors).
