# `libpybee`

[![PyPI - Version](https://img.shields.io/pypi/v/libpybee?style=flat-square&label=Version&color=yellow)](https://pypi.org/project/libpybee/)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/Dyl-M/libpybee/python-publish.yml?label=Build&style=flat-square)](https://github.com/Dyl-M/libpybee/actions/workflows/python-publish.yml)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/Dyl-M/libpybee/test.yml?label=Tests&style=flat-square)](https://github.com/Dyl-M/libpybee/actions/workflows/test.yml)

[![GitHub last commit](https://img.shields.io/github/last-commit/Dyl-M/libpybee?label=Last%20commit&style=flat-square)](https://github.com/Dyl-M/libpybee/branches)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/w/Dyl-M/libpybee?label=Commit%20activity&style=flat-square)](https://github.com/Dyl-M/libpybee/branches)
[![DeepSource](https://app.deepsource.com/gh/Dyl-M/libpybee.svg/?label=active+issues&show_trend=true&token=QCUsSXrxx0Gn8hbQxa9G0KcW)](https://app.deepsource.com/gh/Dyl-M/libpybee/)

A MusicBee Library Parser, by Dylan "[Dyl-M](https://github.com/Dyl-M)" Monfret, based on [Liam "liamks" Kaufman's](http://liamkaufman.com/) [`libpytunes`](https://github.com/liamks/libpytunes).

## MusicBee settings requirements and Disclaimers

* To use this package, you need to enable MusicBee to export the library in XML format for iTunes (`Edit` > `Edit Preferences` > `Library`), as shown in the image below.

![](https://raw.githubusercontent.com/Dyl-M/libpybee/main/_media/MB_Preferences_Screenshot.jpg)

* The file should end up in the same place as your library's `.mbl` file.
* The language in which this file is exported depends on the language set in MusicBee. For the time being, this package will only support library XML files written in English, so you'll need to set MusicBee's language to English (`Edit` > `Edit Preferences` > `General`). "English (US)" is recommended.
* Before using `libpybee`, it is also recommended to back up / to copy this XML file associated to your MusicBee Library elsewhere. I cannot guarantee at this time that no damage will occur to your file while using the package.
* Runs on Python 3.8 and above.

## Installation

```shell
python -m pip install --upgrade pip # Optional
pip install libpybee
```

## Usage

```python
import libpybee

XML = "../MusicBee/iTunes Music Library.xml"  # Needs to be modified depending on the location of your MB library.
MY_LIBRARY = libpybee.Library(XML)

print(MY_LIBRARY)  # Displays a short summary of MB library status

for track in MY_LIBRARY.tracks.values():
    print(track, track.genre)  # Displays each track with their genres
```

More samples will be available in the [`_examples`](https://github.com/Dyl-M/libpybee/tree/dev/_examples) folder in the near future.

## Documentation

> Work In Progress.

## Acknowledgements

All contributors from the legacy project `libpytunes` are listed [here](https://github.com/liamks/libpytunes/graphs/contributors).