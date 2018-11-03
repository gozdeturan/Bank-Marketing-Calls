from math import pi
from flask import Flask
from flask import render_template
from flask import request
from bokeh.plotting import figure, output_file, save, reset_output
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
import pandas as pd

app = Flask(__name__)

def save_to_html(new_df, filename, sample_count):
    reset_output()
    output_file(filename)

    sample = new_df.sample(sample_count)
    source = ColumnDataSource(sample)
    clients = source.data['client_name'].tolist()

    p = figure(x_range=clients)
    p.vbar(x='client_name', top='test_prediction', source=source, width=0.50, color='red')

    p.xaxis.major_label_orientation = pi / 2
    p.yaxis.major_label_orientation = "vertical"

    p.title.text = 'Bank Marketing Predictions'
    p.yaxis.axis_label = 'Prediction rate'

    hover = HoverTool()
    hover.tooltips = [
        ('Client Name', '@client_name'),
        ('Account Code', '@account_code'),
        ('Age', '@age'),
        ('Campaign', '@campaign'),
        ('Pdays', '@pdays'),
        ('Previous', '@previous'),
        ('Marital status', '@marital_married'),
        ('Target', '@test_prediction')
    ]
    p.add_tools(hover)
    save(p)

def save_to_html_for_account_code(new_df, filename, account_code):
    reset_output()
    output_file(filename)

    sample = new_df.loc[new_df['account_code'] == account_code]
    source = ColumnDataSource(sample)
    clients = source.data['client_name'].tolist()
    p = figure(x_range=clients)
    p.vbar(x='client_name', top='test_prediction', source=source, width=0.50, color='red')
    p.xaxis.major_label_orientation = "vertical"

    p.title.text = 'Bank Marketing Predictions'
    p.yaxis.axis_label = 'Prediction rate'

    hover = HoverTool()
    hover.tooltips = [
        ('Client Name', '@client_name'),
        ('Account Code', '@account_code'),
        ('Age', '@age'),
        ('Campaign', '@campaign'),
        ('Pdays', '@pdays'),
        ('Previous', '@previous'),
        ('Marital status', '@marital_married'),
        ('Target', '@test_prediction')
    ]
    p.add_tools(hover)
    save(p)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot', methods=['GET', 'POST'])
def plot():
    new_df = pd.read_pickle('./new_df')
    folder = 'templates/plots/'
    filename = 'bank_plot_' + request.args["sample_count"] + '.html'
    save_to_html(new_df, folder + filename, int(request.args['sample_count']))
    return render_template('plots/' + filename)

@app.route('/plot-for-account', methods=['GET', 'POST'])
def plot_for_account():
    new_df = pd.read_pickle('./new_df')
    folder = 'templates/plots/'
    filename = 'bank_plot_for_account_' + request.args["account_code"] + '.html'
    save_to_html_for_account_code(new_df, folder + filename, int(request.args['account_code']))
    return render_template('plots/' + filename)
