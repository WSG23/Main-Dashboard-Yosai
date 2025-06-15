"""Deep analytics page layout."""

from dash import html
from ..components.analytics import upload_card, data_preview, analytics_charts

layout = html.Div(
    [
        upload_card(),
        data_preview([]),
        analytics_charts(),
    ]
)
