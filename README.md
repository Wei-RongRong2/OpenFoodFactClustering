# OpenFoodFactClustering

This project explores the application of clustering algorithms to categorize food products based on their nutritional content. The goal is to identify distinct nutritional profiles within a diverse dataset using K-Means, Fuzzy C-Means, and DBSCAN clustering methods.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Dashboard](#dashboard)
- [Methodology](#methodology)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [References](#references)

## Introduction

The project addresses the challenge of clustering food products based on nutritional attributes to improve dietary recommendations and health outcomes. By leveraging unsupervised learning methods, this research aims to identify meaningful clusters in food data.

## Installation

To set up the project environment, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Wei-RongRong2/OpenFoodFactClustering.git
    ```
2. Navigate to the project directory:
    ```bash
    cd OpenFoodFactClustering
    ```
3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the clustering analysis, follow these steps:

1. Ensure you have Jupyter Notebook installed. If not, you can install it using:
    ```bash
    pip install notebook
    ```

2. Navigate to the project directory where the Jupyter Notebook is located:
    ```bash
    cd OpenFoodFactClustering
    ```

3. Launch Jupyter Notebook:
    ```bash
    jupyter notebook
    ```

4. In the Jupyter Notebook interface, open the `OpenFoodFactClustering.ipynb` file.

5. Download the dataset from [Open Food Facts](https://world.openfoodfacts.org/data) and rename it as `en.openfoodfacts.org.products.tsv`. Place the file in the same directory as the Jupyter Notebook.

6. Run the cells in the notebook to execute the clustering analysis.

## Dashboard

A simple dashboard has been created using Streamlit to visualize the clustering results. You can view the dashboard online at the following URL:

**[OpenFoodFactClustering Dashboard](https://dashboardpy-ctqwx5fvp9ht6et6xvh4dm.streamlit.app/)**

The code for the dashboard and the CSV files containing the results are located in the `Dashboard` folder within this repository.

To run the dashboard locally, follow these steps:

1. Navigate to the `Dashboard` folder:
    ```bash
    cd Dashboard
    ```

2. If you have not installed the full set of dependencies for the project and only want to view the dashboard, install the required packages by running:
    ```bash
    pip install -r requirements.txt
    ```
   *(This `requirements.txt` file is located in the `Dashboard` folder.)*

3. Run the Streamlit application:
    ```bash
    streamlit run Dashboard.py
    ```

## Methodology

The project utilizes the Open Food Facts dataset and applies K-Means, Fuzzy C-Means, and DBSCAN algorithms to cluster food products. The dataset undergoes preprocessing, including missing value handling, data validation, and outlier removal.

### Data Collection

- **Source:** Open Food Facts dataset available on [Open Food Facts](https://world.openfoodfacts.org/data)
- **Size:** 356,027 rows and 163 columns
- **Attributes:** Product names, categories, nutritional information, ingredients, labels, and packaging details

### Preprocessing

- **Missing Values:** Removed columns with >20% missing data; imputed others.
- **Data Validation:** Identified and corrected/removal of invalid data and extreme outliers.
- **Data Types:** One-hot encoded categorical variables; scaled numerical features.
- **Duplicate Data:** Removed duplicate rows and redundant columns.

### Clustering Algorithms

1. **K-Means Clustering:** Used for partitioning the data into k clusters based on nutritional attributes.
2. **Fuzzy C-Means Clustering:** Allows for overlapping clusters with varying degrees of membership.
3. **DBSCAN Clustering:** Density-based algorithm to identify clusters of varying shapes and sizes, with noise detection.

## Results

The clustering analysis identified distinct clusters within the dataset, providing insights into dietary trends and nutritional patterns. Below are the key findings:

- **K-Means:** Four distinct clusters were identified, showing robustness in initial settings.
- **Fuzzy C-Means:** Improved cluster coherence and separation post-tuning.
- **DBSCAN:** Significant improvement in cluster definition after tuning.

For a more detailed explanation of these steps and results, refer to the full report: [Report - Clustering Food Products based on Nutritional Attributes.pdf](./Report%20-%20Clustering%20Food%20Products%20based%20on%20Nutritional%20Attributes.pdf).

## Contributing

Contributions are welcome! Please fork this repository, make your changes in a new branch, and submit a pull request for review.

1. Fork the repo
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Create a new Pull Request

## License

This project is part of an academic course and is intended for educational purposes only. It may contain references to copyrighted materials, and the use of such materials is strictly for academic use. Please consult your instructor or institution for guidance on sharing or distributing this work.

For more details, see the [LICENSE](./LICENSE.txt) file.

## Contact

Created by [Tay Wei Rong](https://github.com/Wei-RongRong2) - feel free to contact me!

## References

- **Open Food Facts Dataset:** [Kaggle Link](https://www.kaggle.com/datasets/openfoodfacts/world-food-facts)
- **Machine Learning Algorithms:** Scikit-Learn Documentation
- **Evaluation Metrics:** "Silhouette Score," "Davies-Bouldin Index," "Calinski-Harabasz Index"
