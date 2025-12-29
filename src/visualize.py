import matplotlib.pyplot as plt
import seaborn as sns

def plot_expression_histograms(raw_df, log_df):
    plt.figure()
    plt.hist(raw_df.values.flatten(), bins=50)
    plt.title("Raw Expression Distribution")
    plt.xlabel("Expression")
    plt.ylabel("Frequency")
    plt.show()

    plt.figure()
    plt.hist(log_df.values.flatten(), bins=50)
    plt.title("Log-Normalized Expression Distribution")
    plt.xlabel("log(Expression + 1)")
    plt.ylabel("Frequency")
    plt.show()


def plot_top_variable_genes(df_log, top_n=30):
    gene_variance = df_log.var(axis=1)
    top_genes = gene_variance.sort_values(ascending=False).head(top_n).index

    plt.figure(figsize=(10, 6))
    sns.heatmap(df_log.loc[top_genes], cmap="viridis")
    plt.title(f"Top {top_n} Most Variable Genes")
    plt.show()