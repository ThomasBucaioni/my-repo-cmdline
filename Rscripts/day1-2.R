# Quizz----
ll = list(1:5, 5:10, 12:25)
ll
ll[[3]][2]
DN[[2]]
DN[2]
DN[[2]] == DN[2]
rev(DN[[2]]) == DN[2]
# Exercises----
Kars[Kars$Type == "4 x 4",]
Kars[Kars$Type == "Citadine" & Kars$Tarif >= 20000,]
subset(Kars, subset = Kars$Type=='4 x 4') # Attention, plus lent que les crochets
subset(Kars, select = 5)
subset(Kars, subset = Kars$Type=='Citadine' & Kars$Tarif >= 20000, select = c(4,6))
subset(Kars, subset = Kars$Type=='Citadine' & Kars$Tarif >= 20000, select = c("Tarif","Cylindree"))
Kars.4x4=subset(Kars, subset = Kars$Type=='4 x 4') 
(DN.avalanche.massifsEcrinsVanoise.ForceSup50.subset = subset(DN, subset = (DN$Massif=='Ecrins' | DN$Massif=='Vanoise') & DN$Force >= 50) )
(DN.avalanche.massifsEcrinsVanoise.ForceSup50.crochet = DN[DN$Massif!='Mont-Blanc' & DN$Force >= 50,])
(DN.avalanche.massifsEcrinsVanoise.ForceSup50.subset = subset(DN, subset = DN$Force <= 50 | DN$Massif=='Mont-Blanc', drop = FALSE) )
# Après la pause, ajout de variable----
(Tarif2=Kars$Tarif-2000)
Kars2=read.xlsx("Kars.xlsx")
Kars2$Tarif=Kars$Tarif
Kars2$Tarif2=Kars$Tarif-2000
# Kars2=Kars2[-c(13)] # complexe
Kars2$Tarif2=NULL
Kars[seq(5,10,3),]
Kars[,3]
Kars[3]
Kars[3:5]
Kars["Tarif"]
Kars$Tarif
# Kars[-3:5] # faux
Kars[-c(3:10)]
Kars[-(3:10)]
Kars[,3:10]
Kars[3:10]
Kars[3:10,]
Kars[seq(1,3,1)]
Kars[seq(1,3,1),]
Kars[c("Tarif", "Cylindree", "Puissance")]
# Which
which(Kars$Type=="Citadine")
Kars[which(Kars$Type=="Citadine"),]
Kars[Kars$Type=="Citadine",] # idem, plus simple
# Moyenne sur l'extraction des lignes
Kars=read.xlsx("Kars.xlsx")
Kars.Citadine.Tarif=Kars[Kars$Type=="Citadine",][,"Tarif"]
# mean(Kars[Kars$Type=="Citadine",]["Tarif"]) # renvoie une erreur
mean(Kars.Citadine.Tarif)
# Moyenne sur l'extraction des lignes - OPTIMISÉ
library(Rmisc)
summarySE(Kars,measurevar = "Tarif", groupvars = "Type")
aggregate(data=Kars, Tarif~Type,mean)
tapply(Kars$Tarif,Kars$Type,mean) # Fonctions de la famille apply plus rapide

# Gestion des Données manquantes----
QM=read.csv2("4 materiaux.csv")
View(QM)
mean(QM$Acier, na.rm = T)
colMeans(QM, na.rm = T)
colMeans(na.omit(QM))
QM$Acier[QM$Acier=="NA"]
QM$Acier[QM$Acier=="NA"]=0
QM$Acier[QM$Acier=="NA"]<-0
irec()
## Recodage de QM$Acier
QM$Acier <- as.character(QM$Acier) # Pas necessaire
QM$Acier[is.na(QM$Acier)] <- "0"
QM$Acier <- as.numeric(QM$Acier) # Pas necessaire
QM$Acier

# Irec sur Kars
irec()
## Recodage de Kars$Marque en Kars$Marque_rec
Kars$Marque_rec <- Kars$Marque
Kars$Marque_rec[Kars$Marque == "Audi"] <- "Allemagne"
Kars$Marque_rec[Kars$Marque == "Bmw"] <- "Allemagne"
Kars$Marque_rec[Kars$Marque == "Citroen"] <- "France"
Kars$Marque_rec[Kars$Marque == "Dacia"] <- "France"
Kars$Marque_rec[Kars$Marque == "Ford"] <- "USA"
Kars$Marque_rec[Kars$Marque == "Honda"] <- "Japon"
Kars$Marque_rec[Kars$Marque == "Jaguar"] <- "RU"
Kars$Marque_rec[Kars$Marque == "Lexus"] <- "Japon"
Kars$Marque_rec[Kars$Marque == "Mercedes"] <- "Allemagne"
Kars$Marque_rec[Kars$Marque == "Opel"] <- "Allemagne"
Kars$Marque_rec[Kars$Marque == "Peugeot"] <- "France"
Kars$Marque_rec[Kars$Marque == "Porsche"] <- "France"
Kars$Marque_rec[Kars$Marque == "Renault"] <- "France"
Kars$Marque_rec[Kars$Marque == "Smart"] <- "Suisse"
Kars$Marque_rec[Kars$Marque == "Toyota"] <- "Japon"
Kars$Marque_rec[Kars$Marque == "VW"] <- "Allemagne"

colSums(is.na(QM))
# Biblio naniar
install.packages("naniar")
library(naniar)
pct_complete_var(QM)
?pct_complete_var
pct_miss_var(QM)
