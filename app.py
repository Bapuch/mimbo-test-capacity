
options = [{"label": f"{i:,.0f} €", "value": i} for i in range(0, 10_000_001, 1000)]

app = Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server


app.layout = html.Div([
    html.Div([ 
        dcc.Store(id='capaciy-dataframe'),
        
        #Dashboard Name
        html.Div([
            html.H1(children='Investor Risk Profil - Capacity Risk '),
            html.Div([
                html.H5(children="Client Input Parameters"),            
                ],style={'display': 'inline-block','vertical-align': 'top',  'width': '28%', 'horizontal-align': 'left',
                         'color':'black', 'background-color': '#FFD700', "text-align": "center", 
                         "margin": "5px", "box-shadow": "3px 3px 10px #003136",
                        }), 
            html.Div([
                html.H5(children='Ooouh pretty charts !'),            
                ],style={'display': 'inline-block', 'vertical-align': 'top', 
                         'color':'white', 'width': '68%', "margin": "5px", "box-shadow": "3px 3px 10px #003136",
                         'horizontal-align': 'right','background-color':'#003136', "text-align": "center"}), 
            ],style={'font-family': 'calibri'}),        
         
         #All the Investor Characteristics
                      
#        #********************Demographics Features DropDown********
        html.Div([ 
            html.Div([ 
                
                html.Label('Revenus annuels:', 
                           style={'padding': "5 5 0 5", "font-weight": "bold"}),
                html.Label('1 au minimum, 1 courbe par revenus sur chaque graph:', 
                           style={'padding': "0 5 5 5", "color": "gray"}),
                dcc.Dropdown(
                        id='current_income_list',
                        options = options,
                        multi = True
                        ),
                
            
                html.Label("Patrimoine Annuel", style={'padding': "5 5 0 5", "font-weight": "bold"}),
                html.Label('1 au minimum, par défaut les graph tiennent \
                           compte de la 1ère valeur entrée. Utiliser le dropdown au-dessus des graphs\
                           pour changer la valeur utilisée:', style={'padding': "0 5 5 5",  "color": "gray"}),
                dcc.Dropdown(
                        id='current_estate_list',
                        options = options,
                        multi = True
                        ),

                html.Label("Taux d'épargne:", style={'padding': 5, "font-weight": "bold"}),
                dcc.Slider(
                    id='saving_rate',
                    min = 0, max = 100, step=10,
                    marks={0: '0', 25: '25%', 50: '$50%',75: '75%'},                
                    value=25,
                    tooltip={"placement": "bottom", "always_visible": True}),

                html.Label('Taux de Stabilité Financière:', style={'padding': 5, "font-weight": "bold"}),
                dcc.Slider(
                    id='stability_rate',
                    min = -5,
                    max = 5, step=1,
                    marks={-5: '-5%', -3: '-3%', 0: "0",  3: '3%', 5: '5%'},
                    value=3,
                    tooltip={"placement": "bottom", "always_visible": True}), 

                html.Label('Echéance du projet (en années):', style={'padding': 5, "font-weight": "bold"}),
                dcc.Slider(
                    id='project_duration',
                    min = 1,
                    max = 60,
                    step=1,
                    marks={i: f"{i}" for i in range(0, 61, 10)},
                    value=10,
                    tooltip={"placement": "bottom", "always_visible": True}), 
                html.Br(),
                html.P("CONSTANTES ECONOMIQUES", style={'padding': 10, "font-weight": "bold", 
                                                        "color": "darkgray", "text-align": "center"}),
                html.Label("Taux d'inflation:", style={'padding': 5, "font-weight": "bold"}),
                dcc.Slider(
                    id='inflation_rate',
                    min = 0,
                    max = 10,
                    step=1,
                    marks={i: str(i) + "%" for i in range(0, 11)},
                    value=3,
                    tooltip={"placement": "bottom", "always_visible": True}), 

                html.Label("Rentabilité historique à long terme d'un portefeuille avec un risque moyen:", 
                           style={'padding': 5, "font-weight": "bold"}),
                html.Label("ref Indexa: 8%:", style={'padding': 5, "color": "gray"}),
                dcc.Slider(
                    id='average_return',
                    min = 0,
                    max = 20,
                    step=1,
                    marks={i: str(i) + "%" for i in range(0, 21, 5)},
                    value=3,
                    tooltip={"placement": "bottom", "always_visible": True}),    
                html.Br(),
                html.Br(),
                html.Label("TOLERANCE AU RISQUE:", 
                           style={'padding': 5, "font-weight": "bold", "color": "darkblue",
                                  "text-align":"center"}),
                dcc.Slider(
                    id='tolerance',
                    min = 1,
                    max = 10,
                    step=1,
                    marks={i: str(i)  for i in range(1, 11)},
                    value=1,
                    tooltip={"placement": "bottom", "always_visible": True}),   
           
#                 html.Button(id='capacity_button',
#                                 n_clicks = 0,
#                                 children = 'Calculer la capacité',
#                                 style = {'fontSize': 14, 'marginLeft': '30px', 'color' : 'white',\
#                                          'horizontal-align': 'left','backgroundColor': 'LightBlue'}),                        
              ],style={'width': '80%', "horizontal-align": "center"}),           
            
            ],style={'width': '30%', 'font-family': 'calibri', 'vertical-align': 'top',
                     'display': 'inline-block', "horizontal-align": "center"
                     }),

    # ********************Risk Tolerance Charts********            
       html.Div([    
           html.Div([
               html.Label('Patrimoine Annuel:', style={'padding': 5,}),
               html.Div([
                   dcc.Dropdown(
                       id="current_estate",
                       multi=False,
                       clearable=True,
                       disabled=False,
                   ),
               ],style={'width': '30%','font-family': 'calibri','vertical-align': 'top','display': 'inline-block'}),
           ],style={'width': '100%','display': 'inline-block','font-family': 'calibri','vertical-align': 'top'}),
            
           html.Br(),
           html.Br(),
           html.Div(
               [
                   html.Div(className="row", 
                            children=[
                       html.H3("Capacité en fonction de l'âge", 
                                   style={'padding': 5, "text-align": "center",
                                          "color":"black"}),
                       html.Div([  
                             dcc.Graph(
                                id='capacity-plot',
                                hoverData={'points': [{'customdata': 18}]},
                                 style={"border-radius": "6px"}
                            )
                        ], style={'padding': '0 20', "border":"5px #003136 solid", "border-radius": "6px",
                                     "box-shadow": "3px 2px 5px","margin": "0 5px"}),
                   ],  style={'width': '50%', "horizontal-align": "left", 'display': 'inline-block'}),
                   
                   
                   html.Div(className="row", 
                            children=[
                       html.H3("Profil de risque en fonction de l'âge", 
                                   style={'padding': 5, "text-align": "center", "color":"black"}),
                       html.Div([  
                             dcc.Graph(
                                id='profil-plot',
                                hoverData={'points': [{'customdata': 18}]},
                            )
                        ], style={'padding': '0 20', "border":"5px darkblue solid", "border-radius": "6px",
                                     "box-shadow": "5px 2px 2px","margin": "0 5px", }),
                   ], style={'width': '50%', "horizontal-align":"right", 'display': 'inline-block'}),
                   
           ], style={'width': '100%', "vertical-align":"top"}),
           
           
           html.Br(),
           html.Div([
               html.Div(className="row", 
                        children=[
#                             html.H4("Evolution de la capacité au cours des années", 
#                                    style={'padding': 5, "text-align": "center", "color":"black"}),
                                  html.Div([dcc.Graph(id="capacity-to-expiry-plot"),
                                 ],
                        style={ "border":".5px black solid",
                         "box-shadow": "5px 2px 2px", "margin": "0 5px", })],
                        style={'width': '50%', "horizontal-align": "right", 'display': 'inline-block'}
                       ),
               
               html.Div(className="row", 
                        children=[
#                             html.H4("Evolution du profil de risque au cours des années", 
#                                    style={'padding': 5, "text-align": "center", "color":"black"}),
                            html.Div([dcc.Graph(id="profil-to-expiry-plot"),
                                 ],
                        style={"border":".5px black solid",
                         "box-shadow": "5px 2px 2px", "margin": "0 5px"}
                                          )], 
                        style={'width': '50%', "horizontal-align": "left", 'display': 'inline-block'}),
           ]),
           
       ],style={'width': '70%','display': 'inline-block','font-family': 'calibri','vertical-align': 'top',
                'horizontal-align': 'center'}),
    
    ],style={'width': '95%','display': 'inline-block','font-family': 'calibri','vertical-align': 'top'}),
    
])    

