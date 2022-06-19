# FIN-407 - Financial Econometrics - 2022

The purpose of this project is to determine wether the tone used on regulatory N-CRS and N-CRS reportings impact the performance of mutual funds on the following year.

## Team Members
Zad ABI FADEL : zad.abifadel@epfl.ch <br/>
Etienne BRUNO : etiene.bruno@epfl.ch <br/>

##  Objective
The goal of this project is to analyse annual and semi-annual certified shareholder reports (N-CSR & N-CSRS) of mutual funds. The study involves downloading, processing, cleaning and formatting these reports, publicly available on EDGAR, to perform sentiment analysis. Heuristics models based on lexicons of sentiment-related words as well as machine learning oriented models are implemented. A comparison of performances of the funds is established with the market. The performances of the mutual funds are evaluated based on some metrics. Finally, we contrast the performance of the funds with the the tone expressed in the shareholder reports to assess if there’s a causality between the tone of the reports and the returns of the fund.

## Instructions
First, you need to clone our repository on your computer using the following command via ssh.
```
!git clone git@github.com:etiennebruno/financial_econonometry_project.git fin-407-mutual-funds
```

Then, you if you want to be able to run all models, you can either run notebooks 00 to 02 or download the entire 'data' folder from [HERE](https://www.swisstransfer.com/d/847d31ea-4ad9-4487-b545-9e6f8111888a). The notebooks will download the data and process them (results can be slightly different from results since the notebook create connection to EDGAR which is constantly being updated with new files)


## Overview
Here is a list of the relevant source files 

|Source file | Description|
|---|---|
|`00_download_index.ipynb`           |Get an index of all available reports (of all types)|
|`01_download_reports_filtered_for_crsp_and_unique_fund.ipynb`  | Download all N-CRS and N-CSRS reports available on EDGAR and CRSP|
|`02_data_cleaning.ipynb`            | Perform data cleaning on all reports and save them in a .txt format in a new cleaned folder|
|`03_stopwords.ipynb`   | Create a new file with a relatively exhaustive list of stopwords|
|`04_simple_stats_post_processing.ipynb`   | Used to get few numbers on the distribution of processed files between N-CSR and N-CSRS|
|`05_statistics_classical_models.ipynb`   | perform VADER, TextBlob and Flair pre-trained models on our corpus (take up to 4 hours for flair|
|`06_benchmark_data.ipynb`   | Get from CRSP the benchmark return and returns of all funds - comparisons |
|`07_find_benchmark.ipynb`   | Attempt to find benchmarks with rolling windows and full sentences|
|`08_fin_bert_split.ipynb`   | Perform FinBERT on our corpus - regular autonatic saving (RAM and time consuming)|
|`09_fund_performance_per_report.ipynb`   | Add the return of the fund for the year corresponding to the report to the dataframe containing all reports and saving |
|`10_capm.ipynb`   | -(TODO)- |
|`11_regression.ipynb`   | Perform some regression for analysis |

You will also find a lot of checkpoint files that corresponds to various models and predictions we experimentes througout this project.
