import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Setting the page configuration and titles
st.set_page_config(page_title="Data Clustering Visualization", page_icon=":bar_chart:")
st.title("Open Food Fact Data Clustering Dashboard")


# Function to load data
@st.cache_data
def load_data(filename):
    return pd.read_csv(filename)


# Data loading for clustering results
data_files = {
    "K-means": {
        "PCA": {
            "Pre-tune": "pca_kmeans_set1_pretune.csv",
            "Post-tune": "pca_kmeans_set1_posttune.csv"
        },
        "t-SNE": {
            "Pre-tune": "tsne_kmeans_set1_pretune.csv",
            "Post-tune": "tsne_kmeans_set1_posttune.csv"
        }
    },
    "Fuzzy C-Means": {
        "PCA": {
            "Pre-tune": "pca_fuzzycmeans_set1_pretune.csv",
            "Post-tune": "pca_fuzzycmeans_set1_posttune.csv"
        },
        "t-SNE": {
            "Pre-tune": "tsne_fuzzycmeans_set1_pretune.csv",
            "Post-tune": "tsne_fuzzycmeans_set1_posttune.csv"
        }
    },
    "DBSCAN": {
        "PCA": {
            "Pre-tune": "pca_dbscan_set1_pretune.csv",
            "Post-tune": "pca_dbscan_set1_posttune.csv"
        },
        "t-SNE": {
            "Pre-tune": "tsne_dbscan_set1_pretune.csv",
            "Post-tune": "tsne_dbscan_set1_posttune.csv"
        }
    }
}

# Centroid data files
centroid_files = {
    "K-means": {
        "Pre-tune": "kmeans_pre_centroids.csv",
        "Post-tune": "kmeans_post_centroids.csv"
    },
    "Fuzzy C-Means": {
        "Pre-tune": "fuzzyc_pre_centroids.csv",
        "Post-tune": "fuzzyc_post_centroids.csv"
    },
    "DBSCAN": {
        "Pre-tune": "dbscan_pre_centroids.csv",
        "Post-tune": "dbscan_post_centroids.csv"
    }
}

# Load performance data
performance_data = load_data("cluster_performance.csv")

# Sidebar interaction for method, type of plot, and tuning phase
clustering_method = st.sidebar.selectbox("Select Clustering Method", list(data_files.keys()))
plot_type = st.sidebar.selectbox("Select Plot Type", ["PCA", "t-SNE"])
tuning_phase = st.sidebar.selectbox("Select Tuning Phase", ["Pre-tune", "Post-tune"])

# Conditionally display the 'Include Outliers' checkbox for DBSCAN
include_outliers = True  # Default to include outliers
if clustering_method == "DBSCAN":
    include_outliers = st.sidebar.checkbox("Include Outliers", True)

# Loading selected dataset and centroid data
file_path = data_files[clustering_method][plot_type][tuning_phase]
data = load_data(f"Dashboard/{file_path}")
centroid_path = centroid_files[clustering_method][tuning_phase]
centroids = load_data(centroid_path)

# Optionally filter out outliers for DBSCAN
if clustering_method == "DBSCAN" and not include_outliers:
    data = data[data['Cluster'] != -1]


# Function to plot data
def plot_data(data, title):
    fig, ax = plt.subplots(figsize=(10, 8))
    scatter = ax.scatter(data['PCA1' if plot_type == "PCA" else 'TSNE1'],
                         data['PCA2' if plot_type == "PCA" else 'TSNE2'],
                         c=data['Cluster'], cmap='viridis', alpha=0.7, edgecolors='k')
    plt.colorbar(scatter, ax=ax)
    ax.set_title(f"{title} for {tuning_phase} ({clustering_method})")
    ax.set_xlabel(f"{plot_type} Component 1")
    ax.set_ylabel(f"{plot_type} Component 2")
    ax.grid(True)
    st.pyplot(fig)


# Display the plot
plot_data(data, f"{plot_type} Clusters Plot for Set 1")

# Display centroids
if st.sidebar.checkbox("Show Centroid Data", False):
    st.subheader(f"Centroid Data ({tuning_phase} - {clustering_method})")
    st.write(centroids)

# Optional: Show raw data on user request
if st.sidebar.checkbox("Show Raw Data", False):
    st.subheader(f"Raw Data ({plot_type} - {tuning_phase} - {clustering_method})")
    st.write(data)

# Performance comparison section
if tuning_phase == "Post-tune":
    st.header("Performance Comparison")
    if st.checkbox('Show Performance Metrics', False):
        selected_metrics = performance_data[performance_data['Algorithm'] == clustering_method]
        metrics = ['Silhouette Score', 'Davies-Bouldin Index', 'Calinski-Harabasz Index']
        pre_tuning_values = [
            selected_metrics[selected_metrics['Tuning'] == 'Pre-tuning'][metric].values[0] for metric in metrics
        ]
        post_tuning_values = [
            selected_metrics[selected_metrics['Tuning'] == 'Post-tuning'][metric].values[0] for metric in metrics
        ]

        df = pd.DataFrame({
            'Metric': metrics * 2,
            'Value': pre_tuning_values + post_tuning_values,
            'Condition': ['Pre-Tuning'] * 3 + ['Post-Tuning'] * 3
        })

        # Plotting
        fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))
        palette = {'Pre-Tuning': 'lightblue', 'Post-Tuning': 'pink'}
        for i, metric in enumerate(metrics):
            sns.barplot(x='Metric', y='Value', hue='Condition', data=df[df['Metric'] == metric], ax=axes[i],
                        palette=palette)
            axes[i].set_title(metric)
            axes[i].set_xlabel('')
            axes[i].set_ylabel('Value')
        st.pyplot(fig)
