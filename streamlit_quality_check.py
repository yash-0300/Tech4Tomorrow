import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def show_quality_check():
    st.markdown("<h2 style='text-align: center;'> MedCare Synthetic Data Quality Check</h2>", unsafe_allow_html=True)
    
    # Upload real and synthetic EHR CSV files
    real_file = st.file_uploader("Upload Real EHR Records CSV", type=["csv"])
    synthetic_file = st.file_uploader("Upload Synthetic EHR Records CSV", type=["csv"])
    
    if real_file and synthetic_file:
        # Load the CSV files into DataFrames
        real_data = pd.read_csv(real_file)
        synthetic_data = pd.read_csv(synthetic_file)
        
        # Check if both datasets have the same structure
        if real_data.columns.tolist() != synthetic_data.columns.tolist():
            st.error("The columns in the real and synthetic datasets do not match!")
            return
        
        # Display the dataframes
        st.write("Real EHR Records:")
        st.dataframe(real_data.head())
        
        st.write("Synthetic EHR Records:")
        st.dataframe(synthetic_data.head())
        
        # Statistical comparison: Mean and Standard Deviation
        st.write("Statistical Comparison between Real and Synthetic Data")
        real_stats = real_data.describe().T[['mean', 'std']]
        synthetic_stats = synthetic_data.describe().T[['mean', 'std']]
        
        # Show side-by-side statistics
        stats_comparison = pd.concat([real_stats, synthetic_stats], axis=1, keys=["Real", "Synthetic"])
        st.write(stats_comparison)
        
        # Create two columns for the graphs
        col1, col2 = st.columns(2)
        
        # Graph 1: Distribution Comparison (Histogram) for numerical columns
        st.write("1. Distribution Comparison (Histogram)")
        numerical_cols = real_data.select_dtypes(include=np.number).columns
        
        with col1:
            for col in numerical_cols[:len(numerical_cols)//2]:
                fig, ax = plt.subplots()
                ax.hist(real_data[col], bins=20, alpha=0.5, label='Real Data')
                ax.hist(synthetic_data[col], bins=20, alpha=0.5, label='Synthetic Data')
                ax.set_title(f"Histogram: {col}")
                ax.set_xlabel(col)
                ax.set_ylabel("Frequency")
                ax.legend()
                st.pyplot(fig)
        
        with col2:
            for col in numerical_cols[len(numerical_cols)//2:]:
                fig, ax = plt.subplots()
                ax.hist(real_data[col], bins=20, alpha=0.5, label='Real Data')
                ax.hist(synthetic_data[col], bins=20, alpha=0.5, label='Synthetic Data')
                ax.set_title(f"Histogram: {col}")
                ax.set_xlabel(col)
                ax.set_ylabel("Frequency")
                ax.legend()
                st.pyplot(fig)
        
        # Graph 2: Boxplot for each numerical column to compare spread
        st.write("2. Boxplot Comparison")
        
        with col1:
            for col in numerical_cols[:len(numerical_cols)//2]:
                fig, ax = plt.subplots()
                sns.boxplot(data=[real_data[col], synthetic_data[col]], ax=ax)
                ax.set_xticklabels(['Real Data', 'Synthetic Data'])
                ax.set_title(f"Boxplot Comparison for {col}")
                st.pyplot(fig)
        
        with col2:
            for col in numerical_cols[len(numerical_cols)//2:]:
                fig, ax = plt.subplots()
                sns.boxplot(data=[real_data[col], synthetic_data[col]], ax=ax)
                ax.set_xticklabels(['Real Data', 'Synthetic Data'])
                ax.set_title(f"Boxplot Comparison for {col}")
                st.pyplot(fig)
        
        # Graph 3: Correlation Heatmap for real vs synthetic data
        st.write("3. Correlation Heatmap")
        fig, ax = plt.subplots()
        real_corr = real_data.corr()
        synthetic_corr = synthetic_data.corr()
        corr_diff = real_corr - synthetic_corr
        sns.heatmap(corr_diff, annot=True, cmap="coolwarm", center=0, ax=ax)
        ax.set_title("Correlation Difference (Real vs Synthetic)")
        st.pyplot(fig)
        
        # Graph 4: Pairplot to visualize relationships between columns
        st.write("4. Pairplot to visualize relationships")
        if len(numerical_cols) <= 5:
            combined_data = pd.concat([real_data[numerical_cols], synthetic_data[numerical_cols]], axis=0, keys=["Real", "Synthetic"])
            sns.pairplot(combined_data, hue="Level_0", markers=["o", "s"])
            st.pyplot()
        else:
            st.write("Pairplot skipped due to more than 5 numerical columns.")
        
        # Graph 5: T-test for comparing means between real and synthetic data
        st.write("5. T-Test to compare means")
        ttest_results = {}
        for col in numerical_cols:
            t_stat, p_value = stats.ttest_ind(real_data[col], synthetic_data[col], equal_var=False)
            ttest_results[col] = {"T-Statistic": t_stat, "P-Value": p_value}
        
        ttest_df = pd.DataFrame(ttest_results).T
        st.write("T-Test Results (T-statistic and P-value):")
        st.write(ttest_df)
        
        # Interpretation of T-test
        st.write("Interpretation of T-Test Results:")
        for col in numerical_cols:
            p_value = ttest_df.loc[col, "P-Value"]
            if p_value < 0.05:
                st.write(f"For {col}, there is a significant difference between real and synthetic data (p-value < 0.05).")
            else:
                st.write(f"For {col}, there is no significant difference between real and synthetic data (p-value >= 0.05).")
        
        # Provide download option for comparison results
        comparison_csv = stats_comparison.to_csv().encode('utf-8')
        st.download_button(
            label="Download Statistical Comparison as CSV",
            data=comparison_csv,
            file_name="statistical_comparison.csv",
            mime="text/csv"
        )
