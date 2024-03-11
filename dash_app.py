from mitosheet.mito_dash.v1 import Spreadsheet, mito_callback, activate_mito
from dash import Dash, html, Input, Output
import pandas as pd

app = Dash(__name__)
activate_mito(app)

fund_info = pd.read_csv('./fund_info.csv')
performance = pd.read_csv('./performance.csv')
performance['Date'] = pd.to_datetime(performance['Date'])

app.layout = html.Div([
    html.H1('Fund Performance Dashboard'),
    Spreadsheet(
        fund_info, 
        performance,
        id={'type': 'spreadsheet', 'id': 'sheet'},
    ),
    html.Div(id='output')
])

@mito_callback(
    Output('output', 'children'),
    Input({'type': 'spreadsheet', 'id': 'sheet'}, 'spreadsheet_result'),
)
def update_output(spreadsheet_result):
    return html.Div([
        html.H3('Generated Python Code'),
        html.Code(spreadsheet_result.code(), style={'white-space': 'pre'}),
    ])

if __name__ == '__main__':
    app.run_server(debug=True)