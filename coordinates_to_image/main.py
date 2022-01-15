import folium
from html2image import Html2Image
import click


@click.command()
@click.option('--coordinates', 'coordinates', help="Enter the coordinates as a list")
@click.option('--output-image', 'output_image', help="Output image name")
@click.option('--zoom', 'zoom_start', help="Map zoom in range 1 to 22")
@click.option('--size', 'size', help="Enter size map in tuple e.g. (400, 400)")
def entrypoint(coordinates, output_image, zoom_start, size):
    m = folium.Map(location=coordinates, zoom_start=zoom_start, zoomControl=False)
    m.save('tmp/coordinates_map.html')

    hti = Html2Image(custom_flags=['--virtual-time-budget=10000', '--hide-scrollbars'])
    hti.screenshot(html_file='tmp/coordinates_map.html', save_as=output_image, size=size)


if __name__ == '__main__':
    entrypoint()
