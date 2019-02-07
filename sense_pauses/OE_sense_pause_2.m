% order: Genesis A, Genesis B, Christ I, Christ II, Christ III, Elene,
% Juliana, Beowulf 1 - KD, Beowulf 2 - KD, Beowulf 1 - Klaeber, Beowulf 2 - Klaeber, corpus mean, Iliad, Odyssey 


ratio = [0.72632, 0.61406, 0.60432, 0.64748, 0.46383, 0.71205, 0.69547, 0.60078, 0.57558, 0.65969, 0.65179, 0.396324706, 0.24813, 0.32873];
error = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.233896736, 0, 0];

bar(ratio)
hold on
errorbar(1:14,ratio,error)
hold off

% statistical comparison between "single" and "multiple" author cases
% group 1 - "multiple author" differences

group1 = [ratio(1) - ratio(2), ratio(4) - ratio(3), ratio(3) - ratio(5), ratio(4) - ratio(5)];
mean(group1);

% group 2 - "single author" differences

group2 = [ratio(6) - ratio(7), ratio(8) - ratio(9), ratio(10) - ratio(11)];
mean(group2);

% t-test
[h, p, ci, stats] = ttest2(group1, group2)

m1 = mean(group1);
m2 = mean(group2);
s1 = std(group1);
s2 = std(group2);

sd_pooled = sqrt((s1^2 + s2^2)/2);

cohen_d = (m1 - m2)/sd_pooled



