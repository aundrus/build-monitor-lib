from django.db import models

# Extend Django model options with custom fields for table configuration
models.options.DEFAULT_NAMES += (
    'allColumns',      # List of all columns to display
    'orderColumns',    # Columns used for ordering
    'primaryColumns',  # Primary columns for identification
    'secondaryColumns',# Secondary columns for additional info
    'columnTitles',    # Custom titles for columns
    'filterFields',    # Fields used for filtering
)
