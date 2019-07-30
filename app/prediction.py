from app.models import Prediction

Prediction.objects.from_csv(
    '.predict.csv',
    dict(item_name='ITEM NAME', x='ds', y='y')
)