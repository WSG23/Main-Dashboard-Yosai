from __future__ import annotations

from typing import Any, Dict, Sequence

import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_table import DataTable


def create_data_table(data: Sequence[Dict[str, Any]]) -> DataTable:
    """Create a simple DataTable from a sequence of dictionaries."""
    records = list(data)
    columns = [{"name": key, "id": key} for key in records[0].keys()] if records else []
    return DataTable(data=records, columns=columns)


def upload_card() -> dbc.Card:
    """Return the upload component wrapped in a bootstrap Card."""
    return dbc.Card(
        dbc.CardBody(
            [
                dcc.Upload(
                    id="upload-data",
                    children=html.Div(["Drag and drop or ", html.A("select files")]),
                )
            ]
        )
    )


def parse_contents(contents: str, filename: str) -> dbc.Row:
    """Parse uploaded file contents and return a Bootstrap Row."""
    return dbc.Row([html.Div(f"Received file: {filename}")])
