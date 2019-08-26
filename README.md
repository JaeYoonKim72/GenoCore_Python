# GenoCore : a simple and fast algorithm for core subset selection from large genotype datasets

The GenoCore python version was developed by Seonmun Jeong and Jae-Yoon Kim. 

This program is based on the GenoCore R version available at https://github.com/lovemun/Genocore.

Source code was written in Python language and supported on windows and linux platform.



# Usage

The GenoCore consists of three submodules: VCFtoCSV, CoreSet, SelectVCF

Basic usage : python run_genocore.py [ VCFtoCSV | CoreSet | SelectVCF ]  [ Options ]

![GenoCore1](https://user-images.githubusercontent.com/49300659/63691262-b5379f80-c849-11e9-9288-3337b1695431.jpg)



## 1) VCFtoCSV
The "VCFtoCSV" submodule converts a VCF file into a CSV file for GenoCore.

Usage: python run_genocore.py VCFtoCSV -i [VCF file] -o [Output name] -p [Y or N (phased)] -g [Y or N (gziped)]

Example: python run_genocore.py VCFtoCSV -i ExampleData/Test_420sample.vcf.gz -o ExampleData/Test_420sample.csv -p Y -g Y

![2](https://user-images.githubusercontent.com/49300659/63691813-2b88d180-c84b-11e9-9284-3b3cc2bc8197.png)


# Requirement

python3, numpy

GenoCore python version also works in python 2.0, but we recommend running it in python 3.0 for handling a large data set.


# Contact
lovemun@kribb.re.kr

jaeyoonkim72@gmail.com


# Citation

Jeong S, Kim JY, Jeong SC, Kang ST, Moon JK, et al. (2017) GenoCore: A simple and fast algorithm for core subset selection from large genotype datasets. PLOS ONE 12(7): e0181420. https://doi.org/10.1371/journal.pone.0181420
