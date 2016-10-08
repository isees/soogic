# coding: utf-8

from flask import Flask, render_template
from soogic import db
from soogic.ext.models import IDModel

image_host = 'http://www.shimano-china.com'


class Product(IDModel):
    fitting_image_standard = db.Column(db.String, nullable=False)
    fitting_class = db.Column(db.String, nullable=False)
    fitting_series = db.Column(db.String, nullable=False)
    fitting_features = db.Column(db.String, nullable=False)
    fitting_attributes = db.Column(db.String, nullable=False)
    fitting_model = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)

    @property
    def image_url(self):
        return image_host+self.fitting_image_standard

