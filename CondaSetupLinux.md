
# How to setup conda on linux (+GPU setup)

## Steps
 1. Install either anaconda or miniconda(reccomended)
 2. Deactivate the default environment with ```conda deactivate```
 3. Create a new conda environment with ```conda create env -n your_name python=3.9```
 4. Open the conda environment with ```conda activate your_name```
 5. Install tensorflow **FIRST**:
    - ##### If you want to use a GPU, follow these extra steps:
        - Install your CUDA drivers. This is **extremely** implementation defined so I can't provide accurate steps, but [this link](https://www.nvidia.com/en-us/drivers/) is a good start.
        - Install tensorflow using the command ```pip install tensorflow[and-cuda]```
        - Verify your installation with:
            - ```python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"```
            - You should see a list of GPUs (or just one)
        - Install tensorRT with ```pip install tensorrt```
            - This may not work. You'll just get some warnings and a less optimized model =(
        - See [this link](https://docs.nvidia.com/deeplearning/tensorrt/install-guide/index.html#installing) for more information on tensorRT and it's supporting libraries
    - ##### If you aren't using a GPU, you can just install tensorflow with ```pip install tensorflow```
6. Install the rest of the libraries with pip:
    - ```pip install jupyter```
    - ```pip install scikit-image```
    - ```pip install scikit-learn```
    - ```pip install scipy```
    - ```pip install pandas```
    - ```pip install pandas-datareader```
    - ```pip install matplotlib```
    - ```pip install seaborn```
    - ```pip install pillow```
    - ```pip install tqdm```
    - ```pip install h5py```
    - ```pip install pyyaml```
    - ```pip install flask```
    - ```pip install boto3```
    - ```pip install ipykernel```
    - ```pip install graphviz```
    - ```pip install bayesian-optimization```
    - ```pip install gym```
    - ```pip install kaggle```
    - ```pip install pydot```
    - ```pip install tensorflow-datasets```
7. All done! Your conda environment should now be set up!
    - Keep in mind that all future packages should be installed with ```pip install``` and not ```conda install``` and there should be no issues!