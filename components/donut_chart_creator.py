import plotly.graph_objects as go

from backend.text_functions import get_sentiment_vader


def make_donut_chart(vs):
    fig = go.Figure(
        data=go.Pie(
            labels=list(vs.keys()),
            values=list(vs.values()),
            name="Sentiment",
            hole=.4,
            domain={"column": 0}
        )
    )
    return fig


def get_donut_plot(sentence):
    vs = get_sentiment_vader(sentence)
    vs = {k: v for k, v in vs.items() if k != "compound"}
    fig = make_donut_chart(vs)
    return fig



def make_bar_chart(vs):
    fig = go.Figure(
        data=go.Bar(
            x=list(vs.keys()),
            y=list(vs.values()),
            name="Sentiment Bar chart",
        )
    )
    return fig


def get_bar_chart(sentence):
    vs = get_sentiment_vader(sentence)
    vs = {k:v for k, v in vs.items() if k!="compound"}
    fig = make_bar_chart(vs)
    return fig
