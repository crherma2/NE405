filename=$1

python postprocess.py $filename time "TCV 1 Pos."
python postprocess.py $filename time "TBV 1 Pos."
python postprocess.py $filename time "SG 1 Flow"
python postprocess.py $filename time "Feed Flow 1"
python postprocess.py $filename time "SG 1 WR"
python postprocess.py $filename time "SG 1 NR"
python postprocess.py $filename time Wturb
python postprocess.py $filename time "Psg 1"
python postprocess.py $filename time Tinfnew
python postprocess.py $filename time Pp
python postprocess.py $filename time PrzLvl
python postprocess.py $filename time Qhtr
python postprocess.py $filename time "Prz Spray"
python postprocess.py $filename time Mcharging
python postprocess.py $filename time "M let dwn"
python postprocess.py $filename time Trxnew
python postprocess.py $filename time Reactivity
python postprocess.py $filename time "Rho Fuel"
python postprocess.py $filename time "Rho Mod"
python postprocess.py $filename time "Rho Boron"
python postprocess.py $filename time "Rod Worth"
python postprocess.py $filename time Qthnew
python postprocess.py $filename time "Rod Withdrawal"
