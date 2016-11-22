#/bin/bash
iterations=$1
path=$2
if ! [[ -n $iterations ]]; then
  echo "Cantidad de parametros invalida, deberia usarse de la siguiente forma:"
  echo "./experimento.bash iterations [dir]"
  exit
fi

if [[ -n $path ]]; then
  if [[ -d $path  ]]; then
    echo "La carpeta ya existe"
  else
    mkdir $path
  fi
  cd $path
fi

epsilon=0.2
gamma=1.0
alpha=0.3
rewardWin=10
rewardTie=0.5
rewardLose=-10
rewardTurn=0
saveDic=1
challengeIters=10000

echo "Creo carpeta de resultados"
mkdir Caso1
mkdir Caso1/QvsQ
mkdir Caso1/QvsR

mkdir Caso2
mkdir Caso2/QvsQ
mkdir Caso2/QvsR
mkdir Caso2/QvsRvsQ
mkdir Caso2/QvsQvsR

mkdir Caso3
mkdir Caso3/QvsR
mkdir Caso3/QvsQ
mkdir Caso3/QvsS

echo "Primer paso entreno Q vs Random."
date
python ../fourInLine.py p q r $alpha $gamma $epsilon $alpha $gamma $epsilon $rewardWin $rewardTie $rewardLose $rewardTurn $saveDic $iterations

echo "Me guargo los .dic y .dat en los 3 casos"
date
cp A-1\(Qlearner\)vs2-\(random\).dat Caso1/QvsR/
cp A-1\(Qlearner\)vs2-\(random\).dat Caso2/QvsR/
mv A-1\(Qlearner\)vs2-\(random\).dat Caso3/QvsR/
cp A-2\(random\)vs1-\(Qlearner\).dat Caso1/QvsR/
cp A-2\(random\)vs1-\(Qlearner\).dat Caso2/QvsR/
mv A-2\(random\)vs1-\(Qlearner\).dat Caso3/QvsR/
cp Q1vsrandom.dic Caso1/QvsR.dic
cp Q1vsrandom.dic Caso2/QvsR.dic
mv Q1vsrandom.dic Caso3/QvsR.dic

echo "Segundo paso entreno otro Q vs otro Q"
date
python ../fourInLine.py p q q $alpha $gamma $epsilon $alpha $gamma $epsilon $rewardWin $rewardTie $rewardLose $rewardTurn $saveDic $iterations

echo "Me guargo los .dic y .dat en los 3 casos casos"
cp A-1\(Qlearner\)vs2-\(Qlearner\).dat Caso1/QvsQ/
cp A-1\(Qlearner\)vs2-\(Qlearner\).dat Caso2/QvsQ/
mv A-1\(Qlearner\)vs2-\(Qlearner\).dat Caso3/QvsQ/
cp A-2\(Qlearner\)vs1-\(Qlearner\).dat Caso1/QvsQ/
cp A-2\(Qlearner\)vs1-\(Qlearner\).dat Caso2/QvsQ/
mv A-2\(Qlearner\)vs1-\(Qlearner\).dat Caso3/QvsQ/
cp Q1vsQlearner.dic Caso1/QvsQ.dic
cp Q1vsQlearner.dic Caso2/QvsQ.dic
mv Q1vsQlearner.dic Caso3/QvsQ.dic
# rm Q2vsQlearner.dic

echo "Tercer paso ponemos a entrenar contra el metodo faltante para el caso 2"
cd Caso2

echo "Entreno el QentrenadoVsR contra un q fresco"
date
python ../../fourInLine.py p QvsR.dic q $alpha $gamma $epsilon $alpha $gamma $epsilon $rewardWin $rewardTie $rewardLose $rewardTurn $saveDic $iterations

echo "Me guardo los .dic y .dat"
mv A-1\(Qlearner\)vs2-\(Qlearner\).dat QvsRvsQ/A-1\(QvsR\)vs2-\(Qlearner\).dat
mv A-2\(Qlearner\)vs1-\(Qlearner\).dat QvsRvsQ/A-2\(Qlearner\)vs1-\(QvsR\).dat
mv QvsR.dic QvsRvsQ.dic
# rm Q2vsQlearner.dic

