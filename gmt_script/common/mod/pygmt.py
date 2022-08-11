#!/usr/bin/env python3

############################## pygmt
import pygmt
from .science import *

from pygmt.clib import Session
from pygmt.helpers import GMTTempFile
from io import StringIO
#import pandas as pd

def sean_pygmt_project(project_arguments: str) -> pd.DataFrame:
    print('\x1b[1;33;40mThis function is going deprecated!!!!!!!!!!!!!!!!!!!!!111\x1b[0m')
    with Session() as ses:
        with GMTTempFile() as fout:
            ses.call_module('project',f'{project_arguments} ->{fout.name}')
            session_output_string=fout.read().strip()
    DATA=StringIO(session_output_string)
    session_output_dataframe=pd.read_csv(DATA,header=None,delim_whitespace=True,names=['latitude','longitude','distance'])
    return session_output_dataframe

def couple_projection(coord:pd.DataFrame,
                      nonproject_columns_name:list,
                      project_line_a:list,
                      project_line_b:list,
    ) -> tuple[pd.DataFrame, pd.DataFrame] :
    coord_for_proj = coord[['longitude','latitude'] + nonproject_columns_name ]
    projected_df_a = pygmt.project(
            data=coord_for_proj,
            center=f'{project_line_a[0][0]}/{project_line_a[0][1]}',
            endpoint=f'{project_line_a[1][0]}/{project_line_a[1][1]}',
            length='w',
            width='-100/100',
            convention='pz',
            unit=True
    )
    projected_df_b = pygmt.project(
            data=coord_for_proj,
            center=f'{project_line_b[0][0]}/{project_line_b[0][1]}',
            endpoint=f'{project_line_b[1][0]}/{project_line_b[1][1]}',
            length='w',
            width='-100/100',
            convention='pz',
            unit=True
    )
    projected_df_a.columns = ['projected_x'] + nonproject_columns_name
    projected_df_b.columns = ['projected_x'] + nonproject_columns_name
    return(projected_df_a,projected_df_b)