# Run the app
@app.callback(Output('capaciy-dataframe', 'data'),     
#               Input('capacity_button', 'n_clicks'),
              Input('current_income_list', 'value'),
              Input('current_estate_list', 'value'), Input('saving_rate', 'value'), 
              Input('stability_rate', 'value'), Input('project_duration', 'value'),
              Input('inflation_rate', 'value'), Input('average_return', 'value'),
             Input('tolerance', 'value'))
def get_capacity_df(current_income_list, current_estate_list, saving_rate, 
                         stability_rate, project_duration, inflation_rate, average_return, tolerance):
#     print("in capacity !!")
    saving_rate = saving_rate / 100
    stability_rate = stability_rate / 100
    project_duration = int(project_duration)
    inflation_rate = inflation_rate / 100
    average_return = average_return / 100
    # n_clicks != None and 
    if isinstance(current_estate_list, list) and isinstance(current_income_list, list):    

        df_capacity = get_df_age(current_estate_list, current_income_list, saving_rate, project_duration, 
                     inflation_rate, stability_rate, average_return, tolerance)
#         print("new capcities:", df_capacity.shape)
        return df_capacity.to_dict(orient='records')

@app.callback(
    Output("current_estate", "options"), [Input("current_estate_list", "value")],
)
def current_estate_options(current_estate_list):
    if type(current_estate_list) == list and len(current_estate_list) > 0:

        return [{"label": f"{i:,.0f}€", "value": i} for i in current_estate_list]

    return [{"label": "0 €", "value": 0}]


