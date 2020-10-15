import dash_bootstrap_components as dbc
import dash_html_components as html


def make_graph_card(title, number, graph=None):
    children = []
    if graph:
        children.append(graph)
    card = dbc.Card(
        dbc.CardBody(
            [
                html.H4(title, id=f"card-title-{number}",
                        className="card-header",
                        style={"text-align":"center"}),
                html.Div(id=f"graph-{number}", children=children)
            ]
        ), outline=True
    )
    return card