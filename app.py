import numpy as np
import pandas as pd
import plotly.graph_objs as go
import dash
from click import option
from dash import html, dcc, callback
from dash.dependencies import Input,Output
import plotly.express as px
from numpy.f2py.auxfuncs import options
from setuptools.command.install import install

external_stylesheet = [
    {
       "rel":"stylesheet",
       "href":"https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css",
       "integrity":"sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2",
       "crossorigin":"anonymous"
    }
]


patients = pd.read_csv("state_wise_daily data file IHHPET.csv")
# To get total of all
Total = patients.shape[0]  #.shape gives ue total count (rows ki number)
Active = patients[patients["Status"]=="Confirmed"].shape[0]
Recovered = patients[patients["Status"]=="Recovered"].shape[0]
Deceased = patients[patients["Status"]=="Deceased"].shape[0]

#  creat options for Dropdown for row3
options=[
    {"label":"All", "value":"All"},
    {"label":"Hospitalized", "value":"Hospitalized"},
    {"label": "Recovered", "value": "Recovered"},
    {"label": "Deceased", "value": "Deceased"}
    ]


#  creat options for Dropdown for row-2, card-1
options1=[
    {"label":"All", "value": "All"},
    {"label": "Mask", "value": "Mask"},
    {"label": "Sanitizer", "value": "Sanitizer"},
    {"label": "Oxygen", "value": "Oxygen"}
    ]

#  creat options for Dropdown for row-2, card-1
options2=[
    {"label":"All", "value":"All"},
    {"label":"Red Zone", "value":"Red Zone"},
    {"label": "Blue Zone", "value": "Blue Zone"},
    {"label": "Green Zone", "value": "Green Zone"},
    {"label": "Orange Zone", "value": "Orange Zone"}
    ]

app = dash.Dash(__name__,external_stylesheets=external_stylesheet)



app.layout = html.Div([
    html.H1("Corona Virus Pandemic",style={"color":"#fff","text-align":"center"}),
    #row 1
    html.Div([

        #row1 card1/ column 1
        html.Div([

            html.Div([
                html.Div([
                    html.H3("Total Cases", className = "text-light"),
                    html.H4(Total, className = "text-light")
                ],className="card-body")
            ],className="card bg-danger")

        ],className="col-md-3"),

        # row1 card 2 / column 2
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Active Cases", className="text-light"),
                    html.H4(Active, className="text-light")
                ], className="card-body")
            ], className="card bg-info")

        ], className="col-md-3"),

        # row1 card 3/ column 3
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Recovered Cases", className="text-light"),
                    html.H4(Recovered, className="text-light")
                ], className="card-body")
            ], className="card bg-warning")

        ], className="col-md-3"),

        # row1 card 4 / column 4
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Total Deaths", className="text-light"),
                    html.H4(Deceased, className="text-light")
                ], className="card-body")
            ], className="card bg-success")

        ], className="col-md-3"),
    ],className="row"),




    # row 2
    html.Div([

        # row-2, card 1 / column 1
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id="plot-graph",options=options1,value="All"),
                    dcc.Graph(id="graph")
                ],className="card-body")
            ],className="card bg-success")
        ],className="col-md-6"),


        # row-2, card 2 / column 2
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id="my_dropdown",options=options2,value="All"),
                    dcc.Graph(id="the_graph")
                ],className="card-body")
            ],className="card bg-info")
        ], className="col-md-6")

    ], className="row"),



    #row 3
    html.Div([

        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id="picker",options=options, value="All"),
                    dcc.Graph(id="bar")
                ],className="card-body")
            ],className="card bg-warning")
        ],className="col-md-12")

    ], className="row")

],className="container")



# callback for row-3
@app.callback(Output("bar","figure"), #Callback function ka role hai dcc.Dropdown
              [Input("picker","value")])      #aur dcc.Graph ke beech ka connection banana.

def update_graph(type):
    if type=="All":
        return {"data":[go.Bar(x=patients["State"], y=patients["Total"])],
                "layout":go.Layout(title="State Total Count",plot_bgcolor="orange")
                }
    if type=="Hospitalized":
        return {"data":[go.Bar(x=patients["State"], y=patients["Hospitalized"])],
                "layout":go.Layout(title="State Total Count",plot_bgcolor="orange")
                }
    if type=="Recovered":
        return {"data":[go.Bar(x=patients["State"], y=patients["Recovered"])],
                "layout":go.Layout(title="State Total Count",plot_bgcolor="orange")
                }
    if type=="Deceased":
        return {"data":[go.Bar(x=patients["State"], y=patients["Deceased"])],
                "layout":go.Layout(title="State Total Count",plot_bgcolor="orange")
                }



# callback for row-2, card-1
@callback(Output("graph","figure"),
          [Input("plot-graph","value")])

def generate_graph(type):
    if type== "All":
        return {"data":[go.Line(x=patients["Status"],y=patients["Total"])],
                "layout":go.Layout(title="Commodities Total Count",plot_bgcolor="pink")
                }
    if type== "Mask":
        return {"data":[go.Line(x=patients["Status"],y=patients["Mask"])],
                "layout":go.Layout(title="Commodities Total Count",plot_bgcolor="pink")
                }
    if type== "Sanitizer":
        return {"data":[go.Line(x=patients["Status"],y=patients["Sanitizer"])],
                "layout":go.Layout(title="Commodities Total Count",plot_bgcolor="pink")
                }
    if type== "Oxygen":
        return {"data":[go.Line(x=patients["Status"],y=patients["Oxygen"])],
                "layout":go.Layout(title="Commodities Total Count",plot_bgcolor="pink")
                }



# callback/ decorator function for row-2, card-2
@callback(Output("the_graph","figure"),
          [Input("my_dropdown","value")])


def generate_piechart(my_dropdown):
    # Check if the selected value is a valid column in the DataFrame
    if my_dropdown == "All":
        piechart = px.pie(data_frame=patients, names="Status", hole=0.3)
    else:
        piechart = px.pie(data_frame=patients,names= my_dropdown,hole=0.3)
    return piechart




if __name__=="__main__":         #If we’re running this file directly (like running a script by itself), then __name__ becomes "__main__".
    app.run_server(debug=True)   #This line starts the Dash app.

