import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os


def import_excel_data():
    try:
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Import data (Excel file)", "Choose your matrix of inputs.")
        file_path = filedialog.askopenfilename()
        file_name = os.path.basename(file_path)
        labels = pd.read_excel(file_path, 0)
        label_df = pd.DataFrame(labels)
        xdata = pd.read_excel(file_path, 1)
        x_df = pd.DataFrame(xdata)
        ydata = pd.read_excel(file_path, 2)
        y_df = pd.DataFrame(ydata)
        return label_df, x_df, y_df, file_name
    except:
        print("An exception occurred while importing excel file.")


def data_to_excel(file_name, all_df, outliers_df):
    path = os.path.expanduser("~/Desktop") + '/foodscienceml' + '/' + file_name.replace('.xlsx', '').replace('.xls', '')
    if not os.path.exists(path):
        os.makedirs(path)
    writer = pd.ExcelWriter(path + '\Mahalanobis_report.xlsx')
    all_data = pd.DataFrame(all_df)
    all_data.to_excel(writer, 'Selected data')
    outliers_data = pd.DataFrame(outliers_df)
    outliers_data.to_excel(writer, 'Outliers data')
    writer.save()


def summary_data_to_excel(df, file_name):
    path = os.path.expanduser("~/Desktop") + '/foodscienceml' + '/' + file_name.replace('.xlsx', '').replace('.xls', '')
    if not os.path.exists(path):
        os.makedirs(path)

    writer = pd.ExcelWriter(path + '\PLS_Report.xlsx')
    all_data = pd.DataFrame(df)
    all_data.to_excel(writer, 'PLS SUMMARY')
    writer.save()


def summary_outlier_to_excel(df, file_name):
    path = os.path.expanduser("~/Desktop") + '/foodscienceml' + '/' + file_name.replace('.xlsx', '').replace('.xls', '')
    if not os.path.exists(path):
        os.makedirs(path)

    writer = pd.ExcelWriter(path + '\Outliers_Report.xlsx')
    all_data = pd.DataFrame(df)
    all_data.to_excel(writer, 'OUTLIERS SUMMARY')
    writer.save()


def data_describe_to_excel(df, df_outliers, file_name):
    path = os.path.expanduser("~/Desktop") + '/foodscienceml' + '/' + file_name.replace('.xlsx', '').replace('.xls', '')
    if not os.path.exists(path):
        os.makedirs(path)

    writer = pd.ExcelWriter(path + '\PCA_stats_report.xlsx')
    df_describe = pd.DataFrame(df.describe())
    df_describe.to_excel(writer, 'Descriptive statistics inliers')
    df_describe_out = pd.DataFrame(df_outliers.describe())
    df_describe_out.to_excel(writer, 'Descriptive statistics outliers')
    writer.save()

