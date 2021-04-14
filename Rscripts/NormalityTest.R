PvnTest = function(x) {shapiro.test(x)$p.value}
NormalityTest=function(X){
  Normality=apply(X[sapply(X,is.numeric)],2,PvnTest)
  Verdict=ifelse(Normality>=0.05,"Variable can be considered Gaussian", "Non Gaussian")
  (TF=cbind(Normality,Verdict))
}
NormalityTest2=function(X){
  Normality=apply(X[sapply(X,is.numeric)],2,function(x) {shapiro.test(x)$p.value})
  Verdict=ifelse(Normality>=0.05,"Variable can be considered Gaussian", "Non Gaussian")
  (TF=cbind(Normality,Verdict))
}