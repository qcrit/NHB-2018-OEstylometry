function [prior,inpaper]=OECompClustNHB2
%Clustering analysis of OE poems based on compound words
load('OEdat_by_comp.mat','cf','cvec','cvecBEO');
%######INPUTS
%cf: vector of frequencies of non-hapax compounds. Note that
%'middangeard','heofonrice','heofoncyning', and 'wuldorcyning' have their
%frequency set to 0 here as per the paper.
%
%cvec: Number of compounds in each poem, counting Beowulf 1-2300 and
%2301-end as separate
%
%cvecBEO: Same as above but counting Beowulf as one poem


prior=zeros(243);
for trial=1:10000
pair=zeros(243);
pairbeo=zeros(242);
matter=cvec./sum(cvec); %Probability distribution that a random iteration of a compound word ends up in a given poem
matterbeo=cvecBEO./sum(cvecBEO);
for Compound=1:length(cf) %Loop over all OE compounds
    texts=[];
    for Instance=1:cf(Compound)
        samp=gdist(matter',1,1);
        texts=[texts,samp]; %Assign iteration of compound to a text based on 'matter' probability distribution
    end   
    texts=sort(unique(texts)); %We don't count frequencies, just appearances, so 'unique' removes multiple iterations of a compound
    for lbj=1:length(texts)
        for jfk=1:length(texts)
            if texts(lbj)~=texts(jfk)
                pair(texts(lbj),texts(jfk))=pair(texts(lbj),texts(jfk))+1; %Match all poems with overlapping compounds
            end
        end
    end
end

%Now, do the same thing but with Beowulf counting as one poem. Note that
%this is necessary to avoid compound overlaps. 

for Compound=1:length(cf)
    textsbeo=[];
    for Instance=1:cf(Compound)
        samp=gdist(matterbeo',1,1);
        textsbeo=[textsbeo,samp];
    end   
    textsbeo=sort(unique(textsbeo));
    for lbj=1:length(textsbeo)
        for jfk=1:length(textsbeo)
            if textsbeo(lbj)~=textsbeo(jfk)
                pairbeo(textsbeo(lbj),textsbeo(jfk))=pairbeo(textsbeo(lbj),textsbeo(jfk))+1;
            end
        end
    end
    
end

pair(1,3:end)=pairbeo(1,2:end); %Count Beowulf-poem pairings from version where Beowulf is one poem

prior=prior+pair;

end %of trials
prior=triu(prior)/10000;
inpaper=[prior(6,8),prior(6,41),prior(6,12),prior(4,6),prior(6,10),prior(6,14),prior(1,6),prior(8,41),prior(8,12),prior(4,8),prior(8,10),prior(8,14),prior(1,8),prior(12,41),prior(4,41),prior(10,41),prior(14,41),prior(1,41),prior(4,12),prior(10,12),prior(12,14),prior(1,12),prior(4,10),prior(4,14),prior(1,4),prior(10,14),prior(1,10),prior(1,14),prior(1,2)];
csvwrite('Compound_Prior.csv',prior);
csvwrite('Compound_Plotted.csv',inpaper);


function T = gdist(pvec,N,M)
Pnorm=[0 pvec]/sum(pvec);
Pcums=cumsum(Pnorm);
N=round(N);
M=round(M);
R=rand(1,N*M);
V=1:length(pvec);
[~,inds] = histc(R,Pcums); 
T = V(inds);
T=reshape(T,N,M);
end %of gdist
end %of OECompClust