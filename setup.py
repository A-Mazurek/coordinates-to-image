from setuptools import setup

setup(
    name='coordinates-to-image',
    version='1.0.0',
    url='https://github.com/A-Mazurek/coordinates-to-image.git',
    description='Coordinates to image.',
    download_url='https://github.com/pmazurek/aws-fuzzy-finder/tarball/v1.1.1',
    author='Andrzej Mazurek',
    keywords=['coordinates', 'image', 'png', 'jpg'],
    packages=['coordinates_to_image'],
    install_requires=[
        'folium==0.12.1.post1',
        'html2image==2.0.1',
        'click>=6.6'
    ],
    entry_points=dict(
        console_scripts=[
            'coordinates-image = coordinates_to_image.main:entrypoint',
        ]
    )
)
