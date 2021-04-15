# Importation----
library(openxlsx) # to read .xlsx files (read.csv(2) is available)
DN=read.xlsx("DataNeige.xlsx")
ozone=read.csv2("ozone.csv")
Kars=read.xlsx("Kars.xlsx")
QM=read.csv2("4 materiaux.csv")
Titanic=read.xlsx("Titanic.xlsx")
install.packages("RColorBrewer")
install.packages("ggsci")
install.packages("ggpmisc")
install.packages("car")
install.packages("leaps")
library(tidyverse)
library(corrplot)
library(openxlsx)
library(RColorBrewer)
library(ggsci)
library(ggpmisc)
library(ggpubr)
library(car)
library(leaps)
library(lmtest)

# First part, plotting (end)----
stripchart(data = DN , Couche~Massif, vertical = T)
stripchart(data = DN , Couche~Massif, vertical = T,method = "stack") 
stripchart(data = DN , Couche~Massif, vertical = T,method = "jitter") # random x coordinate
stripchart(data = DN , Couche~Massif, vertical = T,method = "stack", pch=20, 
           col = round(runif(3,0,25), digits = 0))

points(tapply(DN$Force, DN$Massif, mean), pch=3, cex=3)

# Z-score
stripchart(Maths, vertical = T, pch = 20)
(MathsNorm=(Maths-mean(Maths))/sd(Maths))
stripchart(MathsNorm, vertical = T, pch = 20)
stripchart(scale(Maths), vertical = T, pch = 20)
scale(Maths) == MathsNorm

stripchart(scale(DN$Tempneige), vertical = T, pch=20)
system.time(which(scale(DN$Tempneige)<=(-3)))
system.time(
  for (i in 1:length(DN$Tempneige)){
  Z = (DN$Tempneige[i]-mean(DN$Tempneige))/sd(DN$Tempneige)
  #print(paste(i, Z))
  if ((Z>=3) || (Z<=-3)) {print(paste("Indice :", i))}
})

(Maths = round(rnorm(10000,0,20), digits = 2))
Maths[1] = 1000
Maths
which((scale(Maths)<=(-3)) | (scale(Maths)>=3))
system.time(which(scale(Maths)<=(-3)) || (scale(Maths)>=3) )
system.time(
  for (i in 1:length(Maths)){
    Z = (Maths[i]-mean(Maths))/sd(Maths)
    #print(paste(i, Z))
    if ((Z>=3) | (Z<=-3)) {print(paste("Indice :", i))}
  })

# First part, diaries----
##### Introduction script
# Abstract: summary project/script
# Author(s)
# Version, date
# Last update
#####
# Prepare workspace----
## Clean workspace----
rm(list=ls()) # empties the memory
## Packages needed to build the dataframe----
library(openxlsx) # read xlsx files
library(lme4) # for MM
library(lmertest) # for p-values
library(car) # for `scatterplot`
library(Rmisc) # for `summarySE`
library(tidyverse) # for tidy syntax and ggplot2
## Custom functions----

# Build the DataFrame----
## Imports----
## Cleaning----
## Fusion----
## Recoding----
irec()

# Analysis----
## Description analysis----
## Modelisation----
## Graphs----