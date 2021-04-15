# Standardmodel
Provides a list of existing particles. Via console one can easily access all
information of a certain particle.
## Usage
### Add to windows path variables
I recommend to add this python file to windows path variables.
- Therefore safe the downloaded files in a directory of your choice and copy
the path of this directory, e.g. C:\Users\adami\Documents\Python\standardmodel
- Edit sm.bat and write the console command for the execution of the sm.py file, e.g.
```batch
python C:\Users\adami\Documents\Python\standardmodel\sm.py %1 %2 %3 %4 %5
```
and keep the %1 to %5
- Add the path of the batch file (e.g. C:\Users\adami\Documents\Python\standardmodel)
to the global windows path variables
- Now you can access this programm via cmd-console from any diractory, e.g.
```bash
sm --particle electron
```
### Usage without adding sm.py to path variables
Simply execute the sm.py file:
```bash
python sm.py --particle electron
```
## Methods
comming soom
## Versions
### Version 1.1
Uploaded: 14.04.2021
Added:
- README.md
- electron neutrino, charm-quark, strange-quark, muon, muon neutrino
### Version 1.0
Uploaded: 14.04.2021.
- Initial version of the programm
Added particles:
- proton, electron, up-quark
