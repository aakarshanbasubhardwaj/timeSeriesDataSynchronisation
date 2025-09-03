# Steps to replicate the experiment

The experiment can be replicated by installing all the required dependencies and following the below mentioned steps.

## Dependencies

The following dependencies must be present and installed on the system where the experiment is to be reproduced

### Python
The system must have Python 3.3 or greater installed.

Check your current Python version using the below
```bash
python --version
```
Note - if the above command returns errors or a version lower than 3.3 then you need to install/upgrade python for your operating system from [here](https://www.python.org/downloads/)

### Code
The experiment code files can be found under the ```experiment``` branch.
Clone the branch ```experiment```.

```bash
git clone --branch experiment --single-branch git@github.com:aakarshanbasubhardwaj/timeSeriesDataSynchronisation.git
```

### Python dependencies
The below mentioned python libraries/packages must be installed globally with the specific version number
 - pandas v2.2.3
 - numpy v1.26.3
 - tqdm v4.67.1
 - dtaidistance v2.3.13

The cloned ```experiment``` branch contains a file ```requirements.txt```. It can be used in the following manner to download and install all the python dependencies mentioned above.
```bash
pip install -r requirements.txt
```

### Source Data
The WEAR dataset has been made use of in the experiment. The complete dataset can be downloaded [here](https://ubi29.informatik.uni-siegen.de/wear_dataset/raw/inertial/50hz/).

### IDE
Jupyter Notebook has been used to run the experiment, It can be downloaded and installed by following the instructions [here](https://docs.jupyter.org/en/stable/install/notebook-classic.html#alternative-for-experienced-python-users-installing-jupyter-with-pip)

## Experiment Setup

Once the above mentioned dependencies are resolved follow the below steps
- Navigate to the directory containing the experiment branch cloned previously.
- Create a folder in this directory called ```raw_data```
```bash
mkdir raw_data
```
- Copy the downloaded source data from WEAR in the raw_data folder.

- If followed correctly, the directory will look as follows
```
experiment/
├── raw_data/
│   ├── sbj_0.csv
│   ├── sbj_1.csv
│   ├── ...
│   ├── sbj_24.csv
├── experiment.ipynb
├── graph.ipynb
├── README.md
├── requirements.txt
```
- If your directory structure looks any different from the above, the experiment will fail to execute successfully. Please make sure you have the exact same structure as shown above. If not, then please follow the [setup steps](#experiment-setup) again to have the same structure as required.

## Execution
- Launch Jupyter Notebook from the terminal using below -
```bash
jupyter notebook
```
- Navigate to the folder location created in step 1 and open the experiment.ipynb file in jupyter notebook.
- Run the code using the run button.
- This will start executing the experiment and generate detailed reports in a .csv file named ```dtw_results.csv```.
-Open the graph.ipynb file in jupyter notebook and run the code to visualise the results.
- Upon experiment completion graphs will be generated and saved in the location ```graphs```.

# What happens in the experiment
The experiment when run does the following per subject -
- Magnitude Calculation per subject
- Variance Calculation per subject using the magnitudes from the last step
- Labelling of rest and motion segments in the data stream. This is done by making use of variance calculated in the last step.
- Generation of balanced windows by looking up the labels. The windows have a rest and motion segments in the ratio of 1:1.
- The generated windows are used to look up in the target stream to find the best match.
- To find the best match in the target stream -
  - Calculation of the search space in the target stream with 10 seconds worth of data on both sides of the balanced window.
  - DTW matching between the balanced window and the selected candidate window in the target stream.
- The step for finding the best match for each balanced window is executed in parallel with max available workers on the machine.

## Artifacts explanation
TODO add screenshots of the reports and graphs generated and explain the grpah as well
The experiment generates a .csv report containing details about 
- how much unsynchronisation was introduced in each limb of each subject
- the lead/lag among the limbs of each subject

The experiment generates the following artifacts per subject -
- Four .csv reports (one each for comparing right arm with left arm, left arm with right arm, right leg with left leg and left leg with right leg) for each subject containing the following details
  - balanced window start and end index in the data stream
  - best matching window start and end index in the target stream
  - plot name for the balanced window and best matching window

Aditionally the four box plots also generated to show the degree of correctness of synchronisation achieved