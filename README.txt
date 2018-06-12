Licensing:

<Heatmap Module program to provide real time representation of nodes and node clustering intensities based on color signature patterns.>
    Copyright (C) <2018>  <Hrishikesh Narayanankutty>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.


Introduction:

The following is a documentation and detailed guide usage for the java script based heatmap module. It includes functionalities which are listed down in the functionalities section. Step by step guide is also provided in the sample run through section for helping users run their first program.

What is Heatmap?

A heat map (or heatmap) is a graphical representation of data where the individual values contained in a matrix are represented as colors. "Heat map" is a newer term but shading matrices have existed for over a century.

Included in Bundle:

The heatmap bundle includes a python script that will auto generate random and real time data that is used as input to the heatmap module for signature represenatation.

Pipeline and How it works:

The software included works out of the box and no special programming modification is required. A real time representation from real sensors and other sensory data can be made to be represented with slight modification of the internal js code. There are two stages that are part of the data signature respresentation.

1. The first is the python script - generate.py to generate real time random data to be used by heatmap js module for data representation. This data list is stored in a file called list.csv .
2. The second part of the pipeline is the heatmap module itself, retrieving data from the list.csv file and representing it on a web interface.

Functionalities:

1. Since it is js and web based, the whole module is platform independent. It can run on any device and operating system.
2. The range and number of the entries in the dataset can be easily varied and thus different intensities of data can be easily plotted.
3. There are various colorschemes that can be used for the data plot itself.


Pre-requisites:

An installation of python 2.7 environment must be present on the device of usage. On Ubuntu and other linux systems, this environment is present by default. For windows machines, python 2.7 can be obtained from the following site:

https://www.python.org/

After installation of python environment, set path to python installation in the environment variable "Path" of the windows operating system. Guide on how to run a sample program is mentioned in the Sample Run section.

Sample Run:

The following are the variouss steps involved in running the program.

1. python generate.py ##generates and populates list.csv
2. open index.html with any js supported web browser. Data generated from step 1 is immediately represented and the corresponding heat map signature is generated.

upon refresh, real time updation of data is observed. 



