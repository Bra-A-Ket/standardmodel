# Standardmodel
Provides a list of existing particles. Via console one can easily access all
information of a certain particle.
## Usage
### Add to windows path variables
I recommend to add this python file to windows path variables.
- Therefore save the downloaded files in a directory of your choice and copy
the path of this directory, e.g. C:\Users\adami\Documents\Python\standardmodel
- Edit sm.bat and write the console command for the execution of the sm.py file, e.g.
```batch
python C:\Users\adami\Documents\Python\standardmodel\sm.py %1 %2 %3 %4 %5
```
and keep the %1 to %5
- Add the path of the batch files' directory (e.g. C:\Users\adami\Documents\Python\standardmodel)
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
## Commands/methods
- With -i or --info print out some informations about this programm
```bash
sm -i
sm --info
```
- Use -v or --version to show the version
```bash
sm -v
sm --version
```
- Use -p <name> or --particle <name> to see all information about the particle <name>
```bash
sm -p electron
sm --particle electron
```
You can also show several particles at the same time
```bash
sm -p proton electron
```
## List of particles
| particle name | syntax |
| ------------------ | ------------------ |
| up-quark | up |
| down-quark | down |
| charm-quark | charm |
| strange-quark | strange |
| top-quark | top |
| bottom-quark | bottom |
| electron | electron |
| muon | muon |
| tau | tau |
| electron-neutrino | nue |
| muon-neutrino | num |
| tau-neutrino | nut |
## Versions
### Version 1.1
Uploaded: 15.04.2021
Added:
- README.md
- electron neutrino, charm-quark, strange-quark, muon, muon neutrino, tau, tau neutrino
### Version 1.0
Uploaded: 14.04.2021.
- Initial version of the programm
Added particles:
- proton, electron, up-quark
