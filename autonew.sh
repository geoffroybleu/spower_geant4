cd
cd Desktop/Geant4-dev-master/examples/extended/medical/dna/spower
rm -r build
mkdir build
cd build

cmake .. -DCMAKE_INSTALL_PREFIX=$HOME/Geant4-dev-master-install -DGEANT4_USE_OPENGL_X11=ON -DGEANT4_USE_QT=ON -DGEANT4_BUILD_MULTITHREADED=ON
make -j4 
make install
source $HOME/Geant4-dev-master-install/bin/geant4.sh

head -n 34 $HOME/Desktop/Geant4-dev-master/examples/extended/medical/dna/spower/spower.in > spower_run.in

sed -i '' 's/\/gun\/particle .*/\/gun\/particle e-/' spower_run.in

for arg in "$@"
do
    echo "/gun/energy $arg eV" >> spower_run.in
    echo "/run/beamOn 100" >> spower_run.in
    
done



./spower spower_run.in

cp spower.txt ~/Desktop/stage/automatisation_spower/spowernew.txt

cd
cd Desktop/stage/automatisation_spower

python3 graphe.py
