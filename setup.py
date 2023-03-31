from setuptools import setup

setup(name='chicagohouses',
      version='0.0.1',
      description='Get a filterable list of houses in Chicago.',
      author='Travis Birch',
      author_email='aml-toolbox-feedback@googlegroups.com',
      packages=['chicagohouses'],
      package_data={'chicagohouses': 'data/houses.parquet.gzip'}
      include_package_data=True,
      install_requires=['polars', 'geopandas', 
                        'pandas', 'pyarrow']
     )