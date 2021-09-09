# Geography-in-Gutenberg-Corpus

## Project Introduction



## File Directory
### **Individual Files**

    - **ideas.txt**:  file provides a logbook-like account of our work. It also contains 
     files that were generated or used during the intermediate process.

    - **report_YellowOctopus.pdf**: scientific report outlining our findings. 

     - **gutenberg_analysis.py**: All data manipulation and plotting code

### **Folders and their contents**
 
**Data**: 

    - geo_alldata.json   ###all data collected from the Gutenberg corpus 

    - timeseries.csv  ###time series data for country mentions by book (once per book)

    - timseriestotal.csv  ###time series data for country mentions by book 

    - timeseriescities.csv  ###time series data for city by book (once perbook)

**VACC_code**:   used to collect original data

    - gutenberg_VACC.py   ###gathers place names from a list of gutenberg books
 
    - geo_script.script   ###submits one job to the VACC

    - submit_jobs.script   ###submits all jobs to the VACC

    - combine_outputs    ###combines outputs from the VACC into one json file

