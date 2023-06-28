import seaborn as sns
import matplotlib.pyplot as plt
from ydata_profiling import profile_report
from sklearn.datasets import fetch_california_housing, load_iris

def func(dataframe, target=None, widget=False):
    """Saves auto-eda report and pair plots of numerical fields

    Args:
        dataframe (pandas.Dataframe): The raw data being analysed
        target (pandas.Series, optional): Target fields. Defaults to None.
        widget(Boolean, optional): Create widget (or html file). Defaults to False.
    """
    # Auto-generated report
    report = profile_report.ProfileReport(dataframe)
    if widget == False:
        report.to_file('report.html')
    else:
        report.to_widgets()


    if target is None:
        # Scatter plots and histograms with no target
        sns.pairplot(dataframe, corner=True)
    else:
        # Scatter plots and histograms with target
        dataframe['target'] = target
        sns.pairplot(dataframe, hue='target', palette='viridis', corner=True)
    
    plt.savefig('pair_plots.png')


# Examples
if __name__ == '__main__':
    df_cali = fetch_california_housing(as_frame=True).frame
    df_iris, target_iris = load_iris(return_X_y=True, as_frame=True)
    func(df_cali)
    func(df_iris, target=target_iris)