echo "Entreno el QentrenadoVsQ contra un random"
date
python ../../fourInLine.py p QvsQ.dic r $alpha $gamma $epsilon $alpha $gamma $epsilon $rewardWin $rewardTie $rewardLose $rewardTurn $saveDic $iterations

echo "Me guardo los .dic y .dat"
mv A-1\(Qlearner\)vs2-\(random\).dat QvsQvsR/A-1\(QvsQ\)vs2-\(random\).dat
mv A-2\(random\)vs1-\(Qlearner\).dat QvsQvsR/A-2\(random\)vs1-\(QvsQ\).dat
mv QvsQ.dic QvsQvsR.dic
cd ..

echo "Cuarto Paso ponemos a entrenar un q contra un sq"
date
python ../fourInLine.py p q s $alpha $gamma $epsilon $alpha $gamma $epsilon $rewardWin $rewardTie $rewardLose $rewardTurn $saveDic $iterations

echo "Me guardo los .dic y .dat"
mv A-1\(Qlearner\)vs2-\(SmartQlearner\).dat Caso3/QvsS
mv A-2\(SmartQlearner\)vs1-\(Qlearner\).dat Caso3/QvsS
mv Q1vsSmartQlearner.dic Caso3/QvsS.dic
# rm Q2vsQlearner.dic

echo "Ultimo paso Ponemos a competir con 10000 iteraciones, sin aprendar nada"
echo "Caso 1"
cd Caso1
date
python ../../fourInLine.py p QvsQ.dic QvsR.dic 0 0 0 0 0 0 $rewardWin $rewardTie $rewardLose $rewardTurn 0 $challengeIters
mv A-1\(Qlearner\)vs2-\(Qlearner\).dat A-1\(QvsQ\)vs2-\(QvsR\).dat
mv A-2\(Qlearner\)vs1-\(Qlearner\).dat A-2\(QvsR\)vs1-\(QvsQ\).dat

echo "Caso 2"
cd ../Caso2
date
python ../../fourInLine.py p QvsQvsR.dic QvsRvsQ.dic 0 0 0 0 0 0 $rewardWin $rewardTie $rewardLose $rewardTurn 0 $challengeIters
mv A-1\(Qlearner\)vs2-\(Qlearner\).dat A-1\(QvsQvsR\)vs2-\(QvsRvsQ\).dat
mv A-2\(Qlearner\)vs1-\(Qlearner\).dat A-2\(QvsRvsQ\)vs1-\(QvsQvsR\).dat

echo "Caso 3 triangular:"
cd ../Caso3
echo "QQ vs QS"
date
python ../../fourInLine.py p QvsQ.dic QvsS.dic 0 0 0 0 0 0 $rewardWin $rewardTie $rewardLose $rewardTurn 0 $challengeIters
mv A-1\(Qlearner\)vs2-\(Qlearner\).dat A-1\(QvsQ\)vs2-\(QvsS\).dat
mv A-2\(Qlearner\)vs1-\(Qlearner\).dat A-2\(QvsS\)vs1-\(QvsQ\).dat

echo "QR vs QS"
date
python ../../fourInLine.py p QvsR.dic QvsS.dic 0 0 0 0 0 0 $rewardWin $rewardTie $rewardLose $rewardTurn 0 $challengeIters
mv A-1\(Qlearner\)vs2-\(Qlearner\).dat A-1\(QvsR\)vs2-\(QvsS\).dat
mv A-2\(Qlearner\)vs1-\(Qlearner\).dat A-2\(QvsS\)vs1-\(QvsR\).dat

echo "QQ vs QR"
date
python ../../fourInLine.py p QvsQ.dic QvsR.dic 0 0 0 0 0 0 $rewardWin $rewardTie $rewardLose $rewardTurn 0 $challengeIters
mv A-1\(Qlearner\)vs2-\(Qlearner\).dat A-1\(QvsQ\)vs2-\(QvsR\).dat
mv A-2\(Qlearner\)vs1-\(Qlearner\).dat A-2\(QvsR\)vs1-\(QvsQ\).dat

echo "Listo"
date
