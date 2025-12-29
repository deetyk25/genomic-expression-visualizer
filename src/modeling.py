from sklearn.decomposition import PCA

def run_pca(df_log, n_components=2):
    X = df_log.T
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X)
    return X_pca, pca
