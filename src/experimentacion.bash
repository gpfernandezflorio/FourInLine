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

echo "Primer paso entreno Q vs Random."
python ../fourInLine.py p q r $alpha $gamma $epsilon $alpha $gamma $epsilon $rewardWin $rewardTie $rewardLose $rewardTurn $saveDic $iterations

echo "Me guargo los .dic y .dat en ambos casos"
cp A-1\(Qlearner\)vs2-\(random\).dat Caso1/QvsR/
mv A-1\(Qlearner\)vs2-\(random\).dat Caso2/QvsR/
cp A-2\(random\)vs1-\(Qlearner\).dat Caso1/QvsR/
mv A-2\(random\)vs1-\(Qlearner\).dat Caso2/QvsR/
cp Q1vsrandom.dic Caso1/QvsR.dic
mv Q1vsrandom.dic Caso2/QvsR.dic

echo "Segundo paso entreno otro Q vs otro Q"

python ../fourInLine.py p q q $alpha $gamma $epsilon $alpha $gamma $epsilon $rewardWin $rewardTie $rewardLose $rewardTurn $saveDic $iterations

echo "Me guargo los .dic y .dat en ambos casos"
cp A-1\(Qlearner\)vs2-\(Qlearner\).dat Caso1/QvsQ/
mv A-1\(Qlearner\)vs2-\(Qlearner\).dat Caso2/QvsQ/
cp A-2\(Qlearner\)vs1-\(Qlearner\).dat Caso1/QvsQ/
mv A-2\(Qlearner\)vs1-\(Qlearner\).dat Caso2/QvsQ/
cp Q1vsQlearner.dic Caso1/QvsQ.dic
mv Q1vsQlearner.dic Caso2/QvsQ.dic
rm Q2vsQlearner.dic

echo "Tercer paso ponemos a entrenar contra el metodo faltante para el caso 2"
cd Caso2

echo "Entreno el QentrenadoVsR contra un q fresco"
python ../../fourInLine.py p QvsR.dic q $alpha $gamma $epsilon $alpha $gamma $epsilon $rewardWin $rewardTie $rewardLose $rewardTurn $saveDic $iterations

echo "Me guardo los .dic y .dat"
mv A-1\(Qlearner\)vs2-\(Qlearner\).dat QvsRvsQ/A-1\(QvsR\)vs2-\(Qlearner\).dat
mv A-2\(Qlearner\)vs1-\(Qlearner\).dat QvsRvsQ/A-2\(Qlearner\)vs1-\(QvsR\).dat
mv QvsR.dic QvsRvsQ.dic
rm Q2vsQlearner.dic

echo "Entreno el QentrenadoVsQ contra un random"
python ../../fourInLine.py p QvsQ.dic r $alpha $gamma $epsilon $alpha $gamma $epsilon $rewardWin $rewardTie $rewardLose $rewardTurn $saveDic $iterations

echo "Me guardo los .dic y .dat"
mv A-1\(Qlearner\)vs2-\(random\).dat QvsQvsR/A-1\(QvsQ\)vs2-\(random\).dat
mv A-2\(random\)vs1-\(Qlearner\).dat QvsQvsR/A-2\(random\)vs1-\(QvsQ\).dat
mv QvsQ.dic QvsQvsR.dic

echo "Ponemos a competir con 10000 iteraciones, sin aprendar nada"
echo "Caso 1"
cd ../Caso1
python ../../fourInLine.py p QvsQ.dic QvsR.dic 0 0 0 0 0 0 $rewardWin $rewardTie $rewardLose $rewardTurn 0 $challengeIters
mv A-1\(Qlearner\)vs2-\(Qlearner\).dat A-1\(QvsQ\)vs2-\(QvsR\).dat
mv A-2\(Qlearner\)vs1-\(Qlearner\).dat A-2\(QvsR\)vs1-\(QvsQ\).dat

echo "Caso2"
cd ../Caso2
python ../../fourInLine.py p QvsQvsR.dic QvsRvsQ.dic 0 0 0 0 0 0 $rewardWin $rewardTie $rewardLose $rewardTurn 0 $challengeIters
mv A-1\(Qlearner\)vs2-\(Qlearner\).dat A-1\(QvsQvsR\)vs2-\(QvsRvsQ\).dat
mv A-2\(Qlearner\)vs1-\(Qlearner\).dat A-2\(QvsRvsQ\)vs1-\(QvsQvsR\).dat
