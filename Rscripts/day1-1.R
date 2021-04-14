# Matinée rappels----
ll=list(c(2,6,9,10),c("camion","avion","tractopelle","side-car"),c(TRUE,FALSE,FALSE,TRUE))
(ll.DF=as.data.frame(ll))
ll.DF=rename.variable(ll.DF, old = names(ll.DF)[1:3], new = c("numérique", "caractère", "logique"))
ll.DF
# Fin du premier chapitre. Exemple de commentaires et affichage de chapitre----
# Commentaire 1
# Commentaire 2
ll
ll.DF
# Accès aux données et aux variables----
mean(DN$Force)
attach(DN)
mean(Force)
Force=runif(100,0,1)
print(Force)
mean(DN$Force)
rm(Force)
mean(Force)
with(DN,mean(Force))
Force=runif(100,0,1)
with(DN,mean(Force))
lapply(list(DN$Force, ozone$T9), mean)
lapply(list(DN[,2], ozone[,3]), mean)
mean(ozone[,3]) 
ozone[3] # DataFrame colonne -> présentée en colonne
ozone[,3] # vecteur -> présenté en ligne
mean(seq(1,10,1))
mean(1:10) # "1:10" est un vecteur
