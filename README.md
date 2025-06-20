# Tropospheric Ozone Prediction

This repository contains code and data for predicting ground-level tropospheric ozone (O₃) concentrations using machine learning techniques. The aim is to model the relationship between meteorological parameters, precursor gases, and ozone formation using supervised learning methods.

## Project Overview

- Developed machine learning models (Random Forest Regressor, XGBoost) to predict ozone concentrations.
- Achieved an R² score of 0.80 after hyperparameter tuning and feature engineering.
- Used SHAP and Gini Importance to explain feature contributions and improve interpretability.
- Converted NetCDF meteorological datasets to CSV using `xarray` for preprocessing.

## Files in This Repository

- `Source Link.ipynb` - Jupyter notebook containing the full workflow: preprocessing, modeling, evaluation.
- `Netcdf to csv.py` - Python script to convert `.nc` (NetCDF) files into `.csv` using `xarray`.
- `Final Data Set.csv` - Final dataset after preprocessing, used for model training and testing.

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/tropospheric-ozone-prediction.git
    cd tropospheric-ozone-prediction
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Jupyter notebook:
    ```bash
    jupyter notebook "Source Link.ipynb"
    ```

4. (Optional) Convert NetCDF data to CSV:
    ```bash
    python "Netcdf to csv.py"
    ```

## Dependencies

- Python 3.x
- pandas
- numpy
- scikit-learn
- xgboost
- shap
- xarray
- matplotlib
- seaborn

## Model Summary

- Model used: XGBoost Regressor and Random Forest Regressor
- Evaluation metric: R² Score
- Best performance: 0.80 R²
- Key features: Temperature, Relative Humidity, Wind Speed, NO₂, CO

## References

- NetCDF conversion: https://gist.github.com/copernicusmarinegist/b57417225d0d4ea47c5d6200f9d8cac3
- SHAP documentation: https://shap.readthedocs.io/en/latest/

## Acknowledgements

This work was carried out as part of an academic research project under IIT Jodhpur.
