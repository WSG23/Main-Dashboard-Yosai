from __future__ import annotations

from typing import Sequence, Dict, Any

from dash import html
declare = html.Div # for type hints
# We'll implement simple DataTable using dash_table
from dash_table import DataTable


def data_preview(data: Sequence[Dict[str, Any]]) -> html.Div:
    """Return a basic DataTable preview wrapped in a Div."""
    records = list(data)
    columns = [{"name": key, "id": key} for key in records[0].keys()] if records else []
    table = DataTable(data=records, columns=columns)
    return html.Div(table)
