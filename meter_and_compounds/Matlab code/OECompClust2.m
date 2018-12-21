function [pair]=OECompClust2
%Clustering analysis of OE poems based on compound words
load('OEdat_by_comp.mat');
cf=cf(cf>1);
cf=cf(cf<10);
wordz=zeros(578,239);
matter=cvec./sum(cvec);
for Compound=1:length(cf)
    texts=[];
    for Instance=1:cf(Compound)
        tast=gendist(matter',1,1);
        wordz(Compound,tast)=wordz(Compound,tast)+1;
    end
end
for wod=1:578
    texts=find(wordz(wod,:));
    if length(texts)>1
    combos=unique(nchoosek(sort(texts),2),'rows');
    for jj=1:length(combos(:,1))
        if combos(jj,1)~=combos(jj,2)
            pair(combos(jj,1),combos(jj,2))=pair(combos(jj,1),combos(jj,2))+1;
        end
    end
    end
end
end