# load libraries
install.packages("effsize")
library(effsize)

# sense-pause ratio data

# order: Genesis A, Genesis B, Christ I, Christ II, Christ III, Elene,
# Juliana, Beowulf 1 - KD, Beowulf 2 - KD, Beowulf 1 - Klaeber, Beowulf 2 - Klaeber, corpus mean, Iliad, Odyssey 
ratio <- c(0.72632, 0.61406, 0.60432, 0.64748, 0.46383, 0.71205, 0.69547, 0.60078, 0.57558, 0.65969, 0.65179, 0.396324706, 0.24813, 0.32873)
error <- c(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.233896736, 0, 0)

# define the two groups
group1 <- c(ratio[1] - ratio[2], ratio[4] - ratio[3], ratio[3] - ratio[5], ratio[4] - ratio[5])
group2 <- c(ratio[6] - ratio[7], ratio[8] - ratio[9], ratio[10] - ratio[11])

# run the t-test, compute Cohen's d 
t.test(group1, group2, var.equal=TRUE)
cohen.d(group1,group2)

# Cynewulf nominal compound data 

# load data (the file is "cynewulf_data.csv")
my_data <- read.csv(file.choose())

# run the one-way ANOVA and display results
res.aov <- aov(weight ~ group, data = my_data)
summary(res.aov)

# run Tukey post-hoc tests
TukeyHSD(res.aov)

# compute the Q values for each pairwise comp
N <- length(my_data$weight) # total sample size
k <- length(unique(my_data$group)) # number of treatments
qtukey(p = 1-0.8898732, nmeans = k, df = N - k)
qtukey(p = 1-0.0410199, nmeans = k, df = N - k)
qtukey(p = 1-0.0293919, nmeans = k, df = N - k)

# compute Cohen's d for each pairwise comp
cynewulf_cynewulf <- c(1,	0.457142857,	2.275,	1.164285714,	2.871428571,	2.564285714)
cynewulf_andreas <- c(1.067857143,	1.914285714,	2.432142857,	2.314285714)
other <- c(0.210714286,	0.714285714,	0.45,	0.95,	0.378571429,	0.603571429,	1.132142857,	2.046428571,	1.260714286,	0.603571429,	0.155714286)
cohen.d(cynewulf_cynewulf, cynewulf_andreas)
cohen.d(cynewulf_cynewulf, other)
cohen.d(cynewulf_andreas, other)