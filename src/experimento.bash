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

mkdir QvsRandom
mkdir QvsQ

echo "Primer caso: Q vs random, Q vs q y Q vs random."

echo "creamos carpeta de resultados"
mkdir QEntrenadovsRandom
cd QEntrenadovsRandom

echo "Entrenamos un QLearner contra un random"
python ../../fourInLine.py q r $1

echo "Me guardo el resultado para el caso basico Q vs random"
cp A-1\(Qlearner\)vs2-\(random\).dat ../Qvsrandom/
cp A-2\(random\)vs1-\(Qlearner\).dat ../Qvsrandom/

echo "renombro el dat a A-1(Qlearner)vs2-(random)-arrancando-de-cero.dat"
mv A-1\(Qlearner\)vs2-\(random\).dat A-1\(Qlearner\)vs2-\(random\)-arrancando-de-cero.dat
mv A-2\(random\)vs1-\(Qlearner\).dat A-2\(random\)vs1-\(Qlearner\)-arrancando-de-cero.dat

echo "Entreno el mismo Qlearner anterior vs otro Qlearner"
python ../../fourInLine.py Q1vsrandom.dic q $1

echo "Renombro los dats de este experimento a QLearnerEntrenadoConRandomvsQlearnerFresco"
mv A-1\(Qlearner\)vs2-\(Qlearner\).dat A-1\(QlearnerEntrenadoConRandom\)vs2-\(QlearnerFresco\).dat
mv A-2\(Qlearner\)vs1-\(Qlearner\).dat A-2\(QlearnerFresco\)vs1-\(QlearnerEntrenadoConRandom\).dat

echo "Entreno el mismo Qlearner contra otra random"
python ../../fourInLine.py Q1vsrandom.dic r $1

echo "Renombro los dats de este experimento a QLearnerMegaEntrenado"
mv A-1\(Qlearner\)vs2-\(random\).dat A-1\(QLearnerMegaEntrenado\)vs2-\(random\).dat
mv A-2\(random\)vs1-\(Qlearner\).dat A-2\(random\)vs1-\(QLearnerMegaEntrenado\).dat


echo "Segundo caso: Q vs q, Q vs random y Q vs Q."

echo "creamos carpeta de resultados"
cd ..
mkdir QEntrenadovsQ
cd QEntrenadovsQ

echo "Entrenamos un QLearner contra otro q"
python ../../fourInLine.py q q $1


echo "Me guardo el resultado para el caso basico Q vs Q"
cp A-1\(Qlearner\)vs2-\(Qlearner\).dat ../QvsQ/
cp A-2\(Qlearner\)vs1-\(Qlearner\).dat ../QvsQ/

echo "renombro el dat a A-1(Qlearner)vs2-(Qlearner)-arrancando-de-cero.dat"
mv A-1\(Qlearner\)vs2-\(Qlearner\).dat A-1\(Qlearner\)vs2-\(Qlearner\)-arrancando-de-cero.dat
mv A-2\(Qlearner\)vs1-\(Qlearner\).dat A-2\(Qlearner\)vs1-\(Qlearner\)-arrancando-de-cero.dat

echo "Entreno el mismo Qlearner anterior vs otro Qlearner"
python ../../fourInLine.py Q1vsQLearner.dic r $1

echo "Renombro los dats de este experimento a QlearnerEntrenadoConQ vs random"
mv A-1\(Qlearner\)vs2-\(random\).dat A-1\(QlearnerEntrenadoConQ\)vs2-\(random\).dat
mv A-2\(random\)vs1-\(Qlearner\).dat A-2\(random\)vs1-\(QlearnerEntrenadoConQ\).dat

echo "Entreno el mismo Qlearner contra otro q"
python ../../fourInLine.py Q1vsQLearner.dic q $1

echo "Renombro los dats de este experimento a QLearnerMegaEntrenado"
mv A-1\(Qlearner\)vs2-\(Qlearner\).dat A-1\(QLearnerMegaEntrenado\)vs2-\(Qlearner\).dat
mv A-2\(Qlearner\)vs1-\(Qlearner\).dat A-2\(Qlearner\)vs1-\(QLearnerMegaEntrenado\).dat
