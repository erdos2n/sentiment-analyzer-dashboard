import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from backend.text_functions import get_sentiment, get_sentiment_vader
from components.donut_chart_creator import get_donut_plot, get_bar_chart
from components.card_creator import make_graph_card

from dash.dependencies import Input, Output

external_stylesheets = [dbc.themes.MATERIA]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


donut_card = make_graph_card("Donut Graph", number=1)
bar_card = make_graph_card("Bar Graph", number=2)

card_container_style = {"width": "100%",
                        "margin-left": "30px",
                        "margin-right": "30px",
                        "margin-top": "10px"}

app.layout = html.Div([
    html.H1("Sentiment Analyzer", style={"text-align":"center"}),
    html.Div(id="top-container",
             className="jumbotron",
             children=[
                 dbc.Textarea(id='my-id',
                              value='Sentences go here',
                              className="textarea--box"),
                 html.Br(),
                 dbc.CardGroup(
                    [
                         donut_card,
                         bar_card
                     ],
            )],
             style=card_container_style)
    ])




@app.callback(
    Output(component_id='graph-1', component_property='children'),
    Output(component_id="graph-2", component_property="children"),
    [Input(component_id='my-id', component_property='value')]
)
def update_sentiment_div(input_value):
    # sentiment = get_sentiment_vader(input_value)
    donut_fig = get_donut_plot(input_value)
    bar_fig = get_bar_chart(input_value)
    donut_graph = dcc.Graph(id='sentiment-donut',
                            figure=donut_fig)
    bar_graph = dcc.Graph(id="sentiment-bar",
                      figure=bar_fig)
    return donut_graph, bar_graph


if __name__ == '__main__':
    app.run_server(host='localhost', debug=True)
