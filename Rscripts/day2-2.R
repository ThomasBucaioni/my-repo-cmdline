# Importation----
library(openxlsx) # to read .xlsx files (read.csv(2) is available)
DN=read.xlsx("DataNeige.xlsx")
ozone=read.csv2("ozone.csv")
Kars=read.xlsx("Kars.xlsx")
QM=read.csv2("4 materiaux.csv")

# First part----
# Shapiro: normal data?
shapiro.test(DN$Force) # p-value=0.4216 so the normality is not excluded (it would take 0.05 to say the normality is exceptional)
shapiro.test(DN$Force[DN$Massif == "Ecrins"])
shapiro.test(DN$Force[DN$Massif == "Mont-Blanc"])
shapiro.test(DN$Force[DN$Massif == "Vanoise"])
aggregate(data=DN,Force~Massif,shapiro.test) # doesn't return the p-value
(ST=shapiro.test(DN$Force))
ST$p.value

aggregate(data=DN,Force~Massif,function(x) shapiro.test(x)$p.value) # returns the p-value
z=aov(data=DN, Force~Massif)
zz=summary(z) #View(z)
zz[[1]][5]

aggregate(data=DN,Force~Massif,hist)
aggregate(data=DN,Force~Massif,stripchart, vertical=T, pch=20)
aggregate(data=DN,Force~Massif,boxplot)
aggregate(data=DN,Force~Massif,function(x) {
  stripchart(x, vertical=T, pch=20) 
  points(mean(x),pch=3,cex=3)
  })

stripchart(DN$Force~DN$Massif, 
           vertical=T, pch=20, cex=.8, col=rainbow(3))
points(tapply(DN$Force,DN$Massif,mean),pch=3,cex=3,col="gray")

# Apply function
apply(DN[-c(1,6,9)],2,mean)

apply(Tailles[-1],1,mean)
Tailles$Moyenne = apply(Tailles[-1],1,mean)
View(Tailles)

pvn = function(x) {shapiro.test(x)$p.value}
Tailles$pvn = apply(Tailles[-1],1,pvn)
View(Tailles)

apply(DN[-c(1,6,9)],2,pvn)
(apply(Kars[-c(1,2,3)],2,min))
(apply(QM,2,mean,na.rm=T)) # mean(data, na.rm = T)
# NO: apply(na.omit(QM),2,mean) # avoid removing lines

QM_lg=stack(QM,)
QM_lg=na.omit(QM_lg)
names(QM_lg)=c("Resistance", "Metal")
# tapply: produces a vector (convenient for long format data)
(tapply(QM_lg$Resistance,QM_lg$Metal,mean))
aggregate(data=QM_lg,Resistance~Metal,mean) # returns a data frame. Tapply produces a vector

# lapply, sapply----
list.of.col = list(Kars$Tarif,DN$Force,QM_lg$Resistance)
View(list.of.col)
lapply(list.of.col, mean)# if NAs: add `na.rm=T`
sapply(list.of.col, mean)# if NAs: add `na.rm=T`

# Example of application of sapply
sapply(DN, is.numeric)
(apply(DN[sapply(DN, is.numeric)],2,pvn)) # Juantitative variables
(DN.Quan=DN[sapply(DN, is.numeric)==T]) # Quantitative variables
(DN.Qual=DN[sapply(DN, is.numeric)==F]) # Qualitative variables

# Example of application to convert in factor data set (Titanic data set)
Titanic=read.xlsx("Titanic.xlsx")
View(Titanic)
str(Titanic)
summary(Titanic)
(TitanicDF=as.data.frame(lapply(Titanic, as.factor))) # 
View(TitanicDF)
# (Titanic=sapply(Titanic, as.factor)) # produces a matrix
DN=read.xlsx("DataNeige.xlsx")
(DN[, which(sapply(DN, is.character))] =
  lapply(DN[, which(sapply(DN, is.character))], as.factor)
  )

# Second part----
# If
(set.seed(1905))
(Maths = round(runif(20,0,20), digits = 0))
(MeanMaths = mean(Maths))
if (MeanMaths>=10) "Good class" else "Needs to study"
ifelse (MeanMaths>=10, "Good class", "Needs to study")
print("End study")

ifelse(Maths>=10, "Good class", "Needs to study")

# Normality test
Normality=function(X){
  Normality=apply(X[sapply(X,is.numeric)],2,pvn)
  Verdict=ifelse(Normality>=0.05,"Variable can be considered Gaussian", "Non Gaussian")
  (TF=cbind(Normality,Verdict))
}
Normality(ozone)
Normality(Kars)

rm(Normality) # remove the name  
source("mesScripts/NormalityTest.R")
NormalityTest(ozone)
NormalityTest(Kars)
NormalityTest2(ozone)
NormalityTest2(Kars)
