# Draft of BASH version of rebuild_db.bat

DBNAME=spade.db
MANAGE_SCRIPT=manage.py
EXT=db
PYTHON_EXEC=python3

rm $DBNAME
touch $DBNAME

$PYTHON_EXEC $MANAGE_SCRIPT version_control --url=sqlite:///$DBNAME

sed -i.bu "s;sqlite:///.*\.${EXT};sqlite:///${DBNAME};g" $MANAGE_SCRIPT

$PYTHON_EXEC $MANAGE_SCRIPT upgrade
