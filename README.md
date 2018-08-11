# fontLib

(A font library for use in data visualizations. This public repository has been created
for very specific private uses and isnt really intended for public dissemination. The
information on this page are mostly notes-to-self.)

#### Initial Commit Notes
Right now, this repo contains a bunch of fonts from Windows and Google fonts. I might add
other fonts based on requirements. Only tested with ttf files.
The json file in the root directory (fontNames.json) relates the ttf files stored in the fonts
directory to the human readable names.
This json file can be regenerated using the createJson.py
script. The createJson.py script requires fontTools (https://github.com/fonttools/fonttools).

