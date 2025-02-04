# A python script to manage roms from the Myrent project
# Download, install, remove, update, list, search, etc.
# Fetch boxart, screenshots, etc.

# Importing modules
import os, sys, json, requests, shutil, zipfile, time, re, argparse
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Global variables
roms_dir = 'roms/'
console_name = {
    'nes': {
        'name': 'Nintendo Entertainment System',
        'urls': {
            'url1' : {
                'name': 'Nintendo Entertainment System (Headered)',
                'provider': 'Myrent',
                'no_intro': True,
                'url': 'https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Nintendo%20Entertainment%20System%20%28Headered%29/'
            },
            'url2' : {
                'name': 'Nintendo Entertainment System (Headerless)',
                'provider': 'Myrent',
                'no_intro': True,
                'url': 'https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Nintendo%20Entertainment%20System%20%28Headerless%29/'
            }
        }
    },
    'snes': {
        'name': 'Super Nintendo Entertainment System',
        'urls': {
            'url1' : {
                'name': 'Super Nintendo Entertainment System',
                'provider': 'Myrent',
                'no_intro': True,
                'url': 'https://myrient.erista.me/files/No-Intro/Super%20Nintendo%20Entertainment%20System/'
            }
        }
    },
    'n64': 'Nintendo 64',
    'gb': 'Game boy',
    'gbc': 'Game Color',
    'gba': 'Game Boy Advance',
    'ds': 'Nintendo DS',
    'dsi': 'Nintendo DSi',
    '3ds': 'Nintendo 3DS',
    'n3ds': 'Nintendo New 3DS',
    'wii': 'Nintendo Wii',
    'wiiu': 'Nintendo Wii U',
    'virtualboy': 'Nintendo Virtual Boy',
    'psx': 'PlayStation',
    'ps2': 'PlayStation 2',
    'ps3': 'PlayStation 3',
    'megadrive': 'Sega Mega Drive',
    'mastersystem': 'Sega Master System',
    'saturn': 'Sega Saturn',
    'dreamcast': 'Sega Dreamcast',
    'gamegear': 'Sega Game Gear',
    'pcengine': 'PC Engine',
    'neogeo': 'Neo Geo',
    'neogeocd': 'Neo Geo CD',
    'atari800' : 'Atari 800',
    'atari2600': 'Atari 2600',
    'atari5200': 'Atari 5200',
    'atari7800': 'Atari 7800',
    'lynx': 'Atari Lynx',
    'jaguar': 'Atari Jaguar',
    'colecovision': 'ColecoVision',

}