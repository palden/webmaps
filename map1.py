import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

def color_producer(height):
    if height < 1000:
        return "green"
    elif height < 2000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=(38.58, -99.89), zoom_start=8, tiles='Stamen Terrain')

fgv = folium.FeatureGroup(name="Volcanoes")

for index, item in data.iterrows():
#    fg.add_child(folium.CircleMarker(location=(item.LAT, item.LON), tooltip=str(item.ELEV) + " m. " + item.STATUS, color=color_producer(item.ELEV), fill=True, fill_color=color_producer(item.ELEV)))
    fgv.add_child(folium.Marker(location=(item.LAT, item.LON), popup=str(item.ELEV) + " " + item.STATUS, icon=folium.Icon(color=color_producer(item.ELEV))))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':"green" if x['properties']['POP2005'] < 10000000
else 'orange' if x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save('Map1.html')
