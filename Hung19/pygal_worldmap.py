# -*- coding: utf-8 -*-
"""
it requires install additional packages:
    pip install pygal_maps_world
"""
import pygal.maps.world


def show_world_map():
    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = 'Some countries'
    worldmap_chart.add('F countries', ['fr', 'fi'])
    worldmap_chart.add('M countries', ['ma', 'mc', 'md', 'me', 'mg',
                                       'mk', 'ml', 'mm', 'mn', 'mo',
                                       'mr', 'mt', 'mu', 'mv', 'mw',
                                       'mx', 'my', 'mz'])
    worldmap_chart.add('U countries', ['ua', 'ug', 'us', 'uy', 'uz'])
    worldmap_chart.render()



if __name__ == '__main__':
    show_world_map()