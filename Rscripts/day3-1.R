# Importation----
library(openxlsx) # to read .xlsx files (read.csv(2) is available)
DN=read.xlsx("DataNeige.xlsx")
ozone=read.csv2("ozone.csv")
Kars=read.xlsx("Kars.xlsx")
QM=read.csv2("4 materiaux.csv")
Titanic=read.xlsx("Titanic.xlsx")

# First part, for loops----
source("mesScripts/NormalityTest.R")
NormalityTest(ozone)
NormalityTest(Kars)
NormalityTest2(ozone)
NormalityTest2(Kars)

(set.seed(1))
(Maths = round(runif(20,0,20), digits = 0))
for (i in 1:length(Maths)){
  Avis = ifelse(Maths[i] < 10, "Pas terrible", "OK")
  cat ("Note en Maths : ", Maths[i], Avis, "\n")
}

lm(data = DN, Force~Massif)
(a=tapply(DN$Force,list(DN$Massif), mean))
anova(lm(data = DN, Force~Massif))
aov(data=DN,Force~Massif)
summary(aov(data=DN,Force~Massif))

for (i in c(1,3:9)){
  cat("Nom de la variable : ", names(DN)[i], "\n") # On affiche le nom de la variable
  
  ifelse(is.numeric(DN[,i]), # Selon la nature de la variable, 
         print(summary(lm(data = DN, Force~DN[,i]))), # si quantitatif, regression lineaire
         print(summary(aov(data = DN,Force~DN[,i])))) # si qualitatif, anova
} # Make a function from the loop?

# Other solution
sink("loopregression.txt") # prints in a file
for (i in 1:length(DN)){
  if (is.numeric(DN[,i] ==T & DN[,i] != DN$Force)){
    rl <- summary(lm(data = DN, Force~DN[,i]))
    print(paste("voici le resultat pour la variable", names(DN)[i]))
    print(rl)
  } else {
    ano <- anova(lm(data = DN, Force~DN[,i]))
    print(paste("voici le resultat pour la variable", names(DN)[i]))
    print(ano)
  }
}
sink() # prints in the Console

# Barplot + loop
for (i in 1:length(Titanic)){
  print(i)
  ifelse(is.numeric(Titanic[,i]), # Selon la nature de la variable, 
         hist(Titanic[,i], main = "Distribution pour ", colnames(DN[i])), # si quantitatif
         barplot(table(Titanic[,i]))) # si qualitatif
}
for (i in 1:length(DN)){
  print(i)
  ifelse(is.numeric(DN[,i]), # Selon la nature de la variable, 
         hist(DN[,i], main = paste("Distribution pour ", colnames(DN[i]))), # si quantitatif
         barplot(table(DN[,i]))) # si qualitatif
} # Make a function to apply to a data frame

# Second part, plots----
Fic <- read.xlsx(file.choose(), sheet = 1) # Function `file.choose` to pick a file with a pop-up box
n <- dim(Fic)[2]
i <- 1
for (i in 1:n)
  if (is.numeric(Fic[,i]) == TRUE){
    PValueNormalite <- shapiro.test(Fic[,i])$p.value
    cat("Résultat : ", names(Fic[i]), "\t", PValueNormalite, "\n")
  }
cat ("FIN ETUDE","\n")
NormalityTest2(Fic) # Same results

# Data visualization - basics
# Packages required
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
# Scaterplots
DN=as.factor(read.cvs2("DataNeige.csv"))
DN=read.cvs2("DataNeige.csv")
plot(DN$Couche,DN$Force, type = 'l')
plot(DN)
scatterplot(DN$Force,DN$Tempair)
ggplot(DN, aes(x=Tempair, y=Force, colour=Massif))+
  geom_point()+
  facet_wrap(~Massif)+
  geom_smooth(method = 'lm')

palette("R3")
hist(DN$Force,
     main="Force des avalanches",
     xlab="Classes de Forces", ylab = "Effectif",
     col = c("green"))
ggplot(DN, aes(Force))+geom_histogram(bins = 5)
qplot(DN$Force) # idem ggplot()+geom_histogram

window(10,10)
par(mfrow=c(1,3))
hist(DN$Force)
hist(DN$Tempneige)
hist(DN$Couche)
par(mfrow=c(1,1))

plot(density(DN$Force))
plot(density(DN$Tempneige))
plot(density(DN$Couche))

barplot(table(DN$Massif))
barplot(table(Kars$Type))

#par(mfrow=c(1,1))
boxplot(data=Kars,Tarif~Type,col=runif(5,0,10))
boxplot(data=DN,Couche~Massif,col=runif(3,0,1000))
points(tapply(DN$Couche,DN$Massif,mean),pch=16,cex=3,col="white")

