#!/usr/bin/env python3

from app import app
from models import db, Bakery, BakedGood

if __name__ == '__main__':
    with app.app_context():
        

        bakeries = []

        for bakery in Bakery.query.all():
            result = bakery.to_dict()
            bakeries.append(result)

    import ipdb; ipdb.set_trace()
