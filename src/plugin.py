from os import listdir
from os.path import join as pjoin, isdir
from imp import find_module, load_module, reload

PLUGIN_PATH = './plugins'
MainModule = '__init__'

class Manager():
    def __init__(self):
        self.plugins = []

        plugin_folders = listdir(PLUGIN_PATH)

        for folder in plugin_folders:
            location = pjoin(PLUGIN_PATH, folder)
            
            if not isdir(location) or not MainModule + '.py' in listdir(location):
                continue

            info = find_module(MainModule, [location])
            self.plugins.append({'name':folder, 'info':info})

        for plugin in self.plugins:
            plugin['module'] = load_module(MainModule, *plugin['info'])
            plugin['object'] = plugin['module'].Plugin()

    def parse(self, data):
        for plugin in self.plugins:
            if data['destination'].lower() == plugin['name'].lower():
                try:
                    plugin['object'].parse(data)
                except BaseException as e:
                    print('Error: ' + plugin['name'] + ': ' + str(e))
                break

    def reload(self):
        try:
            for plugin in self.plugins:
                reload(plugin['module']) 
                plugin['object'] = plugin['module'].Plugin()
        except BaseException as e:
            print('Unable to reload plugins: ' + str(e))
