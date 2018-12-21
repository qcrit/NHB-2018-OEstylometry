This documentation describes how to obtain an equivalent of the file ‘unique_compounds.txt’ in the main data from the Bosworth-Toller dictionary, which can be downloaded from the website http://bosworth.ff.cuni.cz/ in the form given by the file ‘oe_bosworthtoller.txt’, which is what we will be manipulating. 

Before we begin using Terminal regular expression commands, some brief comments on the layout of ‘oe_bosworthtoller.txt’ is useful:

- I have manually inserted the string ‘###’ between the prolegomena of the dictionary and the actual headwords; I recommend removing this portion so that some of it is not accidentally recognized as a dictionary entry. 

- Headwords are marked with HTML commands <B> and </B>. A cursory examination reveals that many headwords contain a hyphen. These are of two essential categories: 1) Nominal compounds — what we are after, 2) Verbs with prefixes — these need to be removed. Old English, being a Germanic language, specifies verbs completely with three principle parts (present, past, past participle); these are denoted p. and pp., and therefore searching out all verbs based on this p. and pp. and removing them is one strategy. A second strategy is based on the fact that all Old English nouns have a gender, masculine or feminine, which is immediately marked after the headword. For instance, the second entry ‘aac’, an oak tree, appears as follows: 

<B>aac,</B> e; <I>f. An oak:</I> -- Aac-tún <I>Acton Beauchamp, Worcestershire,</I> Cod. Dipl. 75 ; A. D. 727; Kmbl. i. 90, 19. v. ác-tún.

<B>aac,</B> is the headword; ‘e;’ is indicating what declension ‘aac’ belongs to; ‘<I>f’ indicates that it is a feminine noun and ‘An oak:</I>’ gives the definition. The rest is of no interest for us. 

I recommend targeting the gendered entries first to remove all verbs. That is, we are first going to run a command which will keep only lines (entries) containing ‘<I>f.’ or ‘<I>m.’ This will ensure we are only working on nouns. We will then run an identical command to keep only lines (of the output) which have a hyphen in the middle of the headword. This is the set of all compound words. 

Here is a sample of my own design of some regular expression commands which will render just the compound words:

1) Remove the prolegomena from the dictionary (everything above the ‘###’ string I have inserted in the base file), call this file ‘oe_bosworthtoller_edited.txt’

2) Keep only nouns:
grep -E "<I>m\.|<I>f\." oe_bosworthtoller_edited.txt > nouns.txt

3) Keep only headwords (i.e. only the part <B> ….. </B>)
a) first, use command+F to replace the string ‘,</B>’ with # , then
b) grep -Eo '^[^#]+#' nouns.txt > headwords.txt
c) use command+F to clean up, removing <B> and #, leaving only nominal headwords

4) Final cleanup
a) Remove OE prefixes which do not form proper nouns. These are a-, be-, ge-, in-, on-, tó-, un-. This can be done with successive uses of awk:
awk '!/tó-/' headwords.txt > headwords2.txt
etc
b) Using command+F to remove hyphens
c) Perhaps a use of cat to organize and check results
