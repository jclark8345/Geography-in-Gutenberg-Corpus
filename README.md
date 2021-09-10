# Geography-in-Gutenberg-Corpus

## Contents

- [Project Introduction](#project-introduction)
- [File Directory](#file-directory)
- [Data](#data)
- [Results](#results)
- [Discussion/Conclusion](#discussionconclusion)
## Project Introduction

Reading literature is often equated to travel, allowing the reader to participate in the
geographic imagination of a culture. Literature has the potential to create geographies of desire, migration, colonialism, and fantasy. This project explores geographies of imagination through mentions of places in English literature. The Gutenberg Corpus provides documents written in and translated into English. This analysis studies mentions of place-names in the documents over time and investigates the relationships between places mentioned. The specific research points addressed in this report are which places are mentioned in the corpus, with what frequency they are mentioned, and how that frequency changes over time.

Time series plots were created from the data under different conditions such as truncation to certain time periods and selection of most-mentioned places. Examination of these plots can provide insight as to which countries were post well known at certain times.

## File Directory
### **Individual Files**

    - ideas.txt: file provides a logbook-like account of our work. It also contains 
     files that were generated or used during the intermediate process.

    - report_YellowOctopus.pdf: scientific report outlining our findings. 

     - gutenberg_analysis.py: All data manipulation and plotting code

### **Folders and their contents**
 
**Data**: 

    - geo_alldata.json: all data collected from the Gutenberg corpus 

    - timeseries.csv: time series data for country mentions by book (once per book)

    - timseriestotal.csv: time series data for country mentions by book 

    - timeseriescities.csv: time series data for city by book (once perbook)

**VACC_code**:   used to collect original data

    - gutenberg_VACC.py: gathers place names from a list of gutenberg books
 
    - geo_script.script: submits one job to the VACC

    - submit_jobs.script: submits all jobs to the VACC

    - combine_outputs: combines outputs from the VACC into one json file

## Data
The main source of data was the Gutenberg Corpus of online eBooks. This provided a nearly exhaustive collection of every literary work written or translated into English (about 60,000 works in all). The corpus is available online and is free for everyone. It was developed so that literature would be more accessible to people. Most of the books included have expired copyrights, so there is no need to pay to read them. Each book can be read in HTML format, and included with each book is publication information.
GeoNames is a database of geographical names with over 25 million entries, andis free under creative commons. (Geonames) We used a subset of the GeoNames database
consisting of all countries, and cities with a population of over 15,000.
The statistical program R contains a specific library devoted to the Gutenberg Corpus, “gutenbergr”. Contained in this library is data about every book in the corpus, including information about the authors. This was used to create the file “authordata.csv”, which contains information on the name, birth date, death date, and Gutenberg identification number for every author who appears in the corpus.

## Data Manipulation
The “geograpy” module in Python is a machine-learning named entity recognition application that searches through text for place names. This was run on every book from the Gutenberg corpus, generating a json file of data for each book. We merged the datasets for author birth year and place mentions or each book. We then created a table of counts for each place name per year. Counts were recorded for both the
number of books mentioning a place name, and number of individual mentions of the place name. We binned the data to show counts for each decade rather than each individual year, and performed time series analysis on the data.
A pipeline to the UVM Vermont Advanced Computing Core (VACC) was created, allowing these computations to be completed quickly and in parallel.


## Results

## Discussion/Conclusion

## References

    Cooper, D. and Gregory, I. N. (2011), Mapping the English Lake District: a literary GIS. 
     Transactions of the Institute of British Geographers, 36: 89-108.
     doi:10.1111/j.1475-5661.2010.00405.x

    Hughes, J. M., Foti, N. J., Krakauer, D. C., & Rockmore, D. N. (2012). Quantitative patterns 
     of stylistic influence in the evolution of literature. Proceedings of the National
     Academy of Sciences, 109(20), 7682–7686. DOI: 1 0.1073/pnas.1115407109

    Murrieta-flores, P., & Howell, N. (2017) Towards the Spatial Analysis of Vague and
     Imaginary Place and Space: Evolving the Spatial Humanities through Medieval Romance, Journal of Map & Geography
     Libraries, 13:1, 29-57, DOI: 1 0.1080/15420353.2017.1307302

    Murrieta-Flores, P., and Martins B. (2019) The geospatial humanities: past, present and future, International Journal of Geographical            Information Science, 33:12, 2424-2429, DOI: 10.1080/13658816.2019.1645336

    Murrieta-Flores, P., Donaldson, C., & Gregory, I.N. (2017). GIS and Literary History:
     Advancing Digital Humanities research through the Spatial Analysis of historical travel 
     writing and topographical literature. Digital  Humanities Quarterly, 11.

    Porter, C., Atkinson, P., and Gregory, I.N. (2018) Space and Time in 100 Million Words: Health and Disease in a Nineteenth-century                NewspaperInternational Journal of Humanities and Arts Computing 2018 12:2, 196-216

    Moretti, F. (1999). Atlas of the European Novel: 1800-1900. New York: Verso.
