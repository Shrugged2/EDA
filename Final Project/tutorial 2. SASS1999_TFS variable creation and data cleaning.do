

******* CHANGE DIRECTORY TO WHERE YOU STORE ALL OF YOUR DATASETS;


cd "C:\Playground\ManagedZone\Academic\ECO4381G empirical data analysis\SASS_1999-00_TFS_2000-01_v1_0_Stata_Datasets\raw datasets" /*replace this directory with your directory */

***** CREATE A LOG FILE TO SAVE ALL OF YOUR PROCEDURE IN A TEXT FILE;
log using SASS1999_data_clean_2022.txt,text replace

***** CLEAR ALL STORED DATASET FROM THE COMPUTER MEMORY;

clear
clear all


*** To Do List
Detailed steps:
1: load/read original data
2: clean data
3: summary statistics based on clean data in step  #2
4: clean data with only variables that you will use for your project
5: summary statistics based on clean data in step #4
6: correlation matrix based on clean data in step #4
7: scatter plot of Y and main X1
8: linear regression of Y on main X1
9: multiple regression of Y on main X1, X2,
10: multiple regression of Y on main X1, X2, X3
11: multiple regression of Y on main X1, X2, X3, X4
12: multiple regression of Y on main X1, X2, X3, X4, X5
You can have more lines of code if you have run additional regression.

use SASS_99_00_S4a_v1_0.dta /*replace this dataset name with your dataset name */
des
*codebook,problems
*codebook,compact


*** change all varible cases from CAPITALIZED to lower;


rename *, lower


 
******* KEEP ALL IMPORTANT IDS;
******* KEEP ALL IMPORTANT IDS;
******* KEEP ALL IMPORTANT IDS;

 


*** keep all of these id numbers or other information that might be useful for merging purposes;
des   cntlnum schcntl  
 
  



sum 






*** recode dummy variables;
*** recode dummy variables;
*** recode dummy variables;


** check your code before recoding;
tab t0070
tab t0070, nolabel


*** create a dummy variable based on what we know from the questionnaire and/or codebook you generated;

gen BAdeg=1 if t0070==1 
replace BAdeg=0 if t0070==2

*** double check your code run smoothly;
tab t0070 BAdeg,missing


*** recode categorical variables;
*** recode categorical variables;
*** recode categorical variables;

** check variable frequency or distribution before you recode;


tab t0051
tab t0051, nolabel

/*

  Main assignment |      Freq.     Percent        Cum.
----------------------------------------+-----------------------------------
              Regular full-time teacher |     38,370       91.17       91.17
              Regular part-time teacher |      1,466        3.48       94.65
Itinerant teacher (i.e., your assignmen |      1,256        2.98       97.64
Long-term substitute (i.e., your assign |        151        0.36       98.00
                                      5 |          4        0.01       98.01
Administrator (e.g., principal, assista |        216        0.51       98.52
  Library media specialist or librarian |         95        0.23       98.75
Other professional staff (e.g., counsel |        512        1.22       99.96
        Support staff (e.g., secretary) |         15        0.04      100.00
                                     32 |          1        0.00      100.00
----------------------------------------+-----------------------------------
                                  Total |     42,086      100.00

*/


*** subset your sample analysis;

****** focus on regular full-time teacher;

*keep if t0051==1 /* if you comment out this statement, you will only keep those teachers who are regular full-time teachers */


**** recode categorical variable;

* main teaching fields;

tab t0102
tab t0102, nolabel

*** you can create dummy variables for each of the categories but this takes up a lot of space;
tab t0102,gen(t0102_)


/*
tab t0102,gen(t0102_)

                   Assignmnt field-code |      Freq.     Percent        Cum.
----------------------------------------+-----------------------------------
                                     -8 |         12        0.03        0.03
                        Prekindergarten |         51        0.12        0.15
                           Kindergarten |      1,229        2.92        3.07
                             Elementary |      7,790       18.51       21.58
American Indian/Native American studies |         59        0.14       21.72
   Architecture or environmental design |         24        0.06       21.78
                                    Art |      1,157        2.75       24.53
     Basic skills or remedial education |        127        0.30       24.83
                    Bilingual education |        175        0.42       25.24
                       Computer science |        416        0.99       26.23
                                  Dance |         38        0.09       26.32
                          Drama/Theater |        157        0.37       26.70
           English as a Second Language |        406        0.96       27.66
Family and consumer science (home econo |        683        1.62       29.28
                                 Gifted |        195        0.46       29.75
                       Health education |        411        0.98       30.72
                            Mathematics |      3,796        9.02       39.74
                       Military science |        116        0.28       40.02
                                  Music |      1,657        3.94       43.96
                             Philosophy |         35        0.08       44.04
                     Physical education |      1,920        4.56       48.60
                               Religion |          6        0.01       48.61
Social studies or social science (inclu |      3,230        7.67       56.29
               English or Language Arts |      4,090        9.72       66.01
                             Journalism |         60        0.14       66.15
                                Reading |        709        1.68       67.83
                                 French |        289        0.69       68.52
                                 German |        112        0.27       68.79
                                  Latin |         62        0.15       68.94
                                Russian |         10        0.02       68.96
                                Spanish |        902        2.14       71.10
                Other foreign languages |        110        0.26       71.36
                Biology or life science |      1,254        2.98       74.34
                              Chemistry |        495        1.18       75.52
            Earth/space science/geology |        320        0.76       76.28
                        General science |        613        1.46       77.74
                       Physical science |        420        1.00       78.73
                                Physics |        172        0.41       79.14
                 Other natural sciences |         64        0.15       79.29
                             Accounting |         77        0.18       79.48
      Agricultural or natural resources |        356        0.85       80.32
                        Business/office |        939        2.23       82.55
                       Career education |        175        0.42       82.97
            Communications technologies |         81        0.19       83.16
                            Cosmetology |         50        0.12       83.28
                          Food services |         51        0.12       83.40
                     Health occupations |        102        0.24       83.65
Trades and industry (e.g., CADD, electr |        650        1.54       85.19
   Other vocational/technical education |        677        1.61       86.80
             Special education, general |      1,684        4.00       90.80
                                 Autism |         48        0.11       90.91
               Deaf and hard-of-hearing |         74        0.18       91.09
                Developmentally delayed |         40        0.10       91.18
      Early childhood special education |         31        0.07       91.26
Emotionally disturbed or behavior disor |        484        1.15       92.41
                  Learning disabilities |      1,153        2.74       95.15
                      Mentally retarded |        303        0.72       95.87
             Mildly/moderately disabled |        271        0.64       96.51
                Orthopedically impaired |         28        0.07       96.58
           Severely/profoundly disabled |        166        0.39       96.97
               Speech/language impaired |        284        0.67       97.65
            Traumatically brain-injured |          4        0.01       97.66
                      Visually impaired |         24        0.06       97.71
                Other special education |        154        0.37       98.08
                             All Others |        808        1.92      100.00
----------------------------------------+-----------------------------------
                                  Total |     42,086      100.00


								 */
								 
*** you need to go back to check what you want to investigate;


gen main_math=(t0102==17)

*** see if you can collapse all STEM teachers into this new categories;

gen main_STEM=(t0102==17|t0102==36)

* check your code;

tab  t0102 main_STEM,missing


log close






