# Importation----
library(openxlsx) # to read .xlsx files (read.csv(2) is available)
Force=runif(10,0,1)
sort(Force) # not registered
DN=read.xlsx("DataNeige.xlsx")
ozone=read.csv2("ozone.csv")
Kars=read.xlsx("Kars.xlsx")
QM=read.csv2("4 materiaux.csv")

# First part----
# Order
DN[order(DN$Massif, DN$Force),] # function 'sort' doesn't work well
order(DN$Force) # returns the lines indices

install.packages("doBy")
library(doBy)
orderBy(~Force,DN)
DN.sorted=orderBy(~Force,DN)
(DN.2=orderBy(~Force+Massif,DN))
(DN.2=orderBy(~Massif+Force,DN))

# Add data
(VarSup=rnorm(22,100,15))
DN$VarSup=VarSup # sol 1
cbind(VarSup,DN) # or sol 2
cbind(DN[1:5],VarSup,DN[6:9]) # in the middle
# incomplete data cbind
(VarSup=rnorm(20,100,15))
cbind(DN[1:5],VarSup,DN[6:9]) # error: rectangular data needed
(VarSup=c(rnorm(20,100,15),NA,NA))
cbind(DN[1:5],VarSup,DN[6:9]) # ok
# Matrix
(VarSup=c(rnorm(20,100,15),NA,NA))
(VarSup2=c(rnorm(21,100,15),NA))
Matrix.Gen=cbind(VarSup,VarSup2) # produces a matrix
is(Matrix.Gen)
# DataFrame
(VarSup=c(rnorm(20,100,15),NA,NA))
(VarSup2=c(rnorm(21,100,15),NA))
DFrame.Gen=as.data.frame(cbind(VarSup,VarSup2)) # produces a DataFrame
is(DFrame.Gen)
# Row binding
(VarSup1=c(rnorm(20,100,15),NA,NA))
(VarSup2=c(rnorm(21,100,15),NA))
(DFrame.Gen=as.data.frame(rbind(VarSup,VarSup2))) # produces a DataFrame
is(DFrame.Gen)
# Warning: quali and quanti conversion
IndSup=c("Ecrins",72,2,-3,50,"Est",12,70,2)
is(IndSup)
str(rbind(DN,IndSup)) # is NOT number dataframe
# Solution
DN=read.xlsx("DataNeige.xlsx")
(IndSup=as.data.frame(t(c("Ecrins",72,2,-3,50,"Est",12,70,2))))
(IndSup2=as.data.frame(c("Ecrins",72,2,-3,50,"Est",12,70,2)))
is(DN)
is(IndSup)
(names(IndSup))
(names(DN))
#library(data.table)
names(IndSup)=names(DN)
(names(IndSup))
rbind(DN,IndSup)
# Array fusion, very important:
# 1. key ;
# 2. key ;
# 3. key.
# Example
library(readr)
CF1 <- read_delim("chanson-française.csv", 
                  ";", escape_double = FALSE, locale = locale(encoding = "ISO-8859-1"), 
                  trim_ws = TRUE)
CF2 <- read_delim("chanson-française-2.csv", 
                  ";", escape_double = FALSE, locale = locale(encoding = "ISO-8859-1"), 
                  trim_ws = TRUE)
View(CF1)
View(CF2)
(CF.test=merge(CF1, CF2)) # Avoid not to bind with the KEY
(CF.test=merge(CF1, CF2, by=c("prenom","nom")))
(CF.test2=merge(CF1, CF2, by=c("prenom","nom"), all.x = T))
(CF.test3=merge(CF1, CF2, by=c("prenom","nom"), all.y = T))
(CF.test4=merge(CF1, CF2, by=c("prenom","nom"), all = T))
# fix(CF2) # to edit data
(CF.test5=merge(CF1, CF2, by=c("prenom","nom")))
(CF.test6=merge(CF1, CF2, by=c("nom")))

# Format: large/long conversion
View(QM)
QM_lg=stack(QM,)
QM_lg=na.omit(QM_lg)
names(QM_lg)=c("Resistance", "Metal")
summary(aov(data=QM_lg,Resistance~Metal))

# large/long conversion with `melt` (also: `reshape`) from package reshape2
Tailles=read.csv2("Taille.csv")
View(Tailles)
library(reshape2)
(TL=melt(data=Tailles))
(TL2=orderBy(~Souris, TL))
(TL3=reshape(Tailles,
        varying = list(2:4), idvar = "Souris",
        direction = "long"))

# Second part----
## Fonctions APPLY
### Fonction `aggregate`
# other solution: `summarySE` with library(Rmisc); summarySE(Kars)
summary(Kars)
library(DescTools)
Desc(Kars)
Desc(DN$Massif)
(C1=aggregate(data=DN, Force~Risque, mean))
(C2=aggregate(data=DN, Force~Risque, median))
(C3=aggregate(data=DN, Force~Risque, sd))
cbind(C1,C2,C3)
(DF1=merge(C1,C2, by="Risque"))
(DF2=merge(DF1,C2, by="Risque"))
(names(DF2)[2:4]=c("Force.mean", "Force.median", "Force.sd"))
DF2
View(DF2)

# Merge aggregates
(C11=aggregate(DN[-c(1,6,9)],list("Massif"=DN$Massif),mean))
# aggregate(DN[-c("Massif","Expo","Risque")],list("Massif"=DN$Massif),mean) # Doesn't work with the names
(C12=aggregate(DN[-c(1,6,9)],list("Massif"=DN$Massif),median))
(C13=aggregate(DN[-c(1,6,9)],list("Massif"=DN$Massif),sd))
length(DN)
length(C11)
length(C12)
length(C13)
(C14=aggregate(DN[-c(1,6,9)],list("Massif"=DN$Massif),length))
# function creation
(C15=aggregate(DN[-c(1,6,9)],list("Massif"=DN$Massif),function(x) sd(x)/sqrt(length(x))))
sd(DN$Force[DN$Massif=="Ecrins"])/sqrt(length(DN$Force[DN$Massif=="Ecrins"])) # Verification
cbind(C11,C12[-1],C13[2],C15[-1]) # very tedious...
(Stat.description=aggregate(DN[-c(1,6,9)],
                            list("Massif"=DN$Massif),
                            function(x) {n=length(x)
                                         Moy=mean(x) 
                                         sd=sd(x) 
                                         sem=sd(x)/sqrt(length(x))
                                         return(c("eff."=n,"Moy"=Moy,"sd"=sd,"sem"=sem))
                                         }
                            )
  )
(Stat.description[[6]][,2])
Stat.description[6]

(C11=aggregate(DN[-c(1,6,9)],list("Massif"=DN$Massif, "Expo"=DN$Expo),mean))

## Function `tapply`
tapply(DN$Force,list(DN$Massif), mean)
tapply(DN$Force,list(DN$Expo, DN$Massif), mean)

# Shapiro: normal data?
shapiro.test(DN$Force) # p-value=0.4216 so the normality is not excluded (it would take 0.05 to say the normality is exceptional)
shapiro.test(DN$Force[DN$Massif == "Ecrins"])
shapiro.test(DN$Force[DN$Massif == "Mont-Blanc"])
shapiro.test(DN$Force[DN$Massif == "Vanoise"])
aggregate(data=DN,Force~Massif,shapiro.test)
(ST=shapiro.test(DN$Force))
ST$p.value