@app.callback(
    [Output('capacity-plot', 'figure')],
    Input('capaciy-dataframe', 'data'),
    Input('current_estate', 'value'),
    State('current_estate_list', 'value'),
    State('project_duration', 'value')
)
def update_risk_capacity(capacity_data,  current_estate, current_estate_list, project_duration):

    if current_estate is None and isinstance(current_estate_list, list):
        current_estate = current_estate_list[0]
        

    df_capacity = pd.DataFrame(capacity_data)

    dff = df_capacity[(df_capacity.year == 0) & 
             (df_capacity.current_estate == current_estate)].round(3)


    fig = px.line(dff, x="age", y="capacity", hover_name="revenue_label", color='current_income', markers=True)
    fig.update_traces(customdata=dff.age)
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')
    fig.update_xaxes(showline=True, linewidth=2, linecolor='black', gridcolor=None)
    fig.update_yaxes(showline=True, linewidth=2, linecolor='black', gridcolor='DarkBlue')
    fig.update_layout(plot_bgcolor="white", paper_bgcolor="white", font_color="#003136")

    return [fig]


@app.callback(
    [Output('profil-plot', 'figure')],
    Input('capaciy-dataframe', 'data'), Input('current_estate', 'value'),
    State('current_estate_list', 'value'), State('project_duration', 'value')
)
def update_risk_profil(capacity_data,  current_estate, current_estate_list, project_duration):

    if current_estate is None and isinstance(current_estate_list, list):
        current_estate = current_estate_list[0]
        

    df_capacity = pd.DataFrame(capacity_data)

    dff = df_capacity[(df_capacity.year == 0) & 
             (df_capacity.current_estate == current_estate)].round(3)


    fig = px.line(dff, x="age", y="profil", hover_name="revenue_label", color='current_income', markers=True)
    fig.update_traces(customdata=dff.age)
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')
    fig.update_xaxes(showline=True, linewidth=2, linecolor='black', gridcolor=None)
    fig.update_yaxes(showline=True, linewidth=2, linecolor='black', gridcolor='DarkBlue')
    fig.update_layout(plot_bgcolor="white", paper_bgcolor="white", font_color="DarkBlue")

    return [fig]
    

@app.callback(
    [Output('capacity-to-expiry-plot', 'figure')],
    Input('capaciy-dataframe', 'data'),
    Input('capacity-plot', 'hoverData'),
    Input('current_estate', 'value'),
    State('current_estate_list', 'value'),
    
)
def update_second_capacity_plot(capacity_data, hoverData, current_estate, current_estate_list):
    age = hoverData['points'][0]['customdata']
    title = f'<b>Age = {age}</b><br>Evolution de la capcité de risque au cours des années'
    if current_estate is None:
        current_estate = current_estate_list[0]

    
    df_capacity = pd.DataFrame(capacity_data)
    dff = df_capacity[(df_capacity.age == age) & (df_capacity.current_estate == current_estate)].round(3)
    
    fig = px.line(dff, x='year', y='capacity', 
                     hover_name= "revenue_label", 
                     color='current_income'
                     , markers=True
                    )
    

    fig.update_xaxes(showgrid=False)

    fig.update_xaxes(showline=True, linewidth=2, linecolor='black', gridcolor=None)#, autorange = "reversed")
    fig.update_yaxes(showline=True, linewidth=2, linecolor='black', gridcolor='DarkBlue')
    fig.update_layout(plot_bgcolor="white", paper_bgcolor="mintcream", title=title)

    return [fig]



@app.callback(
    [Output('profil-to-expiry-plot', 'figure')],
    Input('capaciy-dataframe', 'data'),
    Input('capacity-plot', 'hoverData'),
    Input('current_estate', 'value'),
    State('current_estate_list', 'value'),
    
)
def update_second_profil_plot(capacity_data, hoverData, current_estate, current_estate_list):
    age = hoverData['points'][0]['customdata']
    title = f'<b>Age = {age}</b><br>Evolution du profil de risque au cours des années'
    if current_estate is None:
        current_estate = current_estate_list[0]
    
    df_capacity = pd.DataFrame(capacity_data)
    dff = df_capacity[(df_capacity.age == age) & (df_capacity.current_estate == current_estate)].round(3)
    
    
    fig = px.line(dff, x='year', y='profil', 
                     hover_name= "revenue_label", 
                     color='current_income'
                     , markers=True
                    )
    

    fig.update_xaxes(showgrid=False)

    fig.update_xaxes(showline=True, linewidth=2, linecolor='black', gridcolor=None)#, autorange = "reversed")
    fig.update_yaxes(showline=True, linewidth=2, linecolor='black', gridcolor='DarkBlue')
    fig.update_layout(plot_bgcolor="white", paper_bgcolor="#dffbfb", title=title)

    return [fig]
