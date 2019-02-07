% cynewulf - cynewulf
cynewulf_cynewulf = [1,	0.457142857,	2.275,	1.164285714,	2.871428571,	2.564285714],

% cynewulf - andreas
cynewulf_andreas = [1.067857143,	1.914285714,	2.432142857,	2.314285714],

% other
other = [0.210714286,	0.714285714,	0.45,	0.95,	0.378571429,	0.603571429,	1.132142857,	2.046428571,	1.260714286,	0.603571429,	0.155714286],


% one-way ANOVA
data = [cynewulf_cynewulf cynewulf_andreas other],
group = {'G1','G1','G1','G1','G1','G1','G2','G2','G2','G2','G3','G3','G3','G3','G3','G3','G3','G3','G3','G3','G3'},

[p,tbl,stats] = anova1(data, group)

m1 = mean(cynewulf_cynewulf);
m2 = mean(cynewulf_andreas);
m3 = mean(other);
s1 = std(cynewulf_cynewulf);
s2 = std(cynewulf_andreas);
s3 = std(other);

sd_pooled_12 = sqrt((s1^2 + s2^2)/2);
cohen_d_12 = (m1 - m2)/sd_pooled_12

sd_pooled_13 = sqrt((s1^2 + s3^2)/2);
cohen_d_13 = (m1 - m3)/sd_pooled_13

sd_pooled_23 = sqrt((s2^2 + s3^2)/2);
cohen_d_23 = (m2 - m3)/sd_pooled_23

c = multcompare(stats,'CType','tukey-kramer')

% Tukey calculator 1: http://statpages.info/anova1sm.html
% Tukey calculator 2: http://astatsa.com/OneWay_Anova_with_TukeyHSD/
